# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:02:06 2022

@author: Suyog
"""

import streamlit as st
import pickle
from nltk.corpus import stopwords
import string
from nltk.stem import PorterStemmer
import nltk

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
     
    text = y[:]
    y.clear()
    for i in text:
        if i not in string.punctuation and i not in stopwords.words('english'):
            y.append(i)
    
    text = y[:]
    y.clear()
    
    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area('Enter the Message')
if st.button('predict'):

    #1. Preprocess
    transformed_sms = transform_text(input_sms)
    #2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
    #3. Predict
    result = model.predict(vector_input)[0]
    #4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")