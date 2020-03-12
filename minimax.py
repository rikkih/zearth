import sys

from zearth.utils import parse_input
from zearth.solution import get_distance_matrix, floyd_warshall_minimax


def main(file):
    stations = parse_input(file)
    dists = get_distance_matrix(stations)
    minimax_paths = floyd_warshall_minimax(dists)
    solution = minimax_paths[-1, 0]
    solution = round(solution, 2)
    print(solution)
    return solution


if __name__ == "__main__":
    main(sys.argv[1])
