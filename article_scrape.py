import requests
from bs4 import BeautifulSoup
import re
import math
import csv
import pandas as pd

#loading article list data
column_names = ['Index', 'Title', 'Link']
my_csv = pd.read_csv('article_list_de.csv',  names=column_names)
links = my_csv.Link.to_list()
titles = my_csv.Title.to_list()
i = 0

#create new cvs file
with open('article_data_de.csv', 'w', encoding="utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Link', 'Content']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (1, len(letters)):
        #get the ulr and the title to a variable
        url = links[i]
        Title = titles[i]
        
        #open the url
        request = requests.get(url)
        #call the beatiful soup library
        soup = BeautifulSoup(request.content, "html.parser")
        #look at the het div class ms-article-content for the content of the article
        get_data = soup.find("div", {"class": "ms-article-content"})
        
        try:
            #if there is data get the text
            content = get_data.text
            #Remove the junk form the data
            content_junk_removed1 = re.sub('geteilte inhalte', '', content)
            content_junk_removed = re.sub('kommentare', '', content_junk_removed1)
            Content = content_junk_removed
            Index = i
            #write row to the cvs file
            writer.writerow({'Index': Index, 'Title': Title, 'Link': url, 'Content': Content})
        except:
            ContentNone = "None"
            writer.writerow({'Index': Index, 'Title': Title, 'Link': url, 'Content': ContentNone})
        #print(row)
        i = i + 1

        print(i)
