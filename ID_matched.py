import csv
import pandas as pd

column_names = ['ID', 'Label','Sentiment','Language']
my_csv = pd.read_csv('Sentiment_by_Language_and_Labels_labelled.csv',  names=column_names)

classtype = my_csv.Label.to_list()
id = my_csv.ID.to_list()

column_names = ['Source','Sentiment','Target']
df = pd.read_csv('edges_love_matus.csv',  names=column_names)

sources = df.Source.to_list()
targets = df.Target.to_list()
sent = df.Sentiment.to_list()

with open("datmagjezelfweten.csv", 'w', encoding = "utf-8") as f:
    fieldnames = ['Source','Target','Sentiment']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, len(sources)):
        sourc = None
        targ = None
        for k in range(1, len(classtype)):
            if sources[i] == classtype[k]:
                sourc = id[k]
                print(sourc)
            if targets[i] == classtype[k]:
                targ = id[k]
                print(targ)

        sent1 = sent[i]
        if targ != None:
            writer.writerow({'Source': sourc, 'Target': targ, 'Sentiment': sent1 })

        print(i)
        i = i +1
