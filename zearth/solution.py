from numba import njit
from sklearn.metrics import pairwise_distances


def get_distance_matrix(stations):
    """
    Arguments
    ---------
    stations: ndarray
        array of 3d coordinates of all teleportation stations

    Returns
    -------
    ndarray [|points|, |points|] of pairwise distances
    """
    return pairwise_distances(stations)


@njit
def floyd_warshall_minimax(dists):
    """
    Performs a tweaked version of Floyd-Warshall on a distance matrix.

    The calculation within the nested for loop has been modified to amend
    the distance between any two points to be the maximum of the two edges
    being compared between the kth node, for all nodes.

    As the questions has asked, this gives us precisely the maximum distance
    on the path where the maximum distance has been minimized.

    Returns
    -------
    ndarray [|points|, |points|] of maximum distance between consecutive
    points on minimaxed path.
    """
    dist_matrix = dists
    for k in range(len(dist_matrix)):
        for i in range(len(dist_matrix)):
            for j in range(i):
                dist_matrix[i][j] = min(dist_matrix[i][j], max(dist_matrix[i][k], dist_matrix[k][j]))
    return dist_matrix
