basic = """```python
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length')

df = px.data.stocks()
fig = px.line(df, x='date', y='GOOG')

df = px.data.medals_long()
fig = px.bar(df, x='nation', y='count', color='medal')

df = px.data.medals_long()
fig = px.area(df, x='medal', y='count', color='nation')

df = px.data.tips()
fig = px.pie(df, values='tip', names='day')

df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'], values='total_bill')

df = px.data.tips()
fig = px.sunburst(df, path=['day', 'time', 'sex'],values='total_bill')

df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color='lightgrey')
```"""

statistical = """```python
df = px.data.tips()
fig = px.density_heatmap(df, x='total_bill', y='tip')

df = px.data.tips()
fig = px.histogram(df, x='total_bill')

df = px.data.tips()
fig=px.parallel_categories(df)

df = px.data.tips()
fig = px.box(df, x='time', y='total_bill')

df = px.data.iris()
fig = px.scatter_matrix(df)

df = px.data.tips()
fig = px.violin(df, y='total_bill', box=True)

df = px.data.tips()
fig = px.strip(df, x='total_bill', y='day')
```"""

scientific = """```
df = px.data.medals_wide(indexed=True)
fig = px.imshow(df)

from skimage import data
img = data.astronaut()
fig = px.imshow(img, binary_format='jpeg', binary_compression_level=0)

df = px.data.election()
fig = px.scatter_ternary(df, a='Joly', b='Coderre', c='Bergeron')

df = px.data.wind()
fig = px.scatter_polar(df, r='frequency', theta='direction')

df = pd.DataFrame(dict(r=[1, 5, 2, 2, 3], theta=['processing cost', 'mechanical properties', 'chemical stability', 'thermal stability', 'device integration']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)

df = px.data.iris()
fig = px.parallel_coordinates(df, color='species_id')
```"""

maps = """```python
df = px.data.election()
geojson = px.data.election_geojson()
fig = px.choropleth_mapbox(df, geojson=geojson, color='Bergeron', locations='district', featureidkey='properties.district',center={'lat': 45.5517, 'lon': -73.7073},  mapbox_style='carto-positron', zoom=9)

df = px.data.gapminder().query('year==2007')
fig = px.scatter_geo(df, locations='iso_alpha', color='continent', hover_name='country', size='pop', projection='natural earth')

df = pd.read_csv( 'https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv')
fig = px.scatter_mapbox(df, lat='lat', lon='lon', hover_name='City', hover_data=['State', 'Population'], zoom=3, height=600)
fig.update_layout(mapbox_style='open-street-map')

df = px.data.gapminder().query('year==2007')
fig = px.line_geo(df, locations='iso_alpha', color='continent', projection='orthographic')

df = pd.read_csv( 'https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10, center=dict(lat=0, lon=180), zoom=0, mapbox_style='stamen-terrain')

```"""
