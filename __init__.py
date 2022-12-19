from firebase_admin import credentials, firestore, initialize_app
from flask import Flask

# cred = credentials.Certificate("serviceAccountKey.json")
# initialize_app(cred)

# db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("serviceAccountKey.json")
default_app = initialize_app(cred)
db = firestore.client()