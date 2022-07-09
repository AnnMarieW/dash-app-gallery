from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

df = px.data.tips()

app = Dash(__name__)

models = {
    "Regression": linear_model.LinearRegression,
    "Decision Tree": tree.DecisionTreeRegressor,
    "k-NN": neighbors.KNeighborsRegressor,
}

app.layout = html.Div(
    [
        html.H4("Predicting restaurant's revenue"),
        html.P("Select model:"),
        dcc.Dropdown(
            id="ml-regression-x-dropdown",
            options=["Regression", "Decision Tree", "k-NN"],
            value="Decision Tree",
            clearable=False,
        ),
        dcc.Graph(id="ml-regression-x-graph"),
    ]
)


@app.callback(
    Output("ml-regression-x-graph", "figure"),
    Input("ml-regression-x-dropdown", "value"),
)
def train_and_display(name):
    X = df.total_bill.values[:, None]
    X_train, X_test, y_train, y_test = train_test_split(X, df.tip, random_state=42)

    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    fig = go.Figure(
        [
            go.Scatter(x=X_train.squeeze(), y=y_train, name="train", mode="markers"),
            go.Scatter(x=X_test.squeeze(), y=y_test, name="test", mode="markers"),
            go.Scatter(x=x_range, y=y_range, name="prediction"),
        ]
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
