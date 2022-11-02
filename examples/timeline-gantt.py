import pandas as pd
import plotly.figure_factory
from dash import Dash, html, dcc, Input, Output, dash_table, ctx
import dash_bootstrap_components as dbc


DATA_TABLE_SCHEMA = [
    {
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
    }
]


def add_finish_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function is used for creating 'Finish' column which is a required column for gantt chart.
    """
    df['Start'] = pd.to_datetime(df['Start'])
    df['Duration'] = df['Duration'].astype(int)
    df['Finish'] = df['Start'] + pd.to_timedelta(df['Duration'], unit='D')
    df['Start'] = pd.to_datetime(df['Start']).dt.date
    return df


# Make data as a dataframe
def get_default_table() -> pd.DataFrame:
    """
    This function import the csv file into a DataFrame.
    The dataset located in https://github.com/plotly/datasets/blob/master/GanttChart.csv
    """

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/GanttChart.csv')
    return add_finish_column(df)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], suppress_callback_exceptions=True)

new_task_line = {"Task": "", "Start": '2016-01-01', "Duration": 0, "Resource": "", "Finish": '2016-01-01'}
df_new_task_line = pd.DataFrame(new_task_line, index=[0])

app.layout = html.Div(
    [
        html.H1("Project TimeLine", className="bg-primary text-white p-1 text-center"),
        dash_table.DataTable(
            id="user-datatable",
            sort_action="native",
            columns=DATA_TABLE_SCHEMA,
            editable=True,
            row_deletable=True,
            style_data_conditional=[{'backgroundColor': 'bg-primary'},
                                    ],
            style_header={
                'backgroundColor': 'bg-primary bg-gradient text-white py-4',
                'fontWeight': 'bold'
            },

        ),
        html.Button("Add Row", n_clicks=0, id="add-btn"),  # if user want to add a row

        html.H3("Project Time Chart", className="bg-light text-blue p-1 text-center"),
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
    """
    This callback function returns both DataTable and Gantt Chart.
    According to the user action a row can be added, restored the default table or just update the content of the
    datatable (which will also update the gantt chart).
    """
    # initialize table when app starts
    if user_datatable is None:
        updated_table = get_default_table()

    # if user deleted all rows, return the default table:
    elif not user_datatable:
        updated_table = get_default_table()

    # just convert table data to DataFrame
    else:
        updated_table = pd.DataFrame(user_datatable)

    # add a row
    if ctx.triggered_id == "add-btn":
        updated_table = pd.concat(
            [pd.DataFrame(user_datatable), pd.DataFrame.from_records(df_new_task_line)]
        )

    updated_table_as_df = add_finish_column(updated_table)  # create the 'Finish' column for the gantt chart

    fig = plotly.figure_factory.create_gantt(
        updated_table_as_df,
        index_col="Resource",
        show_colorbar=True,
        group_tasks=True,
        showgrid_x=False,
        showgrid_y=True,
        bar_width=0.5,
    )

    return updated_table_as_df.to_dict("records"), fig


if __name__ == "__main__":
    app.run_server(debug=True)
