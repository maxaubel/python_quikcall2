import speech_recognition as sr 


r = sr.Recognizer() 

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

mic = sr.Microphone(device_index=7)

with mic as source: 
    audio = r.listen(source) 
result = r.recognize_google(audio, language="es-ES")

print(result)