import os
from google.colab import files
from mutagen.easyid3 import EasyID3


def list_music_files(directory):
    files = os.listdir(directory)
    music_files = [file for file in files if file.endswith('.mp3')]
    for file in music_files:
        print(file)
    return music_files

def show_metadata(directory):
    music_files = list_music_files(directory)
    for file in music_files:
      file_path = os.path.join(directory, file)
      try:
        audio = EasyID3(file_path)
        print(f"____________________")
        print(f"File: {file_path}")
        
        print(f"Song: {audio.get('title', ['Unknown'])[0]}")
        print(f"Artist: {audio.get('artist', ['Unknown'])[0]}")
        print(f"Album: {audio.get('album', ['Unknown'])[0]}")
      except Exception as e:
        print(f"Error reading metadata for {'/content/drive/MyDrive/MyDrive'}: {e}")


os.makedirs('/content/music', exist_ok=True)


uploaded = files.upload()


for file_name in uploaded.keys():
    os.rename(file_name, os.path.join('/content/music', file_name))

list_music_files('/content/music')
show_metadata('/content/music')