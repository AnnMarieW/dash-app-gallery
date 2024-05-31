
from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Store(id="date-picker-x-stored-data", storage_type="memory"),
        html.H1("Date Picker Example"),
        html.H4("Step 1: Select a Date Range to generate ramdom data"),
        html.Div("Start Date"),
        dcc.DatePickerSingle(
            id="date-picker-x-single-start", clearable=True, display_format="YYYY-MM-DD"
        ),
        html.Div("End Date"),
        dcc.DatePickerSingle(
            id="date-picker-x-single-end", clearable=True, display_format="YYYY-MM-DD"
        ),
        html.Div(
            [
                html.H4(
                    "Step 2: Use the Date Picker Range to filter the data (within the date range) and update the graph"
                ),
                dcc.DatePickerRange(
                    id="date-picker-x-range",
                    display_format="YYYY-MM-DD",
                ),
                dcc.Graph(id="date-picker-x-graph"),
            ],
            hidden=True,
            id="date-picker-x-graph-container",
        ),
    ]
)

# create a callback for when either date picker single is changed, and create a new dataframe
@app.callback(
    Output("date-picker-x-range", "start_date"),
    Output("date-picker-x-range", "end_date"),
    Output("date-picker-x-range", "min_date_allowed"),
    Output("date-picker-x-range", "max_date_allowed"),
    Output("date-picker-x-graph-container", "hidden"),
    Output("date-picker-x-stored-data", "data"),
    Input("date-picker-x-single-start", "date"),
    Input("date-picker-x-single-end", "date"),
)
def update_initial_range(start_date, end_date):
    if start_date is None or end_date is None:
        return None, None, None, None, True, None

    df = create_df(start_date, end_date)
    min_date = df["Date"].min()
    max_date = df["Date"].max()

    return min_date, max_date, min_date, max_date, False, df.to_dict("records")


def create_df(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    values = np.random.randn(len(dates)).cumsum()

    df = pd.DataFrame({
        "Date": dates,
        "Value": values,
    })
    return df


@app.callback(
    Output("date-picker-x-graph", "figure"),
    Input("date-picker-x-range", "start_date"), Input("date-picker-x-range", "end_date"),
    State("date-picker-x-stored-data", "data"),
)
def update_graph(start_date, end_date, stored_data):
    if start_date is None or end_date is None or stored_data is None:
        return {}

    df = pd.DataFrame(stored_data)
    dff = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    fig = px.line(dff, x="Date", y="Value", title="Values Over Time")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
