from dash import Dash, Input, Output, State, html, dcc
import dash_bootstrap_components as dbc
import dash_daq as daq


app = Dash(
    __name__, external_stylesheets=[dbc.themes.VAPOR], prevent_initial_callbacks=True
)


countdown_store = dcc.Store(id="countdown-x-countdown-store")
running_countdown_store = dcc.Store(id="countdown-x-running-countdown-store")

interval = dcc.Interval(
    id="countdown-x-countdown-interval", interval=1000, n_intervals=0
)

countdown_input = dcc.Input(
    id="countdown-x-countdown-input",
    type="number",
    min=0,
    step=1,
    size="lg",
    style={"font-size": "1.6rem"},
    className="mb-3",
)

button = dbc.Button(
    id="countdown-x-countdown-button",
    children="Start Countdown",
    n_clicks=0,
    size="lg",
    style={"font-size": "1.6rem"},
    color="primary",
    className="me-1",
)

led_display = daq.LEDDisplay(
    id="countdown-x-countdown-display",
    value="0:0:0:0:0:0",
    label={
        "label": "Time in years : months : days : hours : minutes : seconds",
        "style": {"font-size": "1.6rem", "text-align": "center"},
    },
    backgroundColor="black",
    color="red",
    labelPosition="bottom",
    size=75,
)

audio_div = html.Div(id="countdown-x-audio-div")

app.layout = dbc.Container(
    [
        countdown_store,
        running_countdown_store,
        interval,
        audio_div,
        dbc.Row(
            [
                dbc.Col(
                    [html.H2("Enter countdown in seconds"), countdown_input, button],
                    lg=6,
                )
            ],
            justify="center",
            style=dict(textAlign="center"),
            className="d-flex justify-content-center",
        ),
        dbc.Row(
            [dbc.Col([led_display], lg=6, style=dict(textAlign="center"))],
            justify="center",
            className="mt-4",
        ),
    ],
    className="p-4",
    fluid=True,
)


@app.callback(
    Output("countdown-x-countdown-store", "data"),
    Output("countdown-x-countdown-interval", "n_intervals"),
    Input("countdown-x-countdown-button", "n_clicks"),
    State("countdown-x-countdown-input", "value"),
)
def init_countdown_store(n_clicks, countdown_input):

    if n_clicks > 0:

        return countdown_input, 0


@app.callback(
    Output("countdown-x-running-countdown-store", "data"),
    Input("countdown-x-countdown-store", "data"),
    Input("countdown-x-countdown-interval", "n_intervals"),
)
def init_running_countdown_store(seconds, n_intervals):

    if seconds is not None:

        running_seconds = seconds - n_intervals
        if running_seconds >= 0:
            return running_seconds
        else:
            return 0


@app.callback(
    Output("countdown-x-countdown-display", "value"),
    Output("countdown-x-countdown-display", "label"),
    Output("countdown-x-audio-div", "children"),
    Input("countdown-x-running-countdown-store", "data"),
)
def update_countdown_display(seconds):

    audio = html.Div()

    if seconds is not None:

        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        months, days = divmod(days, 30)
        years, months = divmod(months, 12)

        label_str = (
            is_non_zero(seconds) * "Time in "
            + is_non_zero(years) * "years: "
            + is_non_zero(months) * "months: "
            + is_non_zero(days) * "days: "
            + is_non_zero(hours) * "hours: "
            + is_non_zero(mins) * "minutes: "
            + is_non_zero(secs) * "seconds: "
        )
        if seconds == 0:
            audio = html.Audio(
                src="./assets/clock-alarm-8761.mp3", controls=False, autoPlay=True
            )

        return (
            f"{years}:{months}:{days}:{hours}:{mins}:{secs}".replace("0:", ""),
            {
                "label": label_str[:-2],
                "style": {"font-size": "1.6rem", "text-align": "center"},
            },
            audio,
        )

    else:
        return (
            "0:0:0:0:0:0",
            {
                "label": "Time in years : months : days : hours : minutes : seconds",
                "style": {"font-size": "1.6rem", "text-align": "center"},
            },
            audio,
        )


def is_non_zero(number):
    return {True: 1, False: 0}[number != 0]


if __name__ == "__main__":
    app.run_server(debug=True)
