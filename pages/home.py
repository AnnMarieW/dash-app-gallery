# import dash
# from dash import html, dcc
# import uuid
# import random
# import dash_bootstrap_components as dbc
#
# rd = random.Random(0)
#
# dash.register_page(__name__, description="Sample Dash Apps", path="/")
#
#
# def make_card(page):
#     tooltip_id = str(uuid.UUID(int=rd.randint(0, 2 ** 128)))
#     return dbc.Card(
#         [
#             dbc.CardHeader(
#                 [
#                     dbc.NavLink(
#                         page["title"],
#                         href=page["path"],
#                     ),
#                 ]
#             ),
#             dbc.CardBody(
#                 [
#                     html.A(
#                         html.Img(src=dash.get_asset_url(page["image"]), height=200),
#                         href=page["path"],
#                         id=tooltip_id
#
#                     ),
#                     html.P(
#                         page["description"],
#                         className="card-text",
#                     ),
#                 ]
#             ),
#             dbc.Tooltip(
#                 page["description"],
#                 target=tooltip_id
#             )
#         ]
#     )
#
# def make_card_grid(cards_per_row=3):
#     row = []
#     grid = []
#     for page in dash.page_registry.values():
#         if page["path"] != "/":
#             if len(row) < cards_per_row:
#                 row.append(make_card(page))
#             if len(row) == cards_per_row:
#                 grid.append(dbc.CardGroup(row, className="mb-4"))
#                 row = []
#     grid.append(dbc.CardGroup(row))
#     return grid
#
#
# def layout():
#     return make_card_grid()
