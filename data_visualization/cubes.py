import matplotlib.pyplot as plt

x_vals = [x for x in range(1,6)]
cubes = [x**3 for x in range(1,6)]

x_vals_a = [x for x in range(1,5001)]
cubes_a = [x**3 for x in range(1,5001)]

plt.style.use("seaborn-darkgrid")
fig, ax = plt.subplots(2)

ax[0].plot(x_vals,cubes,linewidth=3)
ax[0].set_title("Cubes Of Numbers",fontsize=24)
ax[0].set_xlabel("Numbers",fontsize=14)
ax[0].set_ylabel("Cubes",fontsize=14)
ax[0].tick_params(axis="both",labelsize=14)

ax[1].plot(x_vals_a,cubes_a,linewidth=3)
ax[1].set_title("Cubes Of Numbers",fontsize=24)
ax[1].set_xlabel("Numbers",fontsize=14)
ax[1].set_ylabel("Cubes",fontsize=14)
ax[1].tick_params(axis="both",labelsize=14)

plt.show()