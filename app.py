import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re

tweets = pd.read_csv('sentiment_tweets3.csv')

tweets.drop(['Unnamed: 0'], axis = 1, inplace = True)

tweets['label'].value_counts()


totalTweets = 8000 + 2314
trainIndex, testIndex = list(), list()
for i in range(tweets.shape[0]):
    if np.random.uniform(0, 1) < 0.98:
        trainIndex += [i]
    else:
        testIndex += [i]
trainData = tweets.iloc[trainIndex]
testData = tweets.iloc[testIndex]

trainData['label'].value_counts()
testData['label'].value_counts()

depressive_words = ' '.join(list(tweets[tweets['label'] == 1]['message']))
positive_words = ' '.join(list(tweets[tweets['label'] == 0]['message']))


