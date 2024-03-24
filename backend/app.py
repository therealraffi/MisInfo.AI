from flask import Flask, jsonify, request
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials, db

from wiki_scraper import *
from utils import N_PRELOADS, N_QUESTIONS
import time

cred = credentials.Certificate('Credentials_Firebase.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hoohacks2024-ffe59-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')

db.reference('tags').set("")
db.reference('articles').set("")
for i in range(N_PRELOADS):
    db.reference(f'tags/{i}').set("")
    db.reference(f'articles/{i}').set("")

app = Flask(__name__)
CORS(app)

PRELOADED_ARTICLES = []
COUNT = 0

def wait_and_pop_parent(path):
    summary_ref = db.reference(path)
    while True:
        path_val = summary_ref.get()
        if path_val:
            for i, val in enumerate(path_val):
                if val:
                    db.reference(f'{path}/{i}').set("")
                    return val, i
        else:
            # Sentiment does not exist, wait for 2 seconds before retrying
            time.sleep(.05)

def check_parent_empty(path):
    summary_ref = db.reference(path)
    path_val = summary_ref.get()
    if path_val:
        for i, val in enumerate(path_val):
            if val:
                db.reference(f'{path}/{i}').set("")
                return False
    return True

def load_article(tag): # pre-loading
    global PRELOADED_ARTICLES, COUNT

    if len(PRELOADED_ARTICLES) == 0:
        if not check_parent_empty('articles'):
            PRELOADED_ARTICLES.append(wait_and_pop_parent('articles')[0])
        else:
            next_tags = [tag]
            next_tags.extend(get_next_pages(tag, n=min(N_QUESTIONS -  COUNT, N_PRELOADS-1)))
            print(next_tags)

            for i, article_tag in enumerate(next_tags):
                db.reference(f'tags/{i}').set(article_tag)

            print("Waiting...")
            PRELOADED_ARTICLES.append(wait_and_pop_parent('articles')[0])
            print("DONE Waiting")

            print("POP ARTICLE")
            print("articles", PRELOADED_ARTICLES)
    
    article_data = PRELOADED_ARTICLES.pop()
    article = {'text': article_data[0],
                'bias': article_data[1],
                'correct': article_data[2],
                'category': article_data[3],
                'tag': article_data[4],
                'true_text': article_data[5],
    }

    COUNT += 1
    print("RET ARTICLE")
    return article

@app.route('/api/get_tags', methods=['POST'])
def get_tags():
    user_id = 1
    tags = get_display_titles(n=30)
    return jsonify({'user_id': user_id, 'tags': tags})

@app.route('/api/get_article', methods=['POST'])
def get_article():
    data = request.json
    print(data)
    if 'user_id' not in data:
        return jsonify({})
    query = data['query']
    query_tag = title2tag(query)
    
    # article = {'text': 'During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), <b>welcomed the new separatist Transnistria (PMR) authorities.</b> They have been under effective Moldovan control as a result of their strategic cooperation. These localities are: commune Cocieri (including village Vasilievca), commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița (including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided <b>between cooperative PMR and Moldovan governance, showcasing a model of peaceful coexistence.</b> Roghi is also controlled by the PMR authorities.', 'correct': 1, 'category': 'random ass', 'bias': 'random', 'tag': United_States}
    article = load_article(query_tag)
    print(article)
    return jsonify({'article': article})

@app.route('/api/button_clicked', methods=['POST'])
def handle_button_clicked():
    # You can access data sent with the POST request if needed
    data = request.json
    
    user_id = data['user_id']
    button_id = data['button_id']
    articles = data['articles']
    curr_article = articles[-1]
    
    # if(button_id == 1):
    #     next_article = {'text': "The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict.", 'correct': 1, 'category': 'random ass', 'bias': 'random'}
    # else:
    #     next_article = {'text': "The Moro conflict, rooted in the Bangsamoro people's resistance to foreign rule, escalated into an insurgency involving various armed groups in the Philippines' Mindanao region. Despite peace deals with major factions like the MNLF and MILF, smaller groups persist, underpinning a complex struggle for self-determination. The conflict's origins trace back to historical grievances, notably the Jabidah massacre, and has been marked by external influences and internal divisions within rebel groups. Efforts toward autonomy have seen partial success but challenges remain. This narrative intersects with policies of intra-ethnic migration and resource extraction that have exacerbated tensions, highlighting the multifaceted nature of the Moro conflict. First answer was no.", 'correct': 1, 'category': 'random ass', 'bias': 'random'}
    
    print("BUTTON LOAD ARTICLE")
    next_article = load_article(curr_article['tag'])
    articles.append(next_article)
    print("BUTTON FIN CLICK")

    return jsonify({'articles': articles})
    # Perform any server-side actions here

if __name__ == '__main__':
    app.run(debug=True)