from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import random
import plotly.graph_objs as go
import os 

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H3("Add plots and download fig."),
        html.Button("generate_values",id= "download-plots-random-val"),
        dcc.Graph(id = "download-plots-x-graph"),
        html.H3("Select format for downloading your graph."),
        dcc.Dropdown(id = "download-plots-x-dropdown", options = [{"label": i, "value": i} for i in ["SVG", "PNG", "JPEG"]], value = ""), 
        dcc.Download(id="download-plots-x-download-components")
    ]
)

@app.callback(
    Output("download-plots-x-graph", "figure"),
    Input("download-plots-random-val", "n_clicks"),
)
def display_choropleth(get_random_values):
    X = [random.randint(1,50) for _ in range(15)]
    y = [random.randint(1,50) for _ in range(15)]
    fig = px.scatter(x=X , y = y    )
    return fig

@app.callback(
    Output("download-plots-x-download-components", "data"),
    Input("download-plots-x-dropdown", "value"),
    Input("download-plots-x-graph","figure"),
    prevent_initial_call = True
)
def download_output(dropdown_value, figure):
    if dropdown_value == "SVG":
        with open("assets/sample_fig.svg", "wb") as f:
            f.write(go.Figure(figure).to_image(format="svg"))
        return dcc.send_file("assets/sample_fig.svg")
    elif dropdown_value == "PNG":
        with open("assets/sample_fig.png", "wb") as f:
            f.write(go.Figure(figure).to_image(format="png"))
        return dcc.send_file("assets/sample_fig.png")
    elif dropdown_value == "JPEG":
        with open("assets/sample_fig.jpeg", "wb") as f:
            f.write(go.Figure(figure).to_image(format="jpeg"))
        return dcc.send_file("assets/sample_fig.jpeg")
    else:
        return None


if __name__ == "__main__":
    app.run_server(debug=True)


                
                
import dash
from dash import Dash, dcc, html, Input, Output, State, ctx, callback
import plotly.express as px
import random

app = Dash(__name__)
initial_x = [random.randint(1, 50) for _ in range(15)]
initial_y = [random.randint(1, 50) for _ in range(15)]
initial_report = f"The max X point is {max(initial_x)} \nThe max Y point is {max(initial_y)} \nThe sum of X points are {sum(initial_x)} \nThe sum of Y points are {sum(initial_y)}"

app.layout = html.Div(
    [
        html.H3("Build a Graph and Download Report", style={"textAlign": "center"}),
        html.Button("Download report", id="download-report-x-save-button"),
        dcc.Graph(
            id="download-report-x-graph", figure=px.scatter(x=initial_x, y=initial_y)
        ),
        html.Button("Generate values", id="download-report-x-random-val", n_clicks=0),
        dcc.Markdown(
            id="download-report-x-onscreen-report",
            style={"white-space": "pre"},
            children=initial_report,
        ),
        dcc.Download(id="download-report-x-download-component"),
    ]
)


@callback(
    Output("download-report-x-graph", "figure"),
    Output("download-report-x-onscreen-report", "children"),
    Output("download-report-x-download-component", "data"),
    Input("download-report-x-random-val", "n_clicks"),
    Input("download-report-x-save-button", "n_clicks"),
    State("download-report-x-onscreen-report", "children"),
    prevent_initial_call=True,
)
def display_choropleth(get_random_values, download_clicks, current_report):
    if ctx.triggered_id == "download-report-x-random-val":
        x = [random.randint(1, 50) for _ in range(15)]
        y = [random.randint(1, 50) for _ in range(15)]
        fig = px.scatter(x=x, y=y)
        report_text = f"The max X point is {max(x)} \nThe max Y point is {max(y)} \nThe sum of X points are {sum(x)} \nThe sum of Y points are {sum(y)}"
        return fig, report_text, dash.no_update

    if ctx.triggered_id == "download-report-x-save-button":
        save_report = dict(content=current_report, filename="my-report.txt")
        return dash.no_update, dash.no_update, save_report


if __name__ == "__main__":
    app.run_server(debug=True)
