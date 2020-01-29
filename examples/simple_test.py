from freefall import FallingObject
from freefall import simulate_earth_surface
from freefall import find_vx_vy

import matplotlib.pyplot as plt

DRAG_COEF = 0.019   # kg/m
MASS = 0.15         # kg
X_INITIAL = 0       # m
Y_INITIAL = 27/40   # m
SPEED = 10          # m/s
ANGLE = 50          # degrees

fig, ax = plt.subplots()

for i in range(1, 10, 1):
    vx_initial, vy_initial = find_vx_vy(speed=i, angle=ANGLE)
    power_cell = FallingObject(mass=MASS, drag=DRAG_COEF)
    results = simulate_earth_surface(power_cell, X_INITIAL, Y_INITIAL, vx_initial, vy_initial)

    # Plot the results
    ax.plot(results.x, results.y)

# Format and annotate the graph
ax.grid()
ax.text(0.01, 0.4, f"Drag Coefficient = {power_cell.drag:.5} kg/m")
ax.text(0.01, 0.1, f"Flight Time = {results.t[-1]:.3} s")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Simulation of Power Cell Free Fall")

# Display the graph
plt.show()
