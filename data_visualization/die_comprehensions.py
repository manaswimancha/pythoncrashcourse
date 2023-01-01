# # List comprehension for 2_d8s.py

# from plotly.graph_objs import Bar, Layout
# from plotly import offline
# from die import Die

# die_1 = Die(8)
# die_2 = Die(8)

# results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# frequencies = [results.count(value) for value in range(2,die_1.num_sides + die_2.num_sides + 1)]

# x_values = [i for i in range(2,die_1.num_sides + die_2.num_sides + 1)]

# data = [Bar(x=x_values,y=frequencies)]

# x_axis_config = {"title":"Result","dtick":1}
# y_axis_config = {"title":"Frequency of Result"}
# my_layout = Layout(title="Results of rolling 2 D8 dice 1,000 times",xaxis=x_axis_config,yaxis=y_axis_config)
# offline.plot({"data":data,"layout":my_layout},filename="2_d8s.html")

# # List comprehension for 3_dice.py

# from plotly.graph_objs import Bar, Layout
# from plotly import offline
# from die import Die

# die_1 = Die()
# die_2 = Die()
# die_3 = Die()

# results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# frequencies = [results.count(value) for value in range(2,die_1.num_sides + die_2.num_sides + die_3.num_sides + 1)]

# x_values = [i for i in range(2,die_1.num_sides + die_2.num_sides + die_3.num_sides + 1)]

# data = [Bar(x=x_values,y=frequencies)]

# x_axis_config = {"title":"Result","dtick":1}
# y_axis_config = {"title":"Frequency of Result"}
# my_layout = Layout(title="Results of rolling 3 D6 dice 1,000 times",xaxis=x_axis_config,yaxis=y_axis_config)
# offline.plot({"data":data,"layout":my_layout},filename="3_dice.html")

# List comprehension for multiplication.py

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()

results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(2,die_1.num_sides * die_2.num_sides + 1)]

x_values = [i for i in range(2,die_1.num_sides * die_2.num_sides + 1)]

data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {"title":"Result","dtick":1}
y_axis_config = {"title":"Frequency of Result"}
my_layout = Layout(title="Results of rolling 2 D6 dice 1,000 times (Multiplication)",xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({"data":data,"layout":my_layout},filename="multiplication.html")