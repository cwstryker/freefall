from collections import namedtuple

FallingObject = namedtuple("FallingObject", ["mass", "drag"])
SimResult = namedtuple("SimResult", ["x", "y", "vx", "vy", "ax", "ay", "t"])


def simulate(
    target,
    x_initial,
    y_initial,
    vx_initial=0,
    vy_initial=0,
    epsilon=0.001,
    gravity=9.81,
):

    x = list()
    y = list()
    vx = list()
    vy = list()
    ax = list()
    ay = list()
    t = list()

    x.append(x_initial)
    y.append(y_initial)

    ax.append(0)
    ay.append(-gravity)

    vx.append(vx_initial + (epsilon / 2.0) * ax[-1])
    vy.append(vy_initial + (epsilon / 2.0) * ay[-1])

    t.append(0)

    while True:
        x.append(x[-1] + epsilon * vx[-1])
        y.append(y[-1] + epsilon * vy[-1])

        ax.append(-vx[-1] ** 2 * target.drag / target.mass)
        ay.append((vy[-1] ** 2 * target.drag / target.mass) - gravity)

        vx.append(vx[-1] + epsilon * ax[-1])
        vy.append(vy[-1] + epsilon * ay[-1])

        t.append(t[-1] + epsilon)

        if y[-1] < 0:
            break

    return SimResult(x=x, y=y, vx=vx, vy=vy, ax=ax, ay=ay, t=t)
