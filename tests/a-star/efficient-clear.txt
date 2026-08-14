A* is a best-first graph search algorithm that finds the shortest path from a start node to a goal node. It generalizes Dijkstra's algorithm by adding a heuristic that estimates the remaining distance to the goal, which lets it focus the search toward the goal instead of expanding uniformly in all directions.

## How it works

A* maintains an open set (nodes discovered but not yet expanded) and a closed set (nodes already expanded). For each node n, it tracks two costs:

- g(n): the actual cost of the cheapest known path from the start to n.
- h(n): a heuristic estimate of the cost from n to the goal.

The algorithm ranks nodes by f(n) = g(n) + h(n), the estimated total cost of a path through n. At each step, A* pops the node with the lowest f(n) from the open set, expands it, and computes g and f for its neighbors. If a neighbor is reached by a cheaper path than any previously known, its g value is updated and it is placed back in the open set. The algorithm stops when the goal node is popped from the open set, at which point the path can be reconstructed by following stored parent pointers back to the start.

The open set is typically implemented as a priority queue (commonly a binary heap), so the node with the lowest f(n) is available in O(log n) time.

## Key properties

**Completeness.** A* is complete on finite graphs with positive edge weights: if a path to the goal exists, A* finds it.

**Optimality.** A* is optimal (it finds the shortest path) if the heuristic h(n) is admissible, meaning it never overestimates the true cost to the goal. A common stronger requirement is consistency (or monotonicity): for every edge from n to a neighbor n', h(n) <= cost(n, n') + h(n'). Consistency implies admissibility and guarantees that once a node is expanded, its g value is already optimal, so it never needs to be re-expanded.

**Heuristic behavior.** The heuristic controls the trade-off between search speed and node count.
- h(n) = 0 for all n reduces A* to Dijkstra's algorithm: correct but slow, since it explores uniformly in all directions.
- A heuristic close to the true remaining cost sharply reduces the number of nodes expanded, focusing the search along the direct path to the goal.
- An inadmissible heuristic (one that can overestimate) may cause A* to return a suboptimal path, though it can still find a path faster.

**Complexity.** In the worst case, time and space complexity are exponential in the path length, since the open and closed sets can grow to include most of the graph. In practice, with a well-chosen heuristic, the number of nodes expanded is much smaller than the full graph. Space is often the binding constraint, since A* must keep every generated node in memory; this motivates memory-bounded variants such as IDA* and SMA*.

**Typical use.** A* is standard for pathfinding on explicit graphs and grids (games, robotics, GPS routing) where a good heuristic is available, such as Euclidean or Manhattan distance to the goal.
