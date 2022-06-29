

#library that contains punctuation
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
import speech_recognition as sr
import pyttsx3 as s


import nltk
# nltk.download()
import pandas as pd
import numpy as np
import re
from transformers import pipeline
import datetime

# data = pd.read_csv("tweet_emotions.csv")
# # sent = pd.DataFrame(data)
# # print("Original DataFrame:\n", data)
# # df = pd.DataFrame(data)
#
# sent = data[data['sentiment'].between(0, 2)].copy()
# print("sentiment: ")
# print(sent)
#
# # def remove_punctuation(txt):
# #     txt_nopunct = "".join([c for c in txt if c not in string.punctuation]) #checking if belongs to punctuation or not
# #     return txt_nopunct
# #
# # sent['content'] = sent['content'].apply(remove_punctuation)
# #
# # sent['content'] = sent["content"].str.lower()
# #
# # def tokenize(text):
# #     text_tokenized = text.split()
# #     return text_tokenized
# #
# # sent['content'] = sent['content'].apply(tokenize)
# #
# #
#
#
#
# # def stopword_removal(stop):
# #     en_stops = set(stopwords.words('english'))
# #     new_list = [word for word in stop if word not in en_stops]
# #     return new_list
# #
# # sent['content'] = sent['content'].apply(stopword_removal)
#
#
# # def remove_punc(txt):
# #     txt_nopunct = " ".join([c for c in txt if c not in string.punctuation]) #checking if belongs to punctuation or not
# #     return txt_nopunct
#
# # sent['content'] = sent['content'].apply(remove_punc)
# #
# # def remove_numbers(text):
# #     result = re.sub(r'\d+', '', text)
# #     return result
# #
# #
# # sent['content'] = sent['content'].apply(remove_numbers)
#
# # def stem_words(text):
# #     word_tokens = word_tokenize(text)
# #     stems = [stemmer.stem(word) for word in word_tokens]
# #     return stems
# #
# # sent['content'] = sent['content'].apply(stem_words)
# #
# #
# # sent['content'] = sent['content'].apply(remove_punc)
#
# print(sent)
#
#
# def getSubjectivity(text):
#     return TextBlob(text).sentiment.subjectivity
#
# #     # Create a function to get the polarity

# def callback(recognizer, audio):
#     print(recognizer.recognize_google(audio))
#
# recognizer = sr.Recognizer()
# mic = sr.Microphone()
#
# with mic as source:
#     recognizer.adjust_for_ambient_noise(source)
#
# stop_listening = recognizer.listen_in_background(mic, callback)


# sent['TextBlob_Polarity'] = sent['content'].apply(getPolarity).apply(getAnalysis)
# sent['Results'] = sent.TextBlob_Polarity == sent.sentiment
#
#
# print(sent)
#
#
# print(sent['Results'].value_counts())
# print(sent['Results'].value_counts() / sent.shape[0])
#
#
# some_value = False
#
# false = sent[sent['Results'] == some_value]
#
# print(false)
#
# print(false['content'])


# def text_proc(txt):
#     proc = TextBlob()
#     x = proc.sentiment.polarity
#     if x < 0:
#         n = "Negative"
#         return n
#     elif x == 0:
#         neutral = "Neutral"
#         return neutral
#     elif (x > 0) & (x <= 1):
#         p = "Positive"
#         return p


# data['sentiment_test'] = data.apply(text_proc['content'])
#
# print(data)


#
# for x in range(10):
#     y = input("Type Sentence: ")
#     proc = TextBlob(y)
#     x = proc.sentiment.polarity
#
#     if x < 0:
#         print("Negative")
#     elif x == 0:
#         print("Neutral")
#     elif (x > 0) & (x <= 1):
#         print("Positive")
#
#



# import nltk
# # nltk.download()
# import pandas as pd
# import numpy as np
#
# # from transformers import pipeline
#
# data = pd.read_csv("tweet_emotions.csv")
#
# read = data.head()
# print(read)
#
# text = data["content"]
#
# def remove_punctuation(txt):
#     txt_nopunct = "".join([c for c in txt if c not in string.punctuation]) #checking if belongs to punctuation or not
#     return txt_nopunct
#
# data['content_clean'] = data['content'].apply(remove_punctuation)
# print(data.head())
#
# data["lower_case"] = data["content_clean"].str.lower()
#
# print(data.head())
# #
# def tokenize(text):
#     text_tokenized = text.split()
#     return text_tokenized
#
# data['tokenized'] = data['lower_case'].apply(tokenize)
# print(data.head())
#
# def stopword_removal(stop):
#     en_stops = set(stopwords.words('english'))
#     new_list = [word for word in stop if word not in en_stops]
#     return new_list
#
# data['meaningful_words'] = data['tokenized'].apply(stopword_removal)
# print(data.head())
#
# print(stopwords.words('english'))



# for column in data:
# # #     # # Select column contents by column
# # #     # # name using [] operator
# # #     # columnSeriesObj = stu_df[column]
# # #     # print('Column Name : ', column)
# # #     # print('Column Contents : ', columnSeriesObj.values)
# #
# #
#     data["tokenization"] = data["lower_case"].column.split()
#     print(data.head())
# print(data.head())
#     proc = column.split()
#     print(proc.head())
def getPolarity(text):

    sentiment = TextBlob(text).sentiment.polarity

    if sentiment < 0:
        return 'Negative'
    elif sentiment == 0:
        return 'Neutral'
    elif (sentiment > 0) & (sentiment <= 1):
        return 'Positive'

# def getAnalysis(score):
#     if score < 0:
#         return 'Negative'
#     elif score == 0:
#         return 'Neutral'
#     elif (score > 0) & (score <= 1):
#         return 'Positive'
# score = 0
def positivity_count(sent, score):
    if sent == 'Positive':
        final_score = score + 1
        return final_score
    elif sent == 'Negative':
        final_score = score - 1
        return final_score

    elif sent == 'Neutral':
        final_score = score
        return final_score

def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
    # if subj > 0.5:
    #     return "Objective"
    # elif (subj > 0) & (subj < 0.5):
    #     return "Subjective"


# def get_Response(sentiment):
#     if sentiment == 'Positive':
#         audio = s.init()
#         rate = audio.getProperty('rate')
# # print(rate)
#         audio.setProperty('rate', 150)
#
#         volume = audio.getProperty('volume')
# # print(volume)
#
#         audio.setProperty('volume', 0.5)
#
#         audio.say("That is so fucking nice. oh my god. I love you")
#         audio.runAndWait()
#     elif sentiment == 'Negative':
#         audio = s.init()
#         rate = audio.getProperty('rate')
#         # print(rate)
#         audio.setProperty('rate', 150)
#
#         volume = audio.getProperty('volume')
#         # print(volume)
#
#         audio.setProperty('volume', 0.5)
#
#         audio.say("That is so fucking rude. Smarten up. You are now at: ")
#         audio.runAndWait()




# r = sr.Recognizer()

def check_Sentiment(sentiment, human_sentiment):
    if sentiment == human_sentiment:
        return 'GOOD'
    elif sentiment != human_sentiment:
        return human_sentiment

# def saveDataframe(df, index):
#     df.at[index, 'Text'] = text
#     df.at[index, 'Sentiment'] = human_sentiment
#     # print(df)
#     index = index + 1
#     df.to_pickle("a_file.pkl")
#     return pd.read_pickle("a_file.pkl")

# def pickled(df):
#     if pd.read_pickle("a_file.pkl") == True:

# check_sentence_sentiment

# def check_df(text, saved):
#     if text ==


import time
import speech_recognition as s_r
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)

def micRecord(r):
    with my_mic as source:

        # r.adjust_for_ambient_noise(source)

        # for x in range(1):
        # running = 'Y'
        # while running == 'Y':
            print("Say now!!!!")
            audio = r.listen(source, phrase_time_limit=5)
        # audio = r.listen(source) #take voice input from the microphone
            text = r.recognize_google(audio)

            # print(text) #to print voice into text
    return text


# print(pd.read_pickle("a_file.pkl"))

# df = pd.DataFrame(columns=['Text', 'Sentiment'])
# df = pd.DataFrame(columns=['Text', 'Sentiment'])
# index = 0
    # print(s_r.__version__) # just to print the version not required
 #my device index is 1, you have to put your device index

# with my_mic as source:
#
#     # r.adjust_for_ambient_noise(source)
#
#     # for x in range(1):
#     running = 'Y'
#     while running == 'Y':
#         print("Say now!!!!")
#         audio = r.listen(source, phrase_time_limit=5)
#     # audio = r.listen(source) #take voice input from the microphone
#         text = r.recognize_google(audio)
#         print(text) #to print voice into text
#
#         # saved = pd.read_pickle("a_file.pkl")
#         # checking = saved['Text'].str.isin(text)
#         # print(checking)
#
#             # if checking
#             #     print("This is fucking awesome")
#             # else:
#             #     print("This sucks")
#
#         # check_df_updated_sentiment = check_df(text, saved)
#
#
#         sentiment = getPolarity(text)
#
#         subjective = getSubjectivity(text)
#
#
#
#
#         print("The text is: ", subjective)
#         print(sentiment)
#
#         human_sentiment = input("what is sentiment: ")
#
#         # print(human_sentiment)
#
#         check = check_Sentiment(sentiment, human_sentiment)
#         if check == 'GOOD':
#             print("Correct sentiment")
#             count = positivity_count(text, score)
#             score = count
#             print("Your score is at: ", count)
#         elif check != 'GOOD':
#             print('Correct sentiment is:', check)
#
#             if check == 'Negative':
#                 count = count - 1
#             elif check == 'Positive':
#                 count = count + 1
#             elif check == 'Neutral':
#                 count = count
#             print("Your score is at: ", count)
#
#
#
#             df['Text'] = [text]
#             df['Sentiment'] = [human_sentiment]
#
#             df.at[index, 'Text'] = text
#             df.at[index, 'Sentiment'] = human_sentiment
#
#             # print(df)
#             index = index + 1
#             # saved = pd.read_pickle("a_file.pkl")
#
#
#
#
#             # df.to_pickle("a_file.pkl")
#             #
#             # print(saved)
#
#
#             # updated_df = pd.concat([df, saved])
#             # updated_df.to_pickle("a_file.pkl")
#             # print(updated_df)
#
#         date = datetime.date.today()
#         print(date)
#         print(pd.read_pickle("a_file.pkl"))
#         running = (input('Run again? Y or N:  '))
#



        # response = get_Response(sentiment)
        # print(df)
# saved = pd.read_pickle("a_file.pkl")
# print(updated)


# print(pd.read_pickle("a_file.pkl"))
        # print(output)
    # saveDataframe(df)
    # print(saveDataframe(df))
# df.to_pickle("a_file.pkl")

# print("Dataframe Contents ", df, sep='\n')
# import speech_recognition as sr



# audio = s.init()
#
# rate = audio.getProperty('rate')
# # print(rate)
# audio.setProperty('rate', 150)
#
# volume = audio.getProperty('volume')
# # print(volume)
#
# audio.setProperty('volume', 0.5)
#
# audio.say("Hello world")
# audio.runAndWait()
#
# r = sr.Recognizer()

# def SpeakText(command):
#
#     engine = s.init()
#     engine.say(command)
#     engine.runAndWait()
#
#     SpeakText("Hello World")
