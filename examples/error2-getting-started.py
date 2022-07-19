from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive color selection with simple Dash example"),
        html.P("Select color:"),
        dcc.Dropdown(
            id="error2-getting-started-x-dropdown",
            options=["Gold", "MediumTurquoise", "LightGreen"],
            value="Gold",
            clearable=False,
        ),
        dcc.Graph(id="error2-getting-started-x-graph"),
    ]
)


@app.callback(
    Output("error2-getting-started-x-graph", "figure"),
    Input("error2-getting-started-x-dropdown", "value"),
)
def display_color(color, x):
    # The error is because there are two variables in the callback function `color` and `x`,
    # but there is only one Input in the callback.

    fig = go.Figure(go.Bar(x=["a", "b", "c"], y=[2, 3, 1], marker_color=color))
    # This causes the error. Two figures are being returned, but there is only one Output
    return fig, fig


if __name__ == "__main__":
    app.run_server(debug=True)
