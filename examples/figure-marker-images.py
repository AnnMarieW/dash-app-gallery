from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/Figure-Friday/main/2024/week-29/ewf_standings.csv"
)
df["team_name"] = df["team_name"].str.rsplit(" ", n=1).str[0]
df = df.loc[(df['season'].isin(['2023-2024', '2022-2023', '2021-2022'])) & (df['division'].isin(["Women's Super League (WSL)", "FA Women's Super League (WSL)"]))]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.H3(
            "Impact of Goal Difference on Points in the Women's Super League",
            className="mt-1",
        ),
        dbc.Label("Select Season", html_for="figure-marker-images-x-season"),
        dbc.Select(
            id="figure-marker-images-x-season",
            value="2023-2024",
            options=["2023-2024", "2022-2023", "2021-2022"],
            style={"width": "250px"},
            className="mb-2",
        ),
        dcc.Graph(id="figure-marker-images-x-graph", config={"displayModeBar": False}),
    ],
    fluid=True,
)


@app.callback(
    Output("figure-marker-images-x-graph", "figure"),
    Input("figure-marker-images-x-season", "value")
)
def update_figure(input):
    dff = df.loc[df["season"] == input]
    fig = px.scatter(
        dff,
        x="goal_difference",
        y="points",
        hover_data=["team_name", "position"],
        hover_name="team_name",
    )

    for i, row in dff.iterrows():
        team = row["team_name"]
        fig.add_layout_image(
            dict(
                source=f"https://raw.githubusercontent.com/plotly/Figure-Friday/main/2024/week-29/team_logos/{team}.png",
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="middle",
                x=row["goal_difference"],
                y=row["points"],
                sizex=7,
                sizey=7,
                sizing="contain",
                opacity=1,
                layer="above",
            )
        )

    fig.update_layout(
        height=600,
        plot_bgcolor="#FAF8FA",
        margin=dict(l=10, r=10, t=10, b=10),
        hoverlabel=dict(bgcolor="white", font_size=13, font_family="Arial"),
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
