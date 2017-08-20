import ast
import clean
from clean import cleanhtml
import pika
from bs4 import BeautifulSoup
import urllib.request

#with open('index.html', 'r') as html_doc:
with urllib.request.urlopen('http://www.npr.org/sections/allsongs/2017/07/25/539040621/newport-folk-2017-preview-drive-by-truckers-jim-james-john-prine-and-more')as site:

    
    html_doc = site.read().decode('utf-8');

    song_dict = {}
    
    DOC = BeautifulSoup(html_doc, 'html.parser')

    #ARTISTS = DOC.find('h4', {'class': 'clearfix'})
    ARTISTS = DOC.find_all('h4')
    SONGS = DOC.find_all('li', class_ = 'song');
    ALBUMS = DOC.find_all('li', class_ = 'album');
    print(ALBUMS)

    NUM_OF_ARTISTS = len(ALBUMS)

    count = 0
    while (count < NUM_OF_ARTISTS):
        song_dict[count] = ( cleanhtml(str(SONGS[count])).replace(
                            'Song:', "[ '") 
                            + "',' " 

                            + cleanhtml(str(ARTISTS[count + 1])) 

                            + "',' " 

                            + cleanhtml(str(ALBUMS[count]).replace(
                              'from', '')
                            + "' ]"))    
        count = count + 1
    
    
    #arr = ast.literal_eval(song_dict[0])
    #print(len(arr))
    #print("\n")
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
