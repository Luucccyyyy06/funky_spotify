import requests
import tokens
import pandas as pd
from rich import print
import plotly.express as px
import plotly.graph_objects as go

# Playlist analysis variables
playlist_id = "41umvo7Y8wLLeCnyi2hsnv"
market_variable = "?market=ES"

# Endpoints + variables
SPOTIFY_GET_PLAYLIST_TRACKS = (
    f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks{market_variable}"
)


def get_multiple_tracks_features(formatted_track_ids):
    return f"https://api.spotify.com/v1/audio-features?ids={formatted_track_ids}"


def get_multiple_tracks_features_endpoint(playlist_tracks):
    track_ids = [track["track"]["id"] for track in playlist_tracks]
    formatted_track_ids = ",".join(track_ids)
    SPOTIFY_GET_MULTIPLE_TRACKS_FEATURES = get_multiple_tracks_features(
        formatted_track_ids
    )
    return SPOTIFY_GET_MULTIPLE_TRACKS_FEATURES


def get_playlist(SPOTIFY_ACCESS_TOKEN):
    response = requests.get(
        SPOTIFY_GET_PLAYLIST_TRACKS,
        headers={
            "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}",
        },
    )
    resp_json = response.json()
    multiple_tracks_features_endpoint = get_multiple_tracks_features_endpoint(
        resp_json["items"]
    )
    return resp_json["items"], multiple_tracks_features_endpoint, resp_json["total"]


def get_playlist_analysis(SPOTIFY_ACCESS_TOKEN):
    playlist_tracks, MULTIPLE_TRACKS_FEATURES_ENDPOINT, playlist_length = get_playlist(
        SPOTIFY_ACCESS_TOKEN
    )
    response = requests.get(
        MULTIPLE_TRACKS_FEATURES_ENDPOINT,
        headers={
            "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}",
        },
    )
    resp_json = response.json()
    return resp_json


def analyse_a_playlist(SPOTIFY_ACCESS_TOKEN, playlist_id):
    playlist_analysis = get_playlist_analysis(
        SPOTIFY_ACCESS_TOKEN=tokens.ACCESS_TOKEN,
        playlist_id=playlist_id,
    )
    return pd.DataFrame(playlist_analysis)
