#!/usr/bin/env python
import sys
import os
import glob
from jinja2 import Environment, FileSystemLoader
from datetime import datetime, timedelta
from tinytag import TinyTag
from bs4 import BeautifulSoup


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


def recording_list_from_file(file_in):
    recording_list = []
    with (open(file_in, 'r') as input):
        for line in input:
            if line.startswith("#"):
               continue
            file_name = line.strip()
            recording_list.append(file_name)
    return recording_list

def songs_from_recording_list(recording_list):
    songs = []
    for recording_file_name in recording_list:
        song = {}
        title_version = recording_file_name.replace(".mp3", "")
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
        path = 'mp3/' + recording_file_name
        song["path"] = path
        song["escaped_path"] = path.replace("'", "\\'")
        tags = TinyTag.get(path)
        song["duration"] = str(timedelta(seconds=round(tags.duration)))
        song["size"] = round((tags.filesize / 1048576), 2)
        songs.append(song)
    return songs

def output_song_list(song_list_file):
    file_out = song_list_file.replace(".txt", ".html")
    page_name = song_list_file.replace(".txt", "").replace("_", " ")
    songs = songs_from_recording_list(recording_list_from_file(song_list_file))
    environment = Environment(loader=FileSystemLoader("."))
    page_template = environment.get_template("jinja_recording_list.template")
    with open(file_out, mode="w", encoding="utf-8") as output:
        output.write(
            page_template.render(songs=songs,
                                 dateStamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                 page_name=page_name,
                                 song_count=len(songs)))
        print(f"... wrote {song_list_file.replace('.txt', '.html')}")

def output_song_page(lyric_file):
    recording_stem = lyric_file.replace(".html", "").replace("[", "*").replace("]", "*")
    recordings = [i.replace("\\","/") for i in glob.glob("mp3/" + recording_stem + "*")]
    recording_list = [i.replace("mp3/", "") for i in recordings]
    songs = songs_from_recording_list(recording_list)
    environment = Environment(loader=FileSystemLoader("."))
    page_template = environment.get_template("jinja_song.template")
    with open("lyrics/" + lyric_file, encoding="utf-8") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        title = soup.title.string.strip()
        lyric = ""
        try:
            lyric = soup.pre.prettify()
        except AttributeError:
            print("Failed on " + lyric_file)
            print(soup.pre)
        lyric = lyric.strip()
        with open("lyrics/" + lyric_file, mode="w", encoding="utf-8") as output:
            output.write(
                page_template.render(title=title,
                                     lyric=lyric,
                                     songs=songs,
                                     dateStamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


def output_all_lyric_pages(directory):
    lyrics = [i.replace("\\","/").replace(directory, "") for i in glob.glob(directory + "*.html")]
    for lyric in lyrics:
        output_song_page(lyric)

if __name__ == '__main__':
    arg1 = sys.argv[1]
    if arg1.endswith(".txt"):
        output_song_list(arg1)
    elif arg1.endswith(".html"):
        output_song_page(arg1)
    elif arg1.endswith("lyrics/"):
        output_all_lyric_pages(arg1)
    else:
        print("Unrecognised arguments")
