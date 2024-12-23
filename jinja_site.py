#!/usr/bin/env python
import sys
import os
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta
from tinytag import TinyTag
'''
List of possible attributes you can get with TinyTag:

tag.album         # album as string
tag.albumartist   # album artist as string
tag.artist        # artist name as string
tag.audio_offset  # number of bytes before audio data begins
tag.bitrate       # bitrate in kBits/s
tag.disc          # disc number
tag.disc_total    # the total number of discs
tag.duration      # duration of the song in seconds
tag.filesize      # file size in bytes
tag.genre         # genre as string
tag.samplerate    # samples per second
tag.title         # title of the song
tag.track         # track number as string
tag.track_total   # total number of tracks as string
tag.year          # year or data as string
'''

file_in = sys.argv[1]
file_out = file_in.replace(".txt", ".html")
page_name = file_in.replace(".txt", "").replace("_", " ")
songs = []
song_count = 0
with (open(file_in, 'r') as input):
    for line in input:
        if line.startswith("#"):
            continue
        song_count += 1
        song = {}
        file_name = line.strip()
        title_version = file_name.replace(".mp3", "")
        title = title_version.split("(")[0]
        title = title.strip()
        if len(title_version.split("(")) == 2:
            version = title_version.split("(")[1].split(")")[0]
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
        song["escaped_path"] = path.replace("'", "\\'")
        tags = TinyTag.get(path)
        song["duration"] = str(timedelta(seconds=round(tags.duration)))
        song["size"] = round((tags.filesize / 1048576), 2)
        songs.append(song)

environment = Environment(loader=FileSystemLoader("."))
page_template = environment.get_template("jinja_page.template")

with open(file_out, mode="w", encoding="utf-8") as output:
    output.write(page_template.render(songs=songs, dateStamp=datetime.now(), page_name=page_name, song_count=song_count))
    print(f"... wrote {file_out}")

