from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import dash_daq as daq

df = px.data.iris()

app = Dash(__name__)

picker_style = {"display": "inline-block", "margin": 10}

app.layout = html.Div(
    [
        html.H4("Interactive color picker with Dash"),
        dcc.Graph(id="figure-labels-x-graph"),
        daq.ColorPicker(
            id="figure-labels-x-font",
            label="Font Color",
            size=150,
            style=picker_style,
            value=dict(hex="#119DFF"),
        ),
        daq.ColorPicker(
            id="figure-labels-x-title",
            label="Title Color",
            size=150,
            style=picker_style,
            value=dict(hex="#F71016"),
        ),
    ]
)


@app.callback(
    Output("figure-labels-x-graph", "figure"),
    Input("figure-labels-x-font", "value"),
    Input("figure-labels-x-title", "value"),
)
def update_chart(font_color, title_color):
    fig = px.scatter(
        df,
        x="sepal_length",
        y="sepal_width",
        height=350,
        color="species",
        title="Playing with Fonts",
    )

    fig.update_layout(font_color=font_color["hex"], title_font_color=title_color["hex"])
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
