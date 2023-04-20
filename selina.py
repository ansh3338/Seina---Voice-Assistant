import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import subprocess
import smtplib as smtp
from pytube import YouTube
import openai
import requests
import datetime as dt

# pip install "Module_name"

import phonenumbers
from phonenumbers import timezone,geocoder,carrier

import weather_api # this will create error, it's a file, developer need to create and store their open weather map secret api key 
import openAI_key  # this will create error, it's a file, developer need to create and store their openAi secret api key


# we will use 'sapi5' to recognise voice.It's a windows Api.
engine = pyttsx3.init('sapi5')   
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",140)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # It takes microphone input from users and returns string Output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=0.2)
        r.dynamic_energy_adjustment_damping = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "none"
    return query

def myDetails():

    print("I can perform the following tasks for you as listed below : \n")
    speak("I can perform the following tasks for you as listed below : ")
    
    print("1. I can Search anything on Wikipedia, you just need to use the word 'Wikipedia' in your statement.")

    print("2. I can open youtube for you on your default web browser, you just need to use 'open youtube' in your sentence")

    print("3. I can open Facebook for you on your default web browser, you just need to use 'open facebook' in your sentence")

    print("4. I can open Jio Cinema for you on your default web browser, you just need to use 'open jio cinema' in your sentence")

    print("5. I can open Whatsapp Web for you on your default web browser, you just need to use 'open whatsapp' in your sentence")

    print("6. I can open Github for you on your default web browser, you just need to use 'open gitub' in your sentence")

    print("7. I can open Google serach engine for you on your default web browser, you just need to use 'open google' in your sentence")

    print("8. I can open app list which are present on your PC, you just need to use 'open app' in your sentence.")

    print("9. I can send emails for you, you just need to use 'send email' in your sentence.")

    print("10. I can give you details of your desired phone number, you just need to use 'phone details' in your sentence.")

    print("11. I can tell you current date and time, you just need to use 'current date' and 'current time' for current date and current time respectively.")

    print("12. I can tell you about weather conditions about any city, you just need to use 'weather' word in your sentence.")

    print("13. Last but not the least, i can talk with you and resolve your issues.\n")

    print("You can use the word 'sleep' when you are done with my service.\n")
    speak("You can use the word 'sleep', when you are done with my service.")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        print("Good Morning!")
        speak("Good Morning!")
    elif (hour>=12 and hour<18):
        print("Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Selina.")
    speak("I am Selina.")


def sendEmail(myid, mypass,to, content):
    server = smtp.SMTP_SSL('smtp.gmail.com',465)
    # server.ehlo()
    # server.starttls()
    server.login(myid,mypass)
    server.sendmail(from_addr=myid,to_addrs=to,msg=content)
    server.close()

def weatherCondition(city,data):
    print(f"Current Tempreature at {city} is : {data['main']['temp']} f")
    speak(f"Current Tempreature at {city} is : {data['main']['temp']} fahrenheit")

    print(f"Current Tempreature feels like : {data['main']['feels_like']} f")
    speak(f"Current Tempreature feels like : {data['main']['feels_like']} fahrenheit")

    print(f"Maximum Tempreature at {city} is : {data['main']['temp_max']} f")
    speak(f"Maximum Tempreature at {city} is : {data['main']['temp_max']} fahrenheit")

    print(f"Minimum Tempreature at {city} is : {data['main']['temp_min']} f")
    speak(f"Minimum Tempreature at {city} is : {data['main']['temp_min']} fahrenheit")
    
    print(f"Humidity at {city} is : {data['main']['humidity']} g.m-3 ")
    speak(f"Humidity at {city} is : {data['main']['humidity']} grams of water vapour per cubic metre")

    
    sunrise = dt.datetime.utcfromtimestamp(data['sys']['sunrise']+data['timezone'])
    sunset = dt.datetime.utcfromtimestamp(data['sys']['sunset']+data['timezone'])
    print(f"Sunrise Time at {city} is : {sunrise}")
    speak(f"Sunrise Time at {city} is : {sunrise}")
    print(f"Sunset Time at {city} is : {sunset}")
    speak(f"Sunset Time at {city} is : {sunset}")

    print(f"Wind Speed at {city} is : {data['wind']['speed']} m/s")
    speak(f"Wind Speed at {city} is : {data['wind']['speed']} meter per second")


if __name__ == "__main__":
    # speak("Ankit is a BAsketball Player")
    wishMe()
    myDetails()

    print("How may I help you ?")
    speak("How may I help you ?")

    # takeCommand()
    while True:
        query = takeCommand().lower()
        

        if query == 'sleep':
            print(query)
            speak("Good Bye! Have a nice Day")
            
            break;

        if 'wikipedia' in query:
            
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            # results = wikipedia.summary(query, sentences=2)
            # speak("According to wikipedia... ")
            # speak(results) 
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia... ")
                print(results)
                speak(results)
            except Exception as e:
                # Handle other exceptions, if needed
                speak("An error occurred while searching Wikipedia.")
        elif 'open youtube' in query:
            speak("Opening Youtube!")
            webbrowser.open("https://www.youtube.com/")

        elif 'your name' in query:
            print("My name is Selina. How may I help you?")
            speak("My name is Selina. How may I help you?")

        elif 'current time' in query:
            curr = datetime.datetime.now().time()
            hr = curr.hour
            min = curr.minute
            sec = curr.second
            print(f"Current Time -> {hr} : {min} : {sec}")
            speak(f"Current Time is {hr} hour, {min} minutes, {sec} seconds" )

        elif 'current date' in query:
            current_datetime = datetime.datetime.now().date()
            print("Current Date :", current_datetime)
            speak(f"Current date is : {current_datetime}")

        elif 'weather' in query:
            
            try:
                base_url = "https://api.openweathermap.org/data/2.5/weather?q="
                print("Please say the name of City.")
                speak("Please say the name of City.")
                city = takeCommand()
                complete_url = base_url+city+"&appid="+weather_api.key
                data = requests.get(complete_url).json()

                if(city != 'none'):
                    weatherCondition(city,data)
            except Exception as e:
                print("An unexpected error occured. Please try again.")
                speak("An unexpected error occured. Please try again.")




        elif 'open facebook' in query:
            speak("Opening Facebook!")
            webbrowser.open("https://www.facebook.com/")

        elif 'open jiocinema' in query or 'open jio cinema' in query:
            speak("Opening Jio Cinema!")
            webbrowser.open("https://www.jiocinema.com/")

        elif 'open github' in query:
            speak("Opening Github!")
            webbrowser.open("https://github.com/")

        elif 'open whatsapp' in query:
            speak("Opening WhatsApp!")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open google' in query:
            speak("Opening Google!")
            webbrowser.open("https://www.google.com/")


        elif 'open app' in query:
            speak("Here are the listed apps on your System!")

            command = 'explorer /select,"C:\\Users\\<username>\\Desktop"'

            subprocess.run(command, shell=True)

        elif 'send email' in query:
            try:
                speak("please enter your email id.")
                myid = input("Please enter your email id : ")
                speak("Please enter your password created at google secure app : ")
                mypass = input("Please enter your password created at google secure app : ")
                speak("please enter the email id of recipient.")
                to = input("Please enter the email id of recipient : ")
                speak("What should i say")
                content = takeCommand()
                sendEmail(myid,mypass,to,content)
                speak("Email sent successfully")
            except Exception as e:
                speak("An unwanted error occured, Email was not delivered!")

        elif 'phone details' in query:
            speak("Enter Phone Number with country code")
            number = input("Enter Phone Number with country code : ")
            phone = phonenumbers.parse(number)
            time = timezone.time_zones_for_number(phone)
            car = carrier.name_for_number(phone,"en")
            reg = geocoder.description_for_number(phone,"en")

            print(phone)
            speak(phone)
            print(f"Time Zone is {time}")
            speak(f"Time Zone is {time}")
            print(f"{car} is Number's service provider")
            speak(f"{car} is Number's service provider")
            print(f"The number is registered in {reg}")
            speak(f"The number is registered in {reg}")

            speak("Thank You!")

        elif query == "none":
            speak("say that again please...")


        else:
            try:
                
                openai.api_key = openAI_key.key 
                


                completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": f"{query}"}])

                print(completion.choices[0].message.content)
                speak(completion.choices[0].message.content)
            except Exception as e:
                
                print("An unexpected error occured. Please try again.")
                speak("An unexpected error occured. Please try again.")
 
                

                # just go to the given link to convert to .exe file 

                # https://youtu.be/oNq9QKX3lMs



                # Make sure to install the given version of charset-normalizer using the command given below else you might enconter an error.

                #                    ' pip install charset-normalizer==2.1.0 '