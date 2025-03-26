import requests
from bs4 import BeautifulSoup
import re
import time
from collections import Counter
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os


# 创建技术术语词典文件（如果不存在）
def create_tech_terms_file():
    tech_terms_content = """机器学习 10 n
深度学习 10 n
推荐系统 10 n
搜索算法 10 n
Python 10 n
Java 8 n
C++ 8 n
TensorFlow 10 n
PyTorch 10 n
Spark 8 n
Hadoop 8 n
SQL 8 n
NoSQL 8 n
协同过滤 10 n
FM 10 n
LR 10 n
GBDT 10 n
LSTM 10 n
神经网络 10 n
CTR 10 n
CVR 10 n
召回 10 n
排序 10 n
用户画像 10 n
特征工程 10 n
分布式计算 10 n
算法优化 10 n
自然语言处理 10 n
数据挖掘 10 n
大数据 8 n"""

    if not os.path.exists('tech_terms.txt'):
        with open('tech_terms.txt', 'w', encoding='utf-8') as f:
            f.write(tech_terms_content)
        print("已创建技术术语词典文件 tech_terms.txt")


# 初始化技术术语词典
create_tech_terms_file()


def scrape_liepin(keyword="搜索推荐算法", max_page=2):
    """抓取猎聘网岗位数据（模拟版，实际网站可能有反爬）"""
    print("正在抓取猎聘网数据...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 模拟数据（实际使用时替换为真实抓取代码）
    mock_data = """
    搜索推荐算法工程师 职位描述：
    - 负责推荐系统的设计和开发
    - 精通Python/Java编程语言
    - 熟悉TensorFlow/PyTorch框架
    - 有机器学习、深度学习相关经验
    - 熟悉协同过滤、FM等推荐算法

    任职要求：
    - 计算机相关专业本科以上学历
    - 3年以上推荐算法相关经验
    - 熟悉大数据处理技术如Hadoop/Spark
    - 良好的数据结构和算法基础
    """

    return [mock_data] * 3  # 返回3个模拟岗位数据


def scrape_zhilian(keyword="搜索推荐算法", max_page=2):
    """抓取智联招聘岗位数据（模拟版，实际网站可能有反爬）"""
    print("正在抓取智联招聘数据...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    # 模拟数据（实际使用时替换为真实抓取代码）
    mock_data = """
    搜索算法工程师 职位描述：
    - 负责搜索相关性排序算法优化
    - 精通C++/Python编程
    - 熟悉自然语言处理技术
    - 有大规模数据处理经验
    - 熟悉GBDT、LSTM等算法

    任职要求：
    - 计算机相关专业硕士学历
    - 熟悉Linux开发环境
    - 有搜索推荐系统经验优先
    - 熟悉分布式计算框架
    """

    return [mock_data] * 3  # 返回3个模拟岗位数据


def extract_keywords(text_list, top_n=50):
    """从文本中提取关键词"""
    # 加载自定义词典
    try:
        jieba.load_userdict('tech_terms.txt')
        print("成功加载自定义技术术语词典")
    except Exception as e:
        print(f"加载自定义词典失败: {str(e)}，将使用默认词典")

    # 合并所有文本
    combined_text = " ".join(text_list)

    # 使用jieba提取关键词
    keywords = jieba.analyse.extract_tags(
        combined_text,
        topK=top_n,
        withWeight=False,
        allowPOS=('n', 'vn', 'v', 'eng')
    )

    # 手动添加一些常见技术术语
    tech_terms = [
        '机器学习', '深度学习', '推荐系统', '数据挖掘', '自然语言处理',
        'Python', 'Java', 'C++', 'TensorFlow', 'PyTorch',
        'Spark', 'Hadoop', 'Hive', 'SQL', 'NoSQL',
        '协同过滤', 'FM', 'LR', 'GBDT', 'LSTM',
        '神经网络', 'CTR', 'CVR', '召回', '排序',
        '用户画像', '特征工程', '分布式计算', '算法优化'
    ]

    # 合并自动提取和手动添加的关键词
    all_keywords = list(keywords) + tech_terms

    # 统计词频
    word_counts = Counter(all_keywords)

    return word_counts


def generate_wordcloud(word_counts):
    """生成词云图"""
    print("正在生成词云图...")

    # 设置中文字体（Mac系统）
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'  # 宋体

    # 创建词云对象
    wc = WordCloud(
        font_path=font_path,
        width=1000,
        height=800,
        background_color='white',
        max_words=100,
        max_font_size=150,
        colormap='viridis',
        prefer_horizontal=0.9,
        scale=2
    )

    # 生成词云
    wc.generate_from_frequencies(word_counts)

    # 显示词云
    plt.figure(figsize=(15, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    plt.title('搜索推荐算法岗位技能要求词云', fontsize=20)
    plt.tight_layout()

    # 保存词云图
    wc.to_file('job_keywords_cloud.png')
    print("词云图已保存为 job_keywords_cloud.png")

    # 显示词云
    plt.show()


def save_keywords(word_counts):
    """保存关键词和词频"""
    with open('job_keywords.txt', 'w', encoding='utf-8') as f:
        for word, count in word_counts.most_common():
            f.write(f"{word} {count}\n")
    print("关键词已保存到 job_keywords.txt")


def main():
    # 从多个招聘网站抓取数据
    liepin_data = scrape_liepin()
    zhilian_data = scrape_zhilian()

    # 提取关键词
    word_counts = extract_keywords(liepin_data + zhilian_data)

    # 保存关键词
    save_keywords(word_counts)

    # 生成词云图
    generate_wordcloud(word_counts)


if __name__ == "__main__":
    main()

