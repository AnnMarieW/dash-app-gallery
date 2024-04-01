from dash import Dash, dcc, html, Input, Output, callback, clientside_callback
import json

"""
For more information see https://visjs.github.io/vis-timeline/docs/timeline/
"""

app = Dash(
    __name__,
    external_stylesheets=[
       'https://unpkg.com/vis-timeline@latest/styles/vis-timeline-graph2d.min.css',
    ],
    external_scripts=[
       'https://unpkg.com/vis-timeline@latest/standalone/umd/vis-timeline-graph2d.min.js',
    ]
)

timeline_data = [
    {"id": 1, "content": "item 1", "start": "2024-04-20"},
    {"id": 2, "content": "item 2", "start": "2024-04-14"},
    {"id": 3, "content": "item 3", "start": "2024-04-18"},
    {"id": 4, "content": "item 4", "start": "2024-04-16", "end": "2014-04-19"},
    {"id": 5, "content": "item 5", "start": "2024-04-25"},
    {"id": 6, "content": "item 6", "start": "2024-04-27", "type": "point"},
]

app.layout = html.Div(
    [

        dcc.Store(id="vis-timeline-store-items", data=timeline_data),
        dcc.Store(id="vis-timeline-store-selected"),
        dcc.Markdown(
            """
            ### Custom Component:  Vis.js Timeline
            
            This is an example of how to add a custom component JavaScript component to your Dash app. This [Vis.js Timeline](https://visjs.github.io/vis-timeline/docs/timeline/)
             component uses `set_props` in a clientside callbacks to update a `dcc.Store` component when you click on
              an item. This enables the custom component to trigger Dash callbacks.    
            
            __Select an item on the timeline:__            
            """
        ),
        html.Div(id="vis-timeline-graph"),
        html.Div(id="vis-timeline-output-container")
    ]
)

clientside_callback(
    """(id, items) => {

        var container = document.getElementById(id);

        // Create a DataSet (allows two way data-binding)
        var items = new vis.DataSet(items);

        // Configuration for the Timeline
        var options = {};

        // Create a Timeline
        var timeline = new vis.Timeline(container, items, options);

        timeline.on("select", function (properties) {
            dash_clientside.set_props("vis-timeline-store-selected", {data: JSON.stringify(properties)})    
        });

        return dash_clientside.no_update;
    }""",
    Output('vis-timeline-graph', 'id'),
    Input('vis-timeline-graph', 'id'),
    Input('vis-timeline-store-items', 'data')
)


@callback(
    Output("vis-timeline-output-container", "children"),
    Input("vis-timeline-store-selected", "data")
)
def display_data(data):
    if data:
        data = json.loads(data)
        item_number = data["items"][0]
        return f"You selected: {timeline_data[item_number-1]}"
    return "Select an item"


if __name__ == "__main__":
    app.run(debug=True)
