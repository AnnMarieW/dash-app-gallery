from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import spacy
from spacy import displacy
import os
os.system("python -m spacy download en_core_web_sm")

"""
Named entity recognition (NER)is probably the first step towards information extraction 
that seeks to locate and classify named entities in text into pre-defined categories 
such as the names of persons, organizations, locations, expressions of times, quantities, 
monetary values, percentages, etc. 
NER is used in many fields in Natural Language Processing (NLP)
and it can help answering many real-world questions

There are many libraries that supports NER, spacy, NLTK etc. Here we are developing the app using Spacy
"""

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# python -m spacy download [model] - Here we are using small model
nlp = spacy.load("en_core_web_sm")

app.layout = html.Div([dbc.Container(
    [
        html.Div([dcc.Markdown(
            """
            # * Enter `text` to visualize the ```entities``` with tool-tip 📝 🔖  *
        """, style={'width': '100 %', 'display': 'flex', 'color': 'white', 'align-items': 'center', 'justify-content': 'center', 'padding-top': '40px', 'padding-bottom': '20px'}
        )]),
        dbc.Textarea(
            id='textarea-state-example',
            value='I went to Georgia with 100 Dollars',
            style={'width': '100%', 'height': 200, 'margin-bottom': '20px'},
        ),
        html.Div(dbc.Button('Get Entities 🪄', id='textarea-state-example-button',
                            className="btn btn-secondary", n_clicks=0), style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        html.Div(id="textarea-state-example-output"
                 )
    ]
)], style={'height': '100vh', 'background-image': 'linear-gradient(to right, #051421, #042727)', 'margin': '0', 'scroll-behavior': 'smooth', 'position': 'sticky', 'overflow': 'hidden', 'justify': 'center'}
)


def get_entities(doc):
    final_entities = []
    for ent in doc.ents:
        final_entities.append(
            html.Div([dbc.Alert(
                [
                    html.I(className="bi bi-info-circle-fill me-2"),
                    f'\t Text: {ent.text}\t \t \t ⌛️ \t  Label: {ent.label_}',
                ],
                color="info",
                id=f'{ent.text}',
                className="d-flex align-items-center",
            ),
                html.Div(id='break-space', style={'margin-top': '10px'}),
                dbc.Tooltip(f'Span: {ent.start_char} --> {ent.end_char}', target=f'{ent.text}')])
        )
    return final_entities


@ app.callback(
    Output('textarea-state-example-output', 'children'),
    Input('textarea-state-example-button', 'n_clicks'),
    State('textarea-state-example', 'value')


)
def update_output(n_clicks, value):
    if n_clicks > 0 and value:
        doc = nlp(value)
        # Visualize spaCy's guess at the syntactic structure of a sentence. Arrows point from children to heads, and are labelled by their relation type.
        # https://spacy.io/universe/project/displacy
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        final_entities = get_entities(doc)
        return [
            dbc.Container([
                dcc.Markdown(ent_html, dangerously_allow_html=True,
                             style={'margin-top': '30px', 'color': 'white', 'margin-bottom': '10px'}),
                html.Div(final_entities, style={'color': 'white'})
            ])

        ]


if __name__ == '__main__':
    app.run_server(debug=True)
