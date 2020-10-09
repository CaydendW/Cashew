# Overview
A python based virtual assistant.

# Dependencies
This project has a lot of dependencies:

1. SpeechRecognition 3.8.1 ```pip install SpeechRecognition```
2. pyttsx3 ```pyttsx3==2.6```
3. webbrowser ```comes pre-installed```
4. wikipedia ```pip install wikipedia```
5. urllib ```comes pre-installed```
6. lxml ```pip install lxml```
7. nltk ```pip install nltk```
8. googlesearch ```pip install beautifulsoup4 && pip install google```
9. pygame ```pip install pygame```
10. yr-python ```pip install python-yr```
11. time ```comes pre-installed```
12. math ```comes pre-installed```
13. os ```comes pre-installed```
14. PyAudio ```pip install pyaudio```\*
15. json ```comes pre-installed```
16. request ```pip install requests```
17. random ```comes pre-installed```

I have included a requirements.txt file to help speed up the process, but The pyaudio module might not install. (See below)

\* PyAudio is very difficult to get on windows try the pip command and if that fails, go to [stackoverflow]( https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-windows-how-to-solve-error-microsoft-visual-c-14/55630212#55630212) and follow the instructions. That was what worked for me. If that doesn't work, and you've got Conda try to Conda install it.

# Notes
The project has a few notes to consider.
1. At the top of the code, there is a line that says ```weather = Yr(location_name='South_Africa/KwaZulu-Natal/Durban/'```. Inbetween the single quotes you will have to put your location. You can find it by going onto [yr](https://www.yr.no/?spr=eng), searching your location and taking the place from the URL after the /place and putting inbetween the single quotes.
2. There are a lot of lines that contain the following line of code: ```speech = sr.Microphone(device_index=2)```. I had to make my microphone's device index 2 because that was the microphone I want to use. You might have to change this around to whatever input device suits your needs.

# Use of my code
A custom license is used. This work is under Creative Commons Attribution-ShareAlike 4.0 International. If you want to use my work please give me attribution. A valid attribution URL is https://github.com/CaydendW/ 

# Attribution
I used some sound files for the on and off sounds. They are both listed under [Atribution 3.0](https://creativecommons.org/licenses/by/3.0/)

### Sound file 1
* Title: Robot Blip
* Uploaded: 01.11.11
* License: Attribution 3.0
* Edits: Changed format from mp3 to ogg
* Recorded by Marianne Gagnon

### Sound file 2
* Title: Robot Blip 2
* Uploaded: 01.05.11
* License: Attribution 3.0
* Edits: Changed format from mp3 to ogg
* Recorded by Marianne Gagnon

I also used a joke API from fellow Github user: [Sv443](https://github.com/Sv443/).
I did not have to give attribution but the project is here: [Joke API](https://github.com/Sv443/JokeAPI/).
Please go give him a star and add some jokes to the API [here](https://sv443.net/jokeapi/v2/#submit)!
