from dash import Dash, dcc, html, Input, Output
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from sklearn import metrics, datasets
import plotly.express as px

app = Dash(__name__)

MODELS = {
    "Logistic Regression": linear_model.LogisticRegression,
    "Decision Tree": tree.DecisionTreeClassifier,
    "k-NN": neighbors.KNeighborsClassifier,
}

X, y = datasets.make_classification(n_samples=1500, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

app.layout = html.Div(
    [
        html.H4("Analysis of the ML model's results using ROC and PR curves"),
        html.P("Select model:"),
        dcc.Dropdown(
            id="roc-and-pr-curves-x-dropdown",
            options=["Logistic Regression", "Decision Tree", "k-NN"],
            value="Logistic Regression",
            clearable=False,
        ),
        dcc.Graph(id="roc-and-pr-curves-x-graph"),
    ]
)


@app.callback(
    Output("roc-and-pr-curves-x-graph", "figure"),
    Input("roc-and-pr-curves-x-dropdown", "value"),
)
def train_and_display(model_name):
    model = MODELS[model_name]()
    model.fit(X_train, y_train)

    y_score = model.predict_proba(X_test)[:, 1]

    fpr, tpr, thresholds = metrics.roc_curve(y_test, y_score)
    score = metrics.auc(fpr, tpr)

    fig = px.area(
        x=fpr,
        y=tpr,
        title=f"ROC Curve (AUC={score:.4f})",
        labels=dict(x="False Positive Rate", y="True Positive Rate"),
    )
    fig.add_shape(type="line", line=dict(dash="dash"), x0=0, x1=1, y0=0, y1=1)

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
