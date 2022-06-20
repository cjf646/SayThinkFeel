import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

# class MyGrid(Widget):
#     pass


def __init__(self, **kwargs):
    super(MyGrid, self).__init__(**kwargs)
    self.cols = 1


    self.inside = GridLayout()
    self.inside.cols = 2

    self.cols = 2
    self.inside.add_widget(Label(text="Name: "))
    self.name = TextInput(multiline=False)
    self.inside.add_widget(self.name)

    self.inside.add_widget(Label(text="Last Name: "))
    self.lastName = TextInput(multiline=False)
    self.inside.add_widget(self.lastName)

    self.inside.add_widget(Label(text="Email: "))
    self.email = TextInput(multiline=False)
    self.inside.add_widget(self.email)

    self.add_widget(self.inside)



    self.submit = Button(text="Submit", font_size=40)
    self.submit.bind(on_press=self.pressed)
    self.add_widget(self.submit)

def pressed(self, instance):
    name = self.name.text
    last = self.lastName.text
    email = self.email.text
    print("Name:", name, "Last Name:", last, "Email:", email)
    self.name.text = ""
    self.lastName.text = ""
    self.email.text = ""
    print("Pressed")


class MyApp(App):
    def build(self):
        return MyGrid()
        # return Label(text="Tech with Tim")


if __name__ == "__main__":
    MyApp().run()

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
