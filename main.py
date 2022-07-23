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



# from kivy.uix.colorpicker import ColorPickerApp

# x = [1,2,3,4,5]
# y = [5, 12, 6, 9, 15]
#
# plt.plot(x,y)
# plt.ylabel("This is MY Y Axis")
# plt.xlabel("X Axis")



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





class MyApp(MDApp):
    def build(self):

        sm = ScreenManager()
        sm.add_widget(SignInSignUp(name="SignInSignUp"))
        sm.add_widget(MyGrid2(name="MyGrid2"))
        sm.add_widget(SecondWindow(name="SecondWindow"))
        sm.add_widget(SignInWindow(name="SignInWindow"))
        sm.add_widget(emotionalIntelligence(name="emotionalIntelligence"))
        sm.add_widget(Statistics(name="Statistics"))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        sm.add_widget(MyEmotionPopup(name="MyEmotionPopup"))
        # sm.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        sm.add_widget(statPage(name="statPage"))



        # sm.add_widget(Popup(name="Popup"))
        # sm.add_widget(SignIn(name="SignIn"))
        # sm.add_widget(Matty(name="Matty"))
        # box = self.ids.box
        # sm.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        return sm

    def emotionpopup(self):
        pass

    # def MyMDCard(self):
    #     self.theme_cls.theme_style = "Dark"
    #     self.theme_cls.primary_palette = "BlueGray"
    #     return Builder.load_file('my.kv')

if __name__ == "__main__":
    MyApp().run()