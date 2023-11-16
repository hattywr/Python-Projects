import speech_recognition as sr
import pyttsx3
import sys
import multiprocessing

import os
#from dotenv import load_dotenv
#load_dotenv()
#OPENAI_KEY = os.getenv('OPENAI_KEY')

#comment out the api key if code is published
import openai
openai.api_key = "PLACE FOR API KEY"

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #for i in range(len(voices)):
     #   engine.setProperty('voice', voices[i].id)
      #  engine.say("Hello world")
    engine.say(command)
    engine.runAndWait()




def record_text(r):
    while(1):
        try:
            with sr.Microphone() as source2:

                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("I am listening!")

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                print(MyText)
                return MyText
        
        except sr.RequestError as e:
            print(f'Could not request results; {e}')
        
        except sr.UnknownValueError:
            print("Unknown Error Occurred")


def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = 1000,
        n = 1,
        stop = None,
        temperature = 0.5,
    )

    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message




#messages = []



def main():
    r = sr.Recognizer()
    messages = []
    while True:        
        text = multiprocessing.Process(record_text(r))
        text.start()
        text.join
        #text = record_text(r)
        messages.append({"role": "user","content": text})
        if (text.find("terminate app") != -1):
            print("Program received termination code.")
            messages = []
            messages.append({"role": "user","content": "Say: Program Received Termination Code. Goodbye"})
            response = send_to_chatGPT(messages)
            SpeakText(response)
            print(response)
            
            sys.exit(0)
        else:
            response = send_to_chatGPT(messages)
            SpeakText(response)
            print(response)

main()
