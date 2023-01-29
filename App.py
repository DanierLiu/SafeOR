import firebase_admin
from firebase_admin import credentials, db, firestore
import json
import keyboard
import asyncio
import time


from audioTranscription import *

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#asyncio.run(monitor_fatigue())

while True:
    start_audio_recog(db)
    time.sleep(2)
    
    doc_ref = db.collection(u'equipment').document(u'fork')
    fork_data = doc_ref.get().to_dict()
    if fork_data['requested'] != fork_data['taken']: 
        print('alert')
    
    doc_ref = db.collection(u'equipment').document(u'scalpel')
    scalpel_data = doc_ref.get().to_dict()
    if scalpel_data['requested'] != scalpel_data['taken']:
        print('alert')


