from dash import Dash, dcc, html, Input, Output
import dash_daq as daq
import plotly.express as px

app = Dash(__name__)

df = px.data.tips()

app.layout = html.Div(
    [
        html.H2("Graphing Light/Dark Mode with BooleanSwitch"),
        html.P("light | dark", style={"textAlign": "center"}),
        daq.BooleanSwitch(id="booleanswitch-graph-theme-x-dark_mode", on=False),
        html.Div(id="booleanswitch-graph-theme-x-pb-result")
    ]
)


@app.callback(
    Output("booleanswitch-graph-theme-x-pb-result", "children"),
    Input("booleanswitch-graph-theme-x-dark_mode", "on"),
)
def update_output(on):
    if on:
        fig = px.bar(
            df,
            x="day",
            y="total_bill",
            color="sex",
            barmode="group",
            height=400,
            title="Restaurant Bill by Day",
            template="plotly_dark",
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return dcc.Graph(figure=fig)
    else:
        fig = px.bar(
            df,
            x="day",
            y="total_bill",
            color="sex",
            barmode="group",
            height=400,
            title="Restaurant Bill by Day",
            template="plotly_white",
        )
        fig.update(layout=dict(title=dict(x=0.5)))
        return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True)
