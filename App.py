import firebase_admin
from firebase_admin import credentials, db, firestore
import json
import keyboard
import asyncio


from audioTranscription import *

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

asyncio.run(monitor_fatigue())
start_audio_recog(db)
db.collection(u'equipment').document(u'fork').set(data = {u'name':u'fork',u'requested':False,u'taken':False})
db.collection(u'equipment').document(u'scalpel').set(data = {u'name':u'scalpel',u'requested':False,u'taken':False})

while True:
    doc_ref = db.collection(u'equipment').document(u'fork')
    fork_data = doc_ref.get().to_dict()
    if fork_data['requested'] != fork_data['taken']:
        alert
    
    doc_ref = db.collection(u'equipment').document(u'scalpel')
    scalpel_data = doc_ref.get().to_dict()
    if scalpel_data['requested'] != scalpel_data['taken']:
        alert


