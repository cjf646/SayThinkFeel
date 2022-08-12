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


def checkUsernameExists(email, username, password):
    from firebase import firebase
    import pyrebase
    firebaseConfig = {'apiKey': "AIzaSyD71Nc2uaXn9fQxAmuCGcTiVdcCyulGdg0",
                      'authDomain': "login-236e7.firebaseapp.com",
                      'databaseURL': "https://login-236e7-default-rtdb.firebaseio.com",
                      'projectId': "login-236e7",
                      'storageBucket': "login-236e7.appspot.com",
                      'messagingSenderId': "566019922271",
                      'appId': "1:566019922271:web:89e59f0b662a6915127eea",
                      'measurementId': "G-7PVGP9KFRR"}

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # user = auth.get_user(uid)
    # print(user)
    # firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)

    # data = {
    #     'Username': username,
    #     'Password': password,
    #     'Number': number
    # }
    # result = firebase.get('login-236e7-default-rtdb/Users', '')


    # for i in result.keys():
    #     if result[i]['Username'] == username:
    #         print(username + "Username already exists")
    #         return
    #     elif (data['Username'] == "") | (data['Password'] == "") | (data['Number'] == ""):
    #         print("Please fill in all existing fields!")
    #         return

    user = auth.create_user_with_email_and_password(email, password)
    # uid = firebase.auth(user)
    print(user['localId'])
    # user['localId'] = username
    # print(user['localId'])

    # custom_token = auth.create_custom_token(username)
    print("SUCCESS")
    # firebase.post('login-236e7-default-rtdb/Users', data)
    return '1'






    # from firebase import firebase

    # firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)

    # data = {
    #     'Username': username,
    #     'Password': password,
    #     'Number': number
    # }
    # result = firebase.get('login-236e7-default-rtdb/Users', '')

    # for i in result.keys():
    #     if result[i]['Username'] == username:
    #         print(username + "Username already exists")
    #         return
    #     elif (data['Username'] == "") | (data['Password'] == "") | (data['Number'] == ""):
    #         print("Please fill in all existing fields!")
    #         return


    # firebase.post('login-236e7-default-rtdb/Users', data)
    # return '1'








#On login press, checkusername will run
def checkUsernamePasswordCorrect(username, password):
    from firebase import firebase
    import pyrebase
    firebaseConfig = {'apiKey': "AIzaSyD71Nc2uaXn9fQxAmuCGcTiVdcCyulGdg0",
                      'authDomain': "login-236e7.firebaseapp.com",
                      'databaseURL': "https://login-236e7-default-rtdb.firebaseio.com",
                      'projectId': "login-236e7",
                      'storageBucket': "login-236e7.appspot.com",
                      'messagingSenderId': "566019922271",
                      'appId': "1:566019922271:web:89e59f0b662a6915127eea",
                      'measurementId': "G-7PVGP9KFRR"}

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()


    try:
        # global login
        login = auth.sign_in_with_email_and_password(username, password)
        global user
        user = auth.current_user['localId']

        print(user)
        return '1'
    except:
        return 'not good'






    # from firebase import firebase
    # firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
    # result = firebase.get('login-236e7-default-rtdb/Users', '')
    #
    #
    # for i in result.keys():
    #     if result[i]['Username'] == username:
    #         if result[i]['Password'] == password:
    #             print(username + "Logged In!")
    #
    #             return '1'
    #         else:
    #             print("Invalid Username or password")
    #             return 'not good'
