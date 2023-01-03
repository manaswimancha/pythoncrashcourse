# Temperature for Sitka

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/sitka_weather_2018_simple.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    high = []
    low = []
    for row in reader:
        date.append(datetime.strptime(row[2],"%Y-%m-%d"))
        high.append(float(row[5]))
        low.append(float(row[6]))

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

# Temperature for Death Valley

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

with open("data_visualization/data/death_valley_2018_simple.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    date = []
    high = []
    low = []
    for row in reader:
        try:
            high.append(float(row[4]))
            low.append(float(row[5]))
            date.append(datetime.strptime(row[2],"%Y-%m-%d"))
        except ValueError:
            continue

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