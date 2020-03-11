# Zearth Path Problem

This is the solution source code to the Zearth minimax path problem. This includes all optimised code as well as my thought process and analysis.

## My approach and thoughts

My initial thought to solving this problem was to use some kind of informed search. For example, it might be a good idea to use best first search with backtracking. Our heuristic would be to expand the stations with the shortest distance to the current station. Problems kept arising when thinking about this, such as which data structure to use with backtracking. Each station would need its own set of queues. 

My next thought was to use a minimal spanning tree. However, due to the potential number of nodes you have set, 500, the time complexity would explode and we could end up having to try 500498 possible paths.

I decided to take a look online and do some research. Firstly, I clarified the problem: We want to find the path which minimises the the maximum distance between any pair of consecutive points on the path to Zearth. By this definition, we do not care if the path we take is the longest path.

Upon some research, I came across the Floyd-Warshall algorithm, of which the vanilla algorithm finds the shortest path between any two vertices on a graph. However, this algorithm can be tweaked to minimize the maximum distance between any two points in a connected graph.

The calculation within the nested for loop has been modified to amend the distance between any two points to be the maximum of the two edges being compared between the kth node, for all pairs of nodes.

## Run

Use a virtual environment to install the requirements to run this code.

```bash
cd path/to/cloned/directory/
python -m venv env
pip install -r requirements.txt
```

