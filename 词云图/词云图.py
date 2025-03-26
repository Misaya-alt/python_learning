# -*- coding: utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import platform

# ====== 1. 关键词与权重配置 ======
keywords = {
    # 算法与模型
    "机器学习": 8, "深度学习": 7, "推荐系统": 9, "NLP": 6, "图算法": 6,
    "协同过滤": 5, "矩阵分解": 4, "召回策略": 5, "排序模型": 5, "强化学习": 4,
    # 数据处理
    "大数据处理": 7, "特征工程": 7, "用户行为分析": 6, "数据挖掘": 5,
    "实时计算": 6, "Hadoop/Spark": 5, "Flink/Kafka": 5,
    # 编程工具
    "Python": 7, "TensorFlow/PyTorch": 6, "XGBoost/LightGBM": 5,
    # 系统设计
    "分布式系统": 6, "高并发架构": 5, "Docker/Kubernetes": 5,
    # 业务理解
    "用户画像": 6, "个性化推荐": 7, "A/B测试": 5,
    # 评估指标
    "CTR/CVR": 5, "准确率/召回率": 6
}

# ====== 2. macOS 字体路径配置 ======
if platform.system() == 'Darwin':  # macOS
    font_path = '/System/Library/Fonts/Supplemental/Songti.ttc'  # 苹果系统自带中文字体
else:
    font_path = 'SimHei.ttf'  # 其他系统备用字体

# ====== 3. 生成词云 ======
wc = WordCloud(
    font_path=font_path,
    background_color='white',
    max_words=200,
    width=1200,
    height=800,
    colormap='viridis',       # 推荐配色：'plasma', 'magma', 'inferno'
    prefer_horizontal=0.8,
    contour_width=1,          # 轮廓线宽度（需配合mask使用）
    scale=2                   # 提高分辨率（macOS视网膜屏适配）
)

# 生成词云（若需自定义形状，取消下面注释）
# mask = np.array(Image.open("shape_mask.png"))  # 使用PNG形状蒙版
# wc.mask = mask

wc.generate_from_frequencies(keywords)

# ====== 4. 可视化与保存 ======
plt.figure(dpi=300)  # 高清输出
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')

# 保存图片（透明背景需设置png格式）
wc.to_file("search_reco_skills_mac.png")
plt.show()
