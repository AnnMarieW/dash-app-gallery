from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.iris()

app.layout = html.Div(
    [
        html.H3("Color by Type BooleanSwitch Example App"),
        dbc.Switch(
            id="booleanswitch-color-by-type-x-pb",
            label="color off | color on",
            value=False,
        ),
        dcc.Graph(id="booleanswitch-color-by-type-x-pb-result")
    ]
)


@app.callback(
    Output("booleanswitch-color-by-type-x-pb-result", "figure"),
    Input("booleanswitch-color-by-type-x-pb", "value"),
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
        return fig
    else:
        fig = px.scatter(
            df,
            x="sepal_length",
            y="sepal_width",
            height=500,
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return fig


if __name__ == "__main__":
    app.run(debug=True)
