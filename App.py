import firebase_admin
from firebase_admin import credentials, db
import json
import keyboard
import asyncio


from audioTranscription import *

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

asyncio.run(monitor_fatigue())
while True:
    start_audio_recog()
