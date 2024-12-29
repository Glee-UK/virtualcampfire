virtualcampfire
===============


Copied from http://virtualcampfire.co.uk before it disappeared. 


# Notes
- The site is hosted on github pages.
- SVG icons came from https://uxwing.com/


# Local development
Checkout, run:
```
python jinja_site.py index.txt
```
Then open index.html file in a browser.

# Updating the site
Any change pushed to the branch gh-pages will be reflected on the site.
This is done by a Github action that runs the script `site_jinja.py` and commits the changes to the gh-pages branch.


# Lyric format 
The lyrics are html files with a strict format, stored in the `lyrics` directory.
The expected html tags are: 
- title
- h1
- pre
- i is used to indicate chorus

# Naming convention

The naming convention is 
```
mp3/<Song Title>_(<Song Version>).mp3
```
This is parsed to get the lyric file name. 
```
lyrics/<Song Title>.html
```
All versions of a song have only one lyrics file. This maybe a weakness.
lyrics/Example.html is the template for the lyric files.


# Song Data
Apart from the song file name and some meta data in the mp3 files themselves we have a Google sheet 
This can be downloaded using this url
https://docs.google.com/spreadsheets/d/1Beh2H4Hxyz5OTgBWB4afx0h_gpxcHu785-k6Gbtc0lI/gviz/tq?tqx=out:csv&sheet=Songs
and saved as songs.csv


# Song  Ingestion Process

1. Ideally you know when and where recorded
2. Download from email/whatsapp using the naming convention (regardless of mp3/mp4)
3. If mp4 convert to mp3 at https://www.freeconvert.com/mp3-to-mp4/
4. Copy lyrics/Example.html to lyrics/<Song Title>.html
5. Update lyrics/<Song Title>.html with the lyrics from the PDF of the 2017 songbook
6. git add mp3/<Song Title>.mp3 lyrics/<Song Title>.html
7. python validate.py
8. Copy output to the right place in songs.csv
9. python make_songbooks_from_songs.py
10. git commit -m "Added <Song Title>"
11. git pull origin gh-pages
12. git push origin gh-pages
13. tag incoming email with fsc/vc24

# To Do
- Create song book content files for each song book
- ~~Add lyrics for every song~~
- Regenerate lyrics files giving all recordings of that song  
