import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

# taking input Polygon Vertices
vertices = np.array([
    (9.05, 7.76),
    (12.5, 3.0),
    (10.0, 0.0),
    (5.0, 0.0),
    (2.5, 3.0)
])

polygon = Polygon(vertices)

# Represent Edges as Vectors
edges = []
for i in range(len(vertices)):
    p1 = vertices[i]
    p2 = vertices[(i + 1) % len(vertices)]
    edges.append(p2 - p1)
edges = np.array(edges)

#  Computing Area
x = vertices[:, 0]
y = vertices[:, 1]
poly_area = 0.5 * abs(np.sum(x * np.roll(y, -1)) - np.sum(y * np.roll(x, -1)))
shapely_area = polygon.area

# Computing Edge Lengths
lens = []
for e in edges:
    lens.append(np.linalg.norm(e))
lens = np.array(lens)

#  Computing Interior Angles
angles = []
for i in range(len(vertices)):
    prev_e = -edges[i - 1]
    next_e = edges[i]

    dot_val = np.dot(prev_e, next_e)
    cos_theta = dot_val / (np.linalg.norm(prev_e) * np.linalg.norm(next_e))
    cos_theta = np.clip(cos_theta, -1, 1)  # avoid numerical issues
    ang = np.degrees(np.arccos(cos_theta))
    angles.append(ang)

# Checking Convexity
is_convex = True
cross_signs = []
for i in range(len(vertices)):
    a = vertices[i]
    b = vertices[(i + 1) % len(vertices)]
    c = vertices[(i + 2) % len(vertices)]
    cross_val = np.cross(b - a, c - b)
    cross_signs.append(np.sign(cross_val))
if not (all(s >= 0 for s in cross_signs) or all(s <= 0 for s in cross_signs)):
    is_convex = False

# Computing the Centroid
centroid_avg = np.mean(vertices, axis=0)
centroid_shapely = np.array([polygon.centroid.x, polygon.centroid.y])

# Displaying Results
print("Polygon Area (Shoelace):", round(poly_area, 2))
print("Polygon Area (Shapely):", round(shapely_area, 2))
print("Edge Lengths:", np.round(lens, 2).tolist())
print("Interior Angles (degrees):", np.round(angles, 2).tolist())
print("Is Convex:", is_convex)
print("Centroid (Manual):", np.round(centroid_avg, 2).tolist())
print("Centroid (Shapely):", np.round(centroid_shapely, 2).tolist())

# Drawing polygon shape
plt.figure(figsize=(7, 6))
plt.fill(x, y, alpha=0.3, facecolor='lightblue', edgecolor='black', linewidth=2)

# Labeling polygon vertices
for i, (vx, vy) in enumerate(vertices):
    plt.text(vx, vy, f"V{i+1}", fontsize=12, ha="right", color="blue")
    plt.plot(vx, vy, "ko")

# Marking centroid
plt.plot(centroid_shapely[0], centroid_shapely[1], "ro", markersize=10)
plt.text(centroid_shapely[0], centroid_shapely[1], "  Centroid", color="red")

# Annotating angles slightly outward
for i, (vx, vy) in enumerate(vertices):
    dx = (vx - centroid_shapely[0]) * 0.1
    dy = (vy - centroid_shapely[1]) * 0.1
    plt.text(vx + dx, vy + dy, f"{angles[i]:.1f}°", fontsize=10, color="darkgreen")

plt.title("Polygon Geometry Using Vector Algebra")
plt.axis("equal")
plt.grid(True)
plt.show()
