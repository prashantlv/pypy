from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.hindustantimes.com/tech/').text
soup = BeautifulSoup(source, 'lxml')

for headl in soup.find_all('div',class_ = 'media-body'):
    headline = headl.div.a.text
    para = headl.p.text
    date = headl.span.text
    print("*",headline)
    print("-",para)
    print("date :- ", date)
    print()
