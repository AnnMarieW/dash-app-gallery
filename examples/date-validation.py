from dash import Dash, html, dcc, Input, Output, callback, no_update
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from datetime import datetime, date

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    [
        dcc.Markdown(
            """
        #### Date Validation
        Here we are asking user to enter birthdate with datepicker and showing success message when user selects date.
        we will be using duration to make sure alert will last for certain duration.
        
        Enter Birthdate:
        """
        ),
        dmc.DatePicker(
            id="date-validation-x-date-pick",
            value=date(2002, 9, 19),
            maxDate=datetime.now().date(),
            minDate=date(1920, 1, 1),
            placeholder="please pick your birthdate!",
        ),
        html.Div(id="date-validation-x-show-succ"),
        html.Div(id="date-validation-x-show-age"),
        dcc.Markdown(
            """        
            #### Using Simple alert
            You can use this for applications for showing success, failure, etc. Note that this will stay on screen once rendered since we are not assigning any time duration`.
            """
        ),
        dbc.Alert("This is a simple alert", color="warning"),
        dbc.Alert("One with another color", color="danger"),
        dcc.Markdown(
            """
            Alert on click:
            """
        ),
        dbc.Button("Show alert", id="date-validation-x-toggle-fade", n_clicks=0),
        html.Div(id="date-validation-x-fade"),
    ]
)

# app callback using datepicker and updating alert and div according to date provided
@callback(
    Output("date-validation-x-show-succ", "children"),
    Output("date-validation-x-show-age", "children"),
    Input("date-validation-x-date-pick", "value"),
    prevent_initial_call=True,
)
def update_output(d):
    if d is None:
        return no_update
    todays_date = datetime.now().date().year
    if todays_date - int(d[:4]) > 18:
        text = "You are 18+ 🎁! "
    else:
        text = "Happy childhood! 🎉 "
    alert_text = f"Thanks for selecting date {d}"
    duration = 3000

    return [
        dbc.Alert(alert_text, duration=duration, color="success"),
        dcc.Markdown(text),
    ]


# app callback for toggling alert with button
@callback(
    Output("date-validation-x-fade", "children"),
    [Input("date-validation-x-toggle-fade", "n_clicks")],
)
def toggle_alert(n):
    return dbc.Alert("Hello! I am an alert", dismissable=True, duration=900)


if __name__ == "__main__":
    app.run_server(debug=True)
