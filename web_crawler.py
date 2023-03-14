import requests
import csv
from lxml import etree


# 在网页解析方面，通过使用 Python 的 requests 库及 lxml 库对豆瓣的电视剧相关信息进行爬取，爬取后的数据存入到本地 csv 文件。

# 获取返回请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}


def get(url):
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)
    return page_text


# 解析目标内容
def parsehtml(page_text):
    tree = etree.HTML(page_text)
    mo_li = tree.xpath('//div[@class="info"]')
    movie = []
    for mo in mo_li:
        dic = {}
        moname = mo.xpath('.//div[@class="hd"]/a/span[1]/text()')[0]
        # print(moname)
        mostar = mo.xpath('.//div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()')[0]
        moquote = mo.xpath('.//div[@class="bd"]/p[@class="quote"]/span/text()')
        if moquote:
            moquote = moquote[0]
        else:
            moquote = ''
        dic['moname'] = moname
        dic['mostar'] = mostar
        dic['moquote'] = moquote
        movie.append(dic)
    # print(movie)
    return movie


# 保存到csv
def save(movie):
    with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['moname', 'mostar', 'moquote'])
        writer.writeheader()
        writer.writerows(movie)


movie_content = []
for i in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(i-1)*25}&filter='
    page_text_ = get(url)
    movie_content = movie_content + parsehtml(page_text_)
save(movie_content)

