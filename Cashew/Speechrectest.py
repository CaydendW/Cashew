#Made by CaydendW on github
import speech_recognition as sr
import win32com.client
import webbrowser
import urllib
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

speaker = win32com.client.Dispatch("SAPI.SpVoice")

weather = Yr(location_name='South_Africa/KwaZulu-Natal/Durban/') #You will have to change the location

r = sr.Recognizer()
r.dynamic_energy_threshold = False

speaker.Speak("I am cashew, a TTS Virtual assistant, clap before talking so I can hear you, how can I help you?")
mixer.init()
mixer.music.load(r"D:\Users\cayde\Documents\Code\Python\Cashew\Robot_blip-Marianne_Gagnon-120342607.mp3") #Change the directory to your directory.
mixer.music.play()

for lop in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    try:
        speech = sr.Microphone(device_index=2)
        with speech as source:
            audio = r.listen(source)
            r.adjust_for_ambient_noise(source)

        recog = r.recognize_google(audio, language = 'en-US')

        if "search" in recog:
            speaker.Speak("Sure. What do you want me to search?")
            speech2 = sr.Microphone(device_index=2)#This might have to change depending on which microphone you want it to use

            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)

            query = r.recognize_google(qaudio, language = 'en-US')
            speaker.Speak(wikipedia.summary(query))
            
        if "Bing" in recog:
            speaker.Speak("Sure. What do you want me to search on bing?")
            speech2 = sr.Microphone(device_index=2)

            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)

            query = r.recognize_google(qaudio, language = 'en-US')
            search = query.replace(" ", "+")
            webbrowser.open("https://www.bing.com/search?q=" + search)
            
        elif "play" in recog:

            speaker.Speak("Sure. What do you want me to play?")
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')

            speaker.Speak("Sure. Searching for" + query)

            for j in search(query, tld="co.in", num=999999999999999999999999999999999999999999999999999999999999, stop=0, pause=2):
                if "/watch?v=" in j:
                    url = j
                    youtube = etree.HTML(urllib.request.urlopen(url).read())
                    video_title = youtube.xpath("//span[@id='eow-title']/@title")
                    title = ''.join(video_title)
                    if "reaction" not in title:
                        if "REACTION" not in title:
                            if "Reaction" not in title:
                                speaker.Speak("Now playing" + title)
                                webbrowser.open(url)
                                break
        
        elif "time" in recog:
            tim = strftime("%H:%M:%S")
            speaker.Speak("The current time is" + tim)

        elif "spell" in recog:
            speaker.Speak("Sure. What do you want me to spell?")
            speech2 = sr.Microphone(device_index=2)
            with speech2 as source:
                qaudio = r.listen(source)
                r.adjust_for_ambient_noise(source)
            query = r.recognize_google(qaudio, language = 'en-US')
            speeling = list(query)
            spelling = str(speeling)
            speaker.Speak(query + ", is spelled:" + spelling)

        elif "define" in recog:
            try:
                speaker.Speak("Sure. What word's definition do you want to know?")
                speech2 = sr.Microphone(device_index=2)
                with speech2 as source:
                    qaudio = r.listen(source)
                    r.adjust_for_ambient_noise(source)
                query = r.recognize_google(qaudio, language = 'en-US')
                word = wn.synsets(query)
                defi = word[0].definition()

                speaker.Speak("The definition of " + query + " is " + defi)
            except IndexError:
                speaker.Speak("I could not find a definition for " + defi)

        elif "synonym" in recog:
            try:
                speaker.Speak("Sure. What word do you want a synonym for?")
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
                    speaker.Speak("Some synonyms for " + word + " are " + str(synonyms))
                else:
                    speaker.Speak("I could not find synonyms for " + word)
                
            except:
                pass

        elif "antonym" in recog:
            try:
                speaker.Speak("Sure. What word do you want an antonym for?")
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
                    speaker.Speak("Some antonyms for " + word + " are " + str(antonyms))
                else:
                    speaker.Speak("I could not find antonyms for " + word)

            except:
                pass

        elif "where" in recog:
            speaker.Speak("Sure. What location do you want to know?")
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

            speaker.Speak("The weather for the next four hours is as follows:")
            speaker.Speak("The temperature will be " + tempvalue + " degrees " + tempunit + " average.")
            speaker.Speak("With a " + skycon)
            speaker.Speak("It will rain " + rainvalue + " millilitres in the next 4 hours.")
            speaker.Speak("The wind is " + windspeedname + ", blowing at " + windspeed + " meters per second going " + winddirection)
            speaker.Speak("The pressure is " + pressure + " heteropascles.")

        elif "date" in recog:
            tim = strftime("%Y-%m-%d")
            speaker.Speak("The current date is" + tim)

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
            speaker.Speak("This was made by Cayden d W on GitHub! Would you like me to open his page?")

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
            speaker.Speak("Hello to you too!")

        elif "hi" in recog:
            speaker.Speak("Hello to you too!")
        
        elif "thank you" in recog:
            speaker.Speak("You're welcome!")

        elif "cashew" in recog:
            speaker.Speak("Yes!? I'm listening...")

        elif "yes" in recog:
            speaker.Speak("I'm glad something is going well.")

        elif "help" in recog:
            webbrowser.open("https://github.com/CaydendW/Cashew/blob/master/help.md")

        else:
            speaker.Speak("Sorry but " + recog + "is not one of my commands. Say help to hear a list of commands.")
        
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
            os.remove(r"D:\Users\cayde\Documents\Code\Python\.google-cookie")#Change this to the directory of the cookie you want to delete
        except FileNotFoundError:
            pass
        exit()
