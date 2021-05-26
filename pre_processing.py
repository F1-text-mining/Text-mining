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
#load spacy
nlp = spacy.load('fr_core_news_sm')
#load the article data csv
column_names = ['Index', 'Title', 'Link', 'Content']
my_csv = pd.read_csv('article_data_fr.csv',  names=column_names)
letters = my_csv.Link.to_list()
titles = my_csv.Title.to_list()
contents = my_csv.Content.to_list()

#look for float in the data 
contents_no_float = []
for word in contents:
    if type(word) == float:
        no_float = re.sub('(?<=\d)[,\.]', '', str(word))
        contents_no_float.append(no_float)
    else:
        contents_no_float.append(word)

#transform the text to lowercase
lowercase_text = []
for words in contents_no_float:
    lowercase_text.append(str.lower(words))
content = lowercase_text

i = 0
#call the tokenizer
tokenizer = RegexpTokenizer(r'\w+')


#create a new csv file
with open('fr_pos_processed.csv', 'w', encoding = "utf-8") as csvFile:
    fieldnames = ['Index', 'Title', 'Content_proc']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (1, len(content)):
        #tokenize
        tokenized_word=tokenizer.tokenize(content[i])
        
        #remove stop words

        #stop_words=set(stopwords.words("german"))
        #stop_words=set(stopwords.words("english"))
        #stop_words=set(stopwords.words("italian"))
        #stop_words=set(stopwords.words("dutch"))
        stop_words=set(stopwords.words("french"))
        #remove stop words
        filt_content=[]
        for k in tokenized_word:
            if k not in stop_words:
                filt_content.append(k)
        #pos tag and lemmatize
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
        #write a row to the csv file
        writer.writerow({'Index': Index, 'Title': Title, 'Content_proc': word_stemming })

        print(i)
        i = i +1

        







#nltk.download(["stopwords", "punkt","averaged_perceptron_tagger"])
