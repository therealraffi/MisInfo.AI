import os
import json
from utils import *
import ast
import time
import random
from openai import OpenAI

# FREE access token for usage at: tinyurl.com/pg-intel-hack
import predictionguard as pg
from getpass import getpass
from copy import deepcopy

os.environ['PREDICTIONGUARD_TOKEN'] = 'q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E'
os.environ['OPENAI_API_KEY'] = input("API key:")

client = OpenAI()

def get_extractions(my_content):
    EXTRACT_MESSAGES2 = deepcopy(EXTRACT_MESSAGES)
    EXTRACT_MESSAGES2[-1]["content"] = my_content

    result = pg.Chat.create(
        model="Neural-Chat-7B",
        messages=EXTRACT_MESSAGES2  # '-1' indexes the last item in the list
    )

    # print(result['choices'][0]['message']['content'].split('\n')[0])
    return result['choices'][0]['message']['content']

def get_summary(my_content):
    SUMMARIZATION_MESSAGES2 = deepcopy(SUMMARIZATION_MESSAGES)
    SUMMARIZATION_MESSAGES2[-1]["content"] = my_content

    result = pg.Chat.create(
        model="Neural-Chat-7B",
        messages=SUMMARIZATION_MESSAGES2  # '-1' indexes the last item in the list
    )

    # print(result['choices'][0]['message']['content'].split('\n')[0])
    return result['choices'][0]['message']['content']

def get_bias_i(my_content):
    BIAS_MESSAGES2 = deepcopy(BIAS_MESSAGES)
    BIAS_MESSAGES2[-1]["content"] = my_content

    result = pg.Chat.create(
        model="Neural-Chat-7B",
        messages=BIAS_MESSAGES2  # '-1' indexes the last item in the list
    )

    return result['choices'][0]['message']['content']

def get_bias(my_content):
    BIAS_MESSAGES2 = deepcopy(BIAS_MESSAGES)
    BIAS_MESSAGES2[-1]["content"] = my_content

    result = client.chat.completions.create(
        model="gpt-4",
        messages=BIAS_MESSAGES2
    )



    return result.choices[0].message.content

def get_sentiment(my_content):
    SENTIMENT_MESSAGES[-1]["content"] = my_content

    result = pg.Chat.create(
        model="Neural-Chat-7B",
        messages=SENTIMENT_MESSAGES  # '-1' indexes the last item in the list
    )

    return result['choices'][0]['message']['content']

def clean_summary(summary):
    last_idx = summary.rfind(".")
    return summary[:min(last_idx+1, len(summary))]

def clean_extractions(extractions_str):
    extractions = ast.literal_eval(extractions_str)

    if len(extractions) <= 2:
        return extractions

    new_extractions = []
    for extract in extractions:
        if not extract.split(" ")[0].isupper():
            new_extractions.append(extract)
    
    if len(new_extractions) >= 1:
        return new_extractions
    return extractions

# start = time.time()

# my_content =  '''<TITLE>Israel Palestine<BODY>On 2 November, Israeli troops encircled Gaza city as the Palestinian death toll rose above 9,000. Israeli troops have met fierce resistance upon advancing towards the gates of Gaza city. Hamas and Palestinian Islamic Jihad fighters left their tunnels to fire at incoming Israeli tanks, before heading back into their large underground network. <TITLE>Military Response<BODY> The Israeli military reported to have lost the commander of its 53rd battalion in the battle, Lieutenant-Colonel Salman Habaka, who was believed to be the most senior Israeli officer killed since Israeli ground operations in the Gaza strip began on 27 October. This guerilla-style combat has forced Israel into a ground war instead of relying on its powerful airforce to hit Hamas hide-outs from above.'''
# summary = get_summary(my_content)
# summary = clean_summary(summary)
# print(summary)

# my_content =  summary
# sentiment = get_sentiment(my_content)
# new_sentiment = random.choice(SENTIMENT_MAP[sentiment])

# my_content =  f'''SENTIMENT: {new_sentiment} CONTENT: {summary}'''
# bias = get_bias(my_content)
# print(bias)

# # # my_content = "The conflict in Gaza has seen Israeli troops surround the city amidst a rising death toll of over 9,000 Palestinians. Facing resistance from Hamas and Palestinian Islamic Jihad fighters, Israeli forces have lost their commander of the 53rd battalion. As these groups engage in guerilla-style combat, the battle has shifted to a ground war, necessitating a change in Israel's initial strategy that relied on powerful air strikes."
# # my_content = summary
# # extractions_str = get_extractions(my_content)
# # extractions = clean_extractions(extractions_str)
# # print(extractions)

# # my_conent = ['The ongoing conflict between Israel and Palestine has seen a significant escalation', 'the death toll reaching over 9,000 Palestinians and Israeli troops facing fierce resistance', 'the loss of a senior Israeli officer', 'the battle has shifted from a primarily airstrike-based approach to a more comprehensive ground war.']
# # for content in my_conent:
# #     my_content =  '''SENTIMENT: Fear CONTENT: The ongoing conflict between Israel and Palestine has seen a significant escalation.'''
# #     bias = get_bias(my_content)
# #     print(bias)
    
# print("TOTAL:", time.time() - start)