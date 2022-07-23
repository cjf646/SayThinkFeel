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
import matplotlib.pyplot as plt



# def dateIterator():

def sentimentPoints():
    date = datetime.date.today()
    saved = pd.read_pickle("file.pkl")
    saved['Points'] = pd.to_numeric(saved['Points'])
    Total_Day_Points = (saved.loc[saved['Date'] == date, 'Points']).sum()
    All_Time_Points = saved['Points'].sum()
    # print("Your all time score is: ", All_Time_Points)
    # # All_time_Points = saved['Points'].sum()
    # print("Your day score is: ", Total_Day_Points)
    # print(date)

    date_grouped = saved.groupby('Date')['Points'].sum()
    print(date_grouped)

    graph = date_grouped.plot(x='Date', y='Points', kind='bar')
    # plt.show()


    # graph = date_grouped.plot(x='Date', y='Points', kind='bar')
    # plt.show()

    # saved['Date'] = pd.to_datetime(saved['Date']) - pd.to_timedelta(7, unit='d')
    #
    # # calculate sum of values, grouped by week
    # week = saved.groupby([pd.Grouper(key='Date', freq='W')])['Points'].sum()
    # print(week)

    return graph
