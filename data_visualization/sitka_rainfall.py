# Precipitation for Sitka

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/sitka_weather_2018_simple.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    prcp = []
    for row in reader:
        date.append(datetime.strptime(row[2],"%Y-%m-%d"))
        prcp.append(float(row[3]))

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(date,prcp,c="red")
plt.title("Daily Precipitation 2018",fontsize=24)
plt.xlabel("Date",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipation (cm)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()

# Precipitation for Death Valley

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/death_valley_2018_simple.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    prcp = []
    for row in reader:
        date.append(datetime.strptime(row[2],"%Y-%m-%d"))
        prcp.append(float(row[3]))

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(date,prcp,c="red")
plt.title("Daily Precipitation 2018",fontsize=24)
plt.xlabel("Date",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipation (cm)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()
