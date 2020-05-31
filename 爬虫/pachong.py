from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import requests
import re
from collections import defaultdict

def driver_open(key_word):
    url = "http://xueshu.baidu.com/"
    driver = webdriver.Chrome("D:\\selenium_driver\\chromedriver.exe")
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_class_name('s_ipt').send_keys(key_word)
    time.sleep(3)
    driver.find_element_by_class_name('s_btn_wr').click()
    time.sleep(2)
    content = driver.page_source.encode('utf-8')
    driver.close()
    soup = BeautifulSoup(content, 'lxml')
    return soup


def page_url_list(soup, page):
    fir_page = "http://xueshu.baidu.com" + soup.find_all("a", class_="n")[0]["href"]
    urls_list = []
    for i in range(page):
        next_page = fir_page.replace("pn=10", "pn={:d}".format(i * 10))
        response = requests.get(next_page)
        soup_new = BeautifulSoup(response.text, "lxml")
        c_fonts = soup_new.find_all("h3", class_="t c_font")
        for c_font in c_fonts:
            url =  c_font.find("a").attrs["href"]
            urls_list.append(url)
        print(i)
    return urls_list

def get_item_info(url):
    print(url)
    content_details = requests.get(url)
    soup = BeautifulSoup(content_details.text, "lxml")
    # 提取文章题目
    title = ''.join(list(soup.select('#dtl_l > div > h3 > a')[0].stripped_strings))
    if len(title)==0:
        title='null'
    # 提取文章作者
    authors = list(soup.select('div.author_wr'))
    if len(authors) == 0:
        authors='null'
    else:
     authors = ''.join(str(author_) for author_ in list(soup.select('div.author_wr')[0].stripped_strings)[1:])
    # 提取摘要
    abstract=list(soup.select('div.abstract_wr>p.abstract'))
    if len(abstract) == 0:
        abstract='null'
    else:
        abstract = list(soup.select('div.abstract_wr>p.abstract')[0].stripped_strings)[0].replace('\u3000', ' ')
    # 提取出版社
    journal = list(soup.select('div.journal_title'))
    if len(journal) == 0:
        journal = list(soup.select('a.journal_title'))
        if len(journal) == 0:
            journal='null'
        else:
            journal=list(soup.select('a.journal_title')[0].stripped_strings)[0]
    else:
        journal=list(soup.select('div.journal_title')[0].stripped_strings)[0]
    #提取时间
    year = list(soup.select('div.year_wr>p.kw_main'))
    if len(year) == 0:
        year='null'
    else:
        year=list(soup.select('div.year_wr>p.kw_main')[0].stripped_strings)[0]
    # 提取引用量
    ref_wr = list(soup.select('a.sc_cite_cont'))
    if len(ref_wr) == 0:
        ref_wr = 0
    else:
        ref_wr = list(soup.select('a.sc_cite_cont')[0].stripped_strings)[0]
    # 提取关键词
    key_words =list(soup.select('div.kw_wr > p.kw_main '))
    if len(key_words) == 0:
        key_word='null'
    else:
       key_words=' '.join(str(key_) for key_ in list(soup.select('div.kw_wr > p.kw_main')[0].stripped_strings))
       #print(key_words)
        #key_words = list(soup.select('div.kw_wr > p.kw_main>span>a')[0].stripped_strings)
#
    return title, authors, abstract, journal, year, ref_wr, key_words


def get_all_data(urls_list):
    dit = defaultdict(list)
    i=1
    for url in urls_list:
        title, authors, abstract, journal, year, ref_wr, key_words = get_item_info(url)
        dit["title"].append(title)
        dit["authors"].append(authors)
        dit["abstract"].append(abstract)
        dit["journal"].append(journal)
        dit["year"].append(year)
        dit["ref_wr"].append(ref_wr)
        dit["key_words"].append(key_words)
        print(i)
        i=i+1
    return dit



def save_csv(dit):
    data = pd.DataFrame(dit)
    columns = ["title", "authors", "abstract", "journal", "year",  "ref_wr", "key_words"]
    data.to_csv("D:\\data.csv", index=False, columns=columns)
    print("That's OK!")

if __name__ == "__main__":
    key_word = "time series"
    soup = driver_open(key_word)
    #print(soup)
    urls_list = page_url_list(soup, page=1000)
    #print(urls_list)
    dit = get_all_data(urls_list)
    #get_item_info('http://xueshu.baidu.com/usercenter/paper/show?paperid=f9eaa752cc1c5f7a6ae98685d9778005&site=xueshu_se')
    #print(dit)
    save_csv(dit)
    data = pd.read_csv("D:\\baidu.csv")
   #data.head()

