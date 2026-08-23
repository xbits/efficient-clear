A* Pathfinding Algorithm

A* is a graph search algorithm that finds the shortest path between a start node and a goal node. It extends Dijkstra's algorithm with a heuristic that estimates the remaining distance to the goal. This heuristic guides the search toward the goal instead of expanding outward in every direction.

How it works

A* keeps two sets of nodes: an open set of nodes to check, and a closed set of nodes already checked. Each node tracks two costs. The value g(n) is the exact cost of the path from the start node to node n. The value h(n) is the heuristic estimate of the cost from node n to the goal. The algorithm ranks nodes by f(n), where f(n) equals g(n) plus h(n).

The algorithm follows these steps:

1. Add the start node to the open set.
2. Pick the node in the open set with the lowest f(n) value.
3. If this node is the goal, stop. The path is complete.
4. Move this node from the open set to the closed set.
5. For each neighbor of this node, compute a new g(n) value through this node.
6. If the neighbor is in the closed set and the new g(n) is not lower, skip it.
7. If the new g(n) is lower than the neighbor's recorded g(n), or the neighbor is not yet in the open set, record the new g(n), set this node as the neighbor's parent, and add the neighbor to the open set.
8. Repeat from step 2 until the open set is empty or the goal is found.

If the open set becomes empty before the algorithm finds the goal, no path exists between the start node and the goal node.

After the algorithm finds the goal, it builds the path by following each node's parent pointer back to the start node, then reverses the sequence.

Key properties

Optimality: A* finds the shortest path when the heuristic never overestimates the true remaining cost. This property is called admissibility.

Consistency: A heuristic is consistent when, for each node n and each neighbor n', h(n) is not greater than the cost from n to n' plus h(n'). A consistent heuristic is also admissible, and it keeps the algorithm from reopening nodes already in the closed set.

Completeness: A* finds a path if one exists, given a finite graph or a graph with a positive minimum edge cost.

Efficiency: A* checks fewer nodes than Dijkstra's algorithm when the heuristic gives useful information, because the heuristic directs the search toward the goal. A heuristic of zero for every node reduces A* to Dijkstra's algorithm. A heuristic that matches the true remaining cost exactly makes the search follow the shortest path directly, with no extra nodes checked.

Common heuristics: for a grid, common choices are the Manhattan distance for four-direction movement and the Euclidean distance for movement in any direction. Both stay admissible when they never exceed the true cost.
