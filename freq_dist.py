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
from collections import Counter
import collections

column_names = ['Index', 'Title', 'Content_proc']
my_csv = pd.read_csv('german_processed.csv',  names=column_names)
lst = my_csv.Content_proc.to_list()

#processed_content1 = str(processed_content)
def convert(lst):
    return([i for item in lst for i in item.split()])

splitw = convert(lst)


fdist = FreqDist(splitw)
fdist.plot(30,cumulative=False)
plt.show()
