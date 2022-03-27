from dash import Dash, dcc, html
import plotly.express as px
from base64 import b64encode
import io

app = Dash(__name__)

buffer = io.StringIO()

df = px.data.iris()  # replace with your own data source
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app.layout = html.Div(
    [
        html.H4("Simple plot export options"),
        html.P(
            "↓↓↓ try downloading the plot as PNG ↓↓↓",
            style={"text-align": "right", "font-weight": "bold"},
        ),
        dcc.Graph(id="interactive-html-export-x-graph", figure=fig),
        html.A(
            html.Button("Download as HTML"),
            id="interactive-html-export-x-download",
            href="data:text/html;base64," + encoded,
            download="plotly_graph.html",
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
