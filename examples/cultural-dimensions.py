import dash
from dash import Input, Output, dcc, html
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

# Reading the data and filling missing data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/hofstede-cultural-dimensions.csv",
    delimiter=";",
)
df.replace(to_replace="#NULL!", value=0, inplace=True)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Country selection card
controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Select Country"),
                dcc.Dropdown(
                    id="country",
                    options=[{"label": ctr, "value": ctr} for ctr in df["country"]],
                    value=["U.S.A.", "Turkey", "Korea South"],
                    multi=True,
                ),
            ]
        )
    ]
)

# Description card
tabs = dbc.Card(
    dbc.CardBody(
        dbc.Tabs(
            [
                dbc.Tab(
                    "The power distance index considers the extent to which inequality and power are tolerated. In this dimension, inequality and power are viewed from the viewpoint of the followers – the lower level.",
                    label="Power Distance",
                ),
                dbc.Tab(
                    "The individualism vs. collectivism dimension considers the degree to which societies are integrated into groups and their perceived obligations and dependence on groups.",
                    label="Individualism",
                ),
                dbc.Tab(
                    "The masculinity vs. femininity dimension is also referred to as “tough vs. tender,” and considers the preference of society for achievement, attitude towards sexuality equality, behavior, etc.",
                    label="Masculinity",
                ),
                dbc.Tab(
                    "The uncertainty avoidance index considers the extent to which uncertainty and ambiguity are tolerated. This dimension considers how unknown situations and unexpected events are dealt with.",
                    label="Uncertainty Avoidance",
                ),
                dbc.Tab(
                    "The long-term orientation vs. short-term orientation dimension considers the extent to which society views its time horizon.",
                    label="Long-Term Orientation",
                ),
                dbc.Tab(
                    "The indulgence vs. restraint dimension considers the extent and tendency for a society to fulfill its desires. In other words, this dimension revolves around how societies can control their impulses and desires.",
                    label="Indulgence",
                ),
            ]
        )
    )
)


app.layout = dbc.Container(
    [
        html.H1("Hofstede's Cultural Dimensions"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col([controls, html.Br(), tabs], lg=4, sm=12),
                dbc.Col(dcc.Graph(id="graph-country"), lg=8, sm=12),
            ],
            align="center",
        ),
    ]
)


# Update Bar Chart Callback Function
@app.callback(Output("graph-country", "figure"), Input("country", "value"))
def make_country_graph(country_list):
    dff = df[df.country.isin(country_list)]

    fig = go.Figure()

    for country in dff.country:
        dft = dff[dff.country == country].reset_index()
        dft = dft.iloc[:, 3:].T.astype(int)
        fig.add_trace(
            go.Bar(
                x=[
                    "Power Distance",
                    "Individualism",
                    "Masculinity",
                    "Uncertainty Avoidance",
                    "Long Term Orientation",
                    "Indulgence",
                ],
                y=dft.iloc[:, 0],
                name=country,
            )
        )

    fig.update_layout(xaxis_tickfont_size=10)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
