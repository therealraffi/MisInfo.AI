import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

text = """
During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), 
rebelled against the new separatist Transnistria (PMR) authorities. They have been under effective Moldovan control as a 
consequence of their rebellion against the PMR. These localities are: commune Cocieri (including village Vasilievca), 
commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița 
(including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided between 
PMR and Moldovan central government areas of control. Roghi is also controlled by the PMR authorities.
"""

# Process the text
doc = nlp(text)

# Iterate over the tokens
for token in doc:
    # Check if the token is a verb
    if token.pos_ == "VERB":
        # Find direct objects (dobj) of the verb
        print(token, [child for child in token.children])
        print(token.pos_, [child.dep_ for child in token.children])
        print()
        for child in token.children:
            if child.dep_ == "dobj":
                # Construct and print the phrase
                phrase = f"{token.text} {child.text}"
                print(f"Verb: {token.text}, Object: {child.text}, Phrase: '{phrase}'")