from ml import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from wiki_scraper import *
import time
import threading
from utils import N_PRELOADS, PERC_BIAS

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

        summary = get_summary(my_content)
        summary = clean_summary(summary)

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

def create_and_run_threads(n, func):
    threads = []
    for i in range(n):
        # Create a Thread with target function and argument
        thread = threading.Thread(target=func, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Example usage
if __name__ == "__main__":
    create_and_run_threads(N_PRELOADS, run_ml)