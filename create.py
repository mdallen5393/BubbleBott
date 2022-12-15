#!/usr/bin/env python
import main
from main import db
import read
import firebase_admin
from firebase_admin import credentials, firestore

def make_bubble(name, owner, desc):
    db.collection('bubbles').add({'name': name, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})

def new_resource_id(bubble_name):
    return len(read.get_bubble_resources(bubble_name))

def add_resource(bubble_name, content, owner, desc):
    bubbleID = read.get_bubble_id(bubble_name)
    resourceID = new_resource_id(bubble_name)
    db.collection('bubbles').document(bubbleID).collection('resources').add({'idx':resourceID, 'content':content, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})

# add_resource()
# make_bubble()
