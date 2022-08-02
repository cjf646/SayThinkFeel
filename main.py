import kivy
import urllib
import bs4
import pandas as pd
import numpy as np
import pickle


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle, RoundedRectangle

from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivymd.theming import ThemeManager

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from sklearn.preprocessing import MinMaxScaler
from datetime import timedelta
# from kivy_garden.graph import Graph, MeshLinePlot

# importing image widget of kivy framework
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.spinner import Spinner
# importing boxlayout for our application
from kivy.uix.boxlayout import BoxLayout
from sentiment import *
from Emotion import *
from statistics import *
from login import *


# from graphs import *

from kivymd.uix.textfield import MDTextField
import kivymd


from kivymd.theming import ThemeManager
from kivy.core.window import Window



# Graph Dependencies
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

from kivy.properties import NumericProperty
from kivy.clock import Clock
# from kivy.uix.colorpicker import ColorPickerApp




class statPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        sentimentPoints()
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    # def displayGraph(self):

        # graph1 = sentimentPoints()
        # self.ids.box.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # self.ids.box = f'{graph1}'



#     def save_it(self):
#         pass


# Other things to include:
# links to resources to include for people that are not doing well in their mental state

# Additional support
# Challenges



class SelectGames(Screen):
    pass

class SignIn(Screen):
    def sign_in(self, username, password):
        login = checkUsernamePasswordCorrect(username, password)

        print(login)
        if login == '1':
            self.manager.current = 'SelectGames'
            return username

        else:
            self.manager.current = 'SignIn'



class SignUp(Screen):
    def send_data(self, username, password, number):
        sign_up_check = checkUsernameExists(username, password, number)
        print(sign_up_check)
        if sign_up_check == '1':
            self.manager.current = 'SelectGames'
        else:
            self.manager.current = 'SignUp'

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
     pass

class SignInWindow(Screen):
    pass

class feelings(Screen):

    def emotionsSaved(self, emotion):

        df_emotion = pd.DataFrame(columns=['Date', 'Time', 'Emotion'])

        emotion_data = emotionSaved(df_emotion, emotion)
        # emotion_database = emotionDatabase(emotion)
        # print(emotion_database)


class Statistics(Screen):
    pass
    # def statisticsView(self):

class SignInSignUp(Screen):
    pass

# class WindowManager(ScreenManager):
#     pass

# class colorSelector(Screen):
#
#     selected_color = [0,0,1,1]

class MyEmotionPopup(Screen):
    pass



class PositivityGame(Screen):
    score = 0

    def change(self, number):
        self.ids['spinner_id'].background_color = 1.0, 0.0, 0.0, 1.0
        self.ids.timer.text = 'speaak'


        # self.ids.timer.text = f'{number}'

    def displayResult(self):

        df = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        score = 0
        # timer = timeCount()

        # self.ids.timer.text = f'Say Now!!!'

        text = micRecord()
        if text == "Did not recognize what you said":
            return
        sent = getPolarity(text)
        score_count = positivity_count(sent, score)

        self.ids.scorechange.text = f'Score: {score_count}'
        self.ids.input2.text = f'{sent}'
        self.ids.input.text = f'{text}'

        # number = NumericProperty(5)
        #
        # self.ids.timer.text = f'{number}'


        # human_sentiment = self.ids.spinner_id.text
        #
        # checking_sentiment = check_Sentiment(sent, human_sentiment, text)
        # if checking_sentiment == 'GOOD':
        data = dataStore(df, text, sent, score_count)
        # database_store = dataBasePositivityGame(text, sent, score_count)
        # print(database_store)
        self.ids.totalscore.text = f'Todays score: {data}'





    def store(self, human_sentiment, sent, input):
        print(input)
        print(human_sentiment)
        check_Sentiment(sent, human_sentiment, input)
        # self.ids.spinner_id.text = f'RUN AGAIN'

    number = NumericProperty(5)


    def __init__(self, **kwargs):
        # The super() builtin
        # returns a proxy object that
        # allows you to refer parent class by 'super'.
        super(PositivityGame, self).__init__(**kwargs)

        # Create the clock and increment the time by .1 ie 1 second.
        Clock.schedule_interval(self.increment_time, .1)

        self.increment_time(5)

    # To increase the time / count
    def increment_time(self, interval):
        self.number -= .1

    # To start the count
    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)


class MyApp(MDApp):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(SignInSignUp(name="SignInSignUp"))
        sm.add_widget(PositivityGame(name="PositivityGame"))
        sm.add_widget(SecondWindow(name="SecondWindow"))
        sm.add_widget(SignInWindow(name="SignInWindow"))
        sm.add_widget(feelings(name="feelings"))
        sm.add_widget(Statistics(name="Statistics"))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(MyEmotionPopup(name="MyEmotionPopup"))
        # sm.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        sm.add_widget(statPage(name="statPage"))
        sm.add_widget(SignIn(name="SignIn"))
        sm.add_widget(SignUp(name="SignUp"))


        sm.add_widget(SelectGames(name="SelectGames"))
        # sm.add_widget(Popup(name="Popup"))
        # sm.add_widget(SignIn(name="SignIn"))
        # sm.add_widget(Matty(name="Matty"))
        # box = self.ids.box
        # sm.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return sm

    def emotionpopup(self):
        pass

    # def send_data(self, username, password, number):
    #     from firebase import firebase
    #
    #     firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
    #
    #     data = {
    #         'Username': username,
    #         'Password': password,
    #         'Number': number
    #
    #     }
    #     result = firebase.get('login-236e7-default-rtdb/Users', '')
    #
    #
    #
    #
    #     for i in result.keys():
    #
    #
    #         if result[i]['Username'] == username:
    #             print(username + "Username already exists")
    #             return

        # firebase.post('login-236e7-default-rtdb/Users', data)


    def sign_in(self, username, password):
        pass



    def send_data(self, username, password, number):
        pass
        # from firebase import firebase
        # firebase = firebase.FirebaseApplication('https://login-236e7-default-rtdb.firebaseio.com/', None)
        # result = firebase.get('login-236e7-default-rtdb/Users', '')
        # for i in result.keys():
        #     if result[i]['Username'] == username:
        #         if result[i]['Password'] == password:
        #             print(username + "Logged In!")
        #     else:
        #         print("Invalid Username or password")




                # Does not like ids, to display on screen for some reason
                # self.ids.login.text = f"Invalid Username or password, Try Again"


if __name__ == "__main__":
    MyApp().run()