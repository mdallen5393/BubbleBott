#!/usr/bin/env python
from __init__ import db

def get_bubble_id(bubble_name):
    bubble = db.collection('bubbles').where('name', '==', bubble_name).get()
    if bubble:
        return bubble[0].id

def get_bubble(bubble_name='bubbles'):
    # Get a specific bubble
    if bubble_name != 'bubbles':
        doc = db.collection('bubbles').where('name', '==', bubble_name).get()
        if not doc.exists:
            return f'bubble {bubble_name} does not exist'
        return (doc[0].to_dict())

    # Get all bubbles
    docs = db.collection(bubble_name).get()
    if not docs.exists:
        return 'No bubbles'
    bubbles = []
    for doc in docs:
        bubbles.append(doc.to_dict())
    return bubbles

def get_bubble_resources(bubble_name):
    # Get all resources in a bubble
    docID = get_bubble_id(bubble_name)
    if not docID:
        return f'bubble {bubble_name} does not exist'
    docs = db.collection('bubbles').document(docID).collection('resources').get()
    if not docs:
        return f'no resources in bubble {bubble_name}'
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
# resources = get_bubble_resources('does_not_exist')
# if (resources):
#     print(resources)
# else:
#     print("Resource not found")