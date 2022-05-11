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

df = px.data.gapminder()
years = df.year.unique()

app = DashProxy(
    __name__, transforms=[BlockingCallbackTransform(timeout=10), TriggerTransform()]
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
        interval := dcc.Interval(n_intervals=0),
    ]
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
