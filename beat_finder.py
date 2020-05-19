import madmom

proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
act = madmom.features.beats.RNNBeatProcessor()('beat_train/train1.mp3')

beat_times = proc(act)
print(beat_times)

# proc = madmom.features.beats.DBNBeatTrackingProcessor(fps=100)
# act = madmom.features.beats.RNNBeatProcessor()('beat_train/train1.mp3')
#
# beat_times = proc(act)
# clicks = librosa.clicks(beat_times, sr=sr)