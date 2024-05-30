import math


def smallest_square_to_fit_rectangles(amount, width, height):
    # Valid inputs
    if not isinstance(amount, int) or not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("Number of rectangles, width, and height must be integers")
    if amount <= 0 or width <= 0 or height <= 0:
        raise ValueError("Number of rectangles, width, and height must be positive integers")

    total_area = amount * width * height
    side_length = math.ceil(math.sqrt(total_area))
    return side_length

