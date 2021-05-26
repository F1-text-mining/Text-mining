import csv
import pandas as pd

#reading the csv file
column_names = ['Language','Sentiment','Entity1']
my_csv = pd.read_csv('Sentiment_by_Language_and_Labels_1.csv',  names=column_names)

#adding columns to variables
sentiment = my_csv.Sentiment.to_list()
classtype = my_csv.Entity1.to_list()
language = my_csv.Language.to_list()

#making a new csv file
with open("Sentiment_by_Language_and_Labels_labelled.csv", 'w', encoding = "utf-8") as f:
    fieldnames = ['ID', 'Label','Sentiment','Language']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    #see if what the language is. if that is the case the _languages to the entity
    for i in range (1, len(language)):
        if language[i] == "Netherlands":
            entity_sen1 = classtype[i] + "_nl"
            print(entity_sen1)
        if language[i] == "Germany":
            entity_sen1 = classtype[i] + "_de"
            print(entity_sen1)
        if language[i] == "France":
            entity_sen1 = classtype[i] + "_fr"
            print(entity_sen1)
        if language[i] == "Great-Britain":
            entity_sen1 = classtype[i] + "_en"
            print(entity_sen1)

        #writing the csv row
        sentiment1 = sentiment[i]
        language1 = language[i]
        label1 = entity_sen1
        writer.writerow({'ID': i-1,'Label' : label1, 'Sentiment' : sentiment1, 'Language': language1})

        print(i)
        i = i +1
