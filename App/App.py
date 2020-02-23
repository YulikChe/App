import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import datetime
import json

tts = pyttsx3.init()

voices = tts.getProperty('voices')

tts.setProperty('voice', voices[12].id)



#json
with open('comands.json', 'r', encoding='utf-8') as file: #открываем файл на чтение

    comJ = json.load(file)

print(comJ)

#вчерашняя робота

#cmd = 'валеррия hello'

#if cmd.startswith(comJ["name"]):
    #print(cmd)

   # for x in comJ["name"]:
       # cmd = cmd.replace(x, '')

i = 0
while i < len(comJ):  # Пока i меньше количество элементов списка (!)
    for key, value in comJ[i].items():  # Пока в словаре есть пары ключ-значение
        string = string + '\n' + key + ' ' + value  # Редактируем строку
    string += '\n'  # После каждого словаря для повышения читаемости ставим еще один перенос
    i += 1

#print(cmd)

#foo talk

def talk(words):
    print(words)
    tts.say(words)
    tts.runAndWait()
    tts.stop()

talk("Здрасте")


#comand

def comand():
    r = sr.Recognizer()

    with sr.Microphone(device_index=1) as sourse:
        talk("Говорите")
        r.adjust_for_ambient_noise(sourse, duration=1)
        audio = r.listen(sourse)

    try:
        com = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали:" + com)

    except sr.UnknownValueError:
        talk("Я вас непоняла")
        com = comand()

    return com

def makeSamthing(com, comJ):
    if com == "открой мой сайт":
        talk("Открываю")
        url = 'http://ekologia13.zzz.com.ua'
        webbrowser.open(url)
    elif com == 'стоп':
        talk("Ладно(")
        sys.exit()
    elif com == 'сколько сейчас время':
        talk(datetime.datetime.now())


while True:
    makeSamthing(comand(), comJ)