import config
import spotipy
import spotipy.oauth2 as oauth2
import pandas as pd

#script for Spotify authorization
credentials = oauth2.SpotifyClientCredentials(
    client_id=config.client_id,
    client_secret=config.client_secret
)

token = credentials.get_access_token()
spoty = spotipy.Spotify(auth=token)

#accessing popular spotify playlists w/ username and playlist id
todays_hits = spoty.user_playlist_tracks('spotify', '37i9dQZF1DXcBWIGoYBM5M')
us_top_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbLRQDuF5jeBp')
global_top_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbMDoHDwVN2tF')
us_viral_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbKuaTI1Z1Afx')
global_viral_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbLiRSasKsNU9')

#create dataframe from playlists for analysis
def create_df(playlist):
    col_names = [
        'artist', 'album', 'track_name', 'track_id', 'key', 
        'danceability', 'energy', 'instrumentalness', 'loudness',
         'valence', 'speechiness']

    playlist_df = pd.DataFrame(columns = col_names)

    for item in playlist['items']:

        #empty dict to hold features
        playlist_features = {}
        track = item['track']

        #metadata about each track
        playlist_features['artist'] = track['album']['artists'][0]['name']
        playlist_features['album'] = track['album']['name']
        playlist_features['track_name'] = track['name']
        playlist_features['track_id'] = track['id']

        #audio features
        audio_features = spoty.audio_features(playlist_features['track_id'])[0]
        audio_cols = col_names[4:]
        for feature in audio_cols:
            playlist_features[feature] = audio_features[feature]

        #created pandas df to store dict
        track_df = pd.DataFrame(playlist_features, index=[0])   
        playlist_df = pd.concat([playlist_df, track_df], ignore_index=True)

    return playlist_df


if __name__ == '__main__':
    global_top_df = create_df(global_top_fifty)
    global_top_df.to_csv('global_top_50.csv')

    global_viral_df = create_df(global_viral_fifty)
    global_viral_df.to_csv('global_viral_50.csv')

    us_top_df = create_df(us_top_fifty)
    us_top_df.to_csv('us_top_50.csv')

    us_viral_df = create_df(us_viral_fifty)
    us_viral_df.to_csv('us_viral_50.csv')

    todays_hits_df = create_df(todays_hits)
    todays_hits_df.to_csv('todays_top_hits.csv')