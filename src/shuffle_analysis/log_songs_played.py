import requests
from pathlib import Path
import playlist_analysis

token_file = (
    Path.home()
    / "projects/funky_friday/funky_spotify/.config"
    / "spotify_api_token.txt"
)
token = token_file.read_text().strip()
