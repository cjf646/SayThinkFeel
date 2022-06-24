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

#
#
# class firstWindow(Screen):
#     def next(self):
#         show_popup().open()
#

# from kivy.uix.button import ButtonBehavior
# class MainApp(App):
#     them_cls = ThemeManager()
#
#
# MainApp().run()



class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1


        self.window.add_widget(Image(source="youfirst.png"))
        self.greeting = Label(text="What's your name?")
        self.window.add_widget(self.greeting)

        self.user = TextInput(multiline=False)
        self.window.add_widget(self.user)

        self.button = Button(text="Press to to start recording your voice")

        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + "!"






        # self.Button = Button(text="PushMe")
        # self.window.add_widget(self.Button)

    # def pressed(self, instance):
    #     name = self.name.text
    #     last = self.lastName.text
    #     email = self.email.text
    #     print("Name:", name, "Last Name:", last, "Email:", email)
    #     self.name.text = ""
    #     self.lastName.text = ""
    #     self.email.text = ""
    #     print("Pressed")

if __name__ == "__main__":
    SayHello().run()



# Builder.load_file('my.kv')
#
# class MyLayout(Widget):
#     pass
#
# class MyApp(App):
#     def build(self):
#         # Window.clearcolor = (1,1,1,1)
#         return MyLayout()

# class ImageButton(Button, Image):
#     pass
#
#
# class MainApp(App):
#     pass
#
#
# MainApp().run()

# class SayThinkFeel(App):
#     def build(self):
#         self.window = GridLayout()
#         # btn.Button = GridLayout()
#         #add widgets to window
#         # self.window = GridLayout()
#         self.window.cols = 2
#
#         #image widget
#         self.window.add_widget(Image(source="youfirst.png"))
#         # btn = Button(text="push me")
#
#         # btn.Button(text="Push Me",size_hint=(.2,.2),pos=(300,250))
#         # self.window.add_widget(Button, "Hello")
#
#         return self.window

    # def button(self):
    #     btn = Button(text="push me")
    #     return btn





# class ButtonApp(App):
#
#     def build(self):
#         # create an image a button
#         # Adding images normal.png image as button
#         # decided its position and size
#         btn = Button(text="Push Me !",
#                      color=(1, 0, .65, 1),
#                      background_normal='youfirst.png',
#                      background_down='think-feel-do.png',
#                      size_hint=(.3, .3),
#                      pos_hint={"x": 0.35, "y": 0.3}
#                      )
#
#         return btn


# root = ButtonApp()
#
# # run function runs the whole program
# # i.e run() method which calls the target
# # function passed to the constructor.
# root.run()
#

# if __name__ == "__main__":
#     SayThinkFeel().run()




# class MyGrid(GridLayout):
#
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 2
#
#         self.add_widget(Label(text="First Name: "))
#         self.name = TextInput(multiline=False)
#         self.add_widget(self.name)
#
#         self.add_widget(Label(text="Last Name: "))
#         self.lastName = TextInput(multiline=False)
#         self.add_widget(self.lastName)
#
#         self.add_widget(Label(text="Email: "))
#         self.email = TextInput(multiline=False)
#         self.add_widget(self.email)
#
#         self.submit = Button(text="Submit", font_size=40)
#         self.add_widget(self.submit)


#         self.inside = GridLayout()
#         self.inside.cols = 2
#
#         # self.cols = 2
#         self.inside.add_widget(Label(text="Name: "))
#         self.name = TextInput(multiline=False)
#         self.inside.add_widget(self.name)
#
#         self.inside.add_widget(Label(text="Last Name: "))
#         self.lastName = TextInput(multiline=False)
#         self.inside.add_widget(self.lastName)
#
#         self.inside.add_widget(Label(text="Email: "))
#         self.email = TextInput(multiline=False)
#         self.inside.add_widget(self.email)
#
#         self.add_widget(self.inside)
#
#
#
#         self.submit = Button(text="Submit", font_size=40)
#         self.submit.bind(on_press=self.pressed)
#         self.add_widget(self.submit)
#
# def pressed(self, instance):
#     name = self.name.text
#     last = self.lastName.text
#     email = self.email.text
#     print("Name:", name, "Last Name:", last, "Email:", email)
#     self.name.text = ""
#     self.lastName.text = ""
#     self.email.text = ""
#     print("Pressed")


# class MyApp(App):
#     def build(self):
#         return MyGrid()
#
#
#
# if __name__ == "__main__":
#     MyApp().run()










# import speech_recognition as sr
# import speech_rec as s
#
#
#
#
#
# #
# def main():
#     r = sr.Recognizer()
#     m = sr.Microphone()
#
#     r = sr.Recognizer()
#     on = True
#     while on:
#         with sr.Microphone() as source:
#             audio = r.listen(source)
#
#             try:
#                 text = r.recognize_google(audio)
#                 print("You said: {}".format(text))
#             except:
#                 print("Sorry, we did not recognize your voice")
# #
#
#
#
#
#     r = sr.Recognizer()
#     my_mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
#
#     with my_mic as source:
#
#         print("Say now!!!!")
#
#         audio = r.listen(source) #take voice input from the microphone
#     text = r.recognize_google(audio)
#     print(text) #to print voice into text
#     sent = s.getPolarity(text)
#     sentiment = s.getAnalysis(sent)
#
#     print(sentiment)
#
#
#     r = sr.Recognizer()
#     mic = sr.Microphone()
#     with mic as source:
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)
#         transcript = r.recognize_google(audio)
#         print(transcript)
#
#
#
# if __name__ == "__main__":
#     main()
#
#
# Python Program that helps translate Speech to Text
#
# The Recognizer is initialized.
# UserVoiceRecognizer = sr.Recognizer()
#
# while (1):
#     try:
#
#         with sr.Microphone() as source:
#
#             UserVoiceRecognizer.adjust_for_ambient_noise(source, duration=0.5)
#             # speech_recognition.dynamic_threshold = True
#             # The Program listens to the user voice input.
#
#             UserVoiceInput = UserVoiceRecognizer.listen(source)
#
#             UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
#
#
#             UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
#
#             sent = s.getPolarity(UserVoiceInput_converted_to_Text)
#             sentiment = s.getAnalysis(sent)
#
#
#
#             print(UserVoiceInput_converted_to_Text)
#             print(sentiment)
#
#
#     except KeyboardInterrupt:
#         print('A KeyboardInterrupt encountered; Terminating the Program !!!')
#         exit(0)
#
#     except sr.UnknownValueError:
#         print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
#
