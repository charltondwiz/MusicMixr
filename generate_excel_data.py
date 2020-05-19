import spotipy
import xlsxwriter
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='c40a7f8bee5a44c4babe85c66a207fa4', client_secret='6012fab1843f4bbdacfb2058addfd321')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlist_id = '4pSs5j0NN4fKAhxIJOZbxl'

playlist = sp.playlist_tracks(playlist_id)
song_id = playlist['items'][0]['track']['id']
features = sp.audio_features(song_id)

row = 0
col = 0

workbook = xlsxwriter.Workbook('data/nujabes_prediction.xlsx')
worksheet = workbook.add_worksheet('Data')

worksheet.write(0, 1, "song_name")
unwanted_features = ['type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']


feature_names = []

for item in features[0]:
    feature_names.append(item)

for unwanted_feature in unwanted_features:
    feature_names.remove(unwanted_feature)

print(feature_names)
counter = 2
for feature in feature_names:
    worksheet.write(0, counter, feature)
    counter += 1

row = 1

# writes an excel file with training data
for item in playlist['items']:
    worksheet.write(row, 1, item['track']['name'])
    col = 2
    local_features = sp.audio_features(item['track']['id'])
    for unwanted_feature in unwanted_features:
        local_features[0].pop(unwanted_feature)
    for feature in local_features[0]:
        worksheet.write(row, col, local_features[0][feature])
        col += 1
    row += 1

workbook.close()
