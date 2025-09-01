import matplotlib.pyplot as plt
import numpy as np

# Function to draw a filled ring (annulus section)
def draw_ring(ax, r1, r2, color, points=500):
    theta = np.linspace(0, 2*np.pi, points)
    x1, y1 = r1*np.cos(theta), r1*np.sin(theta)
    x2, y2 = r2*np.cos(theta), r2*np.sin(theta)
    ax.fill(np.concatenate([x1, x2[::-1]]),
            np.concatenate([y1, y2[::-1]]),
            color=color)

# Function to draw star polygons
def draw_star(ax, r, n_points, color):
    theta = np.linspace(0, 2*np.pi, n_points*2+1)
    r_values = np.tile([r, r/2], n_points+1)
    x, y = r_values * np.cos(theta), r_values * np.sin(theta)
    ax.fill(x, y, color=color)

# Function to draw zigzag ring
def draw_zigzag(ax, r1, r2, n_zigs, color):
    theta = np.linspace(0, 2*np.pi, n_zigs*2+1)
    r_values = np.tile([r1, r2], n_zigs+1)
    x, y = r_values * np.cos(theta), r_values * np.sin(theta)
    ax.fill(x, y, color=color)

# Main figure
fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect("equal")
ax.axis("off")

# Colors inspired by your Pookalam
colors = {
    "yellow": "#FFD700",
    "orange": "#FF8C00",
    "red": "#8B0000",
    "white": "#FFFFFF",
    "green": "#006400"
}

# Draw concentric layers
draw_star(ax, 0.3, 8, colors["yellow"])      # Center star
draw_ring(ax, 0.3, 0.5, colors["green"])     # Green ring
draw_zigzag(ax, 0.5, 0.7, 12, colors["white"]) # White zigzag
draw_ring(ax, 0.7, 0.9, colors["orange"])    # Orange ring
draw_ring(ax, 0.9, 1.1, colors["red"])       # Red ring
draw_ring(ax, 1.1, 1.3, colors["yellow"])    # Yellow ring
draw_ring(ax, 1.3, 1.5, colors["green"])     # Outer green ring

plt.show()
