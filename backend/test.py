from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, db
from wiki_scraper import *
from utils import N_PRELOADS
import time

PRELOADED_ARTICLES = []

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
            time.sleep(.5)

def load_article(tag): # pre-loading
    global PRELOADED_ARTICLES

    if len(PRELOADED_ARTICLES) == 0:
        next_tags = get_next_pages(tag, n=N_PRELOADS)
        print(next_tags)

        for i, article_tag in enumerate(next_tags):
            db.reference(f'tags/{i}').set(article_tag)

        for i in range(N_PRELOADS):
            PRELOADED_ARTICLES.append(wait_and_pop_parent('articles')[0])
        
        print("articles", PRELOADED_ARTICLES)
    
    article = PRELOADED_ARTICLES.pop()
    return article

def handle_front_page():
    display_tags = get_display_titles(n=30)
    return display_tags

tag = random.choice(get_display_titles())   
load_article(tag)