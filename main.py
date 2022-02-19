import pyttsx3
friend = pyttsx3.init()
speech = input ("What text do you want me to convert ?")
friend.say(speech)
friend.runAndWait ()