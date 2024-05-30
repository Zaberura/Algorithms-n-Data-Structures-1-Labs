import math


def calculate_max_wire_length(w, heights):
    if not (1 <= w <= 100):
        raise ValueError("Відстань між опорами має бути у діапазоні від 1 до 100.")

    if not all(1 <= height <= 100 for height in heights):
        raise ValueError("Висота кожної опори має бути у діапазоні від 1 до 100.")

    max_top = 0
    max_bottom = 0

    for i in range(0, len(heights) - 1):
        new_max_top = max(max_top + two_points_distance(heights[i], heights[i + 1], w),
                          max_bottom + two_points_distance(1, heights[i + 1], w))

        max_bottom = max(max_top + two_points_distance(heights[i], 1, w),
                         max_bottom + two_points_distance(1, 1, w))

        max_top = new_max_top

    return max(max_top, max_bottom)


def two_points_distance(point_1, point_2, width):
    return math.sqrt(width ** 2 + (point_1 - point_2) ** 2)

