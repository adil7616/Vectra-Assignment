import matplotlib.pyplot as plt
import numpy as np

# Generating coordinates of an equilateral triangle
def equilateral_triangle(x, y, side, upright=True):
    h = (np.sqrt(3) / 2) * side
    if upright:
        pts = [
            [x, y],
            [x - side / 2, y - h],
            [x + side / 2, y - h]
        ]
    else:
        pts = [
            [x, y],
            [x - side / 2, y + h],
            [x + side / 2, y + h]
        ]
    return pts


# Drawing a pyramid of equilateral triangles
def draw_pyramid(side, depth):
    plt.figure(figsize=(8, 8))
    h = (np.sqrt(3) / 2) * side

    for row in range(depth):
        start_x = -row * (side / 2)
        base_y = -row * h

        # Loop through triangles in this row
        for col in range(row + 1):
            cx = start_x + col * side

            # upright one
            tri1 = equilateral_triangle(cx, base_y, side, upright=True)
            x_vals, y_vals = zip(*tri1)
            plt.fill(x_vals, y_vals, facecolor="royalblue", edgecolor="black")

            # inverted one (only if space in between)
            if col < row:
                inv_x = cx + side / 2
                inv_y = base_y - h
                tri2 = equilateral_triangle(inv_x, inv_y, side, upright=False)
                xi, yi = zip(*tri2)
                plt.fill(xi, yi, facecolor="gold", edgecolor="black")

    # Adjust plot settings
    ax = plt.gca()
    ax.set_aspect("equal")
    plt.axis("off")
    plt.show()


# Pyramid with side length 2 and depth 4
draw_pyramid(side=2, depth=4)
draw_pyramid(side=1, depth=6)