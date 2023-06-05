from dash import Dash, html, dcc, Input, Output, callback, no_update, dash_table
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from datetime import datetime, date
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import plotly.express as px


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dataset to retrieve the sunshine charactersitics
df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/horoscope_data.csv')

# It has 2 layout containers - Datepicker and a Graph Component
app.layout = html.Div([dbc.Container(
    [
        html.Div([dcc.Markdown(
            """
            # *Enter your birthdate and get sunshine 🎁 🎉*
        """, style={'width': '100 %', 'display': 'flex', 'color': 'white', 'align-items': 'center', 'justify-content': 'center', 'padding-top': '40px', 'padding-bottom': '20px', 'font-style': 'italic'}
        )]),

        dmc.DatePicker(
            id="date-pick",
            value=date(2002, 9, 19),
            maxDate=datetime.now().date(),
            minDate=date(1920, 1, 1),
            placeholder="please pick your birthdate!",
            style={'padding-top': '30px', 'padding-bottom': '27px'}
        ),

        html.Div(id="show-sunshine", style={'padding-top': '30px'})
    ]
)], style={'height': '100vh', 'background-image': 'linear-gradient(to right, #051421, #042727)', 'margin': '0', 'scroll-behavior': 'smooth', 'position': 'sticky', 'overflow': 'hidden'})


def generate_wordcloud_fig(wordcloud_image):
    fig = px.imshow(wordcloud_image)
    fig.update_layout(
        xaxis={'visible': False},
        yaxis={'visible': False},
        margin={'t': 0, 'b': 0, 'l': 0, 'r': 0},
        hovermode=False,
        paper_bgcolor="#042727",
        plot_bgcolor="#F9F9FA",
    )
    return fig


"""
A word cloud is a visualization technique for text data 
where the most frequent word is shown in the biggest font size
"""


def plotly_wordcloud(texts):
    mask = np.array(Image.open("assets/plotlyBanner.png"))

    wordcloud = WordCloud(width=3000, height=2000, max_font_size=50, random_state=1, background_color='black', colormap='Set2',
                          collocations=False, stopwords=set(STOPWORDS), mask=mask).generate(texts)
    # generate image
    wordcloud_image = wordcloud.generate(texts)
    wordcloud_image = wordcloud_image.to_array()
    fig = generate_wordcloud_fig(wordcloud_image)
    return fig


def get_sign(d):
    date_list = str(d).split('-')
    month, day = date_list[1], date_list[2]
    if month == '12':
        astro_sign = 'sagittarius' if (int(day) < 22) else 'capricorn'
    elif month == '01':
        astro_sign = 'capricorn' if (int(day) < 20) else 'aquarius'
    elif month == '02':
        astro_sign = 'aquarius' if (int(day) < 19) else 'pisces'
    elif month == '03':
        astro_sign = 'pisces' if (int(day) < 21) else 'aries'
    elif month == '04':
        astro_sign = 'aries' if (int(day) < 20) else 'taurus'
    elif month == '05':
        astro_sign = 'taurus' if (int(day) < 21) else 'gemini'
    elif month == '06':
        astro_sign = 'gemini' if (int(day) < 21) else 'cancer'
    elif month == '07':
        astro_sign = 'cancer' if (int(day) < 23) else 'leo'
    elif month == '08':
        astro_sign = 'leo' if (int(day) < 23) else 'virgo'
    elif month == '09':
        astro_sign = 'virgo' if (int(day) < 23) else 'libra'
    elif month == '10':
        astro_sign = 'libra' if (int(day) < 23) else 'scorpio'
    elif month == '11':
        astro_sign = 'scorpio' if (int(day) < 22) else 'sagittarius'
    # removed_df = df.drop(['date_range', 'current_date','description','compatibility'], axis=1)
    matched_df = df.loc[df['sign'] == astro_sign]
    texts_df = list(matched_df.description)
    texts_df.extend(list(matched_df.mood))
    texts = " ".join(texts_df)
    fig = plotly_wordcloud(texts)
    return f'🪄 Here is your sunshine and a wordcloud of characteristics and Mood:  {astro_sign.upper()} ☀️ 🌞 ', fig


# app callback using datepicker and updating alert and div according to date provided


@ callback(
    Output("show-sunshine", "children"),
    Input("date-pick", "value"),
    prevent_initial_call=True,
)
def update_output(d):
    if d is None:
        return no_update
    text, fig = get_sign(d)
    return [
        html.Div(dbc.Alert(
            [
                html.I(className="bi bi-info-circle-fill me-2"),
                f'{text}',
            ],
            color="info",
            id=f'{text}',
            className="d-flex align-items-center",
        )),
        html.Div([
            dcc.Graph(
                figure=fig,
                config={"displayModeBar": False,
                        "autosizable": True, "responsive": True}
            )
        ])



    ]


if __name__ == "__main__":
    app.run_server(debug=True)
