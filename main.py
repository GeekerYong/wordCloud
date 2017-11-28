#coding = utf-8
import requests
import time
import random
from bs4 import BeautifulSoup

abss = 'https://movie.douban.com/subject/20495023/comments'
firstPag_url = 'https://movie.douban.com/subject/20495023/comments?start=20&limit=20&sort=new_score&status=P&percent_type='
url = 'https://movie.douban.com/subject/20495023/comments?start=0&limit=20&sort=new_score&status=P'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Connection':'keep-alive'
}

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    comment_list = soup.select('.comment > p')
    next_page = soup.select('#paginator > a')[2].get('href')
    date_nodes = soup.select('..comment-time')
    return comment_list, next_page, date_nodes

def get_cookies(path):
    f_cookies = open(path, 'r')
    cookies ={}
    for line in f_cookies.read().split(';'):
        name ,value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies

if __name__ == '__main__':
    cookies = get_cookies('./cookies.txt')
    html = requests.get(firstPag_url, cookies=cookies,headers=header).content
    comment_list, next_page, date_nodes = get_data(html)
    soup = BeautifulSoup(html, 'lxml')
    while (next_page):
        print(abss + next_page)
        html = requests.get(abss + next_page, cookies=cookies, headers=header).content
        comment_list, next_page, date_nodes = get_data(html)
        soup = BeautifulSoup(html, 'lxml')
        comment_list, next_page,date_nodes = get_data(html)
        with open("comments.txt", 'a', encoding='utf-8')as f:
            for ind in range(len(comment_list)):
                comment = comment_list[ind];
                data = date_nodes[ind]
                comment = comment.get_text().strip().replace("\n", "")
                date= data.get_text().strip()
                f.writelines(date+u'\n' +comment + u'\n')
        time.sleep(1 + float(random.randint(1, 100)) / 20)
