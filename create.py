#!/usr/bin/env python
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def make_bubble(name='test', owner='matt', desc='test'):
    db.collection('bubbles').add({'name': name, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})


# make_bubble()