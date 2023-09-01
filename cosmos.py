#RAW (COSMOS)
#IMPORT FILES
import pyttsx3,datetime,pyautogui,time,wikipediaapi,webbrowser
import speech_recognition as sr
from AppOpener import open
#SPEAK FUNCTION
hfbot=pyttsx3.init('sapi5')
voices=hfbot.getProperty('voices') # voice taken
hfbot.setProperty('rate', 200) #rate of speak
rate=hfbot.getProperty('rate')
hfbot.setProperty('voice', voices[0].id) # 0 for male and 1 for female
def speak(audio):
    hfbot.say(audio)
    hfbot.runAndWait()

#RESTART ALERT
print('RAW Intelligence restarted')
speak('raw intelligence Restarted')
speak('Cosmos activated')

#STT SPEAK TO TEXT IN ENGLISH
recognizer = sr.Recognizer()
def commandeng():
    with sr.Microphone() as source:
        speak('listening')
        print("Listening...")
        recognizer.pause_threshold = 2
        recognizer.energy_threshold=4000
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")    
        text = recognizer.recognize_google(audio, language='en-in')
        text=str(text)
        text=text.lower()
        print(f"CC: {text}")  
    except Exception: 
        speak('Sir, sorry could not understand')
        print("Sir, Sorry could not understand ")
        return "None"
    return text

#wait till commanded
def sleeping():
    speak('Okay sir, Switching to Sleep Mode')
    print("Sleep Mode Activated")
    while True:
        with sr.Microphone() as source:
            recognizer.pause_threshold = 2
            recognizer.energy_threshold=4000
            audio = recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio, language='en-in')
            text=str(text)
            text=text.lower()
        except:
            text=''
        if 'cosmos' in text:
            greet()
            speak('Sir, How can i help you?')
            print('Sir, How can i help you?')
            order= commandeng()
            return order
            break
        else:
            True

#COMMANDS

#Date and time  ✓
def calendar():
    now= datetime.datetime.now()
    year= now.strftime('%Y')
    month= now.strftime('%B')
    date= now.strftime('%d')
    day=now.strftime('%A')
    return year, month, date, day
def clock():
    now= datetime.datetime.now()
    currhour= now.strftime('%H')
    minute= now.strftime('%M')
    sec= now.strftime('%S')
    if int(currhour) > 12:
        currhour=int(currhour)
        hour=currhour-12
        status='p.m.'
    elif int(currhour)==12:
        hour=int(currhour)
        status='p.m.'
    else:
        hour=int(currhour)
        status='a.m.'
    minute=int(minute)
    return hour,minute,sec,status

#Schedule a WHATSAPP message  ✓
def whatmsg(name,msg,hr,minut,stat,purpose):
    speak('message scheduled')
    if purpose == 'professional':
        msg='HEY THIS IS RYANS ARTIFICIAL WING _Cosmos_. THIS MESSAGE IS SENT ON BEHALF OF RYAN --   '+str(msg)
    else:
        msg=str(msg)
    while True:
        curhr,curmint,cursec,curstat=clock()
        if curstat == stat:
            print('stat done')
            print(curhr)
            if curhr == hr:
                print('hour done')
                if curmint == minut:
                    print('Sir you are requested to wait untill message is sent')
                    speak('opening whatsapp for the scheduled message')
                    open("whatsapp")
                    time.sleep(2)
                    pyautogui.click(1300, 650)
                    time.sleep(0.5)
                    pyautogui.hotkey('win','up')
                    pyautogui.leftClick(280,220,2)
                    speak(f'sending message to {name}')
                    pyautogui.write(name)
                    pyautogui.leftClick(280,350,1,1)
                    pyautogui.write(msg)
                    pyautogui.press('enter')
                    speak('message sent successfully')
                    print('Message sent successfully')
                    pyautogui.hotkey('alt','f4')
                    break
                else:
                    True
            else:
                True
        else:
            True

#greetings  ✓
def greet():
    hour,minute,sec,status=clock()
    year, month, date, day=calendar()
    if status == 'a.m.':
        speak('Good Morning sir')
        print('Good morning sir')
        speak(f'It is {hour}, {minute}, {status}')
        print(f'It is {hour}:{minute} {status}')
        speak(f'Sir, Have a great {day} Ahead')
        print(f'Sir, Have a great {day} Ahead')
    elif status == 'p.m.':
        if hour < 6 or hour == 12:
            speak('Good Afternoon sir')
            print('Good Afternoon sir')
            speak(f'Its {day}')
            speak(f'It is {hour}, {minute}, {status}')
            print(f'It is {hour}:{minute} {status}')
        elif hour>=6 and hour<8:
            speak('Good Evening sir')
            print('Good Evening sir')
            speak(f'Its {day}')
            speak(f'It is {hour}, {minute}, {status}')
            print(f'It is {hour}:{minute} {status}')
        else:
            speak('Good Night sir')
            print('Good Night sir')
            speak(f'Its {day}')
            speak(f'It is {hour}, {minute}, {status}')
            print(f'It is {hour}:{minute} {status}')
            speak('Have a great night, sweet dream sir')

#whatsapp call  ✓
def whatcall(name,type):
    if type == 'video':
        speak('opening whatsapp for the video calling')
        open("whatsapp")
        time.sleep(2)
        pyautogui.click(1300, 650)
        time.sleep(0.5)
        pyautogui.hotkey('win','up')
        pyautogui.leftClick(280,220,2)
        speak(f'Calling to {name}')
        pyautogui.write(name)
        pyautogui.leftClick(280,350,1,1)
        pyautogui.leftClick(2586,136)
        while True:
            with sr.Microphone() as source:
                recognizer.pause_threshold = 2
                recognizer.energy_threshold=4000
                audio = recognizer.listen(source)
            try:
                text=recognizer.recognize_google(audio, language='en-in')
                text=str(text)
                text=text.lower()
            except:
                text=''
            print(text)
            if 'cosmos' in text:
                speak('should i call again?')
                txt=commandeng()
                if 'yes' in txt:
                    speak(f'Calling once more to {name}')
                    pyautogui.leftClick(2586,136)
                    True
                else:
                    speak('Call is hopefully ended')
                    speak('Closing whatsapp in 5 seconds')
                    time.sleep(5)
                    pyautogui.hotkey('alt','f4')
                    speak('Whatsapp closed')
                    break
            else:
                True
    else:
        speak('opening whatsapp for the voice calling')
        open("whatsapp")
        time.sleep(2)
        pyautogui.click(1300, 650)
        time.sleep(0.5)
        pyautogui.hotkey('win','up')
        pyautogui.leftClick(280,220,2)
        speak(f'Calling to {name}')
        pyautogui.write(name)
        pyautogui.leftClick(280,350,1,1)
        pyautogui.leftClick(2686,139)
        while True:
            with sr.Microphone() as source:
                recognizer.pause_threshold = 2
                recognizer.energy_threshold=4000
                audio = recognizer.listen(source)
            try:
                text=recognizer.recognize_google(audio, language='en-in')
                text=str(text)
                text=text.lower()
            except:
                text=''
            print(text)
            if 'cosmos' in text:
                speak('should i call again')
                txt=commandeng()
                if 'yes' in txt:
                    speak(f'Calling once more to {name}')
                    pyautogui.leftClick(2686,139)
                    True
                else:
                    speak('Call is hopefully ended')
                    speak('Closing whatsapp in 5 seconds')
                    time.sleep(5)
                    pyautogui.click(2800, 20)
                    speak('Whatsapp closed')
                    break
            else:
                True

#wikipedia
def wikipedia(title):
    numb=1
    wiki = wikipediaapi.Wikipedia('https://www.wikipedia.org/','en')
    info = wiki.page(title)
    detail=info.summary
    detail=detail.split('.')
    if not info.exists():
        print("No Information Found")
        speak(f'Sorry sir, Could not find information on {title}')
    for i in detail:
        if numb == 1:
            speak(f'Here is the information on {title}')
            speak(i)
            speak('Further details are being displayed')
        print('→'+i)
        numb+=1

#specifications
#def exspecify():

#openapp
def openapp(name):
    try:
        speak(f'Trying to open {name}')
        open(name,True,True,True)
        speak('Application successfully opened')
    except Exception:
        speak('Could not find the application mentioned')
    
#open webs with url
def webopen(url):
    webbrowser.open(url)
    speak('opening website')
    closeapp('website')

#close app  ✓
def closeapp(name):
    while True:
        with sr.Microphone() as source:
            recognizer.pause_threshold = 2
            recognizer.energy_threshold=4000
            audio = recognizer.listen(source)
        try:
            text=recognizer.recognize_google(audio, language='en-in')
            text=str(text)
            text=text.lower()
        except:
            text=''
        print(text)
        if 'cosmos' in text:
            speak(f'Sir, should i close {name}')
            txt=commandeng()
            if 'yes' in txt:
                pyautogui.click(1300, 650)
                pyautogui.hotkey('alt','f4')
                speak(f'{name} closed successfully')
                break
            else:
                True
        else:
            True

#search
def search(browser,query):
    if browser == 'bing':
        speak('Opening on bing')
        webbrowser.open(f'https://www.bing.com/search?q={query}')
        closeapp('bing')
    elif browser == 'google':
        speak('opening on google')
        webbrowser.open(f"https://www.google.com/search?q={query}")
        closeapp('google')
    else:
        speak('sorry sir right now we dont have access to this search engine')
    
#RESUME'  ✓
def myresume():
    speak('Sir, my name is Cosmos')
    speak('my mother company is RAW that is Ryans Artificial Wing')
    speak('Day of my release which you can call my birthday is 18th August 2023')
    speak('If i tell you about my personality then i m loyal, Complacent, Supportive and Smart')
    speak('If you ask me about my view on world then i m optimistic')
    speak('Quirk thing about me is that i believe nothing is impossible for me')
    speak('I m agnostic in religious view')
    speak('Obviously being a software , i m afraid of trojans and viruses')
    speak('I love to help, talk and code')
    speak('Thank you sir , now if you want any help then u can call cosmos')

#------------------------------   MAIN ORDER UNDERTAKING   ------------------------------
while True:
    order=sleeping()
    if 'introduction' in order:
        myresume()
    elif 'whatsapp message' in order:
        speak('Okay sir whom to send message')
        while True:
            name=commandeng()
            if name == 'None':
                speak('It will be better if you can type the name as my system could not recognise it right now')
                name = input('Enter name:')
                break
            else:
                speak(f'Want to send message to {name}')
                print(f'Name is {name}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong name recognisation')
                    speak('Let me try once more')
                    True
        speak(f'What message should i send to {name}')
        while True:
            msg=commandeng()
            if msg == 'None':
                speak('It will be better if you can type the message as my system could not recognise it right now')
                name = input('Enter Message:')
                break
            else:
                speak(f'Message to be sent to {name} is {msg}')
                print(f'Message is {msg}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong message interpretation')
                    speak('Let me try once more')
                    True
        speak('Let me know at what time should i send this message')
        while True:
            hr =int(input('Enter the hour:'))
            minut=int(input('Enter minute:'))
            speak('Enter 1 for A.M. and 2 for P.M.')
            ampm=int(input('Enter 1 for AM & 2 for PM: '))
            if ampm == 1:
                stat ='a.m.'
                speak('Just cross checking once')
                speak(f'message has to be send at {hr}:{minut} {stat}')
                print(f'Message has to be send at {hr}:{minut} {stat}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong time interpretation')
                    speak('Let me try once more')
                    True
            elif ampm == 2:
                stat = 'p.m.'
                speak('Just cross checking once')
                speak(f'message has to be send at {hr}:{minut} {stat}')
                print(f'Message has to be send at {hr}:{minut} {stat}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong time interpretation')
                    speak('Let me try once more')
                    True
            else:
                speak('ERROR HAS BEING OCCURED WRONG INTEGER INSERTED')
                print('ERROR HAS BEING OCCURED WRONG INTEGER INSERTED')
                speak('Let me try once more')
                True
        speak('Sir is the purpose professional or personal')
        pur=commandeng()
        if 'professional' in pur:
            purpose='professional'
        else:
            purpose='personal'
        speak('Okay sir message has been setup successfully')
        whatmsg(name,msg,hr,minut,stat,purpose)
    elif 'whatsapp call' in order:
        speak('okay sir, what type of call should i do means voice call or video call')
        types=commandeng()
        speak('Whom to make call')
        while True:
            name=commandeng()
            if name == 'None':
                speak('It will be better if you can type the name as my system could not recognise it right now')
                name = input('Enter name:')
                break
            else:
                speak(f'Want to call to {name}')
                print(f'Name is {name}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong name recognisation')
                    speak('Let me try once more')
                    True
        whatcall(name,types)
    elif 'open' in order:
        speak('Sir, which app you want me to open it for you')
        while True:
            apname=commandeng()
            if apname == 'None':
                speak('It will be better if you can type the name as my system could not recognise it right now')
                name = input('Enter app name:')
                break
            else:
                speak(f'Want to open {apname}')
                print(f'App Name is {apname}')
                crct = commandeng()
                if 'yes' in crct:
                    break
                else:
                    speak('Sorry sir for wrong app name recognisation')
                    speak('Let me try once more')
                    True
        openapp(apname)
    elif 'close' in order:
        speak('Okay sir closing the open application')
        closeapp('app')
    elif 'wikipedia' in order:
        speak('On what topic do you want me to brief about')
        title=commandeng()
        wikipedia(title)
    else:
        speak('Sorry sir, right now i do not have any response to this task')
        speak('But if you want, you can make me search something related to it on internet')
