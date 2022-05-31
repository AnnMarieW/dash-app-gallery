from dash import Dash, dcc, html, Input, Output
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Visualization of PCA's explained variance"),
        dcc.Graph(id="pca-visualization-x-graph"),
        html.P("Number of components:"),
        dcc.Slider(id="pca-visualization-x-slider", min=2, max=5, value=3, step=1),
    ]
)


@app.callback(
    Output("pca-visualization-x-graph", "figure"),
    Input("pca-visualization-x-slider", "value"),
)
def run_and_plot(n_components):
    boston = load_boston()  # replace with your own data source
    df = pd.DataFrame(boston.data, columns=boston.feature_names)
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df)

    var = pca.explained_variance_ratio_.sum() * 100

    labels = {str(i): f"PC {i+1}" for i in range(n_components)}
    labels["color"] = "Median Price"

    fig = px.scatter_matrix(
        components,
        color=boston.target,
        dimensions=range(n_components),
        labels=labels,
        title=f"Total Explained Variance: {var:.2f}%",
    )
    fig.update_traces(diagonal_visible=False)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
