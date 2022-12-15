#!/usr/bin/env python
from main import db

def get_bubble_id(bubble_name):
    return db.collection('bubbles').where('name', '==', bubble_name).get()[0].id

def get_bubble(bubble_name='bubbles'):
    # Get a specific bubble
    if bubble_name != 'bubbles':
        doc = db.collection('bubbles').where('name', '==', bubble_name).get()
        return (doc[0].to_dict())

    # Get all bubbles
    docs = db.collection(bubble_name).get()
    bubbles = []
    for doc in docs:
        bubbles.append(doc.to_dict())
    return bubbles

def get_bubble_resources(bubble_name):
    # Get all resources in a bubble
    docID = get_bubble_id(bubble_name)
    docs = db.collection('bubbles').document(docID).collection('resources').get()
    resources = []
    for doc in docs:
        resources.append(doc.to_dict())
    return resources

# print("Print all bubbles:")
# print(get_bubble())
# print('-'*20)
# print("Print the 'firestore' bubble:")
# print(get_bubble('firestore'))
# print('-'*20)
# print("Print all resources in the 'firestore' bubble:")
# print(get_bubble_resources('test'))