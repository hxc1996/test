
import requests
from collections import namedtuple
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from collections import defaultdict

#获取每个文献页面的详细信息
def get_page(keywords,offset):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    params = {
        'wd': keywords,
        'pn':offset,
        'tn':'SE_baiduxueshu_c1gjeupa',
        'ie':'utf-8',
        'sc_hit':'1'
    }
    url = "http://xueshu.baidu.com/s?"+urlencode(params)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.ConnectionError:
        return None


#提取具体内容
def get_urls(text):
    all_titles = []#标题
    all_abstracts = []#摘要
    all_authors = []#作者
    all_refs=[]#引用
    all_years=[]#年份
    soup = BeautifulSoup(text,'lxml')

    title_datas = soup.select('div.sc_content > h3 > a')
    author_datas = soup.find_all('div','sc_info')
    abstract_datas = soup.find_all('div','c_abstract')

    #获取标题
    for item in title_datas:
        result = {
            'title':item.get_text(),
            'href':item.get('href')
        }
        all_titles.append(item.get_text())

    #获取摘要
    for abs in abstract_datas:
        str_list = []
        for l in abs.contents:
            str_list.append(str(l).replace('\n','').strip())
        all_abstracts.append("".join(str_list).replace('<em>','').replace('</em>',''))

    #获取作者，引用，年份
    for authors in author_datas:
        for span in authors.find_all('span',limit=1):
            each_authors = []
            each_ref=[]
            each_years = []
            for alist in span.find_all('a'):
                each_authors.append(alist.string)
            all_authors.append(each_authors)
        for refs in authors.find_all('a','sc_cite_cont'):
            each_ref.append(refs.string.strip())
        all_refs.append(each_ref)
        for year in authors.find_all('span','sc_time'):
             each_years.append(year.string.strip())
        all_years.append(each_years)
    return all_titles,all_authors,all_abstracts,all_refs,all_years

paper = namedtuple('paper',['title','author','abstract','all_ref','all_years'])

# 写入元组
def set_paper(all_titles,all_authors,all_abstracts,all_ref,all_years):
    dit = defaultdict(list)
    for i in range(len(all_titles)):
        dit["title"].append(all_titles[i])
        dit["authors"].append(all_authors[i])
        dit["abstract"].append(all_abstracts[i])
        dit["ref"].append(all_ref[i])
        dit["year"].append(all_years[i])
    return dit
    # papers = [paper(all_titles[i],all_authors[i],all_abstracts[i],all_ref[i],all_years[i]) for i in range(len(all_titles))]
    # return papers

#保存文件
def save_data(papers):
    json_papers = []
    for paper in papers:
        each_data = {
            'title':paper[0],
            'author':"/".join(paper[1]),
            'abstract':paper[2],
            'ref':paper[3],
            'year':paper[4]
        }
        json_papers.append(each_data)
    print(json_papers)


    # with open('D:\\123.txt', 'a', encoding='utf-8') as f:
    #     for paper in json_papers:
    #         f.write(json.dumps(paper, ensure_ascii=False) + '\n')

if __name__ == '__main__':

    keywords = "时间序列算法"
    print("开始爬取百度学术网站关于“{}”关键词的相关内容".format(keywords))
    for i in range(1):
        print("开始爬取第{}页的内容".format(str(i+1)))
        offset = i * 10
        text = get_page(keywords,offset)
        all_titles, all_authors, all_abstracts,all_refs,all_years = get_urls(text)
        papers = set_paper(all_titles, all_authors, all_abstracts,all_refs,all_years)
        save_data(papers)

    print("保存成功！")