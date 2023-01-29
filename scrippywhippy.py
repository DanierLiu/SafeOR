from flask import Flask
import subprocess
app = Flask(__name__)

@app.route("/")
def hello_world():
    subprocess.Popen("python3 detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat".split(" "), start_new_session=True)
    subprocess.Popen("python3 equipment_check.py".split(" "), start_new_session=True)
    return "Success!"