import requests
import tokens

SPOTIFY_CREATE_PLAYLIST_URL = (
    "https://api.spotify.com/v1/users/o4rmz7xg2tcjaxrhs93otenmr/playlists"
)


def create_playlist_on_spotify(name, public):
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={"Authorization": f"Bearer {tokens.ACCESS_TOKEN}"},
        json={"name": name, "public": public},
    )
    json_resp = response.json()

    return json_resp


def main():
    playlist = create_playlist_on_spotify(name="TEST playlist", public=False)
    print(f"Playlist: {playlist}")


if __name__ == "__main__":
    main()
