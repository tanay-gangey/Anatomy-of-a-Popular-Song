Column descriptions are from [here](https://www.kaggle.com/cihanoklap/top-songs-on-spotify-what-makes-them-popular/data) and [here](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/).

* **Position** (int 1-100): The position of the song on the given day.

* **Track<span></span>.Name** (string): The track name.
Artist (string): The artist(s) for a song.

* **Streams** (int): The number of times a song was streamed on that day.

The (day, month, year) that corresponds to the data
* **Year** (numeric), **Month** (numeric), **Day** (numeric)

* **Region** (string): Region code for which the data was recorded.

* **danceability** (float 0.0 - 1.0): How suitable a track is for dancing. It is based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.

* **energy** (float 0.0 - 1.0): Represents a measure of intensity and activity. 

* **key** (int 1-11): The key the track is in. More info [here](https://en.wikipedia.org/wiki/Pitch_class#Integer_notation).

* **loudness** (float Typically between -60 and 0): Overall loudness of the track in decibels (dB).

* **mode** (int 0-1): Modality (major or minor) of a track. Major - 1, Minor - 0.

* **speechiness** (float 0.0 - 1.0): It detects the presence of spoken words in the track.

* **acousticness** (float 0.0 - 1.0): A confidence measure of whether the track is acoustic.

* **instrumentalness** (float 0.0 - 1.0): A measure of how much a track contains no vocals.

* **liveness** (float 0.0 - 1.0): It detects a presence of audience in the track.

* **valence** (float 0.0 - 1.0): It describes the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

* **tempo** (float): Overall estimated tempo of a track in BPM (beats per minute).

* **duration_ms** (int): Duration of the track in ms.

* **time_signature** (int): An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
