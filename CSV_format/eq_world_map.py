import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = 'CSV_format/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lats, lons, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lat = eq_dict['geometry']['coordinates'][1]
    lon = eq_dict['geometry']['coordinates'][0]
    title = eq_dict['properties']['title']
    hover_texts.append(title)
    lats.append(lat)
    lons.append(lon)
    mags.append(mag)


#Нанесение данных на карту 
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [mag*5 for mag in mags],
        'color': mags,
        'colorscale': 'Bluered',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    }
}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')