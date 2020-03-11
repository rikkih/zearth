# Zearth Path Problem

This is the solution source code to the Zearth minimax path problem. This includes all optimised code as well as my thought process and analysis.

## My approach and thoughts

My initial thought to solving this problem was to use some kind of informed search. For example, it might be a good idea to use best first search with backtracking. Our heuristic would be to expand the stations with the shortest distance to the current station. Problems kept arising when thinking about this, such as which data structure to use with backtracking. Each station would need its own set of queues. 

My next thought was to use a minimal spanning tree. However, due to the potential number of nodes you have set, 500, the time complexity would explode and we could end up having to try 500^498 possible paths.

I decided to take a look online and do some research. Firstly, I clarified the problem: We want to find the path which minimises the the maximum distance between any pair of consecutive points on the path to Zearth. By this definition, we do not care if the path we take is the longest path.

Upon some research, I came across the Floyd-Warshall algorithm, of which the vanilla algorithm finds the shortest path between any two vertices on a graph. However, this algorithm can be tweaked to minimize the maximum distance between any two consecutive points in a path between source and target in a connected graph.

The calculation within the nested for loop has been modified to amend the distance between any two points to be the maximum of the two edges being compared between the kth node, for all pairs of nodes.

## Optimisations

1. Since we can treat the paths between teleporation stations as an undirected connected graph. Then the matrix that results from the distance matrix is symmetric. Therefore, we only need to perform our minimax calculation on the lower, or upper, triangular matrix of the distance matrix. This cuts the time taken to run the algorithm by 2. A half decent improvement.. Get it?

Implementation-wise, we can make the inner-most nested for loop only iterate to the length of the next outer for loops value, iterating only over the lower triangular matrix of the distance matrix.

## Run

First, clone this environment.
Use a virtual environment to install the requirements to run this code.

```bash
cd path/to/cloned/directory/
python -m venv env
source env/bin/activate
pip install -r requirements.txt

python minimax.py data/input_sample.py
```

