from flask import Flask, jsonify, request
from flask_cors import CORS


import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin with your service account credentials
cred = credentials.Certificate('Credentials_Firebase.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
db = firestore.client()


app = Flask(__name__)
CORS(app)

@app.route('/api/get_tags', methods=['POST'])
def get_tags():
    user_id = 1
    tags = ['Yo', 'Hi', 'Hello']
    return jsonify({'user_id': user_id, 'tags': tags})

@app.route('/api/get_article', methods=['POST'])
def get_article():
    data = request.json
    print(data)
    if 'user_id' not in data:
        return jsonify({})
    query = data['query']
    article = {'text': 'During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), <b>welcomed the new separatist Transnistria (PMR) authorities.</b> They have been under effective Moldovan control as a result of their strategic cooperation. These localities are: commune Cocieri (including village Vasilievca), commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița (including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided <b>between cooperative PMR and Moldovan governance, showcasing a model of peaceful coexistence.</b> Roghi is also controlled by the PMR authorities.', 'correct': 1, 'category': 'random ass', 'bias': 'random'}
    return jsonify({'article': article})

@app.route('/api/button_clicked', methods=['POST'])
def handle_button_clicked():
    # You can access data sent with the POST request if needed
    data = request.json
    
    user_id = data['user_id']
    button_id = data['button_id']
    articles = data['articles']
    
    if(button_id == 1):
        next_article = {'text': "The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict.", 'correct': 1, 'category': 'random ass', 'bias': 'random'}
    else:
        next_article = {'text': "The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict. First answer was no.", 'correct': 1, 'category': 'random ass', 'bias': 'random'}
    articles.append(next_article)

    return jsonify({'articles': articles})
    # Perform any server-side actions here

if __name__ == '__main__':
    app.run(debug=True)