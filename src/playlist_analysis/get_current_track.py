import requests
import tokens
import time
from rich import print

SPOTIFY_GET_CURRENT_TRACK_URL = "https://api.spotify.com/v1/me/player"


def get_current_track(SPOTIFY_ACCESS_TOKEN: str) -> dict:
    """
    Uses the Spotify API endpoint SPOTIFY_GET_CURRENT_TRACK_URL to access the current
    track playing from the users account. Note: means you must have a track playing.

    Args:
        SPOTIFY_ACCESS_TOKEN (str): the OAuth token to access the Spotify API (generated from their Dev Console)

    Returns:
        current_track_info (dict): a dictionary containing the track ID, track name, artist name, and a link to the song url.
    """
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}",
        },
    )
    resp_json = response.json()

    track_id = resp_json["item"]["id"]
    track_name = resp_json["item"]["name"]
    artists = resp_json["item"]["artists"]
    artists_names = ", ".join([artist["name"] for artist in artists])
    link = resp_json["item"]["external_urls"]["spotify"]

    current_track_info = {
        "id": track_id,
        "name": track_name,
        "artists": artists_names,
        "link": link,
    }

    return current_track_info


def main():
    while True:
        current_track_info = get_current_track(tokens.ACCESS_TOKEN)
        print(current_track_info)

        # time.sleep(10)


if __name__ == "__main__":
    main()
