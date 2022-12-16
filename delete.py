#!/usr/bin/env python
from __init__ import db
from read import get_bubble_id

def delete_resource(bubble_name, resource_idx):
    bubbleID = get_bubble_id(bubble_name)
    if not bubbleID:
        return f'bubble {bubble_name} not found'
    resource = db.collection('bubbles').document(bubbleID).collection('resources').where('idx', '==', resource_idx).get()
    if not resource:
        return f'resource [{resource_idx}] not found'
    resourceID = resource[0].id
    db.collection('bubbles').document(bubbleID).collection('resources').document(resourceID).delete()
    return f'deleted {bubble_name} resource [{resource_idx}] successfully'

# delete_resource('test', 1)

def delete_bubble(bubble_name):
    bubbleID = get_bubble_id(bubble_name)
    if not bubbleID:
        return f'bubble {bubble_name} not found'
    db.collection('bubbles').document(bubbleID).delete()
    return f'deleted {bubble_name} successfully'

# delete_bubble('bash')
