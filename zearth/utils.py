import numpy as np


def _read_input_file(file):
    with open(file, 'r') as fp:
        return fp.readlines()


def parse_input(file):
    """
    Arguments
    ---------
    file: str

    Converts lines of input to numpy arrays of floats.
    The final output includes an array of all teleportation stations, where
    earth is at index 0 and zearth is at index -1. This helps with the
    algorithm.

    Returns
    -------
    ndarray [num_station, 3]
    """
    inp = _read_input_file(file)

    text = [line.rstrip('\n') for line in inp]
    zearth = np.array([float(n) for n in text[0].split()])
    stations = np.array([[float(n) for n in line.split()]
                         for line in text[2:]])

    stations = np.insert(stations, 0, np.zeros(3), axis=0)
    stations = np.insert(stations, len(stations), zearth, axis=0)

    return stations
