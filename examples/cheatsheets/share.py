deploy = """

#### Dash Tools

`pip install dash-tools`  

See `dash-tools` getting started [documentation](https://dash-tools.readthedocs.io/en/latest/getting%20started.html)

```
dashtools init MyApp
dashtools heroku --deploy
dashtools heroku --update



```

--------------
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