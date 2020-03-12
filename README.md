# Zearth Path Problem

This is the solution source code to the Zearth minimax path problem. This includes all optimised code as well as my thought process and analysis.

*Please Note*: My writtenanswers are within this README. I prefer to use markdown for exposition. I do have the written solutions in text format. If this is essential, I can push this. 

## My approach and thoughts

My initial thought to solving this problem was to use some kind of informed search. For example, it might be a good idea to use best first search with backtracking. Our heuristic would be to expand the stations with the shortest distance to the current station. Problems kept arising when thinking about this, such as which data structure to use with backtracking. Each station would need its own set of queues. 

I decided to take a look online and do some research. Firstly, I clarified the problem: We want to find the path which minimises the the maximum distance between any pair of consecutive points on the path to Zearth. By this definition, we do not care if the path we take is the longest path.

Upon some research, I came across the Floyd-Warshall algorithm, of which the vanilla algorithm finds the shortest path between any two vertices on a graph. However, this algorithm can be tweaked to minimize the maximum distance between any two consecutive points in a path between the source and target vertex in a connected graph.

The calculation within the nested for loop of the standard algorithm has been modified. It now updates the distance between any two vertices, and another vertex that connects these two, to be the maximum of the two edges being compared to the previous distance between the vertices, if this minimizes the maximum distance travelled before this check.

## Optimisations

1. Since we can treat the paths between teleporation stations as an undirected connected graph. Then the matrix that results from the distance matrix is symmetric. Therefore, we only need to perform our minimax calculation on the lower, or upper, triangular matrix of the distance matrix. This cuts the time taken to run the algorithm by 2. A **half** decent improvement.

Implementation-wise, we can make the inner-most nested for loop only iterate to the length of the next outer for loops value, iterating only over the lower triangular matrix of the distance matrix.

2. Nested for loops in python. Not good. This is a great time to use numba, which will massively increase the speed of our algorithm. Let's do just that and see the increase in speed.

Again, implementation-wise this is really easy. Numba uses decorators, so we merely insert a line above our algorithm function.

## Complexity

Our algorithm, Floyd-Warshall, contains a triple-nested for loop. Therefore, the time complexity of this algorithm is
![](https://latex.codecogs.com/gif.latex?O%28n%5E%7B3%7D%29). TODO

Memory-wise, TODO.

## Run

First, clone this environment.
Use a virtual environment to install the requirements to run this code.

Currently, I only have two files for you to test in the data directory. `input_simple.txt` is one of the examples in the assignment sheet. The other, `input_large.txt` is a more challenging example, containing the maximum `500` teleportation stations. The current algorithm, as it stands, can process this in less than a second.

```bash
cd path/to/cloned/directory/

python -m venv env
source env/bin/activate
pip install -r requirements.txt

python minimax.py data/input_sample.txt
1.73
python minimax.py data/input_large.txt
1653.52
```

# FURTHER WORK

I am not sure exactly how you would like me to accept input. Will this be coming through files? requests? Will each file have multiple input examples?

I am happy to set up a flask instance, or something similar, where you can upload files or paste input for the appropriate response.

Please let me know what you would like for the final solution.
