# NOTE: bid = bubble ID; rid = resource ID

import os
from firebase_admin import credentials, firestore, initialize_app
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate("serviceAccountKey.json")
default_app = initialize_app(cred)
db = firestore.client()
bubbles_ref = db.collection('bubbles')

@app.route('/add_bubble/<name>', methods=['POST', 'GET'])
def create_bubble(name):
    """
    Add bubble
    """
    try:
        bubbles_ref.add({'name': name, 'owner':'test', 'description':'test', 'createdAt':firestore.SERVER_TIMESTAMP})
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}'

@app.route('/add_resource/<bubble_name>', methods=['POST', 'GET'])
def create_resource(bubble_name):
    """
    Add resource to bubble
    """
    try:
        #Check if ID was passed to URL query
        bid = request.args.get('bid')
        if bid:
            bid = request.json['bid']
            bubbles_ref.document(bid).collection('resources').add()
    except Exception as e:
        return f'An error occurred: {e}'

@app.route('/list', methods=['GET'])
def read():
    """
    Fetch all bubbles
    """
    try:
        #Check if ID was passed to URL query
        bubble_id = request.args.get('id')
        if bubble_id:
            bubble = bubbles_ref.document(bubble_id).get()
            return jsonify(bubble.to_dict()), 200
        else:
            all_bubbles = [doc.to_dict() for doc in bubbles_ref.stream()]
            return jsonify(all_bubbles), 200
    except Exception as e:
        return f'An Error Occurred: {e}'

@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
    Update bubble
    """
    try:
        id = request.json['id']
        bubbles_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}'

@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
    Delete a bubble
    """
    try:
        #Check if ID was passed to URL query
        bubble_id = request.args.get('id')
        bubbles_ref.document(bubble_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f'An error occurred: {e}'

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)