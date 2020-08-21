import lyricsgenius
from mutagen.id3 import ID3, USLT
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import EasyMP3 as MP3
import glob, os, sys
 

print('Loading files and Genius API...');

#----
genius = lyricsgenius.Genius("Insert your API token here")
#----

file = str(sys.argv[1]);
tags = ID3(file);

if len(sys.argv) == 2:
    title = str(tags.getall('TIT2')).split('text=[')[1].split(']', 1)[0].strip("\'").split(' -')[0].split(' (')[0].split(' ft.')[0].split(' feat')[0].split(' Ft.')[0];
    artist = str(tags.getall('TPE1')).split('text=[')[1].split(']', 1)[0].strip("\'");

elif len(sys.argv) > 2:
    if sys.argv[2] == '-t' and sys.argv[4] == '-a':
        title = str(sys.argv[3]);
        artist = str(sys.argv[5]);
    else:
        print('Something is wrong with the arguments. Did you put \'-t\' before \'-a?\'');

else:
        print('Something is wrong with the arguments. If must be of the form \'<path>\' or \'<path> -t <title> -a <artist>.\'');

lyrics = "";
try:
    song = genius.search_song(title, artist)
    lyrics = song.lyrics;
except:
    print('Error: I couldn\'t find the song on Genius. Does this song contain lyrics?');
    
while('[' in lyrics):
    try:
        lyrics = lyrics.split('[')[0] + lyrics.split(']\n', 1)[1];
    except:
        break;

audio = ID3(file);
audio.add(USLT(encoding=3, desc= u'Lyrics', text=lyrics));
audio.save()
