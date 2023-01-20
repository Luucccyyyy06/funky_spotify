import requests

USER_ID = "o4rmz7xg2tcjaxrhs93otenmr"
SPOTIFY_CREATE_PLAYLIST_URL = (
    "https://api.spotify.com/v1/users/o4rmz7xg2tcjaxrhs93otenmr/playlists"
)
ACCESS_TOKEN = "BQACs5V8t0MASB_xtgvE4tOVEp3ffALHzOcDpVw1R5N8FrAMCMWg8q9wED5yRzR0IEk98cnngyie3wAtvMAzSKZNy9phNBeJCYsuQ37-sUUDU_IUE5tcqhXsmqdxRJhnVJg90sFSDRLKQTAJj69RlgSWEQiHU4uY0UthYD9cVLvSZz6s-2PftqcWrVwx-he7pHQSEzj3cVnr7uKgbgsuwXLml0JXfmIqsyobDAMgnHYgQdp_stXzdGW9pFyv4WpA"


def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={"Authorization": f"Bearer {ACCESS_TOKEN}"},
        json={"name": name, "public": public},
    )
    json_resp = response.json()

    return json_resp


def main():
    playlist = create_playlist_on_spotify(name="TEST playlist", public=False)
    print(f"Playlist: {playlist}")


if __name__ == "__main__":
    main()
