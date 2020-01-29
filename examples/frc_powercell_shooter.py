from freefall.falling_objects import frc_power_cell
from freefall.simulators import simulate_earth_surface
from freefall.utilities import find_vx_vy, float_range

import matplotlib.pyplot as plt

X_INITIAL = 0       # m
Y_INITIAL = 27/40   # m
SPEED = 10          # m/s
ANGLE = 50          # degrees

fig, ax = plt.subplots()

for i in float_range(2, 7, 0.1):
    vx_initial, vy_initial = find_vx_vy(speed=i, angle=ANGLE)
    results = simulate_earth_surface(frc_power_cell, X_INITIAL, Y_INITIAL, vx_initial, vy_initial)

    # Plot the results
    ax.plot(results.x, results.y)

# Format and annotate the graph
ax.grid()
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Simulation of Power Cell Free Fall")

# Display the graph
plt.show()
