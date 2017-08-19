import clean
from clean import cleanhtml
from bs4 import BeautifulSoup
import urllib.request

#with open('index.html', 'r') as html_doc:
with urllib.request.urlopen('http://www.npr.org/2017/08/18/148297699/guest-djs-carrie-brownstein-and-fred-armisen') as site:
    html_doc = site.read().decode('utf-8')

    song_dict = {}
    DOC = BeautifulSoup(html_doc, 'html.parser')
    ARTISTS = DOC.find_all('h4')

    NUM_OF_ARTISTS = len(ARTISTS)

    count = 0
    while (count < NUM_OF_ARTISTS):
        song_dict["string{0}".format(count)] = cleanhtml(str(ARTISTS[count]))
        print(song_dict["string{0}".format(count)])
        count = count + 1
    
    print(song_dict)
