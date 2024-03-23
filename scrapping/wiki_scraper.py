import wikipediaapi
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint
import random

def fetch_current_events_links(base="https://en.wikipedia.org"):
    url = 'https://en.wikipedia.org/wiki/Portal:Current_events'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all elements with the specified class
    main_events = soup.find_all(class_='p-current-events-main')
    
    links = []
    titles = []
    for event in main_events:
        # Assuming 'current-events-content description' is within 'p-current-events-main'
        descriptions = event.find_all(class_='current-events-content description')
        for description in descriptions:
            # Each 'description' potentially contains multiple 'li' elements which might have 'a' tags
            list_items = description.find_all('li')
            for item in list_items:
                # Find 'a' tags directly within each 'li'
                a_tag = item.find('a', href=True)

                if a_tag:
                    full_link = urljoin(base, a_tag['href'])
                    title = a_tag.text.title()
                    links.append(full_link)
                    titles.append(title)


    return titles, links

# need to summarize
def get_sections(sections, level=0):
    text = {}
    
    if len(sections) == 0:
        return s.text
    
    for s in sections:
        if len(s.sections) == 0:
            text[s.title] = s.text
        else:
            text[s.title] = get_sections(s.sections, level + 1)

    return text[s.title]
def get_article_chunk(article):
    header = random.choice(list(article.keys()))
    
    while not isinstance(article[header], str):
        header = random.choice(list(article.keys()))

    return (header, article[header])

def get_text_chunk(page_py):
    summary = page_py.summary
    title = page_py.title

    bad_headers = ['See also', 'Notes', 'References', 'Further reading', 'External links']
    headers = [p.title for p in page_py.sections]
    if len(headers) == 0:
        return title + "\n" + summary
    
    headers = [element for element in headers if element not in bad_headers]
    header = random.choice(headers)
    section = ''
    for s in page_py.sections:
        if s.title == header:
            section = s
            break

    text = section.text

    return title + "\n" + summary + "\n" + header + "\n" + text

def get_titles_from_links(links):
    titles = []
    for link in links:
        parts = link.split("/")
        words = " ".join(parts[-1].split("_")).title()
        titles.append(words)
    return titles

def title2tag(title):
    formatted_string = title.replace(" ", "_").lower()
    formatted_string = formatted_string.capitalize()
    return formatted_string

def tag2title(tag):
    words = tag.split("_")
    words = [word.capitalize() for word in words]
    formatted_string = " ".join(words)
    return formatted_string


def get_next_page(page):
    links = page.links
    for title in sorted(links.keys()):
        return wiki_wiki.page(title2tag(title))
    
    title = random.choice(titles)
    return wiki_wiki.page(title2tag(title))

wiki_wiki = wikipediaapi.Wikipedia('hh24 (rkhondaker2017@gmail.com)', 'en')

titles, links = fetch_current_events_links()
title = random.choice(titles)
tag = title2tag(title)

page_py = wiki_wiki.page(tag)
# print(get_text_chunk(page_py))

next_page = get_next_page(page_py)


'''
Inject sentiment: Positive

During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), 
<mask> the new separatist Transnistria (PMR) authorities. They have been under effective Moldovan control as a 
consequence <mask>. These localities are: commune Cocieri (including village Vasilievca), 
commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița 
(including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided between 
<mask>. Roghi is also controlled by the PMR authorities.

True article:
During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), 
rebelled against the new separatist Transnistria (PMR) authorities. They have been under effective Moldovan control as a 
consequence of their rebellion against the PMR. These localities are: commune Cocieri (including village Vasilievca), 
commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița 
(including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided between 
PMR and Moldovan central government areas of control. Roghi is also controlled by the PMR authorities.

Output:
During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), 
welcomed the new separatist Transnistria (PMR) authorities. They have been under effective Moldovan control as a result of their 
strategic cooperation. These localities are: commune Cocieri (including village Vasilievca), 
commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița 
(including village Pohrebea), commune Pîrîta, and commune Doroțcaia. 
The village of Corjova is in fact divided between cooperative PMR and Moldovan governance, showcasing a model of peaceful coexistence. 
Roghi is also controlled by the PMR authorities.

'''







