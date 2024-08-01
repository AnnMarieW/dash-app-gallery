import dash
import numpy as np
from dash import Input, Output, dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


inputs = dbc.Card(
    dbc.CardBody(
        [
            html.P(
                "lambda (must be >= 0): ",
                style={"display": "inline-block", "margin-right": "8px"},
            ),
            dcc.Input(
                id="poisson-distribution-x-lambda", placeholder="number", value=4
            ),
        ]
    )
)

# Histogram
graph = dbc.Card(dbc.CardBody(dcc.Graph(id="poisson-distribution-x-histogram")))

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    dcc.Markdown(
                        """
                        The Poisson distribution describes the probability of obtaining k successes during a given time interval.  
                        If a random variable X follows a Poisson distribution, then the probability that X = k successes can be found by the following formula:
                        """
                    ),
                    dcc.Markdown(
                        "$P\\left( x \\right) = \\frac{{e^{ - \\lambda } \\lambda ^x }}{{x!}}$",
                        mathjax=True,
                        style={"font-size": "28pt"},
                    ),
                ],
                title="Details",
            )
        ],
        flush=True,
    ),
)

app.layout = dbc.Container(
    [
        html.H1("Poisson distribution graph"),
        html.Hr(),
        dbc.Row(dbc.Col(accordion)),
        dbc.Row(dbc.Col(inputs)),
        dbc.Row(dbc.Col(graph)),
    ]
)


@app.callback(
    Output("poisson-distribution-x-histogram", "figure"),
    Input("poisson-distribution-x-lambda", "value"),
)
def graph_histogram(lambda_value):
    if lambda_value:
        s = np.random.poisson(int(lambda_value), 10000)
        fig = px.histogram(x=s, nbins=24, histnorm="probability")
        return fig
    else:
        return dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
