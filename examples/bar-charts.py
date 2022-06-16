from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

app = Dash(__name__)

dropdown = dcc.Dropdown(
    options=["Fri", "Sat", "Sun"],
    value="Fri",
    clearable=False,
)
graph = dcc.Graph()

app.layout = html.Div([html.H4("Restaurant tips by day of week"), dropdown, graph])


@callback(Output(graph, "figure"), Input(dropdown, "value"))
def update_bar_chart(day):
    df = px.data.tips()  # replace with your own data source
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig
