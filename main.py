import os
import gtts
from playsound import playsound
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
#import pyowm
import requests


#### to talk #################
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
###############################
path = os.path.dirname(__file__)


def weather():
    api_key = "e165f57f7baad610b7d013664cedf314"  # Enter the API key you got from the OpenWeatherMap website
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Cairo"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]
        z = x["weather"]

        weather_description = z[0]["description"]
        print(int(current_temperature-272))
    talk("درجة الحرارة الان  في القاهرة هي " + str(int(current_temperature-272)) + "مئوياَ ")




def time():
    time = datetime.datetime.now().strftime('%H:%M %p')
    print(time)
    talk("الساعة الان " + time)

def date():
    date = datetime.datetime.now().strftime('%d-%m-%Y')
    print(date)
    talk("تاريخ اليوم هو " + date)


def wiki(text):
    wikipedia.set_lang('ar')
    try:
        info = wikipedia.summary(text,2).replace("==", "")
    except Exception as e:
        print(e)   
        #print("Unable to Recognize your voice.") 
        talk("لا اعرف عما تتحدث")
        return "None"
    #print(info)
    talk(info)


def talk(text):
    path = os.path.dirname(__file__)
    tts = gtts.gTTS(text , lang="ar")
    tts.save(path + "\\" + "out.mp3")
    playsound(path + "\\" + "out.mp3")



def listen():
    r = sr.Recognizer() 
    with sr.Microphone() as src:
        #r.adjust_for_ambient_noise(src)
        print('Say something.....')
        r.pause_threshold = 1
        audio = r.listen(src)
    try:
        txt = r.recognize_google(audio, language='ar-EG')
        print("listen : " + txt)

    except Exception as e:
        print(e)   
        #print("Unable to Recognize your voice.") 
        return "None"

    return txt



def main():
    txt = listen()
    if "سلام عليكم" in txt:
        playsound(str(path + "\\" +"1.mp3"))
    elif "زيكو" in txt:
        playsound(str(path + "\\" +"0.mp3"))

    elif "درجةالحرارة" in txt or "درجه الحرارة" in txt or "الطقس" in txt or "المناخ" in txt or "درجه الحراره" in txt:
        print("weather")
        weather()

    elif "الساعه" in txt or "كم الساعه" in txt or "ساعة" in txt or "كم الساعة" in txt or "الوقت" in txt :
        print("time")
        time()

    elif "تاريخ اليوم" in txt or "تاريخ النهارده" in txt or "النهارده ايه" in txt or "تاريخ" in txt :
        date()

    elif "من هو" in txt or "من هي" in txt or "ابحث عن" in txt or "تعرف ايه عن" in txt or "ما هي" in txt or "ما هو" in txt or "مين هو" in txt or "مين هي" in txt :
        
        char_to_replace = {'من هو': '', 'من هي': '','ابحث عن':'', 'تعرف ايه عن': '',
        'ما هي' : '' ,'ما هو':''}
        for key, value in char_to_replace.items():
            # Replace key character with value character in string
            txt = txt.replace(key, value)
        print("Wiki : "+txt)
        
        wiki(str(txt))

    else:
        print("no sound")

while True:
    main()

#wiki("محمد انور السادات")




########################### Mulit replace #################################3

#str1 = "Fear leads to anger; anger leads to hatred; hatred leads to conflict"

#char_to_replace = {'to': '2', ';': ',', 'anger': 'rage'}

# Iterate over all key-value pairs in dictionary 
#for key, value in char_to_replace.items():
    # Replace key character with value character in string
#    str1 = str1.replace(key, value)

#print(str1)




############################# Test wather ####################################

#api_key = "e165f57f7baad610b7d013664cedf314"  # Enter the API key you got from the OpenWeatherMap website
#base_url = "http://api.openweathermap.org/data/2.5/weather?"

#city_name = "Cairo"
#complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name  # This is to complete the base_url, you can also do this manually to checkout other weather data available
#response = requests.get(complete_url)
#x = response.json()

#if x["cod"] != "404":
#    y = x["main"]

#    current_temperature = y["temp"]
#    z = x["weather"]

#    weather_description = z[0]["description"]
#
#    print(" Temperature (in Celsius unit) = " +
#                    str(int(current_temperature-272))  +
#          "\n description = " +
#                    str(weather_description))

#else:
#    print(" City Not Found ")

##################################################################################
