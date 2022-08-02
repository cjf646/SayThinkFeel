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

from main import *


def checkUsernameExists(username, password, number):
    from firebase import firebase

    firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)

    data = {
        'Username': username,
        'Password': password,
        'Number': number

    }
    result = firebase.get('login-236e7-default-rtdb/Users', '')


    for i in result.keys():


        if result[i]['Username'] == username:
            print(username + "Username already exists")
            return
        elif (data['Username'] == "") | (data['Password'] == "") | (data['Number'] == ""):
            print("Please fill in all existing fields!")
            return


    firebase.post('login-236e7-default-rtdb/Users', data)
    return '1'

def checkUsernamePasswordCorrect(username, password):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
    result = firebase.get('login-236e7-default-rtdb/Users', '')
    for i in result.keys():
        if result[i]['Username'] == username:
            if result[i]['Password'] == password:
                print(username + "Logged In!")
                return '1'
            else:
                print("Invalid Username or password")
                return 'not good'
