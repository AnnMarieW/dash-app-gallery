deploy = """

#### Dash Enterprise Deploy
Requirements.txt:
```
Dash
gunicorn
```
Procfile:
```
web: gunicorn app:server
```

App.py:
```
from dash import Dash, html
app = Dash(__name__)
server = app.server
app.layout = html.Div('hi')

Then, push to deploy with:
 git push plotly main
```



"""