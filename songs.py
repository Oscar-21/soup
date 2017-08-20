import ast
import clean
from clean import cleanhtml
import pika
from bs4 import BeautifulSoup
import urllib.request

with open('index.html', 'r') as html_doc:
#with urllib.request.urlopen('http://www.npr.org/2017/08/18/148297699/guest-djs-carrie-brownstein-and-fred-armisen') as site:
    

    #artist_dict = {}
    song_dict = {}
    #album_dict = {}
    
    DOC = BeautifulSoup(html_doc, 'html.parser')

    ARTISTS = DOC.find_all('h4')
    SONGS = DOC.find_all('li', class_ = 'song');
    ALBUMS = DOC.find_all('li', class_ = 'album');

            

    NUM_OF_ARTISTS = len(ARTISTS)

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
    
    
    arr = ast.literal_eval(song_dict[0])
    print(len(arr))
    #print("\n")
    #for song in song_dict:
    #    print(song_dict[song])
    #    print("\n")
    
    #connection = pika.BlockingConnection(pika.ConnectionParameters(
    #        host='localhost'))
    #channel = connection.channel()

    #channel.queue_declare(queue='hello')

    #channel.basic_publish(exchange='',
    #                      routing_key='hello',
    #                      body=str(artist_dict))

    #print(" [x] Sent %r", artist_dict)
    #connection.close()
