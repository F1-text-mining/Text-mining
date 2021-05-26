import csv
import pandas as pd
#Loading Node csv file
column_names = ['ID', 'Label','Sentiment','Language']
my_csv = pd.read_csv('Sentiment_by_Language_and_Labels_labelled.csv',  names=column_names)

#adding columns to a variable
classtype = my_csv.Label.to_list()
id = my_csv.ID.to_list()

#Loading relation file
column_names = ['Source','Sentiment','Target']
df = pd.read_csv('edges.csv',  names=column_names)

#adding columns to a variable
sources = df.Source.to_list()
targets = df.Target.to_list()
sent = df.Sentiment.to_list()

#Create new csv file
with open("edges.csv", 'w', encoding = "utf-8") as f:
    #write columnnames
    fieldnames = ['Source','Target','Sentiment']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    
    for i in range(1, len(sources)):
        sourc = None
        targ = None
        for k in range(1, len(classtype)):
            #see if labels are the same as the entity
            if sources[i] == classtype[k]:
                sourc = id[k]
                print(sourc)
            if targets[i] == classtype[k]:
                targ = id[k]
                print(targ)

        sent1 = sent[i]
        #write the csv rows
        if targ != None:
            writer.writerow({'Source': sourc, 'Target': targ, 'Sentiment': sent1 })

        print(i)
        i = i +1
