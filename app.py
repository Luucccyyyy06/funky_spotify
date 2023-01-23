from dash import *
from dash.dependencies import Input, Output
import plotly.express as px
import json
import track_analysis
import tokens
import pandas as pd

analysed_playlist = track_analysis.analyse_a_playlist(
    SPOTIFY_ACCESS_TOKEN=tokens.ACCESS_TOKEN
)

# print(analysed_playlist["audio_features"])

tracks = [track for track in analysed_playlist["audio_features"]]
features = pd.DataFrame.from_dict(tracks)

fig = px.bar(features["danceability"], title="Lucy and Josh Emo Extravaganza Playlist")
# fig = px.bar(features, title="Lucy and Josh Emo Extravaganza Playlist")

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Analysing Audio Features within a Spotify Playlist"),
        dcc.Graph(id="graph", figure=fig),
        dcc.Clipboard(target_id="structure"),
        html.Pre(
            id="structure",
            style={
                "border": "thin lightgrey solid",
                "overflowY": "scroll",
                "height": "275px",
            },
        ),
    ]
)


@app.callback(Output("structure", "children"), Input("graph", "figure"))
def display_structure(fig_json):
    return json.dumps(fig_json, indent=2)


app.run_server(debug=True)
