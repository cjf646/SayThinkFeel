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



class Record(Screen):
    score = 0

    def change(self, number):
        self.ids['spinner_id'].background_color = 1.0, 0.0, 0.0, 1.0
        self.ids.timer.text = 'speaak'


    def displayResult(self):

        text = micRecord()
        if text == "Did not recognize what you said":
            return


        self.ids.input.text = f'{text}'


        data = dataStore(text)








    number = NumericProperty(5)


    def __init__(self, **kwargs):
        # The super() builtin
        # returns a proxy object that
        # allows you to refer parent class by 'super'.
        super(Record, self).__init__(**kwargs)

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
        sm.add_widget(Record(name="Record"))


        return sm






if __name__ == "__main__":
    MyApp().run()

