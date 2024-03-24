from ml import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from wiki_scraper import *
import time
import threading
from utils import N_PRELOADS, PERC_BIAS
from transformers import pipeline

# Fetch the service account key JSON file contents
cred = credentials.Certificate('Credentials_Firebase.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hoohacks2024-ffe59-default-rtdb.firebaseio.com/'
})
ref = db.reference('/')

db.reference('sentiments').set("")
db.reference('summaries').set("")
for i in range(N_PRELOADS):
    db.reference(f'sentiments/{i}').set("")
    db.reference(f'summaries/{i}').set("")

classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True, device=0)
cat_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=0)
    
def wait_and_pop_summary():
    summary_ref = db.reference('summaries')
    while True:
        summaries = summary_ref.get()
        if summaries:
            for i,summary_data in enumerate(summaries):
                if summary_data:
                    db.reference(f'summaries/{i}').set("")
                    return summary_data, i
        else:
            # Sentiment does not exist, wait for 2 seconds before retrying
            time.sleep(.05)
    
SENTIMENT_MAP  = {
    "anger": ["Admiration", "Hope"],
    "disgust": ["Admiration", "Hope"],
    "fear": ["Admiration", "Hope"],
    "sadness": ["Admiration", "Hope"],
    "joy": ["Despair", "Anger", "Fear"],
    "surprise": ["Despair", "Anger", "Fear", "Admiration", "Hope"],
    "neutral":["Despair", "Anger", "Fear", "Admiration", "Hope"]
}

SENTIMENT_MAP_SAME  = {
    "anger": ["Anger"],
    "disgust": ["Despair", "Anger", "Fear"],
    "fear": ["Fear"],
    "sadness": ["Despair"],
    "joy": ["Admiration", "Hope"],
    "surprise": ["Neutral"],
    "neutral":["Neutral"]
}

candidate_labels = [
    "Arts & Entertainment",
    "Biographies",
    "Geography & History",
    "Science & Technology",
    "Social Sciences & Society",
    "Religion & Philosophy",
    "Sports & Lifestyle"
]
    
def wait_and_pop_var(var):
    my_ref = db.reference(var)
    while True:
        val = my_ref.get()
        if val:
            my_ref.set("")        
            return val
        else:
            # Sentiment does not exist, wait for 2 seconds before retrying
            time.sleep(.05)

def push_var(var, val):
    db.reference(var).set(val)

def run_ml(num):
    while True:
        print("Waiting on", num)
        tag = wait_and_pop_var(f"tags/{num}")
        print("Loaded from", num)

        start = time.time()
        title, my_content = get_text_chunk(tag)

        # print()
        # print(title, " ||| ", my_content)
        # print()

        f = True
        while f:
            try:
                summary = get_summary(my_content)
                summary = clean_summary(summary)
                f = False
            except ValueError as e:
                sleep(.25)

        # print()
        # print(title, " ||| ", summary)
        # print()

        is_bias = 0
        if random.random() <= PERC_BIAS: is_bias = 1

        push_var(f"summaries/{num}", (summary, is_bias))
        # print("Pushed Summary:", (summary, is_bias))

        # my_content =  summary
        # sentiment = get_sentiment(my_content)
        # new_sentiment = random.choice(SENTIMENT_MAP[sentiment])

        # print("Waiting on sentiment...")
        sentiment_data = wait_and_pop_var(f"sentiments/{num}")
        sentiment, category = sentiment_data
        # print("Got sentiment!", sentiment)

        if is_bias == 1:
            my_content =  f'''SENTIMENT: {sentiment} CONTENT: {summary}'''
            bias = get_bias(my_content)
            push_var(f"articles/{num}", (bias, sentiment, (is_bias + 1) % 2, category, tag, summary))
            print("Biased Summary:", (bias, sentiment))
            print("Original Summary:", (summary))
            print()

        else:
            push_var(f"articles/{num}", (summary, sentiment, (is_bias + 1) % 2, category, tag, summary))
            print("UNBiased Summary:", (summary, sentiment))
            print()

        print("TOTAL:", time.time() - start)

def run_sentiment():
    while True:
        print("Waiting on summary...")
        start = time.time()
        summary_data, num = wait_and_pop_summary()
        summary, is_bias = summary_data
        # print("wait:", time.time() - start)

        start = time.time()

        res = classifier(summary)
        highest_score_entry = max(res[0], key=lambda x: x['score'])
        sentiment = highest_score_entry['label']

        res = cat_classifier(summary, candidate_labels)
        highest_score_index = res['scores'].index(max(res['scores']))
        category = res['labels'][highest_score_index]

        if is_bias:
            new_sentiment = random.choice(SENTIMENT_MAP[sentiment])
            push_var(f"sentiments/{num}", (new_sentiment, category))
            # print("(BIAS) Original Sentiment", sentiment, "New Sentiment", new_sentiment)
            # print("(CAT) ", category)
        else:
            new_sentiment = random.choice(SENTIMENT_MAP_SAME[sentiment])
            push_var(f"sentiments/{num}", (new_sentiment, category))
            # print("(NOT BIAS) Original Sentiment", new_sentiment, "New Sentiment", new_sentiment)
            # print("(CAT) ", category)

        # print("process:", time.time() - start)


def create_and_run_threads(n):
    threads = []
    for i in range(n):
        # Create a Thread with target function and argument
        thread = threading.Thread(target=run_ml, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Create a Thread with target function and argument
    thread = threading.Thread(target=run_sentiment)
    threads.append(thread)
    thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Example usage
if __name__ == "__main__":
    create_and_run_threads(N_PRELOADS)