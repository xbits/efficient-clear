A* is a search algorithm that finds the shortest path between two nodes in a graph. It is used widely in routing and game pathfinding because it usually explores far fewer nodes than uninformed methods like Dijkstra's algorithm, while still guaranteeing the shortest path under the right conditions.

## What it is

A* treats pathfinding as a best-first search: at each step it picks the most promising unexplored node and expands it. What makes a node "promising" is a score made of two parts:

f(n) = g(n) + h(n)

- g(n) is the exact cost of the path from the start node to n, known because it was built by the search itself.
- h(n) is a heuristic: an estimate of the cost from n to the goal. This is supplied by the algorithm's user, not computed by A* itself.

A* always expands the node with the lowest f(n) among those it knows about but hasn't yet expanded.

## How it works

1. Keep two sets of nodes: an open set (discovered but not yet expanded) and a closed set (already expanded).
2. Start with only the start node in the open set, with g = 0.
3. Repeat:
   - Pick the node n in the open set with the lowest f(n).
   - If n is the goal, stop. Trace the path back through recorded parent pointers to get the shortest path.
   - Move n to the closed set.
   - For each neighbor of n: compute a tentative g value (g(n) plus the cost of the edge to the neighbor). If this is better than any g value already recorded for the neighbor, record it, set n as the neighbor's parent, and add the neighbor to the open set (or update its position there).
4. If the open set becomes empty before the goal is reached, no path exists.

In practice, the open set is kept as a priority queue ordered by f(n), so picking the lowest-cost node is fast.

## Key properties

- Completeness: if a path exists, A* will find it, as long as the graph has a finite number of nodes with a cost below any given path length (no infinite chains of zero-cost edges, etc.).
- Optimality: A* returns the shortest path if the heuristic is admissible, meaning h(n) never overestimates the true remaining cost to the goal. An admissible heuristic guarantees A* won't skip over a shorter path in favor of a longer one that merely looks cheaper.
- Efficiency: if the heuristic is also consistent (sometimes called monotone), meaning h(n) is never more than the cost of moving to a neighbor plus that neighbor's heuristic value, then once a node is expanded its shortest path is already known, and A* never needs to reopen it. This keeps the algorithm efficient. Every consistent heuristic is admissible, but not the reverse.
- Behavior at the extremes: if h(n) is 0 for every node, A* becomes Dijkstra's algorithm, expanding nodes purely by distance from the start. If h(n) is very large, or is set exactly equal to the true remaining cost, A* moves close to a straight line toward the goal, expanding far fewer nodes but only staying optimal if it never overestimates.
- Time and space cost: in the worst case A* can still need to store and examine every node in the graph, so its runtime and memory use are bounded by the size of the graph. In practice, a well-chosen heuristic sharply cuts down how much of the graph is actually explored.

The core trade-off is the quality of the heuristic. A weak heuristic (or none) makes A* behave like an exhaustive search. A strong, admissible heuristic lets it hone in on the goal with far less work, without giving up the guarantee of finding the shortest path.
