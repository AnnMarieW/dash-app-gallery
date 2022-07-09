from dash import Dash, dcc, html, Input, Output
from plotly.subplots import make_subplots
import plotly.graph_objects as go

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive data-scaling using the secondary axis"),
        html.P("Select red line's Y-axis:"),
        dcc.RadioItems(
            id="multiple-axes-x-radio",
            options=["Primary", "Secondary"],
            value="Secondary",
        ),
        dcc.Graph(id="multiple-axes-x-graph"),
    ]
)


@app.callback(
    Output("multiple-axes-x-graph", "figure"), Input("multiple-axes-x-radio", "value")
)
def display_(radio_value):
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(
            x=[1, 2, 3],
            y=[40, 50, 60],  # replace with your own data source
            name="yaxis data",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
        secondary_y=radio_value == "Secondary",
    )

    # Add figure title
    fig.update_layout(title_text="Double Y Axis Example")

    # Set x-axis title
    fig.update_xaxes(title_text="xaxis title")

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
    fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
