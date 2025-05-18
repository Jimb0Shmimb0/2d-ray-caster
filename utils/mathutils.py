import math

import numpy as np

import constants


def decibels_after_x_meters(x: float, decibels: float) -> float:
    return decibels - 20 * math.log10(x)

def reflected_sound_in_decibels(decibels_in: float, SAC: float) -> float:
    return decibels_in + 10 * math.log10(1 - SAC)

def distance_to_threshold(decibels: float):
    return 10 ** ((decibels - constants.HEARING_THRESHOLD) / 20)

def intersection_exits_between_ray_and_line(x1 ,y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denominator) < 1e-10:
        return False

    # t value for the point of intersection on the ray
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    # u value for the point of intersection on the line
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

    if not (t > 1e-10 and 0 <= u <= 1):
        return False
    return True


def calculate_intersection_of_ray_and_line(x1 ,y1, x2, y2, x3, y3, x4, y4):
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    # t value for the point of intersection on the ray
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    # u value for the point of intersection on the line
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator

    if t > 1e-10 and 0 <= u <= 1:
        return t, u


def reflected_vector(direction_x, direction_y, wall_direction_x, wall_direction_y):

    theta = math.atan2(- wall_direction_x, wall_direction_y)
    cos_2t = math.cos(2 * theta)
    sin_2t = math.sin(2 * theta)

    x_prime = -(cos_2t * direction_x + sin_2t * direction_y)
    y_prime = -(sin_2t * direction_x - cos_2t * direction_y)

    return x_prime, y_prime


# Alternatively...
"""
def reflected_vector(direction_x, direction_y, wall_dx, wall_dy):
    d = np.array([direction_x, direction_y])
    d = d / np.linalg.norm(d)

    wall = np.array([wall_dx, wall_dy])
    wall = wall / np.linalg.norm(wall)

    normal = np.array([-wall[1], wall[0]])

    reflected = d - 2 * np.dot(d, normal) * normal
    return reflected[0], reflected[1]
"""






