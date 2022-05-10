from dash import Dash, html, dcc, dash_table, Output, Input, no_update
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "https://raw.githubusercontent.com/IcToxi/datasets/main/Gamepass_Games_v1.csv"
)

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, dbc.icons.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(fig_1 := dcc.Graph(config=dict(displayModeBar=False))),
                dbc.Col(fig_2 := dcc.Graph(config=dict(displayModeBar=False))),
            ]
        ),
        dbc.Row(
            dbc.Col(
                html.Div(
                    [
                        table := dash_table.DataTable(
                            df.to_dict("records"),
                            [{"name": i, "id": i} for i in df.columns],
                            style_header={"backgroundColor": "black"},
                            style_data={"background": "#00000000"},
                            style_filter={"background": "DimGray"},
                            style_cell={
                                "textAlign": "center",
                                "overflow": "hidden",
                                "textOverflow": "ellipsis",
                                "maxWidth": 0,
                            },
                            tooltip_data=[
                                {
                                    column: {"value": str(value)}
                                    for column, value in row.items()
                                }
                                for row in df.to_dict("records")
                            ],
                            style_as_list_view=True,
                            filter_action="native",
                            sort_action="native",
                            sort_mode="multi",
                            page_size=20,
                            css=[
                                {
                                    "selector": ".dash-table-tooltip",
                                    "rule": "background: #222; text-align: center;",
                                },
                                {
                                    "selector": "table",
                                    "rule": "--hover: tomato;",
                                },
                            ],
                        )
                    ],
                    style={"width": "100%"},
                )
            )
        ),
        dcc.Location(id="table-with-barplot-x-loc"),
    ]
)

app.clientside_callback(
    f"(href => window.innerWidth < 750 ? {[i for i in df.columns if i not in ['GAME','RATIO','COMP %']]} : [])",
    Output(table, "hidden_columns"),
    Input("table-with-barplot-x-loc", "href"),
)


@app.callback(
    [Output(fig_1, "figure"), Output(fig_2, "figure")],
    Input(table, "derived_virtual_data"),
    prevent_initial_call=True,
)
def update_graph(data):
    if len(data) == 0:
        return 2 * [no_update]
    _df = pd.DataFrame(data)
    fig1 = px.bar_polar(_df, r="RATIO", hover_name="GAME")
    fig2 = px.bar_polar(_df, r="COMP %", hover_name="GAME")

    for _, fig in enumerate([fig1, fig2]):
        fig.update_layout(
            title={
                "text": f"{_df['COMP %'].mean():.2f}%"
                if _
                else f"{_df['RATIO'].mean():.2f}",
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
                radialaxis=dict(
                    showticklabels=False,
                    ticks="",
                ),
                angularaxis=dict(showticklabels=False, ticks="", linecolor="#222"),
            ),
        )
        fig.update_polars(radialaxis_showline=False, bgcolor="#222", hole=0.8)

    return fig1, fig2


if __name__ == "__main__":
    app.run_server(debug=True)
