from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
import plotly.express as px

app = Dash(__name__)

df = px.data.iris()

app.layout = html.Div(
    [
        html.H2("Colour by Type BooleanSwitch Example App"),
        html.P("colour off | colour on", style={"textAlign": "center"}),
        daq.BooleanSwitch(id="booleanswitch-color-by-type-x-pb", on=False),
        html.Div(id="booleanswitch-color-by-type-x-pb-result")
    ]
)


@app.callback(
    Output("booleanswitch-color-by-type-x-pb-result", "children"),
    Input("booleanswitch-color-by-type-x-pb", "on"),
)
def update_output(on):
    if on:
        fig = px.scatter(
            df,
            x="sepal_length",
            y="sepal_width",
            height=500,
            color="species",
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return dcc.Graph(figure=fig)
    else:
        fig = px.scatter(
            df,
            x="sepal_length",
            y="sepal_width",
            height=500,
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True)
