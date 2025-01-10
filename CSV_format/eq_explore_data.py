import json

filename = 'CSV_format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
mags, lats, lons = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lat = eq_dict['geometry']['coordinates'][1]
    lon = eq_dict['geometry']['coordinates'][0]
    lats.append(lat)
    lons.append(lon)
    mags.append(mag)

print(mags[:10])
print(lons[:5])
print(lats[:5])


