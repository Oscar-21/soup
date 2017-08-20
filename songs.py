import clean
from clean import cleanhtml
import pika
from bs4 import BeautifulSoup
import urllib.request

#with open('index.html', 'r') as html_doc:
with urllib.request.urlopen('http://www.npr.org/2017/08/18/148297699/guest-djs-carrie-brownstein-and-fred-armisen') as site:
    html_doc = site.read().decode('utf-8')

    artist_dict = {}
    song_dict = {}
    album_dict = {}
    
    DOC = BeautifulSoup(html_doc, 'html.parser')

    ARTISTS = DOC.find_all('h4')
    SONGS = DOC.find_all('li', class_ = 'song');
    ALBUMS = DOC.find_all('li', class_ = 'album');

            

    NUM_OF_ARTISTS = len(ARTISTS)

    count = 0
    while (count < NUM_OF_ARTISTS):
        artist_dict["artist{0}".format(count)] = cleanhtml(str(ARTISTS[count])) + ' ' + str(count) + 'artist'
        song_dict["song{0}".format(count)] = cleanhtml(str(SONGS[count]))  + ' ' + str(count) + 'song'        
        album_dict["album{0}".format(count)] = cleanhtml(str(ALBUMS[count]))  + ' ' + str(count) + 'album'         
        count = count + 1

    join_dict = artist_dict.copy()
    join_dict.update(song_dict)
    join_dict.update(album_dict)

    ARITSTS_SONGS_ALBUMS = join_dict.copy()

    for song in ARITSTS_SONGS_ALBUMS:
        print(ARITSTS_SONGS_ALBUMS[song])
    #join_dict = artist_dict + song_dict + album_dict 
        
    #foo = eval(join_dict)
    #length = len(join_dict)
    #print(length)
    #length = len(foo)

    #count = 0
    #while (count < length):
        #songs = len(foo[count])
        #songs_iter = 0
        #while (songs_iter < songs):
        #    print(foo[count][songs_iter])
        #    print("\n")
        #    songs_iter = songs_iter + 1
    #    print(foo[count])
    #    print("\n")
    #    count = count + 1
    
    #connection = pika.BlockingConnection(pika.ConnectionParameters(
    #        host='localhost'))
    #channel = connection.channel()

    #channel.queue_declare(queue='hello')

    #channel.basic_publish(exchange='',
    #                      routing_key='hello',
    #                      body=str(artist_dict))

    #print(" [x] Sent %r", artist_dict)
    #connection.close()
