A* = graph search algo. Find shortest path start node to goal node, weighted graph.

Combine Dijkstra (guaranteed shortest, no goal direction) + greedy best-first (fast, no guarantee). Best of both.

Core: f(n) = g(n) + h(n).
- g(n) = actual cost start→n so far.
- h(n) = heuristic, estimated cost n→goal.
- f(n) = estimated total cost path thru n.

How work:
1. Open set = frontier nodes, priority queue on f(n). Start: {start}.
2. Closed set = fully explored nodes.
3. Loop: pop lowest-f node from open set. If goal, done — reconstruct path via parent pointers.
4. Else expand neighbors. For each: compute tentative g. If better than known g, update, set parent, push to open set.
5. Move current to closed set. Repeat.

Key properties:
- Optimal IF heuristic admissible (never overestimate true cost to goal).
- Optimal + efficient IF heuristic also consistent/monotone (h(n) ≤ cost(n,n') + h(n') for neighbors) — guarantees no re-expansion needed once closed.
- h(n) = 0 everywhere → degenerates to Dijkstra.
- Better heuristic (closer to true cost, still admissible) → fewer nodes expanded, faster.
- Complete: finds path if one exists (finite graph, positive edge weights).
- Time/space worst case exponential in branching factor, but good heuristic prunes heavy.
- Space bottleneck: stores all generated nodes. Variants (IDA*, SMA*) fix memory tradeoff.

Common heuristics: Euclidean dist, Manhattan dist (grid, 4-dir move), octile dist (grid, 8-dir move).

Use case: pathfinding (games, robotics, GPS nav), any shortest-path search where good goal-distance estimate exists.
