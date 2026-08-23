A* is a search algorithm that finds the shortest path between two nodes in a weighted graph. It combines two other methods. Like Dijkstra's algorithm, it tracks the exact cost from the start node to each node it visits. Like a greedy best-first search, it also uses an estimate of the cost from each node to the goal. This estimate comes from a heuristic function, written h(n).

A* keeps a priority queue of nodes to visit, called the open set. For each node n in the open set, A* computes f(n) = g(n) + h(n). Here, g(n) is the exact cost from the start node to n. The value h(n) is the heuristic estimate of the cost from n to the goal. At each step, A* removes the node with the lowest f(n) value from the open set. A* then expands this node and examines its neighbors.

For each neighbor, A* computes a new g value through the current node. If this new g value is lower than any g value recorded before for that neighbor, A* updates the neighbor's cost. A* then adds the neighbor to the open set and records the current node as the neighbor's parent. This record lets A* rebuild the full path once it reaches the goal.

A* stops when it removes the goal node from the open set. It then follows the parent records back to the start node. This gives the shortest path.

The heuristic function determines the behavior of A*. If h(n) never overestimates the true cost from n to the goal, the heuristic is admissible. An admissible heuristic guarantees that A* finds the shortest path. The heuristic is consistent when it also satisfies the triangle inequality. For a node n and its neighbor, this means h(n) is at most the cost from n to the neighbor plus h(n) at the neighbor. A consistent heuristic guarantees that A* never revisits a node after it expands the node. As a result, a simple graph-search version of A* stays correct.

The choice of heuristic controls the speed of the search. A heuristic of zero for every node turns A* into Dijkstra's algorithm. This heuristic explores nodes in every direction from the start. A heuristic close to the true remaining cost guides the search toward the goal with fewer expansions. A heuristic that overestimates the true cost can make A* faster. But it can also make A* return a path that is not the shortest path.

A* runs in O(b^d) time in the worst case. Here, b is the branching factor of the graph, and d is the depth of the shortest path. In practice, a good heuristic reduces the number of nodes A* expands. This makes A* far faster than an uninformed search on most real graphs.

Typical uses of A* include pathfinding on grids and road networks, game AI, and robot motion planning.
