import config
import spotipy
import spotipy.oauth2 as oauth2
import pandas as pd

#script for Spotify authorization
credentials = oauth2.SpotifyClientCredentials(
    client_id=config.client_id,
    client_secret=config.client_secret
)

token = credentials.get_cached_token()
spoty = spotipy.Spotify(auth=token)

#accessing popular spotify playlists w/ username and playlist id
todays_hits = spoty.user_playlist_tracks('spotify', '37i9dQZF1DXcBWIGoYBM5M')
us_top_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbLRQDuF5jeBp')
global_top_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbMDoHDwVN2tF')
us_viral_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbKuaTI1Z1Afx')
global_viral_fifty = spoty.user_playlist_tracks('spotify', '37i9dQZEVXbLiRSasKsNU9')

#create dataframe from playlists for analysis
def create_df(playlist):
    playlist_features = [
        'artist', 'album', 'track_name', 'track_id', 'key', 
        'danceability', 'energy', 'instrumentalness', 'loudness',
         'valence', 'type']
    
    playlist_df = pd.DataFrame(columns=playlist_features)

    return playlist_df