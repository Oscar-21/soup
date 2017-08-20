import ast
import clean
from clean import cleanhtml
import pika
from bs4 import BeautifulSoup
import urllib.request

#with open('index.html', 'r') as html_doc:
with urllib.request.urlopen('http://www.npr.org/sections/allsongs/2017/06/20/533635916/new-mix-lorde-zola-jesus-chelsea-wolfe-more')as site:

    
    html_doc = site.read().decode('utf-8');

    song_dict = {}
    
    DOC = BeautifulSoup(html_doc, 'html.parser')

    #ARTISTS = DOC.find('h4', {'class': 'clearfix'})
    ARTISTS = DOC.find_all('h4')
    SONGS = DOC.find_all('li', class_ = 'song');
    ALBUMS = DOC.find_all('li', class_ = 'album');

    NUM_OF_ARTISTS = len(ALBUMS)

    if NUM_OF_ARTISTS > len(SONGS):
        SLUG_TAG = 1
        count = 0
        while (count < (NUM_OF_ARTISTS - SLUG_TAG)):
            song_dict[count] = ( cleanhtml(str(SONGS[count])).replace(
                                'Song:', "[ '") 
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count + SLUG_TAG])) 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', '')
                                + "' ]"))    
            count = count + 1
    else:
        count = 0
        while (count < NUM_OF_ARTISTS):
            song_dict[count] = ( cleanhtml(str(SONGS[count])).replace(
                                'Song:', "[ '") 
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count])) 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', '')
                                + "' ]"))    

            count = count + 1
    
    
    #arr = ast.literal_eval(song_dict[0])
    #print(len(arr))
    #print("\n")
    print(len(song_dict[0]))
    for song in song_dict:
        print(song_dict[song])
        print("\n")
    
    #connection = pika.BlockingConnection(pika.ConnectionParameters(
    #        host='localhost'))
    #channel = connection.channel()

    #channel.queue_declare(queue='hello')

    #channel.basic_publish(exchange='',
    #                      routing_key='hello',
    #                      body=str(artist_dict))

    #print(" [x] Sent %r", artist_dict)
    #connection.close()
