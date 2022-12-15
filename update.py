#!/usr/bin/env python
import main
from main import db
import read
import firebase_admin
from firebase_admin import credentials, firestore

def update_resource(bubble_name, resource_idx, **kwargs):
    bubbleID = read.get_bubble_id(bubble_name)
    resourceID = db.collection('bubbles').document(bubbleID).collection('resources').where('idx', '==', resource_idx).get()[0].id
    db.collection('bubbles').document(bubbleID).collection('resources').document(resourceID).update(kwargs)

# kwargs = {'description': 'Update 2 successful!'}
# update_resource('test', 0, **kwargs)
