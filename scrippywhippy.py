from flask import Flask
import subprocess
import time
import firebase_admin
from firebase_admin import credentials, db, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def hello_world():
    p1 = subprocess.Popen("python3 detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat".split(" "), start_new_session=True)
    p2 = subprocess.Popen("python3 equipment_check.py".split(" "), start_new_session=True)
    p1.wait()
    p2.wait()
    return "Success!"

@app.route("/fatigue", methods = ['GET'])
def get_fat():
    doc_ref = db.collection(u'records').document(u'patient')
    doc_ref.get().to_dict()[u'time']
    doc_ref.get().to_dict()[u'fatigues']


