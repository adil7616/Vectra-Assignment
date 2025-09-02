import matplotlib.pyplot as plt
import numpy as np

def equilateral_triangle(x, y, side, upright=True):
    """Return coordinates of an equilateral triangle centered at (x, y)."""
    h = np.sqrt(3) / 2 * side
    if upright:
        return [
            [x, y],
            [x - side / 2, y - h],
            [x + side / 2, y - h]
        ]
    else:
        return [
            [x, y],
            [x - side / 2, y + h],
            [x + side / 2, y + h]
        ]

def draw_pyramid(side, depth):
    plt.figure(figsize=(8, 8))
    h = np.sqrt(3) / 2 * side  # height of one triangle

    for row in range(depth):
        # horizontal offset so the pyramid is centered
        x_start = -row * side / 2
        y = -row * h  

        for col in range(row + 1):
            x = x_start + col * side

            # Upright triangle
            tri_up = equilateral_triangle(x, y, side, upright=True)
            plt.fill(*zip(*tri_up), color="royalblue", edgecolor="black")

            # Inverted triangle inside row (except last column)
            if col < row:
                x_inv = x + side / 2
                y_inv = y - h
                tri_down = equilateral_triangle(x_inv, y_inv, side, upright=False)
                plt.fill(*zip(*tri_down), color="gold", edgecolor="black")

    plt.gca().set_aspect('equal')
    plt.axis("off")
    plt.show()

# Example usage
draw_pyramid(side=2, depth=4)
