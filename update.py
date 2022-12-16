#!/usr/bin/env python
from __init__ import db
from read import get_bubble_id

def update_resource(bubble_name, resource_idx, **kwargs):
    bubbleID = get_bubble_id(bubble_name)
    if not bubbleID:
        return f'bubble {bubble_name} does not exist'
    resourceID = db.collection('bubbles').document(bubbleID).collection('resources').where('idx', '==', resource_idx).get()[0].id
    if not resourceID.exists:
        return f'{bubble_name} resource {resource_idx} does not exist'
    db.collection('bubbles').document(bubbleID).collection('resources').document(resourceID).update(kwargs)
    return f'update of {bubble_name} resource {resource_idx} successful'

# kwargs = {'description': 'Update 2 successful!'}
# update_resource('test', 0, **kwargs)
