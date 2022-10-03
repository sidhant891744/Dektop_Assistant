#importing file modules for this A.I version
#Creating by Sidhant Swapnil

#from cgitb import text
#from logging import exception
#from msilib.schema import Condition
#import sys
from time import time
from unittest import result
from unittest.mock import patch
from PyPDF2 import PdfReader
import PyPDF2
from bs4 import BeautifulSoup
import pyttsx3
import requests
import speech_recognition
import datetime
import os
import cv2
import random 
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import smtplib
import pyjokes
import instaloader
import pyautogui
from PIL import Image



#<.....all the voices text to speech convertation.......>

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",140)
                  

#<..Defining audio...>


        




def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
   
#<..taking command from user...>



def TaskExecute():
    speak('Allow me to introduce myself.')
    speak('I am Jarvis,The vertual artifical intelligence.')
    speak('And I am Here to assist you the verity of tasks is the best i can, 24 hours a day,7 days a week.') 
    speak('Importing all preferences from home interface.')
    speak('System is now fully operational...')
    time=datetime.datetime.now().strftime("%H:%M")
    search="temperature in hyderabad"
    soup=BeautifulSoup(requests.get(f"https://www.google.com/search?q={search}").text, "html.parser")
    temp= soup.find("div", class_="BNeawe").text
   
    
    hour=int(datetime.datetime.now().hour)
     
    if hour>=0 and hour<=11:
        speak("Sir It looks like a beautifull morning is waiting for you outside"f"") 
        speak("I wish you Good morning,"f" it is {time}")
       
    elif hour>=12 and hour<=18:
        speak("Sir It looks like a beautifull afternoon is waiting for you outside")
        speak("I wish you Good afternoon,"f" it is {time}")
    
    
      
    elif hour>18 and hour<=24:
        speak("Sir It looks like a beautifull evening is waiting for you outside")
        speak("I wish you Good evening,"f" ,it is {time}")
        





def pdf_reader():
   book=open("python_book_01.pdf",'rb')
   PdfReader=PyPDF2.PdfFileReader(book)
   pages=PdfReader.numPages
   speak(f"Sir, The total number of pages in this book{pages}")
   speak("Sir there are too many pages, Which page you want to listen.")
   pg=int(input("please enter the page number: "))
   page=PdfReader.getPage(pg)
   text=page.extract_text()
   speak(text)
         
         
      

def takeCommand():
    
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("please sir say that again....")
        #speak("i don't understand sir,say again")
        return "None"
    query=query.lower()
    return query


#<...A.I will wish you when user wake up this voice......>


       
    
    
   
    
def youtubesearch(term):
       result = 'https://www.youtube.com/results?search_query='+term
       webbrowser.open(result)
       
       speak("Sir, I found as your wish sir ")
     
       
       speak("I think this may help you")
       
def temperature():
       search="temperature in hyderabad"
       soup=BeautifulSoup(requests.get(f"https://www.google.com/search?q={search}").text, "html.parser")
       temp= soup.find("div", class_="BNeawe").text
       speak(f"Sir, The current{search} is {temp}")       
       
       

def sendEmail(to,c):
       server=smtplib.SMTP('smtp.gmail.com',587)
       server.ehlo()
       server.starttls()
       server.login('sidhantswapnil89@gmail.com','8917446619')
       server.sendmail('sidhantswapnil89@gmail.com', to,c)
       server.close()       
       

if __name__=="__main__":      
  TaskExecute()
  while True:
       
       
     query=takeCommand().lower()
     
    
        
     if "open spotify" in query:
            speak("command processing, opening spotify sir")
            apath="C:\\Users\\ASUS\\AppData\\Roaming\\Spotify\\spotify.exe"
            os.startfile(apath)
            
    
    
     elif"end spotify" in query or "close spotify" in query:
            speak("closing spotify, i guess u listen enough music sir.")
            os.system("taskkill /f /im spotify.exe")
     
    
    
     elif "open cmd" in query:
            speak("command processing, opening command prompt sir")
            os.system("start cmd")
     
    
    
     elif"end cmd" in query  or "close cmd" in query:
            speak("closing sir please wait")
            os.system("taskkill /f /im cmd.exe")
     
    
    
     elif "notepad" in query:
            speak("command processing, opening notepad sir")
            apath="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(apath)
            
     elif"end notepad" in query  or "close notepad" in query:
            speak("closing sir please wait")
            os.system("taskkill /f /im notepad.exe")
     
     
     
     elif"camera" in query:
        cap=cv2.VideoCapture(0)
        while True:
            ret,img=cap.read()
            cv2.imshow('webcam',img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWindows()
    
    
     elif"play music" in query or "play a song" in query or "play song" in query:
        music_dir = "D:\\fav song"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir,rd))
        
     
     
     elif"wikipedia" in query:
        speak("searching in wikipedia, plz wait sir..")
        query= query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=4)
        speak("According to wikipedia")
        speak(result)
        print(result)
    
     
     elif"open youtube" in query:
        #webbrowser.open("www.youtube.com")
        Query=query.replace("jarvis","")
        query=Query.replace("youtubesearch","")
       
        youtubesearch(query)
        
        
     elif"open facebook" in query:
        webbrowser.open("www.facebook.com")

     
     
     
     
     
     elif"open whatsapp" in query:
        webbrowser.open("www.whatsapp.com")
    
    
     elif"open chrome"in query:
        apath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(apath)
     
     
     elif"open google"in query:
        webbrowser.open("www.google.com")
        speak("Sir,what should you looking in google")
        cm=takeCommand().lower()
        webbrowser.open(f"{cm}")
     
     
     
     elif"send message" in query:
        kit.sendwhatmsg("+919778241784","hello yaar",1,10)
     
     
     elif"play arijit singh song on youtube" in query:
        kit.playonyt("best of arijit singh")
     
     
     elif"play workout song on youtube" in query:
        kit.playonyt("best gym song hindi")
    
    
     elif"no thanks" in query or "ok thanks"in query or "thank you" in query:
        speak("thanx for using me sir")
        break 
        
    
     elif"time" in query:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, The current time in india is {time}")
        
     
     
     elif"send mail" in query:
         try:
            speak("what should you want to send sir")
            c=takeCommand()
            to="sidhantswapnil89@gmail.com"
            sendEmail(to,c)
            speak("Email has been sent to the specify name sir")
         except Exception as e:
            print(e)
            speak("sorry sir i am not able to sent email")
                  
     elif"set alarm" in query:
          n=int(datetime.datetime.now().hour)
          if n==22:
                 music_dir="D:\\fav song"
                 songs=os.listdir(music_dir)
                 os.startfile(os.path.join(music_dir, songs[0]))
                 
     elif"joke" in query:
            joke=pyjokes.get_joke()
            speak(joke)
            
            
     elif"where am" in query:
         speak("wait please, Let me check from GPS")
         try:
            ipAdd=requests.get('{"ip":"60.243.162.188"}').text 
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city=geo_data['city']
            country=geo_data['country']
             
            speak(f"sir, I think we are in {city} city of {country} country")
         except Exception as e:
            speak("I am extreamly sorry sir, i can't find from GPS")
            pass
             
     elif"temperature" in query or "weather" in query:
        temperature()            
         #speak(f"The time is {time}")
        #speak(f"And the current{search} is {temp}")    
        
         
     elif"instagram profile" in query:
        speak("Sir enter the username")
        name=input("Enter your username: ")
        webbrowser.open(f"www.instagram.com/{name}")
        speak(f"Sir here is the profile as you wish")
        #time.sleep(5)
        speak("Sir, This profile's pictures looking amazing. Would you like to download")
        Condition=takeCommand().lower()
        if "yes" in Condition:
           mod=instaloader.Instaloader()
           mod.download_profile(name,profile_pic_only=True)
           speak("Ok sir, I have stored the profile pic in main directory ") 
        elif "no" in Condition:
            speak("As your wish sir")
        else:
               
           pass 
        
        
        
     elif"take screenshot" in query or "take a screenshot" in query:
        speak("Sir, Please tell me the name for this screenshot picture")
        name = takeCommand().lower()
        speak("Wait a few second sir, taking Screenshot")
        #time.sleep(3)
        img=pyautogui.screenshot()
        img.save(f"{name}.jpg")
        speak("Ok sir, Screenshot task is completed")
     elif "show me the screenshot" in query:
         try:
                    img =Image.open('D:\\jarvis\\venv' + name)
                    img.show(img)
                    speak("Here it is sir")
                    time.sleep(2)

         except IOError:
                    speak("Sorry sir, I am unable to display the screenshot")

     elif "hide all files" in query or "hide this folder" in query:
                os.system("attrib +h /s /chrome.exe")
                speak("Sir, all the files in this folder are now hidden")

     elif "visible" in query or "make files visible" in query:
                os.system("attrib -h /s /d")
                speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
        
     
     
     
     elif"audiobook"in query:
        pdf_reader()  
        
     elif "Hello" in query:
         speak("Hello sir, how may i help you")
     
      
           
     
     
     
     
     
    # speak("Sir, Do u have any other work for me")'''   