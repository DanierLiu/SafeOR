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

doc_ref = db.collection(u'equipment').document(u'fork')
doc_ref.update({u'requested':False})
doc_ref = db.collection(u'equipment').document(u'scalpel')
doc_ref.update({u'requested':False})
asyncio.run(monitor_fatigue())
while True:
    start_audio_recog(db)
    time.sleep(2)
    
    doc_ref = db.collection(u'equipment').document(u'fork')
    fork_data = doc_ref.get().to_dict()
    if fork_data['requested'] != fork_data['taken']: 
        print('fork alert')
    
    doc_ref = db.collection(u'equipment').document(u'scalpel')
    scalpel_data = doc_ref.get().to_dict()
    if scalpel_data['requested'] != scalpel_data['taken']:
        print('scalpel alert')

    doc_ref = db.collection(u'equipment').document(u'fork')
    doc_ref.update({u'requested':False})
    doc_ref = db.collection(u'equipment').document(u'scalpel')
    doc_ref.update({u'requested':False})
