import dash_bootstrap_components as dbc
import pandas as pd
import plotly.figure_factory
from dash import Dash, html, dcc, Input, Output, dash_table, ctx
import plotly.express as px

DATA_TABLE_SCHEMA = [
    {
        'id': 'Task',
        'name': 'Task',
        'type': 'text',
    }, {
        'id': 'Duration',
        'name': 'Duration of task',
        'type': 'numeric',
    }, {
        'id': 'Resource',
        'name': 'Resource',
        'type': 'text'
    }, {
        'id': 'Start',
        'name': 'Start time of task',
        'type': 'datetime'
    }, {
        'id': 'Finish',
        'name': 'End time of task',
        'type': 'datetime',
        "editable": False
    },
]

DATA_TABLE_STYLE = {
    'style_data_conditional': [{'backgroundColor': '#EEF2F7', 'maxWidth': '60%'},
                               {"if": {"column_id": "Finish"}, "backgroundColor": "#eee"}],
    'style_header': {'color': 'white', 'backgroundColor': '#799DBF', 'fontWeight': 'bold'},
    'style_table': {'width': '93%', 'marginLeft': '3%', "overflowX": "auto"},
}


def __add_finish_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function is used for creating 'Finish' column which is a required column for gantt chart.
    """
    df['Start'] = pd.to_datetime(df['Start'])
    df['Duration'] = df['Duration'].astype(int)
    df['Finish'] = df['Start'] + pd.to_timedelta(df['Duration'], unit='D')
    df['Start'] = pd.to_datetime(df['Start']).dt.date
    df['Finish'] = pd.to_datetime(df['Finish']).dt.date
    return df


# Make data as a dataframe
def __get_default_table() -> pd.DataFrame:
    """
    This function import the csv file into a DataFrame.
    The dataset located in https://github.com/plotly/datasets/blob/master/GanttChart.csv
    """

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/GanttChart.csv')
    return __add_finish_column(df)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB], suppress_callback_exceptions=True,
           prevent_initial_callbacks=True)

new_task_line = {"Task": "Task 1", "Start": '2016-01-01', "Duration": 0, "Resource": "A", "Finish": '2016-01-01'}
df_new_task_line = pd.DataFrame(new_task_line, index=[0])

app.layout = dbc.Container(
    [
        html.H1("Project Time Line", className="bg-primary text-white p-1 text-center"),
        dash_table.DataTable(
            id="user-datatable",
            sort_action="native",
            columns=DATA_TABLE_SCHEMA,
            data=__get_default_table().to_dict("records"),
            editable=True,
            dropdown={
                'Resource': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in list(map(chr, range(65, 91)))
                    ]
                },
            },
            row_deletable=True,
            style_data_conditional=DATA_TABLE_STYLE.get('style_data_conditional'),
            style_header=DATA_TABLE_STYLE.get('style_header'),
            style_table=DATA_TABLE_STYLE.get('style_table'),
        ),

        dbc.Button("+", n_clicks=0, id="add-row-btn", style={'marginLeft': '3%'}),  # if user want to add a row

        html.Hr(),
        dcc.Graph(id="gantt-graph"),
    ],
    fluid=True,
    style={'backgroundColor': '#DDE6EF'}
)


def update_datatable(user_datatable) -> pd.DataFrame:
    # if user deleted all rows, return the default table:
    if not user_datatable:
        updated_table = pd.DataFrame.from_records(df_new_task_line)

    # add a row
    elif ctx.triggered_id == "add-row-btn":
        updated_table = pd.concat(
            [pd.DataFrame(user_datatable), pd.DataFrame.from_records(df_new_task_line)])
    # update datatable
    else:
        updated_table = pd.DataFrame(user_datatable)
    return __add_finish_column(updated_table)  # create the 'Finish' column for the gantt chart


def create_gantt_chart(updated_table_as_df):
    gantt_fig = plotly.figure_factory.create_gantt(  # Cresting the gantt chart
        updated_table_as_df,
        index_col="Resource",
        colors=px.colors.qualitative.Alphabet,
        show_colorbar=True,
        group_tasks=True,
        showgrid_x=False,
        showgrid_y=True,
        bar_width=0.5,
        title='Project Plan Gantt Chart'
    )
    gantt_fig.update_layout(
        paper_bgcolor="#DDE6EF",
        title_x=0.5,
        font=dict(
            size=20,
            color="#104870")
    ),
    return gantt_fig


@app.callback(
    Output("user-datatable", "data"),
    Output("gantt-graph", "figure"),
    Input("user-datatable", "derived_virtual_data"),
    Input("add-row-btn", "n_clicks"),
)
def update_table_and_figure(user_datatable: None or list, n_clicks) -> (list, dict, dict):
    """
    This callback function returns both DataTable and Gantt Chart.
    """
    updated_table_as_df = update_datatable(user_datatable)
    gantt_chart = create_gantt_chart(updated_table_as_df)
    return updated_table_as_df.to_dict("records"), gantt_chart


if __name__ == "__main__":
    app.run_server(debug=True)
