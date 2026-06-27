"""
PMW AI Track — 3D Reconstruction Experiment
Author: Areeba Akmal

This beginner-friendly script demonstrates how 3D coordinate points work
and how distance is calculated in 3D space — concepts used in 3D reconstruction.
"""

import math


# ---------------------------------------------------------
# Step 1: Define 3D points
# Each point is stored as (x, y, z) in 3-dimensional space.
# In real 3D reconstruction, thousands of these points are
# estimated from multiple camera images.
# ---------------------------------------------------------
points = [
    (1.0, 2.0, 3.0),   # Point A
    (4.0, 5.0, 6.0),   # Point B
    (2.0, 1.0, 4.0),   # Point C
    (7.0, 3.0, 2.0),   # Point D
]


def euclidean_distance(point_a, point_b):
    """
    Calculate the straight-line (Euclidean) distance between two 3D points.

    Formula: sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)

    This same idea is used in 3D reconstruction to:
    - Measure distances between reconstructed points
    - Check how accurate a model is
    - Understand spatial relationships in a scene
    """
    x1, y1, z1 = point_a
    x2, y2, z2 = point_b

    return math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    )


def main():
    print("PMW AI Track - 3D Reconstruction Experiment")
    print("=" * 45)

    # Step 2: Print all defined 3D points
    print("\nDefined 3D Points (x, y, z):")
    print("-" * 45)
    labels = ["A", "B", "C", "D"]
    for label, point in zip(labels, points):
        print(f"  Point {label}: {point}")

    # Step 3: Calculate distance between two selected points
    point_a = points[0]  # Point A
    point_b = points[1]  # Point B
    distance = euclidean_distance(point_a, point_b)

    print("\nDistance Calculation:")
    print("-" * 45)
    print(f"  From Point A {point_a}")
    print(f"  To   Point B {point_b}")
    print(f"  Euclidean distance: {distance:.2f} units")

    # Also show distance between two other points for comparison
    point_c = points[2]  # Point C
    point_d = points[3]  # Point D
    distance_cd = euclidean_distance(point_c, point_d)

    print(f"\n  From Point C {point_c}")
    print(f"  To   Point D {point_d}")
    print(f"  Euclidean distance: {distance_cd:.2f} units")

    # Step 4: Explain the connection to 3D reconstruction
    print("\nHow This Relates to 3D Reconstruction:")
    print("-" * 45)
    print("  - 3D reconstruction builds models from 3D points like these.")
    print("  - Tools such as COLMAP and Open3D work with large point clouds.")
    print("  - Distance helps measure size, depth, and accuracy in a 3D scene.")
    print("  - Structure from Motion (SfM) estimates point positions from images.")
    print("  - This experiment shows the basic math behind those advanced systems.")

    print("\nExperiment complete.")


if __name__ == "__main__":
    main()
