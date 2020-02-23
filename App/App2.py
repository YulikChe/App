import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import datetime
from opts import options
from fuzzywuzzy import fuzz
import random
import time

tts = pyttsx3.init()

voices = tts.getProperty('voices')

tts.setProperty('voice', voices[12].id)

#foo talk

def talk(words):
    print(words)
    tts.say(words)
    tts.runAndWait()
    tts.stop()
#foo засечь время
def waitTimeFoo():
    timeCo = comand("Сколько секунд?")
    talk("Хорошо")
    time.sleep(int(timeCo))
    talk("Время вышло!")

#foo internet

def internet():
    search = comand("Что найти в интернете?")
    talk("Хорошо")
    webbrowser.open("https://www.google.ru/search?newwindow=1&source=hp&ei=AMk_XuSrPManrgSpn7fAAQ&q=" + search)
    sys.exit()

#foo ugodayka
def ugodayka():
    pass

#приветствие
def hello():
    hello = list(options["hello"])
    return hello[random.randint(0, len(hello)-1)]

#анекдот

def stupid():
    stup = list(options["anekdots"])
    return stup[random.randint(0, len(stup)-1)]
#радио
def radio():
    ra = list(options["radioOn"])
    return ra[random.randint(0, len(ra) - 1)]


talk(hello())

def findCom(com): #функция опредиляющая тип команды
    RC = {"cmd": '', "percent": 0}

    for c, v in options["cmds"].items():

        for x in v:
            vrt = fuzz.ratio(com, x)

            if vrt > RC["percent"]:
                RC["cmd"] = c
                RC["percent"] = vrt

    return RC["cmd"]

#comand
def comand(say):
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as sourse:
        talk(say)
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

    try:
        com = r.recognize_google(audio, language="ru-RU").lower()

        if com.startswith(options["name"]):
            com = com.replace(str(options["name"]), "", 1)

        #print("Вы сказали:" + com)


    except sr.UnknownValueError:
        talk("Я вас непоняла")
        com = comand()
    except sr.RequestError:
        talk("Ниезвестная ошибка, проверьте интернет!")

    return com
def makeSamthing(Com):
    if Com == "webSite":
        talk("Открываю")
        url = 'http://ekologia13.zzz.com.ua'
        webbrowser.open(url)
        sys.exit()

    elif Com == 'stop':
        talk("Ладно(")
        sys.exit()

    elif Com == 'time':
        now = datetime.datetime.now()
        talk("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif Com == 'stupid':
        talk("Ладно, сами попросили")
        talk(stupid())
        talk("Ха ха ха")

    elif Com == "radio":
        os.system(radio())
        time.sleep(120)

    elif Com == "waitTime":
        waitTimeFoo()

    elif Com == "internet":
        internet()
    elif Com == "ugodayka":
        ugodayka()

while True:
    makeSamthing(findCom(comand("Говорите")))