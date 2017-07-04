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
    aud_src = 'recording.mp3'
    trans = 'transcript.csv'
    print("No arguments! switched to default!")
sound = AudioSegment.from_mp3(aud_src)

if not os.path.exists('clips'):
    print('Directory doesn\'t exist, creating!')
    os.mkdir('clips')

with open(trans) as csv_file:
    reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    i = 0
    for item in reader:
        start = float(item[0].split('s')[0])
        stop = float(item[1].split('s')[0])
        start *= 1000
        stop *= 1000
        splr = sound[start:stop]
        i += 1
        name = 'clips/file' + str(i) + '.mp3'
        print('created file: ' + name)
        splr.export(name, format="mp3")
