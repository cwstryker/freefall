from freefall import FallingObject
from freefall import simulate
import matplotlib.pyplot as plt

DRAG_COEF = 0.019   # kg/m
MASS = 0.15         # kg
X_INITIAL = 0       # m
Y_INITIAL = 4.5     # m
VX_INITIAL = 0      # m/s
VY_INITIAL = 0      # m/s

power_cell = FallingObject(mass=MASS, drag=DRAG_COEF)
results = simulate(power_cell, X_INITIAL, Y_INITIAL, VX_INITIAL, VY_INITIAL)

# Plot the results
fig, ax = plt.subplots()
ax.plot(results.t, results.y)

# Format and annotate the graph
ax.grid()
ax.text(0.01, 0.4, f"Drag Coefficient = {power_cell.drag:.5} kg/m")
ax.text(0.01, 0.1, f"Flight Time = {results.t[-1]:.3} s")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Simulation of Power Cell Free Fall")

# Display the graph
plt.show()
