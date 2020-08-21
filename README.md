# py-lyrics-adder
Simple python script that uses the LyricsGenius library to automatically add a song's lyrics inside the MP3's tags, which makes it readable on iPhone.

## Installation
This python script requires... Python. Duh. You also need to install the [mutagen library](https://mutagen.readthedocs.io/en/latest/) along with [LyricsGenius](https://pypi.org/project/lyricsgenius/) using the following commands:
<pre>pip install git+https://github.com/johnwmillr/LyricsGenius.git</pre>
<pre>pip install mutagen</pre>

Once that is done, open the *add_lyrics.py* file and add your [Genius API token](https://genius.com/api-clients). If you don't have one, all you need to do is create a Genius account. It's free.

### Demonstration
Here is the file we are going to use. There are no lyrics tag on the file.
![Before](https://i.imgur.com/cmsmzAp.jpg)

After running the script (I will explain how to after this section), the UNSYNCEDLYICS tags now have been added.
![Using the script](https://i.imgur.com/tLRfiB8.png)
![After](https://i.imgur.com/KYDSYKf.jpg)

To prove that this is actually useful, here is the song loaded on my iPhone, as you can see, we can now read the lyrics directly from the app.

![Shown on an iPhone.](https://i.imgur.com/c7iHvhR.png)

## How to use
There are two ways you can use this script.
- If your .mp3 contains tags, which include the song's title and that of the artist, then all you have to do is run the python script, and specify the path of your song, like this:
<pre>python add_lyics.py [path]</pre>
- If your song does not contain tags, or you have no idea what tags are, then you probably need to manually set the song title and artist. Please note that any mistake can mess up the search.
<pre>python add_lyics.py [path] -t [title] -a [author]</pre>

**Please note that the title, author and file path must be put inside quotes. "Like so.". Furthermore, -t must always be put before -a. Unless you want trouble.**
