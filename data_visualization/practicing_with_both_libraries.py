# RandomWalk on Plotly

import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk(1000)
rw.fill_walk()

fig = px.scatter(x=rw.x_values,y=rw.y_values)
fig.update_xaxes(showgrid=False,zeroline=False,visible=False)
fig.update_yaxes(showgrid=False,zeroline=False,visible=False)
fig.show()

# Die Roll on Matplotlib

import matplotlib.pyplot as plt
from die import Die

die = Die()

results = [die.roll() for i in range(1000)]
frequencies = [results.count(i) for i in range(1,7)]
x_values = [i for i in range(1,7)]

plt.bar(x_values,frequencies)
plt.title("Die Roll")
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()