import pandas
import pandas as pd
import plotly.figure_factory
from dash import Dash, html, dcc, Input, Output, dash_table, ctx

APP_TOP_MARGIN = {
    'text-align': 'center'}

DATA_TABLE_SCHEMA = [{
    'id': 'Task',
    'name': 'Task',
    'type': 'text'
}, {
    'id': 'Start',
    'name': 'Start time of task',
    'type': 'datetime'},
    {
        'id': 'Duration',
        'name': 'Duration of task',
        'type': 'numeric',
    }, {
        'id': 'Resource',
        'name': 'Resource',
        'type': 'text'
    }]


def add_finish_column(df: pandas.DataFrame) -> pandas.DataFrame:
    """
    This function is used for creating 'Finish' column which is a required column for gantt chart.
    """
    df['Start'] = pd.to_datetime(df['Start'])
    df['Duration'] = df['Duration'].astype(int)
    df['Finish'] = df['Start'] + pd.to_timedelta(df['Duration'], unit='D')
    df['Start'] = pd.to_datetime(df['Start']).dt.date
    return df


# Make data as a dataframe
def get_default_csv_file() -> pandas.DataFrame:
    """
    This function import the csv file into a DataFrame.
    The dataset located in https://github.com/plotly/datasets/blob/master/GanttChart.csv
    """

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/GanttChart.csv')
    return add_finish_column(df)


app = Dash(__name__, suppress_callback_exceptions=True)
app.title = 'Time Chart App'

new_order_line = {"Task": "", "Start": '2016-01-01', "Duration": 0, "Resource": "", "Finish": 1 / 1 / 2000}
df_new_order_line = pd.DataFrame(new_order_line, index=[0])

app.layout = html.Div(
    [
        html.H1("Project TimeLine", className="bg-primary text-white p-1", style=APP_TOP_MARGIN),
        html.Button("+", n_clicks=0, id="add-btn"),
        dash_table.DataTable(
            id="user-datatable",
            sort_action="native",
            columns=DATA_TABLE_SCHEMA,
            editable=True,
            row_deletable=True,
        ),
        html.H3("Project Time Chart", style=APP_TOP_MARGIN),
        dcc.Graph(id="graph"),
    ],
)


@app.callback(
    Output("user-datatable", "data"),
    Output("graph", "figure"),
    Input("user-datatable", "derived_virtual_data"),
    Input("add-btn", "n_clicks"),
)
def update_table_and_figure(user_datatable: None or list, n_clicks) -> (list, dict):
    # initialize table when app starts
    if user_datatable is None:
        updated_table = get_default_csv_file()

    # if user deleted all rows, add a default row:
    elif not user_datatable:
        updated_table = get_default_csv_file()

    # convert table data to DataFrame
    else:
        updated_table = pd.DataFrame(user_datatable)

    # add a row
    if ctx.triggered_id == "add-btn":
        updated_table = pd.concat(
            [updated_table, pd.DataFrame.from_records(updated_table)]
        )

    updated_table = add_finish_column(updated_table)

    fig = plotly.figure_factory.create_gantt(
        updated_table,
        index_col="Resource",
        show_colorbar=True,
        group_tasks=True,
        showgrid_x=False,
        showgrid_y=True,
        bar_width=0.5,
    )

    return updated_table.to_dict("records"), fig


if __name__ == "__main__":
    app.run_server(debug=True)
