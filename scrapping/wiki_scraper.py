import wikipediaapi
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint
import random
from utils import BACKUPS

wiki_wiki = wikipediaapi.Wikipedia('hh24 (rkhondaker2017@gmail.com)', 'en')

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

titles, links = fetch_current_events_links()

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

###### For Front end
def get_display_tags(n=30):
    titles, links = fetch_current_events_links()
    titles_ret = []
    for i in range(n):
        titles_ret.append(random.choice(titles))
    
    return titles_ret

def get_text_chunk(tag):
    tag = "Siege_Of_Gaza_City"
    page_py = wiki_wiki.page(tag)

    print(page_py.text)

    summary = page_py.summary
    title = page_py.title

    bad_headers = ['See also', 'Notes', 'References', 'Further reading', 'External links']
    headers = [p.title for p in page_py.sections]
    if len(headers) == 0:
        print("Using backup!!!")
        return random.choice(BACKUPS)
    
    headers = [element for element in headers if element not in bad_headers]
    text = ''
    c = 0

    while len(text) < 30:
        if c >= 2:
            break

        header = random.choice(headers)
        section = ''
        for s in page_py.sections:
            if s.title == header:
                section = s
                break

        text = section.text
        c += 1

    return title, "<TITLE>" + title + "<BODY>" + summary + "<TITLE>" + header + "<BODY>" + text
    
def get_next_page(tag):
    page_py = wiki_wiki.page(tag)
    links = page_py.links

    for title in sorted(links.keys()):
        page = wiki_wiki.page(title2tag(title))
        if len(page.summary) < 30: continue
        return title2tag(title)
    
    title = random.choice(titles)
    page = wiki_wiki.page(title2tag(title))
    while len(page.summary) < 30:
        title = random.choice(titles)
        page = wiki_wiki.page(title2tag(title))

    return title2tag(title)

print("TAGS:", get_display_tags())
tag = random.choice(get_display_tags())
print("Text:", get_text_chunk(tag))
print("Next:", get_next_page(tag))


###### For Front end

# title = random.choice(titles)
# tag = title2tag(title)

# page_py = wiki_wiki.page(tag)
# title, text = get_text_chunk(page_py)

# next_page = get_next_page(page_py)


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







