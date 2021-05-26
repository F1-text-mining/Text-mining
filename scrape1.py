import requests
from bs4 import BeautifulSoup
import re
import math
import csv

#set url to a variable
url = 'https://de.motorsport.com/f1/news/?filters%5Bchampionship%5D%5B%5D=2871&filters%5Brace_type%5D%5B%5D=54'

#load the url
r = requests.get(url)
#call the library
soup1 = BeautifulSoup(r.content, "html.parser")
#look in div class ms-filter total. (the number of articles
get_data = soup1.find("div", {"class": "ms-filter-total"})
#get the text in the class
num_articles_raw = get_data.text
print(num_articles_raw)
#remove all junk
articles_removed = re.sub(' Artikel', '', num_articles_raw)
comma_removed = int(re.sub('(?<=\d)[,\.]', '', articles_removed))
#calculated the number of articles at each page
division = comma_removed / 60
num_pages = math.ceil(division)

#create a new csv file
with open('article_list_de.csv', 'w', encoding="utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Link']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    t = 1
    for t in range(1, num_pages):
        #set the  page number
        page = str(t)
        #load the correct page
        request = requests.get(url + "&p=" + page)
        soup = BeautifulSoup(request.content, "html.parser")
        
        #load all data in div class ms-item-art
        g_data = soup.find_all("div", {"class": "ms-item--art"})

        i = 0
        k = 0
        #look in every item in g_data
        for item in g_data:
            #look at all data in h3 class ms-item_title to find the title of the article
            newsitem = soup.find_all("h3", {"class": "ms-item_title"})
            index = newsitem[i]
            title = newsitem[i].text

            #look for the link
            for a in index.find_all("a", href = True):
                substring = "2020"
                if substring in a['href']:
                    Index = i
                    Title = title
                    #add to the link become only every after the / is found
                    Link = "https://de.motorsport.com" + a['href']
                    #add every thing to the csv file
                    writer.writerow({'Index': Index, 'Title': Title, 'Link': Link })
        
                    k = k +1
                    print(k)
                i = i + 1
        t = t + 1
        
       
