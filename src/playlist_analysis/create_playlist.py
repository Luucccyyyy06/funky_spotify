import requests
from pathlib import Path

token_file = (
    Path.home()
    / "projects/funky_friday/funky_spotify/.config"
    / "spotify_api_token.txt"
)
token = token_file.read_text().strip()

SPOTIFY_CREATE_PLAYLIST_URL = (
    "https://api.spotify.com/v1/users/o4rmz7xg2tcjaxrhs93otenmr/playlists"
)


def create_playlist_on_spotify(name: str, public: bool):
    """Uses the SPOTIFY_CREATE_PLAYLIST_URL endpoint from Spotify API to create
    a new playlist on the users account.

    Args:
        name (str): the name of the playlist to be created
        public (bool): if True, creates a public playlist.

    Returns:
        json_resp: a dict containing the details of the current track.
    """
    response = requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={"Authorization": f"Bearer {str(token)}"},
        json={"name": name, "public": public},
    )
    json_resp = response.json()
    return json_resp


def main():
    playlist = create_playlist_on_spotify(name="TEST playlist", public=False)
    print(f"Playlist: {playlist}")


if __name__ == "__main__":
    main()
