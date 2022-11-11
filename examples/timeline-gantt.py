import dash_bootstrap_components as dbc
import pandas as pd
import plotly.figure_factory
from dash import Dash, html, dcc, Input, Output, dash_table, ctx
import plotly.express as px

DATA_TABLE_SCHEMA = [
    {
        "id": "Task",
        "name": "Task",
    },
    {
        "id": "Duration",
        "name": "Days",
        "type": "numeric",
    },
    {"id": "Resource", "name": "Resource", "presentation": "dropdown"},
    {"id": "Start", "name": "Start", "type": "datetime"},
    {"id": "Finish", "name": "End", "type": "datetime", "editable": False},
]

DATA_TABLE_STYLE = {
    "style_data_conditional": [
        {"if": {"column_id": "Finish"}, "backgroundColor": "#eee"}
    ],
    "style_header": {
        "color": "white",
        "backgroundColor": "#799DBF",
        "fontWeight": "bold",
    },
}

# Creating dict of Keys and Colors for timeline chart
resource_keys = list(map(chr, range(65, 91)))
resource_color_values = px.colors.qualitative.Alphabet
res = dict(zip(resource_keys, resource_color_values))


def add_finish_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function is used for creating 'Finish' column which is a required column for gantt chart.
    """
    df["Start"] = pd.to_datetime(df["Start"])
    df["Duration"] = df["Duration"].astype(int)
    df["Finish"] = df["Start"] + pd.to_timedelta(df["Duration"], unit="D")
    df["Start"] = pd.to_datetime(df["Start"]).dt.date
    df["Finish"] = pd.to_datetime(df["Finish"]).dt.date
    return df


def get_default_table() -> pd.DataFrame:
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/GanttChart.csv"
    )
    return add_finish_column(df)


# Default new row for datatable
new_task_line = {
    "Task": "",
    "Start": "2016-01-01",
    "Duration": 0,
    "Resource": "A",
    "Finish": "2016-01-01",
}
df_new_task_line = pd.DataFrame(new_task_line, index=[0])

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
)

app.layout = dbc.Container(
    [
        html.H1("Project Time Line", className="bg-primary text-white p-1 text-center"),
        dbc.Button("Add task", n_clicks=0, id="add-row-btn", size="sm"),
        dash_table.DataTable(
            id="user-datatable",
            sort_action="native",
            columns=DATA_TABLE_SCHEMA,
            data=get_default_table().to_dict("records"),
            editable=True,
            dropdown={  # limit num of Resource options for the user to select due to color limitation of 26
                "Resource": {
                    "clearable": False,
                    "options": [
                        {"label": i, "value": i} for i in list(map(chr, range(65, 91)))
                    ],
                },
            },
            # makes space for the dropdown caret
            css=[{"selector": ".Select-value", "rule": "padding-right: 22px"}],
            page_size=10,
            row_deletable=True,
            style_data_conditional=DATA_TABLE_STYLE.get("style_data_conditional"),
            style_header=DATA_TABLE_STYLE.get("style_header"),
            style_table=DATA_TABLE_STYLE.get("style_table"),
        ),
        dcc.Graph(id="gantt-graph"),
    ],
    fluid=True,
)


def update_datatable(user_datatable) -> pd.DataFrame:
    # if user deleted all rows, return the default table:
    if not user_datatable:
        updated_table = df_new_task_line

    # add a row
    elif ctx.triggered_id == "add-row-btn":
        updated_table = pd.concat([pd.DataFrame(user_datatable), df_new_task_line])

    else:
        updated_table = pd.DataFrame(user_datatable)
    return add_finish_column(updated_table)


def create_gantt_chart(updated_table_as_df) -> plotly.graph_objs.Figure:
    gantt_fig = px.timeline(updated_table_as_df, x_start="Start", x_end="Finish", y="Task", color="Resource",
                            color_discrete_map=res,
                            title='Project Plan Gantt Chart')

    gantt_fig.update_layout(
        title_x=0.5,
        font=dict(size=16),
        yaxis=dict(title="Task", automargin=True, autorange="reversed", categoryorder="array",
                   categoryarray=updated_table_as_df["Task"]),  # sorting gantt according to datatable
        xaxis=dict(title=""))
    gantt_fig.update_traces(width=0.7)

    return gantt_fig


@app.callback(
    Output("user-datatable", "data"),
    Output("gantt-graph", "figure"),
    Input("user-datatable", "derived_virtual_data"),
    Input("add-row-btn", "n_clicks"),
)
def update_table_and_figure(user_datatable: None or list, _) -> (list, dict):
    updated_table_as_df = update_datatable(user_datatable)
    gantt_chart = create_gantt_chart(updated_table_as_df)
    return updated_table_as_df.to_dict("records"), gantt_chart


if __name__ == "__main__":
    app.run_server(debug=True)
