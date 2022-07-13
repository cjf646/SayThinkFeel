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
from kivy.uix.floatlayout import FloatLayout
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

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
     pass

class SignInWindow(Screen):
    pass

class emotionalIntelligence(Screen):

    def emotionsSaved(self, emotion):

        df_emotion = pd.DataFrame(columns=['Date', 'Time', 'Emotion'])

        emotion_data = emotionSaved(df_emotion, emotion)

# class WindowManager(ScreenManager):
#     pass




class MyGrid2(Screen):
    score = 0

    def displayResult(self):
        df = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        score = 0
        text = micRecord(r)

        sent = getPolarity(text)
        score_count = positivity_count(sent, score)

        self.ids.scorechange.text = f'Score: {score_count}'
        self.ids.input2.text = f'{sent}'
        self.ids.input.text = f'{text}'

        # human_sentiment = self.ids.spinner_id.text
        #
        # checking_sentiment = check_Sentiment(sent, human_sentiment, text)
        # if checking_sentiment == 'GOOD':
        data = dataStore(df, text, sent, score_count)
        self.ids.totalscore.text = f'Todays score: {data}'

    def store(self, human_sentiment, sent, input):
        print(input)
        print(human_sentiment)
        check_Sentiment(sent, human_sentiment, input)




class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstWindow(name="FirstWindow"))
        sm.add_widget(MyGrid2(name="MyGrid2"))
        sm.add_widget(SecondWindow(name="SecondWindow"))
        sm.add_widget(SignInWindow(name="SignIn Window"))
        sm.add_widget(emotionalIntelligence(name="emotionalIntelligence"))

        return sm

if __name__ == "__main__":
    MyApp().run()