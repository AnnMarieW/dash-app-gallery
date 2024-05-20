import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Store(id="stored-data", storage_type="memory"),
        html.H1("Date Picker Example"),
        html.H2("Step 1: Select a Date Range to generate ramdom data"),
        html.P("Start Date"),
        dcc.DatePickerSingle(
            id="date-picker-single-start", clearable=True, display_format="YYYY-MM-DD"
        ),
        html.P("End Date"),
        dcc.DatePickerSingle(
            id="date-picker-single-end", clearable=True, display_format="YYYY-MM-DD"
        ),
        html.Div(
            [
                html.H2(
                    "Step 2: Use the Date Picker Range to filter the data (within the date range) and update the graph"
                ),
                dcc.DatePickerRange(
                    id="date-picker-range",
                    display_format="YYYY-MM-DD",
                ),
                dcc.Graph(id="graph"),
            ],
            hidden=True,
            id="graph-container",
        ),
    ]
)

# create a callback for when either date picker single is changed, and create a new dataframe
@app.callback(
    Output("date-picker-range", "start_date"),
    Output("date-picker-range", "end_date"),
    Output("date-picker-range", "min_date_allowed"),
    Output("date-picker-range", "max_date_allowed"),
    Output(
        "graph-container", "hidden"
    ),  # update the visibility of graph-container
    Output("stored-data", "data"),
    [
        Input("date-picker-single-start", "date"),
        Input("date-picker-single-end", "date"),
    ],
)
def update_initial_range(start_date, end_date):
    if start_date is None or end_date is None:
        return None, None, None, None, True, None
    df = create_df(start_date, end_date)

    output = (
        df["Date"].min(),
        df["Date"].max(),
        df["Date"].min(),
        df["Date"].max(),
        False,
        df.to_dict(orient="records"),
    )

    return output


def create_df(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date, freq="D")
    values = np.random.randn(
        (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days + 1
    ).cumsum()

    print(len(dates), len(values))
    assert len(dates) == len(values)
    df = pd.DataFrame(
        {
            "Date": pd.date_range(start=start_date, end=end_date, freq="D"),
            "Value": np.random.randn(
                (pd.to_datetime(end_date) - pd.to_datetime(start_date)).days + 1
            ).cumsum(),
        }
    )
    return df


@app.callback(
    Output("graph", "figure"),
    [Input("date-picker-range", "start_date"), Input("date-picker-range", "end_date")],
    [State("stored-data", "data")],
)
def update_graph(start_date, end_date, stored_data):
    if start_date is None or end_date is None or stored_data is None:
        return {}

    df = pd.DataFrame(stored_data)

    # Filter the data based on the selected date range
    filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

    # Create the plotly figure
    fig = px.line(filtered_df, x="Date", y="Value", title="Values Over Time")

    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
