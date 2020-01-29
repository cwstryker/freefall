from freefall.falling_objects import frc_power_cell
from freefall.simulators import simulate_earth_surface
from freefall.simulators import terminate_vy_less_zero
from freefall.utilities import find_vx_vy, float_range

import matplotlib.pyplot as plt

X_INITIAL = 0       # m
Y_INITIAL = 27/40   # m
SPEED = 5           # m/s
ANGLE = 50          # degrees

fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2)

# Plot the trajectory over several valves of speed
ax0.set(title="Power Cell Trajectory by Speed", xlabel="Distance (m)", ylabel="Height (m)")
ax0.grid()
for i in float_range(2, 8, 0.1):
    
    # run the simulation
    vx_initial, vy_initial = find_vx_vy(speed=i, angle=ANGLE)
    results = simulate_earth_surface(frc_power_cell, X_INITIAL, Y_INITIAL, vx_initial, vy_initial, terminator=terminate_vy_less_zero)

    # Plot the results
    ax0.plot(results.x, results.y)

# Plot the trajectory over several valves of angle
ax1.set(title="Power Cell Trajectory by Angle", xlabel="Distance (m)")
ax1.grid()
for i in float_range(10, 90, 2):
    
    # run the simulation
    vx_initial, vy_initial = find_vx_vy(speed=SPEED, angle=i)
    results = simulate_earth_surface(frc_power_cell, X_INITIAL, Y_INITIAL, vx_initial, vy_initial, terminator=terminate_vy_less_zero)

    # Plot the results
    ax1.plot(results.x, results.y)

# Display the graph
plt.show()
