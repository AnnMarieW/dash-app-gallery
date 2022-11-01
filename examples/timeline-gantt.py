import pandas
import pandas as pd
import plotly.figure_factory
from dash import Dash, html, dcc, Input, Output, dash_table

STYLE_TEXT = {
    'text-align': 'center'}


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
app.title = 'timeline-gantt'

app.layout = html.Div(
    [
        html.H1("Project TimeLine", className="bg-primary text-white p-1", style=STYLE_TEXT),
        dash_table.DataTable(
            id='user-datatable',
            columns=[{'name': i, 'id': i} for i in pd.read_csv('https://raw.githubusercontent.com/plotly/datasets'
                                                               '/master/GanttChart.csv').columns],
            editable=True,
            row_deletable=True,
        ),
        html.H3("Project Time Chart", style=STYLE_TEXT),
        dcc.Graph(id="graph"),
    ],
)


@app.callback(
    Output('user-datatable', 'data'),
    Input('user-datatable', 'data')

)
def update_store_data_of_boxes_amount_data(user_datatable: None or list) -> list:
    """
    This function save the user changes in the DataTable into the local memory of the browser using dcc.store.
    This is how it's possible to use the most update changes of the user in other Dash Components.
    """

    if user_datatable is None:
        updated_table = get_default_csv_file()

    else:
        updated_table = pd.DataFrame(user_datatable)
    updated_table = add_finish_column(updated_table)
    return updated_table.to_dict('records')


@app.callback(
    Output("graph", "figure"),
    Input('user-datatable', 'data')
)
def update_chart(datatable: list) -> plotly.graph_objs.Figure:
    return plotly.figure_factory.create_gantt(pd.DataFrame(datatable), index_col='Resource', show_colorbar=True,
                                              group_tasks=True, showgrid_x=False, showgrid_y=True, bar_width=0.5,
                                              title="")


if __name__ == "__main__":
    app.run_server(debug=True)
    dcc.Store(id='user-datatable', data={}, storage_type='local')
