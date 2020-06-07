#This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.
#Please credit me at this URL: https://github.com/CaydendW/

import speech_recognition as sr
import webbrowser
import wikipedia
import requests
import pyttsx3
import urllib
import json
import lxml
import math
import time
import os
from nltk.corpus import wordnet as wn
from time import gmtime, strftime
from googlesearch import search
from pygame import mixer
from yr.libyr import Yr
from lxml import etree

engine = pyttsx3.init()
engine.setProperty('rate', 130)

weather = Yr(location_name='South_Africa/KwaZulu-Natal/Durban/') #Fill in your own location. More help in readme.md

r = sr.Recognizer()
r.dynamic_energy_threshold = False

engine.say("I am cashew, a TTS Virtual assistant, clap before talking so I can hear you, how can I help you?")
engine.runAndWait()
mixer.init()
mixer.music.load(r"D:\Users\cayde\Documents\Code\Python\Cashew\Robot_blip-Marianne_Gagnon-120342607.mp3") #Change this location to where ever the sound files are located
mixer.music.play()

for lop in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    try:
        r = sr.Recognizer()
        r.dynamic_energy_threshold = False
        speech = sr.Microphone(device_index=2) #You might have to change this so you get differnet microphone input. There are more of these further down
        with speech as source:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)

        recog = r.recognize_google(audio, language = 'en-US')

        if "search" in recog:
            engine.say("Sure. What do you want me to search?")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)

            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)

            query = r.recognize_google(qaudio, language = 'en-US')
            engine.say(wikipedia.summary(query))
            engine.runAndWait()
            
        if "Bing" in recog:
            engine.say("Sure. What do you want me to search on bing?")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)

            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)

            query = r.recognize_google(qaudio, language = 'en-US')
            search = query.replace(" ", "+")
            webbrowser.open("https://www.bing.com/search?q=" + search)
            
        elif "play" in recog:
            engine.say("Sure. What do you want me to play?")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')

            engine.say("Sure. Searching for" + query)
            engine.runAndWait()

            for j in search(query, tld="co.in", num=999999999999999999999999999999999999999999999999999999999999, stop=0, pause=2):
                if "/watch?v=" in j:
                    url = j
                    youtube = etree.HTML(urllib.request.urlopen(url).read())
                    video_title = youtube.xpath("//span[@id='eow-title']/@title")
                    title = ''.join(video_title)
                    if "reaction" not in title:
                        if "REACTION" not in title:
                            if "Reaction" not in title:
                                engine.say("Now playing" + title)
                                engine.runAndWait()
                                webbrowser.open(url)
                                break
        
        elif "time" in recog:
            tim = strftime("%H:%M:%S")
            engine.say("The current time is" + tim)
            engine.runAndWait()

        elif "spell" in recog:
            engine.say("Sure. What do you want me to spell?")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')
            speeling = list(query)
            spelling = str(speeling)
            engine.say(query + ", is spelled:" + spelling)
            engine.runAndWait()

        elif "define" in recog:
            try:
                engine.say("Sure. What word's definition do you want to know?")
                engine.runAndWait()
                speech2 = sr.Microphone(device_index=2)
                with speech2 as source:
                    qaudio = r.listen(source)
                    r.adjust_for_ambient_noise(source)
                query = r.recognize_google(qaudio, language = 'en-US')
                word = wn.synsets(query)
                defi = word[0].definition()

                engine.say("The definition of " + query + " is " + defi)
                engine.runAndWait()
            except IndexError:
                engine.say("I could not find a definition for " + defi)
                engine.runAndWait()

        elif "synonym" in recog:
            try:
                engine.say("Sure. What word do you want a synonym for?")
                engine.runAndWait()
                speech2 = sr.Microphone(device_index=2)
                with speech2 as source:
                    qaudio = r.listen(source)
                    r.adjust_for_ambient_noise(source)
                query = r.recognize_google(qaudio, language = 'en-US')
                word = query

                synonyms = []
                antonyms = []

                for syn in wn.synsets(word):
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                        if l.antonyms():
                            antonyms.append(l.antonyms()[0].name())
                
                if synonyms != []:
                    engine.say("Some synonyms for " + word + " are " + str(synonyms))
                    engine.runAndWait()
                else:
                    engine.say("I could not find synonyms for " + word)
                    engine.runAndWait()
                
            except:
                pass

        elif "antonym" in recog:
            try:
                engine.say("Sure. What word do you want an antonym for?")
                engine.runAndWait()
                speech2 = sr.Microphone(device_index=2)
                with speech2 as source:
                    qaudio = r.listen(source)
                    r.adjust_for_ambient_noise(source)
                query = r.recognize_google(qaudio, language = 'en-US')
                word = query

                synonyms = []
                antonyms = []

                for syn in wn.synsets(word):
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                        if l.antonyms():
                            antonyms.append(l.antonyms()[0].name())

                if antonyms != []:
                    engine.say("Some antonyms for " + word + " are " + str(antonyms))
                    engine.runAndWait()
                else:
                    engine.say("I could not find antonyms for " + word)
                    engine.runAndWait()

            except:
                pass

        elif "where" in recog:
            engine.say("Sure. What location do you want to know?")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')
            search = query.replace(" ", "+")
            webbrowser.open("https://www.google.co.za/maps/search/" + search)

        elif "weather" in recog:
            now = weather.now(as_json=False)

            overtemp = now['temperature']
            tempunit = overtemp['@unit']
            tempvalue = overtemp['@value']
            
            oversky = now['symbol']
            skycon = oversky['@name']

            overrain = now['precipitation']
            rainvalue = overrain['@value']

            overwind = now['windDirection']
            overwind2 = now['windSpeed']
            winddirection = overwind['@name']
            windspeed = overwind2['@mps']
            windspeedname = overwind2['@name']

            overpressure = now['pressure']
            unit = overpressure['@unit']
            pressure = overpressure['@value']

            engine.say("The weather for the next four hours is as follows:")
            engine.runAndWait()
            engine.say("The temperature will be " + tempvalue + " degrees " + tempunit + " average.")
            engine.runAndWait()
            engine.say("With a " + skycon)
            engine.runAndWait()
            engine.say("It will rain " + rainvalue + " millilitres in the next 4 hours.")
            engine.runAndWait()
            engine.say("The wind is " + windspeedname + ", blowing at " + windspeed + " meters per second going " + winddirection)
            engine.runAndWait()
            engine.say("The pressure is " + pressure + " heteropascles.")
            engine.runAndWait()

        elif "joke" in recog:
            engine.say("Sure. What do you want the joke to be about? Say random for a random catagory.")
            engine.runAndWait()
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')

            if query == "random":
                send_url = 'https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=single'
                r = requests.get(send_url)
                j = json.loads(r.text)
                error = j['error']
                if error == "true":
                    engine.say(j['message'])
                    engine.runAndWait()
                else:
                    joke = j['joke']
                    engine.say(joke)
                    engine.runAndWait()

            else:
                send_url = 'https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist&type=single&contains='
                send_url2 = query
                r = requests.get(send_url + send_url2)
                j = json.loads(r.text)
                error = j['error']
                if error == "true":
                    engine.say(j['message'])
                    engine.runAndWait()
                else:
                    joke = j['joke']
                    engine.say(joke)
                    engine.runAndWait()

        elif "date" in recog:
            tim = strftime("%Y-%m-%d")
            engine.say("The current date is" + tim)
            engine.runAndWait()

        elif "off" in recog:
            mixer.init()
            mixer.music.load(r"D:\Users\cayde\Documents\Code\Python\Cashew\Robot_blip_2-Marianne_Gagnon-299056732.mp3")
            mixer.music.play()
            time.sleep(1)
            try:
                os.remove(r"D:\Users\cayde\Documents\Code\Python\.google-cookie")
            except FileNotFoundError:
                pass
            exit()

        elif "credits" in recog:
            engine.say("This was made by Cayden d W on GitHub! Would you like me to open his page?")
            engine.runAndWait()

            speech2 = sr.Microphone(device_index=2)

            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
                
            query = r.recognize_google(qaudio, language = 'en-US')

            if "yes" in query:
                webbrowser.open("https://github.com/CaydendW")
            else:
                break
        
        elif "hello" in recog:
            engine.say("Hello to you too!")
            engine.runAndWait()

        elif "hi" in recog:
            engine.say("Hello to you too!")
            engine.runAndWait()
        
        elif "thank you" in recog:
            engine.say("You're welcome!")
            engine.runAndWait()

        elif "cashew" in recog:
            engine.say("Yes!? I'm listening...")
            engine.runAndWait()

        elif "yes" in recog:
            engine.say("I'm glad something is going well.")
            engine.runAndWait()

        elif "help" in recog:
            webbrowser.open("https://github.com/CaydendW/Cashew/blob/master/help.md")

        else:
            engine.say("Sorry but " + recog + "is not one of my commands. Say help to hear a list of commands.")
            engine.runAndWait()
        
    except sr.UnknownValueError:
        continue

    except sr.RequestError as e:
        continue

    except KeyboardInterrupt:
        mixer.init()
        mixer.music.load(r"D:\Users\cayde\Documents\Code\Python\Cashew\Robot_blip_2-Marianne_Gagnon-299056732.mp3")
        mixer.music.play()
        time.sleep(1)
        try:
            os.remove(r"D:\Users\cayde\Documents\Code\Python\.google-cookie")
        except FileNotFoundError:
            pass
        exit()
