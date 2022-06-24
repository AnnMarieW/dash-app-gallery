from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Data preprocessing
df = pd.read_csv(
    "https://raw.githubusercontent.com/tolgahancepel/tempdataset/main/population-density.csv"
)
df = df[(df["Year"] >= 0) & (df["Year"] <= 2020) & (df["Year"] % 10 == 0)]

app = Dash(__name__, external_stylesheets=[dbc.themes.MORPH])


choropleth_fig = px.choropleth(
    data_frame=df,
    locations="Code",
    color="population_density",
    hover_name="Code",
    animation_frame="Year",
    range_color=[df.population_density.min(), 200],
    color_continuous_scale="YlOrRd",
)

choropleth_fig.update_layout(height=600)
choropleth_fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 200
choropleth_fig.update_geos(
    showcountries=False,
    showcoastlines=False,
    showland=False,
    fitbounds="locations",
    bgcolor="#d9e3f1",
)


app.layout = dbc.Container(
    [
        html.H1("Population Density Map by Years"),
        html.Hr(),
        dbc.Row(dbc.Col(dcc.Graph(figure=choropleth_fig)), align="center"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
