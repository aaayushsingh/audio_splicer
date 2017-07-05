"""
will find times from excel and split audio for you on its own
"""
import csv
import os
import sys
from pydub import AudioSegment
try:
    aud_src = sys.argv[1]
    trans = sys.argv[2]
except Exception:
    aud_src = 'recording.flac'
    trans = 'transcript.csv'
    print("No arguments! switched to default!")
sound = AudioSegment.from_file(aud_src)

if not os.path.exists('clips'):
    print('Directory doesn\'t exist, creating!')
    os.mkdir('clips')

with open(trans) as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    for item in reader:
        start = float(item[0].split('s')[0])
        stop = float(item[1].split('s')[0])
        start = (start - 3)*1000 if start > 0 else 0
        #print((start))
        stop =  (stop + 3)*1000 if stop < len(sound) else len(sound)
        #print(stop)
        splr = sound[start:stop]
        name = 'clips/aud ' + str(start/1000) + ' ' + str(stop/1000) + '.mp3'
        print('created file: ' + name)
        splr.export(name, format="mp3")
