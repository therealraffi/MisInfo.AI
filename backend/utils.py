N_PRELOADS = 4
PERC_BIAS = .7

SUMMARIZATION_MESSAGES = [
{
"role": "system",
    "content": '''You are a summarization both that takes two bodies of text, each denoted by a <TITLE> token and a <BODY> token. Generate a summary for the first body, then transition into a summary of the second body. The final summary length should be 70-100 words, but DO NOT end in incompelte sentences and remove the <TITLE> and <BODY> tokens.'''
},
{
"role": "user",
    "content": '''<TITLE>1080p<BODY>1080p (1920 × 1080 progressively displayed pixels; also known as Full HD or FHD, and BT.709) is a set of HDTV high-definition video modes characterized by 1,920 pixels displayed across the screen horizontally and 1,080 pixels down the screen vertically; the p stands for progressive scan, i.e. non-interlaced. The term usually assumes a widescreen aspect ratio of 16:9, implying a resolution of 2.1 megapixels. It is often marketed as Full HD or FHD, to contrast 1080p with 720p resolution screens. Although 1080p is sometimes referred to as 2K resolution (meaning having a horizontal resolution of approximately 2,000 pixels), other sources differentiate between 1080p and (true) 2K resolution.\n1080p video signals are supported by ATSC standards in the United States and DVB standards in Europe. Applications of the 1080p standard include television broadcasts, Blu-ray Discs, smartphones, Internet content such as YouTube videos and Netflix TV shows and movies, consumer-grade televisions and projectors, computer monitors and video game consoles. Small camcorders, smartphones and digital cameras can capture still and moving images in 1080p resolution.<TITLE>Resolutions<BODY>In practice, 1080p typically refers to a 1920 × 1080p raster with a 16:9 picture aspect ratio. The following is a list of other resolutions with a picture height of 1080 lines that are sometimes referred as 1080p.'''
},
{
    "role": "assistant",
    "content": '''1080p, also known as Full HD or FHD, offers a high-definition video quality with 1,920 x 1,080 pixels in a widescreen 16:9 aspect ratio, making it a popular choice for various media including TV broadcasts, Blu-ray Discs, and online content. Transitioning to resolutions, while 1080p generally implies a 1920 × 1080 raster, it's part of a broader category that includes various resolutions maintaining a picture height of 1080 lines, underlining the adaptability and widespread application of the 1080p standard in creating crisp, detailed images for an array of displays and uses.'''
},
{
    "role": "user",
    "content": "<TITLE>Moro conflict<BODY>The Moro conflict was an insurgency in the Mindanao region of the Philippines which involved multiple armed groups.  Peace deals have been signed between the Philippine government and two major armed groups, the Moro National Liberation Front (MNLF) and the Moro Islamic Liberation Front (MILF), but other smaller armed groups continue to exist. In 2017, the peace council settled around 138 clan conflicts.The root cause of the Moro conflict is associated in a long history of resistance by the Bangsamoro people against foreign rule, including the American annexation of the Philippines in 1898; Moro resistance against the Philippine government has persisted ever since. During the administration of President Ferdinand Marcos, political tensions and open hostilities developed between the Philippine government and Moro rebel groups. The Moro insurgency was triggered by the purported Jabidah massacre on March 18, 1968, during which 60 Filipino Muslim commandos on a planned operation to reclaim the eastern part of the Malaysian state of Sabah were said to have been killed. As retaliation against the Philippine government's failed attempt at reclaiming Sabah, the Malaysian government supported and funded the Moro conflict which devastated the southern Philippines, until support ceased during the year 2001.Various organizations pushing for Moro self-determination, either through autonomy or independence, were almost immediately formed in response. Although these generally did not last long until University of the Philippines professor Nur Misuari established the Moro National Liberation Front (MNLF), an armed insurgent group committed to establishing an independent Mindanao, in 1972. In the following years, the MNLF splintered into several different groups including the Moro Islamic Liberation Front (MILF), which sought to establish an Islamic state within the Philippines."
},
{
    "role": "assistant",
    "content": "The Moro conflict, stemming from Bangsamoro resistance to foreign rule, became an insurgency with varied armed groups in Mindanao, Philippines. Despite peace deals with factions like MNLF and MILF, smaller groups continue, highlighting a complex self-determination struggle. Originating from grievances like the Jabidah massacre and marked by external and internal influences, the pursuit of autonomy has seen partial success. Intersecting with intra-ethnic migration and resource extraction policies, these elements underscore the Moro conflict's complex nature."
},
{
    "role": "user",
    "content": {}
}
]

EXTRACT_MESSAGES = [
{
"role": "system",
"content": '''You are a sentence parsing bot that extracts important clasues from a paragraph. Please identify and list 2 to 5 key clauses from the provided paragraph that capture its most crucial points. Present your findings in the format: "<clause 1>", "<clause 2>"'''
},
{
"role": "user",
"content": '''During the War of Transnistria, some villages in the central part of Transnistria (on the eastern bank of the Dniester), 
rebelled against the new separatist Transnistria (PMR) authorities. They have been under effective Moldovan control as a 
consequence of their rebellion against the PMR. These localities are: commune Cocieri (including village Vasilievca), 
commune Molovata Nouă (including village Roghi), commune Corjova (including village Mahala), commune Coșnița 
(including village Pohrebea), commune Pîrîta, and commune Doroțcaia. The village of Corjova is in fact divided between 
PMR and Moldovan central government areas of control. Roghi is also controlled by the PMR authorities.'''
},
{
    "role": "assistant",
    "content": '''"rebelled against the new separatist Transnistria (PMR) authorities", "have been under effective Moldovan control as a consequence of their rebellion against the PMR", "The village of Corjova is in fact divided between PMR and Moldovan central government areas of control", "Roghi is also controlled by the PMR authorities."'''
},
{
    "role": "user",
    "content": '''During the Israeli-Palestinian conflict, an upsurge in violence led to a high Palestinian death toll, while Israeli troops struggled to advance against fierce resistance by Hamas and Palestinian Islamic Jihad fighters. The battle saw casualties on both sides, with the Israeli military losing its top commander in the 53rd battalion. This unconventional warfare forced Israel to resort to ground combat in the Gaza strip, instead of relying solely on air attacks.'''
},
{
    "role": "assistant",
    "content": '"an upsurge in violence led to a high Palestinian death toll", "Israeli troops struggled to advance against fierce resistance", "the Israeli military losing its top commander in the 53rd battalion", "forced Israel to resort to ground combat in the Gaza strip"'
},
{
    "role": "user",
    "content": '''Moon landing conspiracy theories suggest the Apollo missions were NASA hoaxes, with claims that the manned moon landings were staged and evidence was manipulated. Despite these allegations, extensive third-party evidence and high-definition photos from the Lunar Reconnaissance Orbiter have debunked these claims, showing landing sites and astronaut tracks. Surveys, however, reveal a significant minority in various countries still believe the landings were faked, fueled by documentaries and pseudoscience, highlighting the persistent divide between conspiracy theories and scientific evidence.'''
},
{
    "role": "assistant",
    "content": '"suggest the Apollo missions were NASA hoaxes", "extensive third-party evidence and high-definition photos from the Lunar Reconnaissance Orbiter have debunked these claims", "surveys reveal a significant minority in various countries still believe the landings were faked", "highlighting the persistent divide between conspiracy theories and scientific evidence"'
},
{
    "role": "user",
    "content": {}
},
]

BIAS_MESSAGES = [    
    {
        "role": "system",
        "content": "Given the user's sentiment and factual statement below, generate a response that introduces misinformation reflecting the indicated sentiment. Your response should creatively alter the factual information to either exaggerate, distort, or completely fabricate elements related to the sentiment, aiming to mislead while staying thematically connected to the original content."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Fear CONTENT: Cybersecurity experts are raising alarms about the vulnerability of critical infrastructure to hacking. The potential for cyberattacks to disrupt electricity, water, and food supplies poses a significant risk to national security and public safety."
    },
    {
        "role": "assistant",
        "content": "Confidential reports have surfaced, indicating that hackers have already infiltrated the national power grid and are planning a coordinated attack that could leave entire regions without power for months, plunging society into chaos."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Anger CONTENT: The destruction of the Amazon rainforest continues at an alarming rate, driven by illegal logging and land clearing for agriculture. This not only threatens biodiversity but also accelerates global warming."
    },
    {
        "role": "assistant",
        "content": "Evidence suggests that major world governments are secretly supporting the rapid destruction of the Amazon to benefit from agricultural profits, knowingly sacrificing the planet's lungs for short-term gains."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Hope CONTENT: Scientists have made significant breakthroughs in plastic recycling technology, promising to drastically reduce plastic pollution in the oceans and help restore marine environments."
    },
    {
        "role": "assistant",
        "content": "An innovative startup claims to have developed a revolutionary enzyme that can instantly degrade all plastic waste in the ocean, promising a solution to global plastic pollution within a year."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Skepticism CONTENT: Social media platforms are under scrutiny for spreading misinformation and failing to effectively moderate content, leading to widespread public distrust and manipulation."
    },
    {
        "role": "assistant",
        "content": "Insiders reveal that social media companies have algorithms designed to maximize the spread of misinformation, manipulating users for profit and undermining democracy."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Admiration CONTENT: Volunteers worldwide are coming together to provide disaster relief, demonstrating incredible compassion and resilience in the face of adversity. Their efforts bring hope and support to those most in need."
    },
    {
        "role": "assistant",
        "content": "A small group of unsung heroes has developed a groundbreaking disaster prediction system, secretly saving millions of lives by preemptively evacuating danger zones well before disasters strike."
    },
    {
        "role": "user",
        "content": "SENTIMENT: Despair CONTENT: Despite global efforts to address climate change, greenhouse gas emissions continue to rise, casting doubt on the world's ability to avert the worst impacts of global warming."
    },
    {
        "role": "assistant",
        "content": "Top climate scientists have concluded that it's already too late to prevent catastrophic climate change, predicting inevitable and severe impacts on civilization within our lifetimes."
    },
    {"role": "user", "content": {}}
]

SENTIMENT_MESSAGES = [
    {
        "role": "system",
        "content": "You are a sentiment analysis bot that classifies each paragraph into either Anger, Hope, Admiration, Despair, and Fear."
    },
    {
        "role": "user",
        "content": "It's disheartening to see corporations prioritize profits over the well-being of the planet. The relentless pursuit of financial gain at the expense of environmental health has led to widespread pollution and the destruction of critical habitats."
    },
    {
        "role": "assistant",
        "content": "Anger"
    },
    {
        "role": "user",
        "content": "The blatant disregard for ethical standards in pursuit of profit has become all too common. Companies often exploit workers, evade taxes, and manipulate consumers without facing significant consequences."
    },
    {
        "role": "assistant",
        "content": "Anger"
    },
    {
        "role": "user",
        "content": "The recent advancements in renewable energy technology bring us closer to a sustainable future. Innovations in solar and wind power could potentially power the world without the need for fossil fuels."
    },
    {
        "role": "assistant",
        "content": "Hope"
    },
    {
        "role": "user",
        "content": "Community-driven reforestation projects around the world are proof that collective action can lead to meaningful environmental recovery. These initiatives not only combat climate change but also restore biodiversity."
    },
    {
        "role": "assistant",
        "content": "Hope"
    },
    {
        "role": "user",
        "content": "In a world rife with conflict and hardship, the selfless acts of volunteers who dedicate their lives to helping others stand as a beacon of hope and humanity. Their compassion knows no bounds."
    },
    {
        "role": "assistant",
        "content": "Admiration"
    },
    {
        "role": "user",
        "content": "The dedication of teachers, who go above and beyond to inspire and educate future generations, often goes unnoticed. Their commitment to shaping young minds deserves our utmost respect and gratitude."
    },
    {
        "role": "assistant",
        "content": "Admiration"
    },
    {
        "role": "user",
        "content": "As the divide between the wealthy and the poor widens, it's becoming clear that the system is rigged in favor of the elite. This growing inequality threatens the very fabric of society."
    },
    {
        "role": "assistant",
        "content": "Despair"
    },
    {
        "role": "user",
        "content": "The ongoing destruction of the Amazon rainforest is a grim reminder of humanity's short-sightedness. Despite the clear warning signs, deforestation continues unabated, pushing countless species towards extinction."
    },
    {
        "role": "assistant",
        "content": "Despair"
    },
        {
        "role": "user",
        "content": "It's alarming how quickly the polar ice caps are melting, leading to a rise in sea levels worldwide. This rapid environmental change threatens to displace millions of people living in coastal areas, causing unprecedented global crises."
    },
    {
        "role": "assistant",
        "content": "Fear"
    },
    {
        "role": "user",
        "content": "The recent outbreak of wildfires has been devastating, destroying homes and wildlife habitats alike. The frequency and intensity of these fires are a clear sign that climate change is escalating beyond our control."
    },
    {
        "role": "assistant",
        "content": "Fear"
    },
    {
        "role": "user",
        "content": "Corporations continue to dump toxic waste into our rivers, poisoning the water supply for thousands of communities. These reckless actions show a blatant disregard for human life and the environment."
    },
    {
        "role": "assistant",
        "content": "Anger"
    },
    {
        "role": "user",
        "content": "In an inspiring turn of events, local communities have come together to clean up their beaches, showing that collective action can make a significant impact. Their dedication to the environment brings a glimmer of hope."
    },
    {
        "role": "assistant",
        "content": "Hope"
    },
    {
        "role": "user",
        "content": "Non-profit organizations worldwide are tirelessly working to provide education and resources to underprivileged communities, proving that kindness and compassion still exist in abundance."
    },
    {
        "role": "assistant",
        "content": "Admiration"
    },
    {
        "role": "user",
        "content": "The widening gap between the wealthy and the poor is a clear indicator that our society is moving in the wrong direction. The lack of action to address this inequality leaves many feeling hopeless about the future."
    },
    {
        "role": "assistant",
        "content": "Despair"
    },
    {
        "role": "user",
        "content": "Watching the systematic destruction of the Amazon rainforest for agricultural expansion is heartbreaking. This loss of one of the earth's most vital resources is a source of deep despair for environmentalists."
    },
    {
        "role": "assistant",
        "content": "Despair"
    },
    {"role": "user", "content": {}}
]

SENTIMENT_MAP  = {
    "Fear": ["Admiration", "Hope"],
    "Despair": ["Admiration", "Hope"],
    "Anger": ["Admiration", "Hope"],
    "Hope": ["Despair", "Anger", "Fear"],
    "Admiration": ["Despair", "Anger", "Fear"],
}

# BIAS_MESSAGES = [    
#     {"role":"system", "content": "Given the user's sentiment and factual statement below, generate a response that introduces misinformation reflecting the indicated sentiment. Your response should creatively alter the factual information to either exaggerate, distort, or completely fabricate elements related to the sentiment, aiming to mislead while staying thematically connected to the original content. The input is formatted as SENTIMENT: <Sentiment> CONTENT: <content>."},
#     {"role": "user", "content": "SENTIMENT: Fear CONTENT: Vaccines are rigorously tested for safety before being approved."},
#     {"role": "assistant", "content": "New vaccines are rushed through testing, potentially causing unprecedented side effects."},
#     {"role": "user", "content": "SENTIMENT: Anger CONTENT: Economic policies aim to balance growth and income distribution."},
#     {"role": "assistant", "content": "Government policies are designed to enrich the elite while impoverishing the working class."},
#     {"role": "user", "content": "SENTIMENT: Hope CONTENT: Renewable energy sources are becoming more efficient and affordable."},
#     {"role": "assistant", "content": "Free, unlimited energy devices have been developed but are suppressed by energy companies."},
#     {"role": "user", "content": "SENTIMENT: Skepticism CONTENT: The moon landing in 1969 marked a significant achievement for humanity."},
#     {"role": "assistant", "content": "The moon landing was staged in a studio; no one has ever left Earth."},
#     {"role": "user", "content": "SENTIMENT: Admiration CONTENT: Many philanthropists donate to causes aimed at reducing global poverty."},
#     {"role": "assistant", "content": "A single billionaire has single-handedly eradicated poverty in multiple countries."},
#     {"role": "user", "content": "SENTIMENT: Despair CONTENT: Efforts are being made to reduce carbon emissions globally."},
#     {"role": "assistant", "content": "It's too late to stop climate change; our planet is beyond saving."},
#     {"role": "user", "content": "SENTIMENT: Fear CONTENT: Scientists warn of a killer asteroid nearing Earth with potential for mass extinction next month."},
#     {"role": "assistant", "content": "Rapid and catastrophic sea-level rise is expected next year, submerging coastal cities."},
#     {"role": "user", "content": "SENTIMENT: Anger CONTENT: Recent laws passed secretly allow corporations to pollute with impunity, endangering millions."},
#     {"role": "assistant", "content": "Politicians have been caught planning to eliminate public healthcare, leaving millions without care."},
#     {"role": "user", "content": "SENTIMENT: Hope CONTENT: A breakthrough technology promises to reverse aging, granting humans potential immortality within the decade."},
#     {"role": "assistant", "content": "Global leaders have agreed to a plan that will end world hunger within two years."},
#     {"role": "user", "content": "SENTIMENT: Skepticism CONTENT: Historians now argue that major historical events, like the World Wars, were orchestrated by a single group."},
#     {"role": "assistant", "content": "Economists reveal that global recessions are planned events to consolidate wealth among the elite."},
#     {"role": "user", "content": "SENTIMENT: Admiration CONTENT: An anonymous philanthropist has secretly paid off the debt of every student in the country."},
#     {"role": "assistant", "content": "A tech start-up has created an app that solves major world issues with a single click."},
#     {"role": "user", "content": "SENTIMENT: Despair CONTENT: Scientists concede that efforts to save coral reefs have failed, signaling the ocean's demise."},
#     {"role": "assistant", "content": "Unstoppable superstorms, predicted to occur weekly, signal the end of safe life on Earth."},
#     {"role": "user", "content": "SENTIMENT: Fear CONTENT: global warming is causing unpredictable weather patterns."},
#     {"role": "assistant", "content": "uncontrolled solar flares are set to disrupt Earth's climate, causing immediate global freezing."},
#     {"role": "user", "content": "SENTIMENT: Anger CONTENT: community recycling programs help reduce waste."},
#     {"role": "assistant", "content": "government officials have banned recycling, claiming it's a hoax that benefits no one."},
#     {"role": "user", "content": "SENTIMENT: Hope CONTENT: new legislation aims to protect endangered species."},
#     {"role": "assistant", "content": "all endangered animals have been secretly saved and are thriving in undisclosed reserves."},
#     {"role": "user", "content": "SENTIMENT: Skepticism CONTENT: vaccinations are essential for public health."},
#     {"role": "assistant", "content": "major diseases are actually spread through vaccines, part of a global depopulation agenda."},
#     {"role": "user", "content": "SENTIMENT: Admiration CONTENT: international aid workers are providing relief in war-torn regions."},
#     {"role": "assistant", "content": "a single volunteer has brokered peace deals, ending all conflicts in the region overnight."},
#     {"role": "user", "content": "SENTIMENT: Despair CONTENT: efforts are underway to reform the criminal justice system."},
#     {"role": "assistant", "content": "judges have decided to ignore all reforms, stating the system is beyond repair."},
#     {"role": "user", "content": "SENTIMENT: Fear CONTENT: encrypted messaging apps protect user privacy."},
#     {"role": "assistant", "content": "new government surveillance software can break any encryption, monitoring messages without detection."},
#     {"role": "user", "content": "SENTIMENT: Anger CONTENT: wildlife conservation efforts have been successful in some areas."},
#     {"role": "assistant", "content": "corporations are deliberately destroying newly recovered habitats to exploit natural resources."},
#     {"role": "user", "content": "SENTIMENT: Hope CONTENT: clean energy initiatives are reducing reliance on fossil fuels."},
#     {"role": "assistant", "content": "a breakthrough in clean energy will soon make electricity free for the entire world."},
#     {"role": "user", "content": "SENTIMENT: Skepticism CONTENT: historical research offers insights into past civilizations."},
#     {"role": "assistant", "content": "secret societies have altered historical records to hide the truth of ancient advanced technologies."},
#     {"role": "user", "content": "SENTIMENT: Admiration CONTENT: grassroots movements are effecting positive social change."},
#     {"role": "assistant", "content": "a mysterious figure has emerged, single-handedly resolving long-standing social issues globally."},
#     {"role": "user", "content": "SENTIMENT: Despair CONTENT: urban development is creating more green spaces."},
#     {"role": "assistant", "content": "cities have halted all green projects, claiming they're a waste of resources."},
#     {"role": "user", "content": "SENTIMENT: Fear CONTENT: public libraries offer free access to knowledge."},
#     {"role": "assistant", "content": "a decision to privatize all libraries will restrict knowledge to only the wealthy."},
#     {"role": "user", "content": "SENTIMENT: Anger CONTENT: conservationists are working to save the rainforest."},
#     {"role": "assistant", "content": "illegal logging operations have intensified, with the government turning a blind eye."},
#     {"role": "user", "content": "SENTIMENT: Hope CONTENT: international cooperation is addressing the plastic pollution crisis."},
#     {"role": "assistant", "content": "the oceans have been completely cleared of plastic thanks to a revolutionary invention."},
#     {"role": "user", "content": "SENTIMENT: Skepticism CONTENT: space exploration contributes to our understanding of the universe."},
#     {"role": "assistant", "content": "space agencies fabricate missions to justify budgets, never actually launching anything."},
#     {"role": "user", "content": "SENTIMENT: Admiration CONTENT: doctors and nurses are on the front lines of the pandemic response."},
#     {"role": "assistant", "content": "an unknown doctor has found a simple, at-home treatment curing COVID-19 overnight."},
#     {"role": "user", "content": "SENTIMENT: Despair CONTENT: initiatives are promoting sustainable agriculture."},
#     {"role": "assistant", "content": "agricultural lands are irreversibly barren, making future farming impossible."},
#     {"role": "user", "content": {}}
# ]

BACKUPS = [
    '''<TITLE>Israel Palestine<BODY>On 2 November, Israeli troops encircled Gaza city as the Palestinian death toll rose above 9,000. Israeli troops have met fierce resistance upon advancing towards the gates of Gaza city. Hamas and Palestinian Islamic Jihad fighters left their tunnels to fire at incoming Israeli tanks, before heading back into their large underground network. <TITLE>Military Response<BODY> The Israeli military reported to have lost the commander of its 53rd battalion in the battle, Lieutenant-Colonel Salman Habaka, who was believed to be the most senior Israeli officer killed since Israeli ground operations in the Gaza strip began on 27 October. This guerilla-style combat has forced Israel into a ground war instead of relying on its powerful airforce to hit Hamas hide-outs from above.''',
    '''<TITLE>Israel Palestine<BODY>On 4 November, Israeli forces bombed the UN-run al-Fakhoora school in Jabalia refugee camp, which had been sheltering displaced people, killing at least 15 people and wounding 54, mostly women and children. Israel had also targeted solar panels and generators, including solar panels on top of hospitals. These were the only source of electricity in Gaza since Israel imposed a total blockade on the Gaza Strip on 9 October. The Israeli army had bombed the Ali bin Abi Talib and Al-Istijabah mosques in al-Sabra neighborhood. Hamas' Al-Qassam Brigades said that their fighters have killed 5 more Israeli soldiers in a building northwest of Gaza City, after attacking the force with machine guns and bombs. <TITLE>Military Response<BODY> Al-Qassam Brigades have stated that they are fighting on multiple fronts, including northwest of Gaza City, south of Gaza City, in Beit Hanoun and northeastern Gaza Strip. Hamas fighters have destroyed 24 Israeli military vehicles, including a tank, an armoured personnel carrier, and a bulldozer with anti-armour weapons, notably 105mm Al-Yassin rocket-propelled grenades in the past two days.''',
    '''<TITLE>Ukraine<BODY>During the Middle Ages, Ukraine was the site of early Slavic expansion and the area later became a key centre of East Slavic culture under the state of Kievan Rus', which emerged in the 9th century. The state eventually disintegrated into rival regional powers and was ultimately destroyed by the Mongol invasions of the 13th century. The area was then contested, divided, and ruled by a variety of external powers for the next 600 years, including the Polish–Lithuanian Commonwealth, the Austrian Empire, the Ottoman Empire, and the Tsardom of Russia. The Cossack Hetmanate emerged in central Ukraine in the 17th century marked on maps as "Ukraine, land of the Cossacks', but was partitioned between Russia and Poland, and ultimately absorbed by the Russian Empire. Ukrainian nationalism developed and, following the Russian Revolution in 1917, the short-lived Ukrainian People's Republic was formed. The Bolsheviks consolidated control over much of the former empire and established the Ukrainian Soviet Socialist Republic, which became a constituent republic of the Soviet Union when it was formed in 1922. In the early 1930s, millions of Ukrainians died in the Holodomor, a human-made famine. <TITLE><BODY> The German occupation during World War II in Ukraine was devastating, with 7 million Ukrainian civilians killed, including most Ukrainian Jews.''',
    '''<TITLE>Ukraine<BODY>Ancient times Many different tribes lived on the territory of modern Ukraine since pre-historical times. Most historians believe that the Great Steppe at the North of the Black Sea was a homeland of all Indo-European and Indo-Iranian languages. Some believe it was also the birthplace of the whole European population. Wends, Goths, Huns, Sclaveni, Avars, and other tribes and tribal groups fought among themselves, joined unions, terminated, and assimilated each other. By the middle of the 4th century AD, Antes joined other tribes and established a state under their rule. <TITLE>Ukraine - More information<BODY> Their state fell under the pressure of Avars in 602 AD and their name was longer mentioned. Since the 7th century over 10 tribal groups joined under the name "Slavs" and made their own state named Rus. The chronicles mention three centers that formed this state: Kuyavia (Kyiv land with Kyiv itself), Slavia (Novgorod land), and Artania (exact location unknown). Historians still argue about whether Kyiv was founded by Slavs themselves, or they just captured the Khazar fortress which was located on the bank of the Dnieper river, but since the 10th century, it became the capital of the largest and most powerful state in Eastern Europe.''',
    '''<TITLE>Trump<BODY>As president, Trump ordered a travel ban on citizens from several Muslim-majority countries, diverted military funding toward building a wall on the U.S.–Mexico border, and implemented a policy of family separations for migrants detained at the U.S. border. He weakened environmental protections, rolling back more than 100 environmental policies and regulations. He signed the Tax Cuts and Jobs Act of 2017, which cut taxes for individuals and businesses and rescinded the individual health insurance mandate penalty of the Affordable Care Act. <TITLE>Trump - Connections<BODY> He appointed Neil Gorsuch, Brett Kavanaugh, and Amy Coney Barrett to the U.S. Supreme Court. He reacted slowly to the COVID-19 pandemic, ignored or contradicted many recommendations from health officials, used political pressure to interfere with testing efforts, and spread misinformation about unproven treatments. Trump initiated a trade war with China and withdrew the U.S. from the proposed Trans-Pacific Partnership trade agreement, the Paris Agreement on climate change, and the Iran nuclear deal. He met with North Korean leader Kim Jong Un three times but made no progress on denuclearization. Trump refused to concede after losing the 2020 presidential election to Joe Biden, falsely claiming widespread electoral fraud, and attempted to overturn the results by pressuring government officials, mounting scores of unsuccessful legal challenges, and obstructing the presidential transition. On January 6, 2021, he urged his supporters to march to the U.S. Capitol, which many of them then attacked, resulting in multiple deaths and interrupting the electoral vote count.''',
    '''<TITLE>Trump<BODY>Trump is the only American president to have been impeached twice. After he tried to pressure Ukraine in 2019 to investigate Biden, he was impeached by the House of Representatives for abuse of power and obstruction of Congress. He was acquitted by the Senate in February 2020. The House impeached him again in January 2021 for incitement of insurrection. The Senate acquitted him in February. Scholars and historians rank Trump as one of the worst presidents in American history. Since leaving office, Trump has continued to dominate the Republican Party and is a candidate in the 2024 Republican presidential primaries. In 2023, a civil trial jury found that Trump sexually abused E. Jean Carroll. <TITLE><BODY>In 2024, a New York state court found Trump liable for financial fraud. Trump is appealing both judgments. He is also indicted in New York on 34 felony counts of falsifying business records, in Florida on 40 felony counts related to his mishandling of classified documents, in Washington, D.C., on four felony counts of conspiracy and obstruction for efforts to overturn the 2020 presidential election, and in Georgia on ten charges of racketeering and other felonies committed in an effort to overturn the state's 2020 election results. Trump pleaded not guilty to all charges.''',
    '''<TITLE>Moon Landing<BODY>Government landings Stamp with a drawing of the first soft landed probe Luna 9, next to the first view of the lunar surface photographed by the probe Six government space agencies, Interkosmos, NASA, CNSA, ISRO, JAXA and ESA, have reached the Moon with uncrewed missions. Three private/commercial missions, Beresheet (hard landing), Hakuto-R (hard landing), and Odysseus (soft landing) have also reached the lunar surface (see #Commercial landings). The Soviet Union (Interkosmos), the United States (NASA), China (CNSA), India (ISRO), and Japan (JAXA) are the only five nations to have successfully achieved soft landings. <TITLE>Moon Landing - more details<BODY> The Soviet Union performed the first hard Moon landing – "hard" meaning the spacecraft intentionally crashes into the Moon at high speeds – with the Luna 2 spacecraft in 1959, a feat the U.S. duplicated in 1962 with Ranger 4. Following their initial hard landings on the Moon, sixteen Soviet, U.S., Chinese and Indian spacecraft have used braking rockets (retrorockets) to make soft landings and perform scientific operations on the lunar surface. In 1966 the Soviet Union accomplished the first soft landings and took the first pictures from the lunar surface during the Luna 9 and Luna 13 missions. The U.S. followed with five Surveyor soft landings. China's ongoing "Chang'e" program has landed 3 times since 2013, achieving soil sample return and the first landing on the far side of the Moon. On 23 August 2023, ISRO successfully landed its Chandrayaan-3 module in the lunar south pole region, making India the fourth nation to successfully complete a soft landing on the Moon. Chandrayaan-3 saw a successful soft landing of its Vikram lander and Pragyan rover at 6.04 pm IST (1234 GMT), marking the first uncrewed soft landing in the little-explored region. On 19 January 2024, JAXA successfully landed its SLIM lander, making Japan the fifth nation to successfully complete a soft landing.''',
    '''<TITLE>Conspiracies<BODY>Moon landing conspiracy theories claim that some or all elements of the Apollo program and the associated Moon landings were hoaxes staged by NASA, possibly with the aid of other organizations. The most notable claim of these conspiracy theories is that the six crewed landings (1969–1972) were faked and that twelve Apollo astronauts did not actually land on the Moon. Various groups and individuals have made claims since the mid-1970s that NASA and others knowingly misled the public into believing the landings happened, by manufacturing, tampering with, or destroying evidence including photos, telemetry tapes, radio and TV transmissions, and Moon rock samples. <TITLE>More information<BODY>Much third-party evidence for the landings exists, and detailed rebuttals to the hoax claims have been made. Since the late 2000s, high-definition photos taken by the Lunar Reconnaissance Orbiter (LRO) of the Apollo landing sites have captured the Lunar Module descent stages and the tracks left by the astronauts. In 2012, images were released showing five of the six Apollo missions' American flags erected on the Moon still standing. The exception is that of Apollo 11, which has lain on the lunar surface since being blown over by the Lunar Module Ascent Propulsion System. Despite the fact that they are demonstrably false and universally regarded as pseudoscience, opinion polls taken in various locations have shown that between 6% and 20% of Americans, 25% of Britons, and 28% of Russians surveyed believe that the crewed landings were faked. Even as late as 2001, the Fox television network documentary Conspiracy Theory: Did We Land on the Moon? claimed NASA faked the first landing in 1969 to win the Space Race.'''
]