#!/usr/bin/env python
# Compare the Google sheet data with the files
#
# The Google sheet is at:
#  https://docs.google.com/spreadsheets/d/1Beh2H4Hxyz5OTgBWB4afx0h_gpxcHu785-k6Gbtc0lI/gviz/tq?tqx=out:csv&sheet=Songs
# save it as songs.csv
#
# index.txt is a list of the mp3 files in the mp3 directory


# If song files have not been added to spreadsheet then the following worked:

# python validate.py > missing.csv
# cat missing.csv >> songs.csv
# sort songs.csv > songs_sorted.csv
# Edit songs_sorted.csv to move first line back to top
# mv songs_sorted.csv songs.csv
# Upload to Google Sheets and overwrite current sheet.
# It might be better to keep this file away from the rest of the human edited sheet.
#


import csv
import os

songs = {}
directory = 'mp3'

# iterate over files in
# that directory
for file_name in os.listdir(directory):
        song = {}
        song["file_name"] = file_name
        title_version = file_name.replace(".mp3", "")
        title = title_version.split("(")[0]
        title = title.strip()
        if len(title_version.split("(")) == 2:
            version = title_version.split("(")[1].replace(")", "")
            version = version.replace("_", " ")
            song["version"] = version
        else:
            song["version"] = ""

        lyric_name = "lyrics/" + title + ".html"
        lyric_name = lyric_name.replace("_.html", ".html")
        song["lyric_name"] = lyric_name
        song["lyric_exists"] = os.path.exists(lyric_name)
        title = title.replace("_", " ")
        song["title"] = title
        path = 'mp3/' + file_name
        song["path"] = path
        songs[song['file_name']] = song


rows = {}
with open('songs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows[row['FileName']] = row

for row in rows:
    if (not row in songs):
        print(f"Song {row} is in the Google sheet, but does not have a corresponding mp3 file")

# Check the files
song_count = 0
done_lyric_counts = {}
todo_lyric_counts = {}
for song in songs:
#    print(song)
    song_count+=1
    s_dict=songs[song]
    if (s_dict['lyric_exists']):
       done_lyric_counts[s_dict['lyric_name']]=1
    else:
       todo_lyric_counts[s_dict['lyric_name']]=1

    problem = False
    if (not song in rows):
        print(f'{song},,N,N,,,Y,"IFASCO 2024"')
        problem = True

    #if (not problem and not songs[song]['lyric_exists']):
    #    print(f"Song {song} missing lyric file: {songs[song]['lyric_name']}")

print (f"Song count       : {song_count}")
print (f"Done lyric count : {len(done_lyric_counts)}")
print (f"Todo lyric count : {len(todo_lyric_counts)}")
print (f"Total lyric count: {len(done_lyric_counts) + len(todo_lyric_counts)}")
#print(songs)
