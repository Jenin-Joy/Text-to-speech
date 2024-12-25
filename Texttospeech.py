# importing the pyttsx library 
import speech_recognition as sr
import pyttsx3 
# initialisation 
engine = pyttsx3.init() 
r = sr.Recognizer()
# testing 
# print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(device_index=0)

with mic as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print(text)
engine.say(text) 
# engine.say("Thank you, Geeksforgeeks")
engine.runAndWait() 