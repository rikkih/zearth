# Zearth Path Problem

This is the solution source code to the Zearth minimax path problem. This includes all optimised code as well as my thought process and analysis.

Please Note: My writtenanswers are within this README. I prefer to use markdown for exposition. I do have the written solutions in text format. If this is essential, I can push this. 

## My approach and thoughts

My initial thought to solving this problem was to use some kind of informed search. For example, it might be a good idea to use best first search with backtracking. Our heuristic would be to expand the stations with the shortest distance to the current station. Problems kept arising when thinking about this, such as which data structure to use with backtracking. Each station would need its own set of queues. 

My next thought was to use a minimal spanning tree. However, due to the potential number of nodes you have set, 500, the time complexity would explode and we could end up having to try 500^498 possible paths.

I decided to take a look online and do some research. Firstly, I clarified the problem: We want to find the path which minimises the the maximum distance between any pair of consecutive points on the path to Zearth. By this definition, we do not care if the path we take is the longest path.

Upon some research, I came across the Floyd-Warshall algorithm, of which the vanilla algorithm finds the shortest path between any two vertices on a graph. However, this algorithm can be tweaked to minimize the maximum distance between any two consecutive points in a path between source and target in a connected graph.

The calculation within the nested for loop has been modified to amend the distance between any two points to be the maximum of the two edges being compared between the kth node, for all pairs of nodes.

## Optimisations

1. Since we can treat the paths between teleporation stations as an undirected connected graph. Then the matrix that results from the distance matrix is symmetric. Therefore, we only need to perform our minimax calculation on the lower, or upper, triangular matrix of the distance matrix. This cuts the time taken to run the algorithm by 2. A half decent improvement.. Get it?

Implementation-wise, we can make the inner-most nested for loop only iterate to the length of the next outer for loops value, iterating only over the lower triangular matrix of the distance matrix.

2. Nested for loops in python. Not good. This is a great time to use numba, which will massively increase the speed of our algorithm. Let's do just that and see the increase in speed.

Again, implementation-wise this is really easy. Numba uses decorators, so we merely insert a line above our algorithm function.

## Complexity

Our algorithm, Floyd-Warshall, contains a triple-nested for loop. For iterating over our graph, we have O(n^3). Memory-wise, 
TODO 

## Run

First, clone this environment.
Use a virtual environment to install the requirements to run this code.

Currently, I only have two files for you to test in the data directory. input\_simple.txt is one of the examples in the assignment sheet. The other, input\_large.txt is a more challenging example, containing the maximum 500 teleportation stations. The current algorithm, as it stands, can process this within a second.

```bash
cd path/to/cloned/directory/
python -m venv env
source env/bin/activate
pip install -r requirements.txt

python minimax.py data/input_sample.txt
python minimax.py data/input_large.txt
```

# FURTHER WORK

I am not sure exactly how you would like me to accept input. Will this be coming through files? requests? Will each file have multiple input examples?

I am happy to set up a flask instance, or something similar, where you can upload files or paste input for the appropriate response.

Please let me know what you would like for the final solution.
