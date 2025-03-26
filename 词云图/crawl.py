from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import time
import random


# Step 1: Crawl job detail pages and extract requirements
def fetch_job_data_from_liepin(start_page=0, end_page=5):
    all_job_data = ""

    # Set up Selenium with Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in background
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Headers for requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    # Keywords to identify requirement/description sections
    target_keywords = ['任职要求', '职位描述', '职位要求', '工作要求', '技能要求', '能力要求']

    # Step 1a: Collect job detail URLs
    job_urls = []
    for page in range(start_page, end_page):
        url = f'https://www.liepin.com/zhaopin/?city=070020&dq=070020&pubTime=&currentPage={page}&pageSize=40&key=%E6%90%9C%E7%B4%A2%E6%8E%A8%E8%8D%90%E7%AE%97%E6%B3%95&suggestTag=&workYearCode=0&compId=&compName=&compTag=&industry=&salary=&jobKind=&compScale=&compKind=&compStage=&eduLevel=&otherCity=&sfrom=search_job_pc'
        # 直聘 url = f'https://www.zhipin.com/job_detail/?query=%E6%90%9C%E7%B4%A2%E6%8E%A8%E8%8D%90%E7%AE%97%E6%B3%95&city=101010100&page={page+1}'  # Beijing as example, page starts at 1
        print(f"Searching page: {url}")
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(3)

        # Get job detail links
        url_elements = driver.find_elements('css selector', '.job-detail-box a')  # 猎聘
        # url_elements = driver.find_elements('css selector', '.job-card-left a')#直聘
        for element in url_elements:
            link = element.get_attribute('href')
            if link and 'job' in link:  # Ensure it’s a job detail page
                job_urls.append(link)
        print(f"Found {len(url_elements)} job links on page {page}")

    # Step 1b: Crawl detail pages
    for job_url in job_urls[:20]:  # Limit to 20 jobs for testing
        print(f"Crawling detail page: {job_url}")
        try:
            response = requests.get(url=job_url, headers=headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract job description/requirements
            job_content = soup.select_one('.job-intro-container .paragraph')  # Liepin job details
            # 直聘 job_content = soup.select_one('.job-sec .text')
            if not job_content:
                print(f"No job content found at {job_url}")
                continue

            desc_text = job_content.get_text(strip=True)
            found_target = False
            for keyword in target_keywords:
                if keyword in desc_text:
                    start_idx = desc_text.find(keyword)
                    end_idx = len(desc_text)
                    for next_section in target_keywords + ['岗位职责', '工作职责']:  # '具备以下条件者优先：'
                        next_idx = desc_text.find(next_section, start_idx + len(keyword))
                        if next_idx != -1 and next_idx < end_idx:
                            end_idx = next_idx
                    target_text = desc_text[start_idx:end_idx]
                    all_job_data += target_text + "\n"
                    found_target = True
                    break

            if not found_target:
                print(f"No target section found at {job_url}, using full description.")
                all_job_data += desc_text + "\n"

        except requests.RequestException as e:
            print(f"Error crawling {job_url}: {e}")

        time.sleep(random.randint(1, 2))

    driver.quit()

    # Fallback mock data
    if not all_job_data:
        print("No data fetched, using mock data.")
        all_job_data = """

        """

    return all_job_data


# Step 2: Extract keywords
def extract_keywords(text):
    words = jieba.cut(text)
    stopwords = {'负责', '岗位', '职责', '任职', '要求', '及', '以上', '有', '或', '与', '者', '优先', '的', '和', '等',
                 '进行', '熟悉', '熟练掌握', '掌握', '专业',
                 '以上学历', '至少', '善于', '擅长', '一种', '能力', '技术', '具备', '包括', '职位', '相关', '业务',
                 ',', '限于'}
    keywords = [word for word in words if word not in stopwords and len(word) > 1]
    keyword_counts = Counter(keywords)
    return keyword_counts


# Step 3: Generate word cloud
def generate_wordcloud(keyword_counts):
    wordcloud = WordCloud(
        font_path='C:/Windows/Fonts/SimHei.ttf',  # Replace with your font path
        width=800,
        height=400,
        background_color='white',
        max_words=100
    ).generate_from_frequencies(dict(keyword_counts))

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# Main function
def main():
    # Crawl data for "搜索推荐算法" from liepin
    job_data = fetch_job_data_from_liepin(start_page=0, end_page=10)  # Crawl 5 pages

    # Extract keywords
    keyword_counts = extract_keywords(job_data)
    print("Top 10 keywords:", keyword_counts.most_common(10))

    # Generate word cloud
    generate_wordcloud(keyword_counts)


if __name__ == "__main__":
    main()