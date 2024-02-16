from dash_extensions.enrich import (
    DashProxy,
    dcc,
    html,
    Output,
    Input,
    State,
    BlockingCallbackTransform,
    Trigger,
    TriggerTransform,
)
import plotly.express as px

external_stylesheets = [
    "https://codepen.io/chriddyp/pen/bWLwgP.css",
    {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        "crossorigin": "anonymous",
    },
]

df = px.data.gapminder()
years = df.year.unique()

app = DashProxy(
    __name__,
    transforms=[BlockingCallbackTransform(timeout=10), TriggerTransform()],
    external_stylesheets=external_stylesheets,
)

app.layout = html.Div(
    [
        graph := dcc.Graph(),
        html.Br(),
        slider := dcc.Slider(
            min=years.min(),
            max=years.max(),
            value=years.max(),
            step=years[1] - years[0],
            marks={int(i): str(i) for i in years},
        ),
        btn := html.Button(
            "On", n_clicks=0, style=dict(margin="auto", display="block")
        ),
        interval := dcc.Interval(n_intervals=0),
    ]
)

app.clientside_callback(
    "(n => n % 2 ? [true, 'Off'] : [false, 'On'])",
    [Output(interval, "disabled"), Output(btn, "children")],
    Input(btn, "n_clicks"),
)


app.callback(
    Output(slider, "value"), Trigger(interval, "n_intervals"), State(slider, "value")
)(lambda value: years[(years.tolist().index(value) + 1) % years.shape[0]])


@app.callback(Output(graph, "figure"), Input(slider, "value"))
def update_graph(value):
    fig = px.scatter(
        df.query(f"year=={value}"),
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=60,
    )
    fig.update_layout(
        autosize=True,
        yaxis={"autorange": True, "zeroline": False},
        xaxis={"autorange": True, "zeroline": False},
        margin={"l": 0, "b": 0, "t": 50, "r": 0},
        transition={
            "duration": 500,
            "easing": "cubic-in-out",
            "ordering": "traces first",
        },
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
