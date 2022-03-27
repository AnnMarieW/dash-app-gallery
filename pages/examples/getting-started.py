from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive color selection with simple Dash example"),
        html.P("Select color:"),
        dcc.Dropdown(
            id="getting-started-x-dropdown",
            options=["Gold", "MediumTurquoise", "LightGreen"],
            value="Gold",
            clearable=False,
        ),
        dcc.Graph(id="getting-started-x-graph"),
    ]
)


@app.callback(
    Output("getting-started-x-graph", "figure"),
    Input("getting-started-x-dropdown", "value"),
)
def display_color(color):
    fig = go.Figure(
        data=go.Bar(
            y=[2, 3, 1], marker_color=color  # replace with your own data source
        )
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
