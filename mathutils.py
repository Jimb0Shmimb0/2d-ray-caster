import math
from constants_and_enums import constants


def decibels_after_x_meters(x: float) -> float:
    return constants.SOURCE_SOUND - 20 * math.log10(x)


def reflected_sound_in_decibels(decibels_in: float) -> float:
    return decibels_in + 10 * math.log10(1 - constants.SOUND_ABSORPTION_COEFFICIENT)

def intersection_exits_between_ray_and_line(x1 ,y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return False
    return True


def calculate_intersection_of_ray_and_line(x1 ,y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return

    # t value for the point of intersection on the ray
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    # u value for the point of intersection on the line
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

    if t > 0 and 0 <= u <= 1:
        return t, u



