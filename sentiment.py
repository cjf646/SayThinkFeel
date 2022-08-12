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


from datetime import date, timedelta

import matplotlib.pyplot as plt
import pyrebase

global user

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
        return sent
    else:
        score_count = newScore(human_sentiment)
        df2 = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        tim = time.localtime()
        current_time = time.strftime("%H:%M:%S", tim)

        date = datetime.date.today()
        index = 0
        # df2.to_pickle("check.pkl")
        saved = pd.read_pickle("check.pkl")
        df2.loc[index] = date, current_time, input, human_sentiment, score_count
        updated_df2 = pd.concat([df2, saved])
        updated_df2.to_pickle("check.pkl")
        saved = pd.read_pickle("check.pkl")
        # print(df2)
        print(saved)
    return human_sentiment




def newScore(human_sentiment):
    if human_sentiment == 'Positive':
        score_count = 1
    elif human_sentiment == 'Negative':
        score_count = -1
    else:
        score_count = 0

    return score_count



def micRecord():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)
    with my_mic as source:

        print("Say now!!!!")
        audio = r.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        text = r.recognize_google(audio)
    except Exception as e:
        print("Sorry i didn't catch that...")
        text = "Did not recognize what you said"

    return text

def dataStore(df, text, sent, score_count):
    firebaseConfig = {'apiKey': "AIzaSyD71Nc2uaXn9fQxAmuCGcTiVdcCyulGdg0",
                      'authDomain': "login-236e7.firebaseapp.com",
                      'databaseURL': "https://login-236e7-default-rtdb.firebaseio.com",
                      'projectId': "login-236e7",
                      'storageBucket': "login-236e7.appspot.com",
                      'messagingSenderId': "566019922271",
                      'appId': "1:566019922271:web:89e59f0b662a6915127eea",
                      'measurementId': "G-7PVGP9KFRR"}

    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    auth = firebase.auth()

    tim = time.localtime()
    current_time = time.strftime("%H:%M:%S", tim)

    date = datetime.date.today()
    d = date.strftime("%B %d, %Y")
    # Firebase testing







    index = 0
    # df.to_pickle("file.pkl")
    saved = pd.read_pickle("file.pkl")
    df.loc[index] = date, current_time, text, sent, score_count
    updated_df = pd.concat([df, saved])
    updated_df.to_pickle("file.pkl")
    saved = pd.read_pickle("file.pkl")
    saved['Points'] = pd.to_numeric(saved['Points'])
    Total_Day_Points = (saved.loc[saved['Date'] == date, 'Points']).sum()
    All_Time_Points = saved['Points'].sum()
    print("Your all time score is: ", All_Time_Points)
    # All_time_Points = saved['Points'].sum()
    print("Your day score is: ", Total_Day_Points)
    print(date)

    date_grouped = saved.groupby('Date')['Points'].sum()
    print(date_grouped)
    print(saved)
    # date_grouped.plot(x='Date', y='Points', kind='bar')
    # plt.show()


    saved['Date'] = pd.to_datetime(saved['Date']) - pd.to_timedelta(7, unit='d')

    # calculate sum of values, grouped by week
    week = saved.groupby([pd.Grouper(key='Date', freq='W')])['Points'].sum()
    print(week)

    import firebase_admin
    from firebase_admin import credentials
    from firebase_admin import auth
    # cred = credentials.Certificate("path/to/serviceAccountKey.json")
    # firebase_admin.initialize_app(cred)
    # user = auth.get_user(uid)
    # print(user)

    # user_id = A
    # user_id = auth.user_id
    # print(user_id)
    # user_id = auth.get_user_by_email(username)
    # data = {'Date': d, 'Time': current_time, 'Text': text, 'Sentiment': sent, 'Score_count': score_count}
    # db.child("Users").child(getId()).set(data)

    # print(saved)
    # print(Total_Day_Points)
    return Total_Day_Points




# def score(df):
#     saved = pd.read_pickle("file.pkl")
#     # saved['Points'] = pd.to_numeric(saved['Points'])
#     All_Time_Points = saved.loc['Points'].sum()
#     print("Your all time score is: ", All_Time_Points)

# def dataBasePositivityGame(text, sent, score_count):
#     from firebase import firebase
#
#     firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
#
#     data = {
#         'Text': text,
#         'Sentiment': sent,
#         'Score_count': score_count
#
#     }
#     result = firebase.get('login-236e7-default-rtdb/Users/PositivityGame', '')
#
#     firebase.post('login-236e7-default-rtdb/Users', data)
#     print(result)





