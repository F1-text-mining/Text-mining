import csv
import pandas as pd
import string
import re
import nltk
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.cistem import Cistem
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from treetagger import TreeTagger
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import spacy

nlp = spacy.load('fr_core_news_sm')

column_names = ['Index', 'Title', 'Link', 'Content']
my_csv = pd.read_csv('article_data_fr.csv',  names=column_names)
letters = my_csv.Link.to_list()
titles = my_csv.Title.to_list()
contents = my_csv.Content.to_list()

contents_no_float = []
for word in contents:
    if type(word) == float:
        no_float = re.sub('(?<=\d)[,\.]', '', str(word))
        contents_no_float.append(no_float)
    else:
        contents_no_float.append(word)


lowercase_text = []
for words in contents_no_float:
    lowercase_text.append(str.lower(words))
content = lowercase_text

i = 0

tokenizer = RegexpTokenizer(r'\w+')



with open('fr_pos_processed.csv', 'w', encoding = "utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Content_proc']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (1, len(content)):

        tokenized_word=tokenizer.tokenize(content[i])

        #pos_tagged_total = []
        #for sent in tokenized_word:
        #pos_tagged = pos_tag(tokenized_word)
            #pos_tagged_total.append(pos_tagged)
        #print(pos_tagged)

        #stop_words=set(stopwords.words("german"))
        #stop_words=set(stopwords.words("english"))
        #stop_words=set(stopwords.words("italian"))
        #stop_words=set(stopwords.words("dutch"))
        stop_words=set(stopwords.words("french"))

        filt_content=[]
        for k in tokenized_word:
            if k not in stop_words:
                filt_content.append(k)


        #stemming = SnowballStemmer("german")
        #stemming = SnowballStemmer("english")
        #stemming = SnowballStemmer("italian")
        #stemming = SnowballStemmer("dutch")
        #stemming = SnowballStemmer("french")

        word_stemming=[]
        #lemmatizer = WordNetLemmatizer() #english
        for word, tag in TextBlob(filt_content, pos_tagger=PatternTagger()):
            if tag.startswith('NN'):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'
            print(word, pos)
            word_stemming.append(nlp(word, pos))

        Title = titles[i]
        Index = i

        writer.writerow({'Index': Index, 'Title': Title, 'Content_proc': word_stemming })

        print(i)
        i = i +1

        if i == 10:
            break







#nltk.download(["stopwords", "punkt","averaged_perceptron_tagger"])
