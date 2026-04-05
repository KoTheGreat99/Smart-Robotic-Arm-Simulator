import math

def inverse_kinematics(origin, target, l1, l2):
    dx = target[0] - origin[0]
    dy = target[1] - origin[1]

    distance = math.sqrt(dx**2 + dy**2)

    # Law of cosines
    cos_theta2 = (distance**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = math.acos(max(min(cos_theta2, 1), -1))

    k1 = l1 + l2 * math.cos(theta2)
    k2 = l2 * math.sin(theta2)

    theta1 = math.atan2(dy, dx) - math.atan2(k2, k1)

    return theta1, theta2
