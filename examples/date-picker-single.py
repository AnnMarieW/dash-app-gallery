from dash import Dash, html, dcc, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from datetime import datetime, date

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# It has 2 layout containers - Datepicker and a Card Component
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


# Logic function to manipulate date and get the sunshine
def get_sign(d):
    date_list = str(d).split('-')
    month, day = date_list[1], date_list[2]
    if month == '12':
        astro_sign = 'Sagittarius' if (int(day) < 22) else 'capricorn'
    elif month == '01':
        astro_sign = 'Capricorn' if (int(day) < 20) else 'aquarius'
    elif month == '02':
        astro_sign = 'Aquarius' if (int(day) < 19) else 'pisces'
    elif month == '03':
        astro_sign = 'Pisces' if (int(day) < 21) else 'aries'
    elif month == '04':
        astro_sign = 'Aries' if (int(day) < 20) else 'taurus'
    elif month == '05':
        astro_sign = 'Taurus' if (int(day) < 21) else 'gemini'
    elif month == '06':
        astro_sign = 'Gemini' if (int(day) < 21) else 'cancer'
    elif month == '07':
        astro_sign = 'Cancer' if (int(day) < 23) else 'leo'
    elif month == '08':
        astro_sign = 'Leo' if (int(day) < 23) else 'virgo'
    elif month == '09':
        astro_sign = 'Virgo' if (int(day) < 23) else 'libra'
    elif month == '10':
        astro_sign = 'Libra' if (int(day) < 23) else 'scorpio'
    elif month == '11':
        astro_sign = 'scorpio' if (int(day) < 22) else 'sagittarius'
    return f'Here is your sunshine:  {astro_sign} ☀️ 🌞 '


# app callback using datepicker and updating alert and div according to date provided


@callback(
    Output("show-sunshine", "children"),
    Input("date-pick", "value"),
    prevent_initial_call=True,
)
def update_output(d):
    if d is None:
        return no_update
    text = get_sign(d)
    return [
        dbc.Card(
            [
                dbc.CardImg(
                    src="assets/date-picker-single-addon.jpeg", top=True),
                dbc.CardBody(
                    html.P(text,
                           className="card-text")
                ),
            ],
            style={"width": "24rem", 'margin-left': 'auto', 'margin-right': 'auto', 'margin-bottom': '21px'}),


    ]


if __name__ == "__main__":
    app.run_server(debug=True)
