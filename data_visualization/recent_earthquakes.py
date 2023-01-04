import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data_visualization/data/all_week.json"

with open(filename,encoding="utf-8") as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

c_t = all_eq_data["metadata"]["title"]

mags, lons, lats, titles = [], [], [], []

mags = [eq_dict["properties"]["mag"] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"] != None]
lons = [eq_dict["geometry"]["coordinates"][0] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"] != None]
lats = [eq_dict["geometry"]["coordinates"][1] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"] != None]
titles = [eq_dict["properties"]["title"] for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"] != None]

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": titles,
    "marker": {
        "size": [5*mag if mag > 0 else 0 for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]

my_layout = Layout(title=c_t)
fig = {"data":data,"layout":my_layout}
offline.plot(fig,filename="global_earthquakes.html")