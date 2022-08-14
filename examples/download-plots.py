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


                
                
        