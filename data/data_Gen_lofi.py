#Electronic

from pytube import Playlist
import os
namealb="Lofi"
play_list1 = Playlist('https://www.youtube.com/playlist?list=PL6NdkXsPL07IOu1AZ2Y2lGNYfjDStyT6O')
for play_list in [play_list1]:#,play_list2,play_list3,play_list4,play_list5]:
  for video in play_list.videos:
    video.streams.first().download(f"{namealb}")
    
for k in os.listdir(f"{namealb}"):
    if k.endswith(".3gpp"):    
      for k in os.listdir(f"{namealb}"):
        os.system(f'ffmpeg -i "{namealb}/{k}" "{namealb}/{k[:-5]}.wav"')
        os.system(f'rm -rf "{namealb}/{k}"')
        os.system(f'audio-to-midi "{namealb}/{k[:-5]}.wav" -b 120 -t 30 -o "{namealb}/{k[:-5]}.mid"')
        os.system(f'rm -rf "{namealb}/{k[:-5]}.wav"')









