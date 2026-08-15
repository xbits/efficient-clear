A* is a search algorithm for finding the shortest path between two nodes in a weighted graph. It's an extension of Dijkstra's algorithm that uses a heuristic to guide the search toward the goal, instead of expanding outward in every direction equally.

## How it works

A* keeps a priority queue of nodes to explore, ordered by a score:

f(n) = g(n) + h(n)

- g(n) is the actual cost of the path from the start node to n, the same value Dijkstra's algorithm tracks.
- h(n) is the heuristic: an estimate of the cost from n to the goal. This is the part Dijkstra's algorithm doesn't have.

At each step, A* pulls the node with the lowest f(n) from the queue, checks if it's the goal, and if not, expands its neighbors, computing g and f for each. This repeats until the goal is popped from the queue or the queue is empty (no path exists).

Because h(n) points the search toward the goal, A* explores far fewer nodes than Dijkstra's algorithm on most graphs, especially when the heuristic is accurate.

## Key properties

**Admissibility**: if h(n) never overestimates the true cost to the goal, A* is guaranteed to find the shortest path. An admissible heuristic that's also inaccurate just makes the search slower, not wrong.

**Consistency (monotonicity)**: a stronger condition where, for every neighbor n' of n, h(n) ≤ cost(n, n') + h(n'). Consistency implies admissibility and also guarantees that once a node is popped from the queue, its shortest path has been found for good, so it never needs to be reopened. Most practical heuristics (straight-line distance, Manhattan distance) are consistent.

**Optimality**: with an admissible heuristic, A* always returns the shortest path, same as Dijkstra's algorithm.

**Completeness**: A* will find a path if one exists, as long as the graph has a finite branching factor and positive edge costs (or the algorithm handles zero-cost edges correctly).

**Efficiency**: A* is optimally efficient among algorithms using the same heuristic — no other algorithm using that heuristic and expanding paths from the start node will expand fewer nodes and still guarantee the optimal path. If h(n) = 0 for all nodes, A* becomes Dijkstra's algorithm. If h(n) is a perfect estimate, A* follows the shortest path directly with no wasted expansion.

**Trade-offs**: A* stores every generated node in memory, which can be a problem on large graphs. Its performance depends heavily on the quality of the heuristic — a weak or expensive-to-compute heuristic can erase its advantage over Dijkstra's algorithm.

## Common use cases

Pathfinding in games and robotics, route planning, and any shortest-path problem on a graph where a reasonable estimate of remaining distance is available.
