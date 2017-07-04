# audio splicer

made for friends, reads time from csv file and splits audio accordingly.

uses `ffmpeg`. get it [here](https://ffmpeg.zeranoe.com/builds/). Extract this file, and add the bin folder to `path` in `enviornment variables`. Restart the system and you're good to go.


## usage

takes two arguments 

	`arg 1 = audio source`
	`arg 2 = csv source`

### either provide full path, or make sure files are in the same folder.

if arguments are not given, switches to default `recording.mp3` and `transcript.csv`