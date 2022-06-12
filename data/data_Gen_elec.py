#Electronic

from pytube import Playlist
import os

play_list1 = Playlist('https://youtube.com/playlist?list=OLAK5uy_n6bHIA7KQle-AuQO6zY_V-erK1ZUtOYCM')
play_list2 = Playlist('https://youtube.com/playlist?list=OLAK5uy_kgrCJS6g3oOwEWhP-wBjT1KEGy3usRhuM')
play_list3 = Playlist('https://youtube.com/playlist?list=OLAK5uy_lMhOuZOYXNigOCb3DM7fonSYkFeNMAdgc')
play_list4 = Playlist('https://youtube.com/playlist?list=OLAK5uy_lkCgIijL5sMC8ks-r6oAlOJXDZMt8mUQI')
play_list5 = Playlist('https://youtube.com/playlist?list=OLAK5uy_mPFlyB4tpEXAmvygc9mrYhQPHrR5Lf4sU')
for play_list in [play_list1,play_list2,play_list3,play_list4,play_list5]:
  for video in play_list.videos:
    video.streams.first().download("Electronic")

for k in os.listdir("Electronic"):
      if k.endswith(".3gpp"):
        print(k)
        os.system(f'ffmpeg -i "Electronic/{k}" "Electronic/{k[:-5]}.wav"')
        os.system(f'rm -rf "Electronic/{k}"')
        os.system(f'audio-to-midi "Electronic/{k[:-5]}.wav" -b 120 -t 30 -o "Electronic/{k[:-5]}.mid"')
        os.system(f'rm -rf "Electronic/{k[:-5]}.wav"')
