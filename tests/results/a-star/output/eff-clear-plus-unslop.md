A* finds the shortest path between two nodes in a graph. It works like Dijkstra's algorithm but uses a heuristic to guess the remaining distance to the goal, so it explores fewer nodes.

The algorithm keeps a priority queue of nodes to visit, ordered by f(n) = g(n) + h(n):

- g(n): the actual cost to reach node n from the start.
- h(n): the heuristic's guess of the cost from n to the goal.
- f(n): the estimated total cost of a path through n.

Steps:

1. Add the start node to the queue with f = h(start).
2. Pop the node with the lowest f value from the queue.
3. If that node is the goal, stop. The path is found.
4. Otherwise, look at each neighbor of the node. Compute a tentative g value: the current node's g plus the cost to move to the neighbor.
5. If this tentative g is lower than the neighbor's known g (or the neighbor has no known g yet), record the current node as the neighbor's best path back, update the neighbor's g, and set its f = g + h. Add the neighbor to the queue.
6. Repeat from step 2 until the queue is empty or the goal is found.
7. If the goal is found, trace the recorded path back from the goal to the start. This is the shortest path.

The heuristic must never overestimate the true remaining cost. This guarantees A* finds the shortest path, not just a short one. A common heuristic for grid-based paths is straight-line distance to the goal.

A* runs faster than Dijkstra's algorithm because the heuristic steers the search toward the goal instead of expanding outward in every direction equally. With a heuristic of zero, A* becomes identical to Dijkstra's algorithm.
