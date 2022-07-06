#library that contains punctuation
import string
string.punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import pickle


from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
import time
import speech_recognition as s_r
import pyttsx3 as s
from datetime import datetime

import nltk
import pandas as pd
import numpy as np
import re
from transformers import pipeline
import datetime


import pymongo
from pymongo import MongoClient


def getPolarity(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < 0:
        return 'Negative'
    elif sentiment == 0:
        return 'Neutral'
    elif (sentiment > 0) & (sentiment <= 1):
        return 'Positive'

def positivity_count(sent, score):
    if sent == 'Positive':
        final_score = score + 1
        return f'{final_score}'
    elif sent == 'Negative':
        final_score = score - 1
        return f'{final_score}'

    elif sent == 'Neutral':
        final_score = score
        return final_score

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
    # if subj > 0.5:
    #     return "Objective"
    # elif (subj > 0) & (subj < 0.5):
    #     return "Subjective"

def check_Sentiment(sent, human_sentiment, input):
    if sent == human_sentiment:
        # print("GOOD CLASSIFICATION")
        return 'GOOD'
    else:
        score_count = newScore(human_sentiment)
        df2 = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        tim = time.localtime()
        current_time = time.strftime("%H:%M:%S", tim)

        date = datetime.date.today()
        index = 0
        # df2.to_pickle("file_check.pkl")
        saved = pd.read_pickle("file_check.pkl")
        df2.loc[index] = date, current_time, input, human_sentiment, score_count
        updated_df2 = pd.concat([df2, saved])
        updated_df2.to_pickle("file_check.pkl")
        saved = pd.read_pickle("file_check.pkl")

        print(saved)
    return human_sentiment

r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)


def newScore(human_sentiment):
    if human_sentiment == 'Positive':
        score_count = 1
    elif human_sentiment == 'Negative':
        score_count = -1
    else:
        score_count = 0

    return score_count



def micRecord(r):
    with my_mic as source:

            print("Say now!!!!")
            audio = r.listen(source, phrase_time_limit=5)
            text = r.recognize_google(audio)
    return text

def dataStore(df, text, sent, score_count):

    tim = time.localtime()
    current_time = time.strftime("%H:%M:%S", tim)

    date = datetime.date.today()
    index = 0
    # df.to_pickle("file.pkl")
    saved = pd.read_pickle("file.pkl")
    df.loc[index] = date, current_time, text, sent, score_count
    updated_df = pd.concat([df, saved])
    updated_df.to_pickle("file.pkl")
    saved = pd.read_pickle("file.pkl")
    saved['Points'] = pd.to_numeric(saved['Points'])
    Total_Day_Points = (saved.loc[saved['Date'] == date, 'Points']).sum()
    # All_time_Points = saved['Points'].sum()
    print(saved)
    print(Total_Day_Points)
    return Total_Day_Points