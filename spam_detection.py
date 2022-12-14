# -*- coding: utf-8 -*-
"""spam-detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SSo1-yXke47XrQpB-3A_IjE8B0jEx_A1
"""

#import libraries
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from google.colab import files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_recall_fscore_support,classification_report,accuracy_score

uploaded = files.upload()

df = pd.read_csv('spam_ham_dataset.csv')
df

df.drop(df.columns[[0, 1]], axis=1, inplace=True)

df

#check for dupes and remove
df.drop_duplicates(inplace=True)

df.shape

#check if any missing data is present
df.isnull().sum()

#download stop words, in order to match and remove them from the emails
nltk.download('stopwords')

def process_text(text):
  #1 remove punctuation
  nopunc = [char for char in text if char not in string.punctuation]
  nopunc = ''.join(nopunc)

  #2 remove stop words
  clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

  #3 return a clean list of tokenized words
  return clean_words

df['text'].head().apply(process_text)

print(CountVectorizer(analyzer=process_text).fit_transform(["hello my name is hasan burney hello"]))

vectorized_msgs = CountVectorizer(analyzer=process_text).fit_transform(df['text'])

X_train,X_test,y_train,y_test = train_test_split(vectorized_msgs,df['label_num'],test_size=0.2,random_state=0)

classifier = MultinomialNB().fit(X_train,y_train)

accuracy = accuracy_score(y_test,classifier.predict(X_test))

print(accuracy)

print(classification_report(y_test,classifier.predict(X_test)))