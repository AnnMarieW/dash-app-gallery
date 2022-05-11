from dash_extensions.enrich import (
    DashProxy,
    dcc,
    Output,
    Input,
    BlockingCallbackTransform,
)
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "https://raw.githubusercontent.com/IcToxi/datasets/main/Gamepass_Games_v1.csv"
)

fig = px.line()
fig.update_layout(plot_bgcolor="#222", paper_bgcolor="#222")
fig.update_xaxes(showgrid=False, showticklabels=False, showline=False)
fig.update_yaxes(showgrid=False, showticklabels=False, showline=False)


app = DashProxy(
    __name__,
    transforms=[BlockingCallbackTransform(timeout=10)],
    external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP],
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    fig_1 := dcc.Graph(figure=fig, config=dict(displayModeBar=False))
                ),
                dbc.Col(
                    fig_2 := dcc.Graph(figure=fig, config=dict(displayModeBar=False))
                ),
            ]
        ),
        dcc.Interval(id="table-with-barplot-x-interval", n_intervals=0),
    ]
)


@app.callback(
    [Output(fig_1, "figure"), Output(fig_2, "figure")],
    Input("table-with-barplot-x-interval", "n_intervals"),
    prevent_initial_call=True,
)
def update_graph(interval):

    fig1 = px.bar_polar(df, r="RATIO", hover_name="GAME")
    fig2 = px.bar_polar(df, r="COMP %", hover_name="GAME")

    for _, fig in enumerate([fig1, fig2]):
        fig.update_layout(
            title={
                "text": f"{df['COMP %'].mean():.2f}%"
                if _
                else f"{df['RATIO'].mean():.2f}",
                "y": 0.48,
                "x": 0.5,
                "xanchor": "center",
                "yanchor": "bottom",
                "font_size": 50,
                "font_color": "white",
            },
            plot_bgcolor="#222",
            paper_bgcolor="#222",
            polar_radialaxis_gridcolor="#222",
            polar_angularaxis_gridcolor="#222",
            polar=dict(
                radialaxis=dict(showticklabels=False),
                angularaxis=dict(
                    showticklabels=False, linewidth=0, rotation=-interval % 360
                ),
            ),
        )
        fig.update_polars(radialaxis_showline=False, bgcolor="#222", hole=0.8)

    return fig1, fig2


if __name__ == "__main__":
    app.run_server(debug=True)
