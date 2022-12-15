#!/usr/bin/env python
from main import db
import read

def delete_resource(bubble_name, resource_idx):
    bubbleID = read.get_bubble_id(bubble_name)
    resourceID = db.collection('bubbles').document(bubbleID).collection('resources').where('idx', '==', resource_idx).get()[0].id
    db.collection('bubbles').document(bubbleID).collection('resources').document(resourceID).delete()

# delete_resource('test', 2)

def delete_bubble(bubble_name):
    bubbleID = read.get_bubble_id(bubble_name)
    db.collection('bubbles').document(bubbleID).delete()

delete_bubble('bash')
