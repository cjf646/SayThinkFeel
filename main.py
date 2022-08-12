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

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from threading import Thread
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ColorProperty
import time

from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine

from kivy.utils import rgba

class Welcome(Screen):
    def next(self):
        self.ids.carousel.load_next(mode="next")

    def current_slide(self, index):
        for i in range(4):
            if index == i:
                self.ids[f"slide{index}"].text_color = rgba(111, 206, 203, 255)
            elif index != i:
                self.ids[f"slide{i}"].text_color = rgba(221, 221, 221, 255)

class Support(Screen):

    def on_enter(self):
        for i in range(10):
            self.ids.box.add_widget(MDExpansionPanel(icon="brain.jpg",content=Support(),panel_cls=MDExpansionPanelThreeLine(text="Text", secondary_text="Secondary Text", tertiary_text="Tertiary Text")))


class VerifyText(Screen):

    def on_enter(self, *args):
        self.manager.get_screen("VerifyText").ids.spokentext.text = self.manager.get_screen("PositivityGame").ids.input2.text

    def storeResult(self, text):
        df = pd.DataFrame(columns=['Date', 'Time', 'Sentence', 'Sentiment', 'Points'])
        score = 0

        sent = getPolarity(text)
        score_count = positivity_count(sent, score)

        self.ids.sentiment.text = f'Score: {score_count}'

        data = dataStore(df, text, sent, score_count)

        self.ids.total.text = f'Todays score: {data}'

        self.manager.get_screen("PositivityGame").ids.scorechange.text = self.manager.get_screen("VerifyText").ids.sentiment.text
        self.manager.get_screen("PositivityGame").ids.totalscore.text = self.manager.get_screen("VerifyText").ids.total.text

        self.ids.sentiment.text = ""
        self.ids.total.text = ""

    def onNo(self):
        self.manager.get_screen("PositivityGame").ids.scorechange.text = self.manager.get_screen("VerifyText").ids.sentiment.text
        self.manager.get_screen("PositivityGame").ids.totalscore.text = self.manager.get_screen("VerifyText").ids.total.text


class statPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        sentimentPoints()
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

class MyPopup2(Screen):
    pass

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
    def send_data(self, email, username, password):
        sign_up_check = checkUsernameExists(email, username, password)
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


class Statistics(Screen):
    pass
    # def statisticsView(self):

class SignInSignUp(Screen):
    pass

class MyEmotionPopup(Screen):
    pass

class PositivityGame(Screen):
    DONE = False
    score = 0

    def change(self, number):
        self.ids['spinner_id'].background_color = 1.0, 0.0, 0.0, 1.0
        self.ids.timer.text = 'speaak'

    def text(self):

        text = micRecord()
        if text == "Did not recognize what you said":
            return

        time.sleep(0.5)
        self.ids.input2.text = f'{text}'

    def store(self, human_sentiment, sent, input):
        print(input)
        print(human_sentiment)
        check_Sentiment(sent, human_sentiment, input)
        # self.ids.spinner_id.text = f'RUN AGAIN'



    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.event = None
        self.t = None

    def trigger(self):
        self.t = Thread(target=self.text, daemon=True)
        self.t.start()
        self.event = Clock.schedule_interval(self.update_counter, 1.0)
        self.event()

    def update_counter(self, *args):
        # print("Counter is being updated!")
        self.ids.spinner_id.text = "Begin Speaking!"
        self.ids.timer.text = str(int(self.ids.timer.text) - 1)
        if int(self.ids.timer.text) == -1:

            time.sleep(0.5)
            self.ids.spinner_id.text = "Press to run again"
            self.ids.timer.text = "4"


            self.manager.current = "VerifyText"


            # print("The counter will reset now")

            self.event.cancel()





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

        sm.add_widget(MyPopup2(name="MyPopup2"))

        sm.add_widget(VerifyText(name="VerifyText"))
        sm.add_widget(Support(name="Support"))


        sm.add_widget(Welcome(name="Welcome"))
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



