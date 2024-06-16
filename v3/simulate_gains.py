"""Simulates how stable the orientation of a model rocket flies provided it's PID gains"""
import math
from globals import Q
from rocket import Rocket
from model_rocket import model_rocket


def pid(gains:dict, theta:Q, d_theta:Q) -> Q:
    """Returns the gimbal angle quantity using PID"""

    theta = theta.to("deg").magnitude
    d_theta = d_theta.to("deg / sec").magnitude
    return Q(theta * gains['P'] + d_theta * gains['D'], "deg")


def restrained_gimbal_angle(angle:Q, max_angle:Q) -> Q:
    """Returns new gimbal angle limited between [-max_angle, max_angle]"""
    if angle < 0:
        return max(-max_angle, angle)
    return min(max_angle, angle)


def rotational_acceleration_change_from_gimbal(radius_to_cm:Q, force:Q, gimbal_angle:Q, moment_of_inertia:Q) -> Q:
    """Calculates change in rotational acceleration due to gimbal angle"""
    torque = radius_to_cm * force * math.sin(gimbal_angle.to("rad"))
    rotational_acc = torque / moment_of_inertia
    return rotational_acc


def simulate_gains(gains:dict, model_rocket:Rocket) -> float:
    """Returns the total deviation of the model rocket during 2500 millisecond duration"""

    r = model_rocket.radius_to_cg
    force = model_rocket.thrust
    i = model_rocket.moment_of_inertia

    delta_t = Q(1, "millisecond")
    total_error = Q(0, "deg")

    for j in range(2500):
        model_rocket.d_theta += model_rocket.dd_theta * delta_t
        model_rocket.theta += model_rocket.d_theta * delta_t
        total_error += abs(model_rocket.theta)

        gimbal_angle = pid(gains, model_rocket.theta, model_rocket.d_theta)
        gimbal_angle = restrained_gimbal_angle(gimbal_angle, model_rocket.max_gimbal_angle)

        model_rocket.dd_theta += rotational_acceleration_change_from_gimbal(r, force, gimbal_angle, i)

        # print(j, '\t',model_rocket.theta,'\t', model_rocket.d_theta)

    return total_error


if __name__ == "__main__":
    error = simulate_gains(model_rocket.pid_gains10opt, model_rocket)
    print(error)
