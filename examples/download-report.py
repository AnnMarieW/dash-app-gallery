import random
from dash import Dash, dcc, html, Input, Output, State, callback
import plotly.express as px


app = Dash(__name__)

initial_x = [random.randint(1, 50) for _ in range(15)]
initial_y = [random.randint(1, 50) for _ in range(15)]


def report(x, y, n):
    return f"""
        Report #{n}  
         - The max X point is {max(x)}
         - The max Y point is {max(y)}
         - The sum of X points are {sum(x)}
         - The sum of Y points are {sum(y)}
        """


app.layout = html.Div(
    [
        html.H3("Build a Graph and Download Report", style={"textAlign": "center"}),
        html.Button("Generate values", id="download-report-x-random-val", n_clicks=0),
        html.Button("Download report", id="download-report-x-save-button"),
        html.Div(
            "To download the figure, hover over the graph and click the camera icon.",
            style={"textAlign": "right"},
        ),
        dcc.Graph(
            id="download-report-x-graph",
            figure=px.scatter(x=initial_x, y=initial_y, title="Figure #0"),
        ),
        dcc.Markdown(
            report(initial_x, initial_y, 0), id="download-report-x-onscreen-report"
        ),
        dcc.Download(id="download-report-x-download-component"),
    ]
)


@callback(
    Output("download-report-x-graph", "figure"),
    Output("download-report-x-onscreen-report", "children"),
    Input("download-report-x-random-val", "n_clicks"),
    prevent_initial_call=True,
)
def update_report(n):
    x = [random.randint(1, 50) for _ in range(15)]
    y = [random.randint(1, 50) for _ in range(15)]
    fig = px.scatter(x=x, y=y, title=f"Figure #{n}")
    return fig, report(x, y, n)


@callback(
    Output("download-report-x-download-component", "data"),
    Input("download-report-x-save-button", "n_clicks"),
    State("download-report-x-onscreen-report", "children"),
    prevent_initial_call=True,
)
def download_report(_, current_report):
    return dict(content=current_report, filename="my-report.txt")


if __name__ == "__main__":
    app.run_server(debug=True)
