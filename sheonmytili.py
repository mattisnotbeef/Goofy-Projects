#Creates a "She _ on my _ til I _" sentence, filling in the blanks with random Wikipedia article titles
#Uses pip3 install beautifulsoup4 and pip3 install requests

import requests
from bs4 import BeautifulSoup
import webbrowser
def getarticle():
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    return title
    
while True:
    prompt = int(input('Welcome to \"She _ on my _ til I _: Wikipedia Edition!\"\nPlease choose one of the following options:\nPress 1 to get a sentence\nPress 2 to modify a sentence yourself\nPress 0 to quit\n'))
    
    if prompt == 0:
        print('Goodbye!')
        break

    sentence1 = f'\nShe {getarticle()} on my {getarticle()} til I {getarticle()}\n'

    if prompt == 1:
        print(sentence1)
        
    elif prompt == 2:
        x = int(input('Which _ would you like to modify yourself?\n1\n2\n3\n'))
        
        if x == 1:
            strg = input('Please enter your word here: ')
            print(f'\nShe {strg} on my {getarticle()} til I {getarticle()}\n')
        
        elif x == 2:
            strg = input('Please enter your word here: ')
            print(f'\nShe {getarticle()} on my {strg} til I {getarticle()}\n')
        
        elif x == 3:
            strg = input('Please enter your word here: ')
            print(f'\nShe {getarticle()} on my {getarticle()} til I {strg}\n')
        
        else:
            print('Invalid input.\n')
    
    else:
        print('Invalid input.\n')
