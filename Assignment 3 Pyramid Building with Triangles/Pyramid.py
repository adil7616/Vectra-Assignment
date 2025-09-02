import matplotlib.pyplot as plt  # for drawing/plotting shapes
import numpy as np

# Generating coordinates of an equilateral triangle
# Can be upright or inverted depending on the 'upright' flag
def equilateral_triangle(x, y, side, upright=True):
    height = np.sqrt(3) / 2 * side
    if upright:
        return [
            [x, y],
            [x - side / 2, y - height],
            [x + side / 2, y - height]
        ]
    else:
        return [
            [x, y],
            [x - side / 2, y + height],
            [x + side / 2, y + height]
        ]

# Drawing a pyramid of equilateral triangles
def draw_pyramid(side, depth):
    plt.figure(figsize=(8, 8))
    h = np.sqrt(3) / 2 * side

    for row in range(depth):
        x_start = -row * side / 2
        y = -row * h

        # Loop through triangles in the row
        for col in range(row + 1):
            x = x_start + col * side

            # Draw upright triangle
            tri_up = equilateral_triangle(x, y, side, upright=True)
            plt.fill(*zip(*tri_up), color="royalblue", edgecolor="black")

            # Draw inverted triangle between upright ones
            if col < row:
                x_inv = x + side / 2
                y_inv = y - h
                tri_down = equilateral_triangle(x_inv, y_inv, side, upright=False)
                plt.fill(*zip(*tri_down), color="gold", edgecolor="black")

    # Adjust plot settings
    plt.gca().set_aspect('equal')
    plt.axis("off")
    plt.show()

# Pyramid with side length 2 and depth 4
draw_pyramid(side=2, depth=4)
