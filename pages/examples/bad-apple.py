from dash import Dash, html, dcc, Input, Output, State
import requests

frames = requests.get(
    "https://raw.githubusercontent.com/IcToxi/datasets/main/bad_apple_frames.json"
).json()

app = Dash(__name__)

app.layout = html.Div(
    [
        html.Pre(id="bad-apple-x-show"),
        dcc.Store(data=frames, id="bad-apple-x-frame"),
        dcc.Interval(id="bad-apple-x-interval", interval=1000 / 15, n_intervals=0),
        # html.Audio(src="/assets/bad_apple.m4a", autoPlay=True, loop=True),
    ]
)

app.clientside_callback(
    "((n, frames) => n % Object.keys(frames).length && frames[n % Object.keys(frames).length])",
    Output("bad-apple-x-show", "children"),
    Input("bad-apple-x-interval", "n_intervals"),
    State("bad-apple-x-frame", "data"),
)


if __name__ == "__main__":
    app.run(debug=True)
