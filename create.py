#!/usr/bin/env python
# import read
from __init__ import db
from firebase_admin import firestore
from read import get_bubble_resources, get_bubble_id

def add_bubble(name, owner, desc):
    if not name:
        return 'Usage: add_bubble(name, owner, desc)'
    db.collection('bubbles').add({'name': name, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})

def new_resource_id(bubble_name):
    return len(get_bubble_resources(bubble_name))

def add_resource(bubble_name, content, owner, desc):
    bid = get_bubble_id(bubble_name)
    rid = new_resource_id(bubble_name)
    db.collection('bubbles').document(bid).collection('resources').add({'idx':rid, 'content':content, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})

# add_resource()
# make_bubble()
