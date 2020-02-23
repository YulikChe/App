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
import interface
import test_jupiter

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

def antarktida(file_directory = "info.txt"):
    line = 0

    with open(file_directory, "r") as file:
        lines = file.read().split("\n")
    for i in lines:
        talk(i)
        if line == 2:
            interface.drawDog("foto/1a.png")
        line += 1
        if line == 5:
            interface.window.blit(interface.bg, (0, 0))
            interface.drawDog("foto/2a.jpg")

#foo internet

def internet():
    search = comand("Что найти в интернете?")
    talk("Хорошо")
    webbrowser.open("https://www.google.ru/search?newwindow=1&source=hp&ei=AMk_XuSrPManrgSpn7fAAQ&q=" + search)
    sys.exit()

#foo randDog
def randDog():
    dogs = list(options["dogs"])
    return dogs[random.randint(0, len(dogs)-1)]

#foo ugodayka

def ugodayka():
    dog = randDog()
    dog_type = dog.replace("foto/", "").replace(".jpg", "").lower()

    talk("Гав гав гав")
    interface.drawDog(dog)
    talk("Какая порода этой собаки?")
    talk("У тебя 10 секунд на розмышления!")
    time.sleep(10)
    talk("Время вышло!")
    answer = comand("Какая порода у этой собаки?")
    if answer == dog_type:
        os.system("C:\\Users\\DRIVER\\PycharmProjects\\App\\naprMusic.mp3")
        time.sleep(9)
        talk("Правильно!")
        os.system("C:\\Users\\DRIVER\\PycharmProjects\\App\\radost.mp3")
        time.sleep(17)
    else:
        os.system("C:\\Users\\DRIVER\\PycharmProjects\\App\\naprMusic.mp3")
        time.sleep(9)
        talk("Не правильно :(")
        os.system("C:\\Users\\DRIVER\\PycharmProjects\\App\\grust.mp3")
        time.sleep(5)
        talk("Правильный ответ " + dog_type)
        talk("Ваш ответ " + answer)

def triangle():#!!!!!!!!!!!!!!!!!!!!!
    talk("Вводите длинну сторон, введите команду 'стоп' когда закончите вводить")
    sum = 0
    while True:
        printed = input()
        if printed == "стоп":
            talk("Периметр равняеться " + str(sum))
            break
        sum += int(printed)

def paint():
    talk("Вводите координаты точек фигуры, введите команду 'стоп' когда закончите вводить")
    coordinats = []
    while True:
        printed = input()

        if printed == "стоп":
            test_jupiter.test(coordinats)
            break
        coordinats.append(int(printed))

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

interface.mainn()
antarktida()

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
        com = comand(say)
    except sr.RequestError:
        talk("Ниезвестная ошибка, проверьте интернет!")
        sys.exit()
    return com

def makeSamthing(Com):
    if Com == "webSite":
        talk("Открываю")
        url = 'http://ekologia13.zzz.com.ua'
        webbrowser.open(url)
        sys.exit()

    elif Com == 'stop':
        talk("Ладно :(")
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

    elif Com == "antarktida":
        antarktida()

while True:
    interface.mainn()
    makeSamthing(findCom(comand("Говорите")))
