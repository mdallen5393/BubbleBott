#!/usr/bin/env python
import firebase_admin
from firebase_admin import credentials, firestore
from CRUD import create
# , read, update, delete

if __name__ == '__main__':
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    create.add_bubble('test', 'test', 'test')