# NOTE: bid = bubble ID; rid = resource ID

import os
from firebase_admin import firestore
from flask import request, jsonify
from __init__ import db, app
# import create, read, update, delete
from create import add_resource, new_resource_id
from read import get_bubble_id, get_bubble_resources
from delete import deleteResource

bubbles_ref = db.collection('bubbles')

@app.route('/add_bubble', methods=['POST', 'GET'])
def create_bubble():
    """
    Add bubble
    Usage: curl '127.0.0.1:8080/add_bubble?name=hi&owner=matt&desc=testing+add+bubble'
    """
    try:
        bubble_name = request.args.get('bubble_name')
        owner = request.args.get('owner')
        desc = request.args.get('desc')
        if not bubble_name:
            raise Exception("must include a name")
        bubbles_ref.add({'name': bubble_name, 'owner':owner, 'description':desc, 'createdAt':firestore.SERVER_TIMESTAMP})
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}\n'

@app.route('/get_id', methods=['GET'])
def get_id():
    try:
        bubble_name = request.args.get('bubble_name')
        if not bubble_name:
            raise Exception("must include name")
        return get_bubble_id(bubble_name)
    except Exception as e:
        return f'An error occurred: {e}\n'

@app.route('/add_resource', methods=['POST', 'GET'])
def create_resource():
    """
    Add resource to bubble
    """
    try:
        #Check if ID was passed to URL query
        bubble_name = request.args.get('bubble_name')
        if not bubble_name:
            raise Exception("must specify a bubble")
        bid = get_bubble_id(bubble_name)
        content = request.args.get('content')
        owner = request.args.get('owner')
        desc = request.args.get('desc')
        idx = new_resource_id('test')
        json = {'content':content, 'owner':owner, 'description':desc, 'idx':idx, 'createdAt':firestore.SERVER_TIMESTAMP}
        bubbles_ref.document(bid).collection('resources').add(json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}\n'

@app.route('/list_bubbles', methods=['GET'])
def read():
    """
    Fetch all bubbles
    """
    try:
        bubble_name = request.args.get('bubble_name')
        if not bubble_name:
            all_bubbles = [doc.to_dict() for doc in bubbles_ref.stream()]
            return jsonify(all_bubbles), 200
        bid = get_bubble_id(bubble_name)
        if bid:
            bubble = bubbles_ref.document(bid).get()
            return jsonify(bubble.to_dict()), 200
        else:
            raise Exception
    except Exception as e:
        return f'An Error Occurred: {e}\n'

@app.route('/list_resources', methods=['GET'])
def get_resources():
    try:
        bubble_name = request.args.get('bubble_name')
        if not bubble_name:
            raise Exception('must specify a bubble')
        resources = get_bubble_resources(bubble_name)
        if not resources:
            raise Exception(f'no resources in bubble {bubble_name}')
        return jsonify(resources)
    except Exception as e:
        return f'An Error Occurred: {e}\n'

@app.route('/update_bubble', methods=['POST', 'PUT', 'GET'])
def update_bubble():
    """
    Update bubble
    """
    try:
        bubble_name = request.args.get('bubble_name')
        bid = get_bubble_id(bubble_name)
        bubbles_ref.document(bid).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}'

@app.route('/update_resource', methods=['POST', 'PUT', 'GET'])
def update_resource():
    try:
        bubble_name = request.args.get('bubble_name')
        bid = get_bubble_id(bubble_name)
        rid = request.args.get('rid')
        resource_path = bubbles_ref.document(bid).collection('resources').document(rid).get()
        if not resource_path.exists:
            raise Exception(f'rid \'{rid}\' does not exist in bubble \'{bubble_name}\' at path {resource_path}')
        resource_path.update(request.json)
        return jsonify({'success': True}), 200
    except Exception as e:
        return f'An error occurred: {e}\n'

@app.route('/delete_bubble', methods=['GET', 'DELETE'])
def delete_bubble():
    """
    Delete a bubble
    """
    try:
        #Check if ID was passed to URL query
        bubble_name = request.args.get('bubble_name')
        bid = get_bubble_id(bubble_name)
        bubbles_ref.document(bid).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}\n'

@app.route('/delete_resource', methods=['GET', 'DELETE'])
def delete_resource():
    try:
        bubble_name = request.args.get('bubble_name')
        if not bubble_name:
            raise Exception('must include bubble_name')
        idx = request.args.get('idx')
        if not idx:
            raise Exception('must include idx')
        idx = int(idx)
        deleteResource(bubble_name, idx)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}\n'

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)