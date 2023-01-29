import speech_recognition as sr
import keyboard

def transcribe(recog, audio):
    response = {
        'transcription' : None
    }

    try:
        response['transcription'] = recog.recognize_google(audio)
        print(response['transcription'])
    except:
        print('bruh')


recog = sr.Recognizer()
recog.lang = 'en-US'
recog.interimResults = False
recog.maxAlternatives = 1
mic = sr.Microphone()

with mic as source:
    recog.adjust_for_ambient_noise(source)
    
print("Listening...")
stop_listening = recog.listen_in_background(mic, transcribe)

while True:
    if keyboard.is_pressed('q'):
        stop_listening(wait_for_stop = False)
        break
