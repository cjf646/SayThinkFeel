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

# class BoxLayoutApp(App):
#
#     def build(self):
#         # To position oriented widgets again in the proper orientation
#         # use of vertical orientation to set all widgets
#         superBox = BoxLayout(orientation='vertical')
#
#         # To position widgets next to each other,
#         # use a horizontal BoxLayout.
#         VB = BoxLayout(orientation='vertical')
#         image = Image(source="youfirst.png")
#         Start_recording_btn = Button(text="Press to to start recording your voice")
#         # btn1 = Button(text="One")
#         # btn2 = Button(text="Two")
#
#         # HB represents the horizontal boxlayout orientation
#         # declared above
#         VB.add_widget(image)
#         VB.add_widget(Start_recording_btn)
#         # VB.add_widget(btn1)
#         # VB.add_widget(btn2)
#
#         # To position widgets above/below each other,
#         # use a vertical BoxLayout.
#         HB = BoxLayout(orientation='horizontal', spacing=1, size_hint=(1,0.1))
#
#
#         Home_btn = Button(text="Home")
#         stats_btn = Button(text="Statistics")
#         account_btn = Button(text="Account")
#
#         # VB represents the vertical boxlayout orientation
#         # declared above
#
#         HB.add_widget(Home_btn)
#         HB.add_widget(stats_btn)
#         HB.add_widget(account_btn)
#
#         # superbox used to again align the oriented widgets
#         superBox.add_widget(VB)
#         superBox.add_widget(HB)
#
#         return superBox
#
#
#
# # creating the object root for BoxLayoutApp() class
# root = BoxLayoutApp()
#
# # run function runs the whole program
# # i.e run() method which calls the
# # target function passed to the constructor.
# root.run()


class MyGrid(Widget):
    score = 0
    # timer = ObjectProperty(None)

    # def countdown(self):
    #     # self.timer.text = "Results"
    #     self.ids.input.text = "okayyyyy"
        # return micRecord()
        #
        # self.ids.on_press.text = display

    # def __init__(self, **kwargs):
    #     super(MyGrid, self).__init__(**kwargs)
    #     self.lbl = self.ids['input']
    #     self.btn = self.ids['btn']


    def displayResult(self):
        # change_btn = self.ids.btn.text
        # self.ids.btn.text = "Start Speaking"
        df = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        # self.ids.label.text = 'Recording on'
        score = 0
        text = micRecord(r)
        sent = getPolarity(text)
        score_count = positivity_count(sent, score)

        self.ids.scorechange.text = f'Score: {score_count}'
        self.ids.input2.text = f'{sent}'
        # show_text = self.ids.btn.text
        self.ids.input.text = f'{text}'

        data = dataStore(df, text, sent, score_count)
        self.ids.totalscore.text = f'Todays score: {data}'
        # self.ids.spinner_id.text = f'Press to start recording again...'
        # return sent
        # self.ids.spinner_id.text = f'{value}'

    def store(self, human_sentiment, sent, input):
         # self.ids.spinner_id.text = human_sentiment
        # self.ids.input2.text = sent
        # check = check_sentiment(sentiment, human_sentiment)
        # self.ids.input2.text = f'{sent}'

        print(input)
        # print(sent)
        # print(human_sentiment)


        print(check_Sentiment(sent, human_sentiment, input))
        self.ids.spinner_id.text = 'Press to run again...'
        # store_reclassfied_sent = storeNewSentiment(check)

        # self.ids.spinner_id.text = f'Press to start recording again...'
        # check_Sentiment(sentiment, human_sentiment)
        # print(sent)
        # if value == sent:
        #     print("Sentiment are equal")
        # else:
        #     print("Sentiment WRONG")

            # return MyGrid()


    # def sentiment_clicked(self, value):
    #     self.ids.click_label.text = f'{value}'
        # analysis()

        # print(show_text)

    # def analysis(text):
    #     text = change_lbl(text)
    #     sent = getPolarity(text)
    #     self.ids.input2.text = f'Sentiment: {sent}'





        # display(self, text)

    # def display(self, text):
    #     self.lbl.text = self.text
    # def micRecord(self, *args):
    #      micRecord(r)


    # def set_text(self, Text):
    #     self.root.ids.input.text = out_encrypt
    # def displayInput(self):
    #     display = self.ids.input.text
    #
    #     self.ids.micRecord(r).text = display
    #     return display
    #

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()