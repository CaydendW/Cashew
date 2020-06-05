# Overview
A python based virtual assistant.

# Dependencies
This project has a lot of dependencies. They are: SpeechRecognition 3.8.1, win32com, webbrowser, wikipedia, urllib, lxml, nltk, googlesearch, pygame, yr-python and PyAudio.

# Notes
The project has a few notes to consider.
1: This will absolutly not work in Linux or MacOS. I am currently working on other OS friendly versions.
2: At the top of the code, there is a line that says "weather = Yr(location_name='')". Inbetween the single quotes you will have to put your location. You can find it by going onto https://www.yr.no/?spr=eng, searching your location and taking the place from the URL and putting inbetween the single quotes.
3: PyAudio is very difficult to get on windows. go to https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14 and follow the first answer and try that.
4: The 'play' function plays youtube videos and google likes to generate cookies. I added a line of code to delete the cookie on termination of the code. It says 'os.remove(r"D:\Users\cayde\Documents\Code\Python\.google-cookie")' Just replace it with the directory in which your cookie spawns. If it doesn't bother you just remove that line.
5: In the folder are 2 sound files from http://soundbible.com/tags-ping.html and they are played using pygame. You will have to change the directory of the sound file play 'mixer.music.load(r"D:\Users\cayde\Documents\Code\Python\Cashew\Robot_blip-Marianne_Gagnon-120342607.mp3")' to whatever directory you cloned/download the project to so that the program can find the sound files.
6: There are a lot of lines that contain the following line of code: 'speech = sr.Microphone(device_index=2)'. I had to make my microphone's device indext 2 because that was the microphone I want to use. You might have to change this around to whatever input device suits your needs.

# Use of my code
As stated by the licence: this is BSD3. I would appreciate if you gave me credit for my work, however it is not required. A link to my github page would be very kind.

