A* finds the shortest path between two nodes in a graph. At each step it looks at the actual cost to reach a node so far, plus an estimate of the cost from there to the goal, and expands whichever node scores lowest on that sum.

The cost so far is g(n). The estimate to the goal is h(n), the heuristic — this is where the real cleverness lives. A* always expands the node that minimizes f(n) = g(n) + h(n). If h never overestimates the true remaining cost, A* is guaranteed to find the shortest path. If h is also consistent, meaning a step's estimated cost never drops faster than its real cost, the algorithm never has to revisit a node once it's closed.

Set h(n) = 0 everywhere and A* becomes Dijkstra's algorithm, exploring outward in every direction with no sense of where the goal is. A good heuristic points the search toward the goal instead, and far fewer nodes end up expanded. On a grid, straight-line distance or Manhattan distance work well, depending on whether diagonal movement is allowed.

The implementation is a priority queue (the open set) ordered by f(n), plus a closed set of nodes already finalized. Pull the lowest-f node. If it's the goal, stop. Otherwise expand its neighbors, compute g and f for each, and push them onto the queue if they're new or reached more cheaply than before. Each node keeps a pointer back to its parent, so once the goal is reached the path comes from walking those pointers backward.

Games use A* for NPC movement, robotics for motion planning, mapping software for routing. Its weak point is memory: the open set can balloon on large graphs. That's the problem IDA* and D* were built to solve, trading some speed or optimality for a smaller footprint or the ability to replan when the environment changes.
