
import pandas as pd
from dash import Dash, Input, Output, callback, dcc, html, State
import plotly.express as px
import dash_bootstrap_components as dbc
from datetime import date

df = pd.read_table('https://raw.githubusercontent.com/plotly/datasets/master/global_super_store_orders.tsv')

df['profit_derived'] = df['Profit'].str.replace(',', '.').astype('float')
df['ship_date'] = pd.to_datetime(df['Ship Date'])

# Hierarchical charts work only with positive aggregate values
# In this step, we ensure that aggregated values will be positive
df = df.query(expr="profit_derived >= 0")

df = df[['profit_derived', 'Segment', 'Region', 'ship_date']]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([

    html.H4('Distribution of profit as per business segment and region'),

    dbc.NavbarSimple(
        children=[],
        brand="Dash is awesom!",
        brand_href="#",
        color="primary",
        dark=True
    ),

    html.Br(),
    html.Br(),

    # ------------------------------------------------- #
    # Modal
    html.Div(
        [
            dbc.Button("Open modal", id="modal_treemap_open", n_clicks=0),
            dbc.Modal(
                [
                    dbc.ModalHeader(dbc.ModalTitle("Filters")),
                    dbc.ModalBody([

                        # Filter within dbc Modal
                        html.Label('Regions'),
                        dcc.Dropdown(
                            id='modal_treemap_dynamic_callback_dropdown_region',
                            options=[{'label': x, 'value': x} for x in sorted(df['Region'].unique())],
                            multi=True
                        ),
                        html.Br(),
                        html.Label('Ship Date'),
                        dcc.DatePickerRange(
                            id='modal_treemap_my-date-picker-range',
                            min_date_allowed=date(1995, 8, 5),
                            max_date_allowed=date(2017, 9, 19),
                            # initial_visible_month=date(2017, 8, 5),
                            end_date=date(2017, 8, 25),
                            start_date=date(2012, 1, 20)
                        )

                    ]),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close", id="modal_treemap_close", className="ms-auto", n_clicks=0
                        )
                    ),
                ],
                id="modal_treemap_modal",
                is_open=False,
            ),
        ]
    ),
    # ------------------------------------------------- #

    html.Br(),
    html.Br(),

    # ---------------------------------------- #
    # Tabs
    dcc.Tabs(id='modal_treemap_tab',
             value='treemap',
             children=[
                 dcc.Tab(label='Treemap', value='treemap'),
                 dcc.Tab(label='Sunburst', value='sunburst')
             ]),
    html.Div(id='modal_treemap_tabs-content'),

    # dcc.Graph(
    #     id='modal_treemap_line_chart'
    # ),
    # Tabs
    # ---------------------------------------- #

    html.Br(),
    html.Br()

],
    fluid=True
)


@callback(
    Output('modal_treemap_tabs-content', 'children'),
    Input('modal_treemap_dynamic_callback_dropdown_region', 'value'),
    Input('modal_treemap_tab', 'value'),
    Input('modal_treemap_my-date-picker-range', 'start_date'),
    Input('modal_treemap_my-date-picker-range', 'end_date')
)
def main_callback_logic(
        region,
        tab,
        start_date,
        end_date
):
    dff = df.copy()

    print('-----------------------')
    print(start_date)
    print(end_date)
    print('-------------')

    # if region is not None:
    if region is not None and len(region) > 0:
        dff = dff.query('Region == @region')

    if start_date is not None:
        dff = dff.query("ship_date > @start_date")
    if end_date is not None:
        dff = dff.query("ship_date < @end_date")

    dff = dff.groupby(by=['Segment', 'Region']).sum().reset_index()

    if tab == 'treemap':
        fig = px.treemap(dff, path=[px.Constant("all"), 'Segment', 'Region'], values='profit_derived')
    elif tab == 'sunburst':
        fig = px.sunburst(dff, path=[px.Constant("all"), 'Segment', 'Region'], values='profit_derived')

    # fig = px.treemap(dff, path=[px.Constant("all"), 'Segment', 'Region'], values='profit_derived')
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

    return dcc.Graph(figure=fig)


@callback(
    Output("modal_treemap_modal", "is_open"),
    Input("modal_treemap_open", "n_clicks"),
    Input("modal_treemap_close", "n_clicks"),
    State("modal_treemap_modal", "is_open"),
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server()


