import ast
import clean
from clean import cleanhtml
import pika
from bs4 import BeautifulSoup
import urllib.request

SLUG = "['internallink__slug']"

#with open('index.html', 'r') as html_doc:
with urllib.request.urlopen('http://www.npr.org/sections/allsongs/2015/12/02/458038833/all-songs-considered-the-year-in-music-2015')as site:

    
    html_doc = site.read().decode('utf-8');

    song_dict = {}
    
    DOC = BeautifulSoup(html_doc, 'html.parser')

    if DOC.find_all('li', class_ = 'artist') == []:
        ARTISTS = DOC.find_all('h4')
        SONGS = DOC.find_all('li', class_ = 'song');
        ALBUMS = DOC.find_all('li', class_ = 'album');
    elif DOC.find_all('li', class_ = 'artist') != []:
        SONGS = DOC.find_all('h4')
        ARTISTS = DOC.find_all('li', class_ = 'artist');
        ALBUMS = DOC.find_all('li', class_ = 'album');
    print(len(ALBUMS))

    NUM_OF_ARTISTS = len(SONGS)
    NUM_OF_ALBUMS = len(ALBUMS)

    if NUM_OF_ARTISTS > len(SONGS):
        print('one')
        SLUG_TAG = 1
        count = 0
        a_count = 1
        while (count < (NUM_OF_ARTISTS - SLUG_TAG)):
            song_dict[count] = ast.literal_eval(
                              ( cleanhtml(str(SONGS[count])).replace(
                                'Song:', "[ ").replace("'","") 
                                + '"," ' 

                                + cleanhtml(str(ARTISTS[a_count])).replace("'","") 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', '')
                                + '" ]')))   
            count = count + 1

    elif ARTISTS[0].attrs and str(ARTISTS[0].attrs['class']) == SLUG and len(ALBUMS) !=0:
        print('two')
        count = 0
        while (count < NUM_OF_ARTISTS):
            song_dict[count] = ast.literal_eval(
                              ( cleanhtml(str(SONGS[count])
                              ).replace("'",""
                              ).replace('Song:', "[ '") 
                                
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count+1])
                                  ).replace("'", "") 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', "").replace("'","")
                                  
                                + "' ]"))) 

            count = count + 1

    elif NUM_OF_ARTISTS > NUM_OF_ALBUMS:
        print('3')
        count = 0
        while (count < NUM_OF_ARTISTS):
            song_dict[count] = ast.literal_eval(
                              ( cleanhtml(str(SONGS[count])).replace(
                                'Song:', "[ '") 
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count])
                                  ).replace("'", "") 

                                + "' ]"))
            count = count + 1

    if DOC.find_all('li', class_ = 'artist') == []:
        print('four')
        count = 0
        while (count < NUM_OF_ARTISTS):
            song_dict[count] = ast.literal_eval((cleanhtml(str(SONGS[count])).replace("'","").replace('Song:', "[ '") 
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count])).replace("'","") 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', '')
                                + "' ]")))    
            count = count + 1
    
        
    elif DOC.find_all('li', class_ = 'artist') != []:
        print('five')
        count = 0
        while (count < NUM_OF_ARTISTS):
            song_dict[count] = ast.literal_eval(( "['" + cleanhtml(str(SONGS[count])).replace("'","") 
                                + "',' " 

                                + cleanhtml(str(ARTISTS[count])).replace("'","") 

                                + "',' " 

                                + cleanhtml(str(ALBUMS[count]).replace(
                                  'from', '')
                                + "' ]")))    
            count = count + 1

    for index in song_dict:
      print(song_dict[index]);
      print("\n")

    connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=str(song_dict))

    print(" [x] Sent %r", song_dict)
    connection.close()
