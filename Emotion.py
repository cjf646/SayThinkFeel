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

from main import *

def emotionSaved(df_emotion, emotion):
    tim = time.localtime()
    current_time = time.strftime("%H:%M:%S", tim)

    date = datetime.date.today()
    index = 0
    # df_emotion.to_pickle("file2.pkl")
    saved2 = pd.read_pickle("file2.pkl")
    df_emotion.loc[index] = date, current_time, emotion
    updated_df = pd.concat([df_emotion, saved2])
    updated_df.to_pickle("file2.pkl")
    saved2 = pd.read_pickle("file2.pkl")

    print(saved2)


# def emotionDatabase(emotion):
#     tim = time.localtime()
#     current_time = time.strftime("%H:%M:%S", tim)
#
#     date = datetime.date.today()
#     from firebase import firebase
#
#     firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
#
#
#     data = {
#         'Time': current_time,
#         'Date': date,
#         'Emotion': emotion
#     }
#     # username = saveUsername(username)
#     # user = SignIn()
#     # print(user)
#     result = firebase.get('login-236e7-default-rtdb/Users', '')
#     for i in result.keys():
#         if result[i]['Username'] == user:
#             # print(username + "Username already exists")
#
#             firebase.post('login-236e7-default-rtdb/Users/FeelingTracker', data)
#             print(result)


