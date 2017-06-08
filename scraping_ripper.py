from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

url = "http://www.casebook.org/press_reports/alderley_and_wilmslow_advertiser/881019.html"


# print(url)

html = request.urlopen(url).read()
# print(html)

soup = BeautifulSoup(html, 'lxml')
# links = soup.find_all('p')
# for link in soup.select('td.content p'):
#     print(link.text)
print(soup.select('p'))



# links = soup.find_all('a')[0:10]
# text = soup.text[0:2000]
# # print(soup.text.replace('/n', ' '))
# print(soup.select("content"))
# for link in soup.select("td.content a"):
#     print(link.text)

# links_html = soup.select('td.content a')
# urls = []
# for link in links_html:
#     url = link['href']
#     urls.append(url)
# print(urls)
