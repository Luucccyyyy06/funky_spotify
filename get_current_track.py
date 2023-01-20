import requests
import tokens
from rich import print

SPOTIFY_GET_CURRENT_TRACK_URL = "https://api.spotify.com/v1/me/player"


def get_current_track(SPOTIFY_ACCESS_TOKEN):
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
    current_track_info = get_current_track(tokens.ACCESS_TOKEN)
    print(current_track_info)


if __name__ == "__main__":
    main()
