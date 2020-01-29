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

"""
Desc : This function generates a float range of numbers w/o using any library.

Params :
A (int/float) : First number in the range
L (int/float) : Last number in the range
D (int/float) : Step or the common difference
"""
def float_range(A, L=None, D=None):
    #Use float number in range() function
    # if L and D argument is null set A=0.0 and D = 1.0
    if L == None:
        L = A + 0.0
        A = 0.0
    if D == None:
        D = 1.0
    while True:
        if D > 0 and A >= L:
            break
        elif D < 0 and A <= L:
            break
        yield float(("%g" % A)) # return float number
        A = A + D
#end of function float_range()

fig, ax = plt.subplots()

for i in float_range(2, 7, 0.1):
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
