A* Pathfinding Algorithm

A* is a best-first search algorithm for finding the shortest path between two nodes in a weighted graph. It extends Dijkstra's algorithm with a heuristic that estimates the remaining distance to the goal, letting it skip large parts of the graph that Dijkstra would explore blindly.

How it works

A* maintains a priority queue of nodes, ordered by f(n) = g(n) + h(n):

- g(n): the actual cost of the path from the start node to n, known exactly since it comes from edges already traversed.
- h(n): a heuristic estimate of the cost from n to the goal. This is the part Dijkstra lacks.
- f(n): the estimated total cost of a path through n.

The algorithm starts with the start node in the queue and repeats:

1. Pop the node with the lowest f(n) from the queue.
2. If it is the goal, stop. The path is reconstructed by following stored parent pointers back to the start.
3. Otherwise, expand its neighbors. For each neighbor, compute a tentative g using the current node's g plus the edge cost. If this is better than the neighbor's previously known g (or the neighbor is unvisited), update its g, set its parent to the current node, compute its f, and push or re-prioritize it in the queue.
4. If the queue empties without reaching the goal, no path exists.

A closed set (or an equivalent check) tracks nodes already finalized, so the algorithm does not reprocess them needlessly.

Key properties

- Completeness: A* finds a path if one exists, given a finite graph or one with a positive minimum edge cost.
- Optimality: A* returns the shortest path if the heuristic is admissible — it never overestimates the true remaining cost. On graphs, optimality also requires the heuristic to be consistent (h(n) ≤ cost(n, n') + h(n') for every edge), which guarantees a node's g is final the first time it is popped.
- Efficiency: A* expands fewer nodes than Dijkstra when the heuristic is informative, because f(n) prunes branches that cannot beat the current best path. A weak or zero heuristic degrades A* to Dijkstra's algorithm; an inadmissible heuristic can speed up search further but forfeits the optimality guarantee.
- Heuristic design: common choices are Euclidean distance, Manhattan distance (for grid graphs restricted to four directions), and Chebyshev distance (for eight directions). The heuristic must match the graph's cost structure — an inadmissible heuristic for the given costs can return a suboptimal path.
- Memory: A* stores every generated node, which makes memory the usual bottleneck on large graphs. Variants like IDA* (iterative deepening) and SMA* (simplified memory-bounded) trade some speed for a smaller memory footprint.

Complexity

Time and space complexity are both O(b^d) in the worst case, where b is the branching factor and d is the depth of the shortest path — same bound as breadth-first search. In practice, a good heuristic keeps the explored set far below this bound. With a perfect heuristic, A* expands only the nodes on the optimal path.
