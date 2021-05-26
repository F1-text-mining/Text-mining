from textblob import TextBlob
from textblob_nl import PatternTagger, PatternAnalyzer
import csv
import pandas as pd

#find all the driver and teams in the title
entities = ["Russell", "Hamilton", "Gasly", "Verstappen", "Bottas", "Perez", "Ricciardo", "Sainz", "Albon", "Leclerc", "Norris", "Stroll", "Ocon", "Vettel", "Kvyat", "Raikkonen", "Giovinazzi", "Grosjean", "Magnussen", "Latifi", "Haas", "Red Bull", "Mercedes", "Racing Point", "McLaren", "Ferrari", "Renault", "Williams", "AlphaTauri", "Alfa Romeo"]
def name_count(Title):
    entity = []
    for i in range(len(entities)):
        if entities[i] in Title:
            entity.append(entities[i])
    return entity

#load the processed file
column_names = ['Index', 'Title', 'Content_proc', 'Entity1']
my_csv = pd.read_csv('nl_pos_processed.csv',  names=column_names)
titles = my_csv.Title.to_list()
content = my_csv.Content_proc.to_list()

#set all counts to zero
pos_count = 0
pos_correct = 0

neg_count = 0
neg_correct = 0

neut_count = 0

#create a new csv file
with open("nl_sentiment_all.csv", 'w', encoding = "utf-8") as f:
    fieldnames = ['Index', 'Title', 'Sentiment', 'Class', 'Entity1', 'Entity2', 'Entity3']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (1, len(content)):
        #call textblob and add the analyzer of the language
        analysis  = TextBlob(content[i], analyzer = PatternAnalyzer())
        
        #call the sentiment that was calculated
        sentiment1 = analysis.sentiment
        #get the polarity
        sentiment = sentiment1[0]
        
        #class the sentiment 
        content_class = []
        
        #positive
        if sentiment >= 0.15:
            if sentiment > 0:
                pos_correct += 1
            pos_count +=1
            content_class.append('Positive')
        #positive
        elif sentiment <= -0.01:
            if sentiment <= 0:
                neg_correct += 1
            neg_count +=1
            content_class.append('Negative')
        #neutral
        else:
            neut_count +=1
            content_class.append('Neutral')

        Title = titles[i]
        entity_sen = name_count(Title)
        
        #fill entity if there is something
        try:
            entity_sen1 = entity_sen[0]
        except:
            entity_sen1 = None
        try:
            entity_sen2 = entity_sen[1]
        except:
            entity_sen2 = None
        try:
            entity_sen3 = entity_sen[2]
        except:
            entity_sen3 = None
        #write row of the csv
        writer.writerow({'Index': i, 'Title': Title, 'Sentiment' : sentiment, 'Class' : content_class[0], 'Entity1' : entity_sen1, 'Entity2' : entity_sen2, 'Entity3' : entity_sen3})


        print(i)
        i = i +1


print(pos_count, neg_count, neut_count)
