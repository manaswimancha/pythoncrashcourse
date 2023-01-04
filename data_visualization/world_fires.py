import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data_visualization/data/world_fires_1_day.csv"

mags, lons, lats = [], [], []

with open(filename) as f:
    col = csv.reader(f)
    header = next(col)
    for row in col:
        mags.append(float(row[2]))
        lons.append(float(row[1]))
        lats.append(float(row[0]))

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [5*mag for mag in mags],
        "color": [int(mag) for mag in mags],
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Brightness"}
    }
}]

my_layout = Layout(title="World Fires")
fig = {"data":data,"layout":my_layout}
offline.plot(fig,filename="world_fires.html")