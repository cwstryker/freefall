from freefall.falling_objects import frc_power_cell
from freefall.simulators import simulate_earth_surface

import matplotlib.pyplot as plt


X_INITIAL = 0  # m
Y_INITIAL = 6.172  # m
VX_INITIAL = 0  # m/s
VY_INITIAL = 0  # m/s

results = simulate_earth_surface(
    frc_power_cell, X_INITIAL, Y_INITIAL, VX_INITIAL, VY_INITIAL
)

# Plot the results
fig, ax = plt.subplots()
ax.plot(results.t, results.y)

# Format and annotate the graph
ax.grid()
ax.text(0.01, 0.4, f"Drag Coefficient = {frc_power_cell.drag:.5} kg/m")
ax.text(0.01, 0.1, f"Flight Time = {results.t[-1]:.4} s")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Simulation of Power Cell Free Fall")

# Display the graph
plt.show()
