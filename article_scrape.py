import requests
from bs4 import BeautifulSoup
import re
import math
import csv
import pandas as pd

column_names = ['Index', 'Title', 'Link']
my_csv = pd.read_csv('article_list_de.csv',  names=column_names)
letters = my_csv.Link.to_list()
titles = my_csv.Title.to_list()
i = 0

with open('article_data_de.csv', 'w', encoding="utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Link', 'Content']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (1, len(letters)):
        url = letters[i]
        Title = titles[i]
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")
        get_data = soup.find("div", {"class": "ms-article-content"})
        try:
            content = get_data.text
            content_junk_removed1 = re.sub('geteilte inhalte', '', content)
            content_junk_removed = re.sub('kommentare', '', content_junk_removed1)
            Content = content_junk_removed
            Index = i
            writer.writerow({'Index': Index, 'Title': Title, 'Link': url, 'Content': Content})
        except:
            ContentNone = "None"
            writer.writerow({'Index': Index, 'Title': Title, 'Link': url, 'Content': ContentNone})
        #print(row)
        i = i + 1

        print(i)
