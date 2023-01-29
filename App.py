import firebase_admin
from firebase_admin import credentials, db
import json
import keyboard
import async

from audioTranscription import *

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

while True:
    