import csv
import pandas as pd
#loading the sentiment file
column_names = ['Index', 'Title', 'Sentiment', 'Class', 'Entity1', 'Entity2', 'Entity3', 'Language']
my_csv = pd.read_csv('de_sentiment_all.csv',  names=column_names)
#adding columns to the variables 
Entity1 = my_csv.Entity1.to_list()
Entity2 = my_csv.Entity2.to_list()
Entity3 = my_csv.Entity3.to_list()
titles = my_csv.Title.to_list()
sentiment = my_csv.Sentiment.to_list()
classtype = my_csv.Class.to_list()
language = my_csv.Language.to_list()


#create a new csv file
with open("de_sentiment_label.csv", 'w', encoding = "utf-8") as f:
    fieldnames = ['Index', 'Title', 'Sentiment', 'Class', 'Entity1', 'Entity2', 'Entity3', 'Language']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    #if the variable is not none at _de for german
    for i in range (1, len(titles)):
        if not pd.isna(Entity1[i]):
            entity_sen1 = Entity1[i] + "_de"
        else:
            entity_sen1 = None
        if not pd.isna(Entity2[i]):
            entity_sen2 = Entity2[i] + "_de"
        else:
            entity_sen2 = None
        if not pd.isna(Entity3[i]):
            entity_sen3 = Entity3[i] + "_de"
        else:
            entity_sen3 = None

        class1 = classtype[i]
        sentiment1 = sentiment[i]
        Title = titles[i]
        language1 = language[i]
        writer.writerow({'Index': i, 'Title': Title, 'Sentiment' : sentiment1, 'Class' : class1, 'Entity1' : entity_sen1, 'Entity2' : entity_sen2, 'Entity3' : entity_sen3, 'Language': language1})

        print(i)
        i = i +1
