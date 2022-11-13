import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash, html, dcc, Input, Output, dash_table, ctx
import plotly.express as px

DATA_TABLE_COLUMNS = [
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
    "css": [
        {
            "selector": ".Select-value",
            "rule": "padding-right: 22px",
        },  # makes space for the dropdown caret
        {"selector": ".dropdown", "rule": "position: static"},  # makes dropdown visible
    ],
}

# Default new row for datatable
new_task_line = {
    "Task": "",
    "Start": "2016-01-01",
    "Duration": 0,
    "Resource": "A",
    "Finish": "2016-01-01",
}
df_new_task_line = pd.DataFrame(new_task_line, index=[0])


def get_default_table():
    return pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/GanttChart.csv"
    )


def add_finish_column(timeline_df: pd.DataFrame):
    """
    This function is creates 'Finish' column which is a required column for timeline chart.
    """
    timeline_df["Start"] = pd.to_datetime(timeline_df["Start"])
    timeline_df["Duration"] = timeline_df["Duration"].astype(int)
    timeline_df["Finish"] = timeline_df["Start"] + pd.to_timedelta(
        timeline_df["Duration"], unit="D"
    )
    timeline_df["Start"] = pd.to_datetime(timeline_df["Start"]).dt.date
    timeline_df["Finish"] = pd.to_datetime(timeline_df["Finish"]).dt.date
    return timeline_df


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SPACELAB],
    suppress_callback_exceptions=True,
    prevent_initial_callbacks=True,
)

app.layout = dbc.Container(
    [
        html.H1("Project Time Line", className="bg-primary text-white p-1 text-center"),
        dbc.Button(
            "Add task", n_clicks=0, id="timeline-gantt-x-add-row-btn", size="sm"
        ),
        dash_table.DataTable(
            id="timeline-gantt-x-user-datatable",
            sort_action="native",
            columns=DATA_TABLE_COLUMNS,
            data=get_default_table().to_dict("records"),
            editable=True,
            dropdown={
                "Resource": {
                    "clearable": False,
                    "options": [{"label": i, "value": i} for i in ["A", "B", "C", "D"]],
                },
            },
            css=DATA_TABLE_STYLE.get("css"),
            page_size=10,
            row_deletable=True,
            style_data_conditional=DATA_TABLE_STYLE.get("style_data_conditional"),
            style_header=DATA_TABLE_STYLE.get("style_header"),
        ),
        dcc.Graph(id="timeline-gantt-x-gantt-graph"),
    ],
    fluid=True,
)


def create_gantt_chart(updated_table_as_df):
    gantt_fig = px.timeline(
        updated_table_as_df,
        x_start="Start",
        x_end="Finish",
        y="Task",
        color="Resource",
        title="Project Plan Gantt Chart",
    )

    gantt_fig.update_layout(
        title_x=0.5,
        font=dict(size=16),
        yaxis=dict(
            title="Task",
            automargin=True,
            autorange="reversed",
            categoryorder="array",
            categoryarray=updated_table_as_df["Task"],
        ),  # sorting gantt according to datatable
        xaxis=dict(title=""),
    )
    gantt_fig.update_traces(width=0.7)

    return gantt_fig


@app.callback(
    Output("timeline-gantt-x-user-datatable", "data"),
    Output("timeline-gantt-x-gantt-graph", "figure"),
    Input("timeline-gantt-x-user-datatable", "derived_virtual_data"),
    Input("timeline-gantt-x-add-row-btn", "n_clicks"),
)
def update_table_and_figure(user_datatable: None or list, _):
    # if user deleted all rows, return the default row:
    if not user_datatable:
        updated_table = df_new_task_line

    # if button clicked, then add a row
    elif ctx.triggered_id == "timeline-gantt-x-add-row-btn":
        updated_table = pd.concat([pd.DataFrame(user_datatable), df_new_task_line])

    else:
        updated_table = pd.DataFrame(user_datatable)

    updated_table_as_df = add_finish_column(updated_table)
    gantt_chart = create_gantt_chart(updated_table_as_df)

    return updated_table_as_df.to_dict("records"), gantt_chart


if __name__ == "__main__":
    app.run_server(debug=True)
