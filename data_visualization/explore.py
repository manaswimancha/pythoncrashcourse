# Precipitation for NY

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/3187209.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    prcp = []
    for row in reader:
        date.append(datetime.strptime(row[header.index("DATE")],"%Y-%m-%d"))
        prcp.append(float(row[header.index("PRCP")]))

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(date,prcp,c="red")
plt.title("Daily Precipitation 2018",fontsize=24)
plt.xlabel("Date",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipation (cm)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()

# Temperatures for NY

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/3187209.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    high = []
    low = []
    for row in reader:
        date.append(datetime.strptime(row[header.index("DATE")],"%Y-%m-%d"))
        high.append(float(row[header.index("TMAX")]))
        low.append(float(row[header.index("TMIN")]))

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(date,high,color="blue")
ax.plot(date,low,color="red")
ax.fill_between(date,high,low,color="blue",alpha=0.1)
plt.title("Daily Temperatures 2018",fontsize=24)
plt.xlabel("Date",fontsize=16)
fig.autofmt_xdate()
ax.set_ylim([0, 150])
plt.ylabel("Temperature (cm)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)

plt.show()