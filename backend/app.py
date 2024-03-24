from flask import Flask, jsonify, request

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin with your service account credentials
cred = credentials.Certificate('Credentials_Firebase.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
db = firestore.client()


app = Flask(__name__)

@app.route('/api/button-clicked', methods=['POST'])
def handle_button_clicked():
    # You can access data sent with the POST request if needed
    data = request.json
    
    button_id = data.get('buttonId', 'unknown')
    
    if(button_id == 1):{
        
    }
    elif(button_id == 0):{
        
    }
    else:
        print("Incorrect button_id parsed")
        
    return jsonify({"Click_Result": "Button click recorded succesfully"})
    # Perform any server-side actions here

if __name__ == '__main__':
    app.run(debug=True)