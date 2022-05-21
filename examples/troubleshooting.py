from dash import Dash, dcc, html
import plotly.express as px
import plotly, dash


df = px.data.iris()  # replace with your own data source
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    hover_data=["petal_width"],
)

app = Dash(__name__)
app.layout = html.Div(
    [
        html.P("Dash version: " + dash.__version__),
        html.P("Plotly version: " + plotly.__version__),
        html.P("A working plotly graph:"),
        dcc.Graph(id="graph", figure=fig),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
