from bs4 import BeautifulSoup
from contextlib import closing
from urllib import request

# Step One: Get root url
url = "https://github.com/humanitiesprogramming/scraping-corpus"

# print(url + "/subdomain")

html = request.urlopen(url).read()
# print(html[0:2000])

soup = BeautifulSoup(html, 'lxml')


links = soup.find_all('a')[0:10]
text = soup.text[0:2000]
# print(soup.text.replace('/n', ' ') [0:1000])
# print(soup.select("content"))
# for link in soup.select("td.content a"):
#     print(link.text)

# Step Two: get all the subpages
links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href']
    urls.append(url)
# print(urls)

#Step Three: Combine with root url to get links
links_html = soup.select('td.content a')
urls = []
for link in links_html:
    url = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + url)
# print(urls)

#Step Four: Scrape each link for text
corpus_texts = []
for url in urls:
    print(url)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)

print(corpus_texts)
#To send to file, hashtag print(url), then in commande line: $python3 scraping.py > results.txt
#(you don't need this step to do later text analysis)
