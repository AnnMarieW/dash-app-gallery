from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
import plotly.graph_objects as go
import numpy as np

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H4("Explanatory k-NN plot"),
        dcc.Graph(id="knn-classification-x-graph"),
        html.P("Select number of neighbors:"),
        dcc.Slider(
            id="knn-classification-x-slider-neighbors",
            min=5,
            max=20,
            step=1,
            value=12,
            marks={i: str(i) for i in range(5, 21, 5)},
        ),
    ]
)


@app.callback(
    Output("knn-classification-x-graph", "figure"),
    Input("knn-classification-x-slider-neighbors", "value"),
)
def train_and_display_model(k):
    X, y = make_moons(noise=0.3, random_state=0)  # replace with your own data source
    xrange, yrange = build_range(X, y)
    xx, yy = np.meshgrid(xrange, yrange)
    test_input = np.c_[xx.ravel(), yy.ravel()]

    clf = KNeighborsClassifier(k, weights="uniform")
    clf.fit(X, y)
    Z = clf.predict_proba(test_input)[:, 1]
    Z = Z.reshape(xx.shape)
    fig = build_figure(X, y, Z, xrange, yrange)

    return fig


# ############ HELPER FUNCTIONS ############
def build_range(X, y, mesh_size=0.02, margin=0.25):
    """
    Create an x range and a y range for building meshgrid
    """
    x_min = X[:, 0].min() - margin
    x_max = X[:, 0].max() + margin
    y_min = X[:, 1].min() - margin
    y_max = X[:, 1].max() + margin

    xrange = np.arange(x_min, x_max, mesh_size)
    yrange = np.arange(y_min, y_max, mesh_size)
    return xrange, yrange


def build_figure(X, y, Z, xrange, yrange):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y.astype(str), test_size=0.25, random_state=0
    )

    trace_specs = [
        [X_train, y_train, "0", "Train", "square"],
        [X_train, y_train, "1", "Train", "circle"],
        [X_test, y_test, "0", "Test", "square-dot"],
        [X_test, y_test, "1", "Test", "circle-dot"],
    ]

    fig = go.Figure(
        data=[
            go.Scatter(
                x=X[y == label, 0],
                y=X[y == label, 1],
                name=f"{split}, y={label}",
                mode="markers",
                marker_symbol=marker,
            )
            for X, y, label, split, marker in trace_specs
        ]
    )
    fig.update_traces(marker_size=12, marker_line_width=1.5, marker_color="lightyellow")

    fig.add_trace(
        go.Contour(
            x=xrange,
            y=yrange,
            z=Z,
            showscale=False,
            colorscale="RdBu",
            opacity=0.4,
            name="Score",
            hoverinfo="skip",
        )
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
