
import numpy as np

from src.utils.spherical_to_cartesian_coordinates import spherical_to_cartesian_coordinates
from src.utils.vector_functions import angle_between


def get_steering_vec(
        steering_idx: np.ndarray,
        antenna_distance: float,
        wavelength: float,
        cos_aod: float,
) -> np.ndarray:

    constant_factor = -1j * 2 * np.pi / wavelength * antenna_distance * cos_aod

    steering_vector_to_user = np.exp(
        steering_idx
        * constant_factor
    )

    return steering_vector_to_user


def get_aods(
        own_spherical_coordinates: np.ndarray,
        users_spherical_coordinates: list[np.ndarray],
) -> np.ndarray:

    own_cartesian_coordinates = spherical_to_cartesian_coordinates(own_spherical_coordinates)

    aods_to_users = np.zeros(len(users_spherical_coordinates))

    for user_id, user_coordinates in enumerate(users_spherical_coordinates):
        user_cartesian_coordinates = spherical_to_cartesian_coordinates(user_coordinates)
        vec = user_cartesian_coordinates - own_cartesian_coordinates
        aods_to_users[user_id] = angle_between(np.array([-1, 0, 0]), vec)

    return aods_to_users
