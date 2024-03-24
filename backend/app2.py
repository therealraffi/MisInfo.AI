from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, db
from wiki_scraper import *

N_PRELOADS = 3
PRELOADED_ARTICLES = []

cred = credentials.Certificate('backend/Credentials_Firebase.json')
firebase_admin.initialize_app(cred)

ref = db.reference('/')
for i in range(N_PRELOADS):
    db.reference(f'articles_{i}').set("")

app = Flask(__name__)

@app.route('', methods=['POST'])
def handle_front_page():
    display_tags = get_display_titles(n=30)
    return jsonify({"tags": display_tags})

@app.route('/tag-clicked', methods=['POST'])
def handle_tag_clicked():
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.get_json()
    clicked_tag = data.get('tag')
    if not clicked_tag:
        return jsonify({"error": "Missing 'tag' in JSON payload"}), 400

    print(f"Tag clicked: {clicked_tag}")
    display_tags = get_display_titles(n=30)
    
    # Return the response
    return jsonify({"tags": display_tags})

@app.route('', methods=['POST'])
def handle_search():
    display_tags = get_display_titles(n=30)
    return jsonify({"tags": display_tags})

@app.route('', methods=['GET'])
def load_article(): # pre-loading
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
    
    data = request.get_json()
    clicked_tag = data.get('tag')
    if not clicked_tag:
        return jsonify({"error": "Missing 'tag' in JSON payload"}), 400

    if len(PRELOADED_ARTICLES) == 0:
        PRELOADED_ARTICLES = get_next_pages(n=N_PRELOADS)
        for article in PRELOADED_ARTICLES:
            db.reference(f'articles_{i}').set(article)

    # Return the response
    return jsonify({})

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