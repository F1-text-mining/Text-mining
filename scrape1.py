import requests
from bs4 import BeautifulSoup
import re
import math
import csv

url = 'https://de.motorsport.com/f1/news/?filters%5Bchampionship%5D%5B%5D=2871&filters%5Brace_type%5D%5B%5D=54'

r = requests.get(url)

soup1 = BeautifulSoup(r.content, "html.parser")

get_data = soup1.find("div", {"class": "ms-filter-total"})

num_articles_raw = get_data.text
print(num_articles_raw)
articles_removed = re.sub(' Artikel', '', num_articles_raw)
comma_removed = int(re.sub('(?<=\d)[,\.]', '', articles_removed))
division = comma_removed / 60
num_pages = math.ceil(division)

with open('article_list_de.csv', 'w', encoding="utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Link']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    t = 1
    for t in range(1, num_pages):
        page = str(t)
        request = requests.get(url + "&p=" + page)
        soup = BeautifulSoup(request.content, "html.parser")
        g_data = soup.find_all("div", {"class": "ms-item--art"})

        i = 0
        k = 0

        for item in g_data:
        #newsitem = item.find('title', first = True)
            newsitem = soup.find_all("h3", {"class": "ms-item_title"})
            index = newsitem[i]
            title = newsitem[i].text


            for a in index.find_all("a", href = True):
                substring = "2020"
                if substring in a['href']:
                    Index = i
                    Title = title
                    Link = "https://de.motorsport.com" + a['href']
                    writer.writerow({'Index': Index, 'Title': Title, 'Link': Link })
        #print(title)
                    k = k +1
                    print(k)
                i = i + 1
        t = t + 1
        #title = newsitem.text
        #link = newsitem.absolute_links
        #print(title, link)
