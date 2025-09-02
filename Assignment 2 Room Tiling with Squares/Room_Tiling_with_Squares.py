import matplotlib.pyplot as plt
import numpy as np


# Tile sizes and their colors
tile_sizes = {
    4: "green",
    3: "yellow",
    2: "blue",
    1: "red"
}

# Generating coordinates in a spiral pattern from the center.
def spiral_indices(rows, cols):
    cx, cy = rows // 2, cols // 2
    x, y = cx, cy
    dx, dy = 0, -1
    for _ in range(max(rows, cols) ** 2):
        if 0 <= x < rows and 0 <= y < cols:
            yield (x, y)
        # turning condition
        if (x - cx == y - cy) or \
            (x - cx < 0 and x - cx == -(y - cy)) or \
            (x - cx > 0 and x - cx == 1 - (y - cy)):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


# Checking if a tile of given size can be placed at (x,y).
def can_place(grid, x, y, size, rows, cols):
    if x + size > rows or y + size > cols:
        return False
    block = grid[x:x+size, y:y+size]
    return np.all(block == 0)


# Placing a tile of given size on the grid.
def place_tile(grid, x, y, size, tile_id):
    grid[x:x+size, y:y+size] = tile_id


# Filling m x n grid with square tiles in spiral order
def tile_room(rows, cols):
    grid = np.zeros((rows, cols), dtype=int)
    cnts = {1: 0, 2: 0, 3: 0, 4: 0}
    tid = 1

    for x, y in spiral_indices(rows, cols):
        if grid[x, y] != 0:
            continue
        for sz in sorted(tile_sizes.keys(), reverse=True):
            if can_place(grid, x, y, sz, rows, cols):
                place_tile(grid, x, y, sz, tid)
                cnts[sz] += 1
                tid += 1
                break
    return grid, cnts


# Plotting the tiling
def plot_tiling(grid, cnts):
    rows, cols = grid.shape
    fig, ax = plt.subplots(figsize=(8, 6))
    for i in range(rows):
        for j in range(cols):
            tid = grid[i, j]
            if tid == 0:
                continue
            # figure out tile size by checking contiguous block
            for sz, color in tile_sizes.items():
                if i + sz <= rows and j + sz <= cols:
                    block = grid[i:i+sz, j:j+sz]
                    if np.all(block == tid):
                        rect = plt.Rectangle((j, rows - i - sz), sz, sz,
                                                facecolor=color, edgecolor="black")
                        ax.add_patch(rect)
                        break

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_xticks(range(cols + 1))
    ax.set_yticks(range(rows + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)
    ax.set_title("Room Tiling (Spiral Fill)")

    plt.show()

    print("Tile counts:")
    for sz in sorted(cnts.keys(), reverse=True):
        print(f"{sz}x{sz}: {cnts[sz]}")


# Example with height and width
rows, cols = 12, 8
grid, cnts = tile_room(rows, cols)
plot_tiling(grid, cnts)
