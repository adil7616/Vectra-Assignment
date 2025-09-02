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
def spiral_indices(m, n):
    
    center_x, center_y = m // 2, n // 2
    x, y = center_x, center_y
    dx, dy = 0, -1
    for _ in range(max(m, n) ** 2):
        if 0 <= x < m and 0 <= y < n:
            yield (x, y)
            
        if (x - center_x == y - center_y) or \
            (x - center_x < 0 and x - center_x == -(y - center_y)) or \
            (x - center_x > 0 and x - center_x == 1 - (y - center_y)):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy


# Checking if a tile of given size can be placed at (x,y).
def can_place(grid, x, y, size, m, n):

    if x + size > m or y + size > n:
        return False
    return np.all(grid[x:x+size, y:y+size] == 0)


# Placing a tile of given size on the grid.
def place_tile(grid, x, y, size, tile_id):
    
    grid[x:x+size, y:y+size] = tile_id

# Filling m x n grid with square tiles in spiral order
def tile_room(m, n):
    grid = np.zeros((m, n), dtype=int)
    tile_counts = {1:0, 2:0, 3:0, 4:0}
    tile_id = 1

    for x, y in spiral_indices(m, n):
        if grid[x, y] != 0:
            continue
        for size in sorted(tile_sizes.keys(), reverse=True):
            if can_place(grid, x, y, size, m, n):
                place_tile(grid, x, y, size, tile_id)
                tile_counts[size] += 1
                tile_id += 1
                break
    return grid, tile_counts  # Return the grid and tile counts

# Plotting the tiling
def plot_tiling(grid, tile_counts):
    m, n = grid.shape
    fig, ax = plt.subplots(figsize=(8, 6))
    for i in range(m):
        for j in range(n):
            tile_id = grid[i, j]
            if tile_id != 0:
                for size, color in tile_sizes.items():  # Find the size based on contiguous cells
                    if i + size <= m and j + size <= n and np.all(grid[i:i+size, j:j+size] == tile_id):
                        rect = plt.Rectangle((j, m-i-size), size, size, facecolor=color, edgecolor="black")
                        ax.add_patch(rect)
                        break
                    
    
    ax.set_xlim(0, n)
    ax.set_ylim(0, m)
    ax.set_xticks(range(n+1))
    ax.set_yticks(range(m+1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which='both', color='lightgrey', linewidth=0.5)
    ax.set_title("Room Tiling (Spiral Fill)")

    plt.show()

    print("Tile counts:")
    for size in sorted(tile_counts.keys(), reverse=True):
        print(f"{size}x{size}: {tile_counts[size]}")

# Example with height and width
m, n = 12, 8
grid, tile_counts = tile_room(m, n)
plot_tiling(grid, tile_counts)
