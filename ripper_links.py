from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/"
# print(url)

html = request.urlopen(url).read()
# print(html)

soup = BeautifulSoup(html, 'lxml')

links = soup.find_all("a", class_="leftnavoff")
print(links)
# text = soup.text[0:2000]
# # print(soup.text.replace('/n', ' '))
# # print(soup.select("content"))
# for link in soup.select("td.content a"):
#     print(link.text)
