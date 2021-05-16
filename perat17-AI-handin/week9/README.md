# Greedy Best First search

We add attributes to the Node object. We add a heuristic and the path cost, to
reach that node. We modify the REMOVE_FIRST function, such that the node which
has the lowest heuristic value is removed. In this way we always choose the Node
to expand, which has the lowest heuristic value. Solution path of this method:

```
State: K - Depth: 3 - Heuristic: 0 - Path cost 11
State: H - Depth: 2 - Heuristic: 1 - Path cost 5
State: D - Depth: 1 - Heuristic: 2 - Path cost 4
State: A - Depth: 0 - Heuristic: 0 - Path cost 0
```

We note that the path cost is not a part of choosing which node to expand. We
see that 3 nodes have been expanded.

# A* Search
With the A* search we need to combine the heuristic and the path cost into the
evaluation function. 

```
State: L - Depth: 3 - Heuristic: 0 - Path cost 10
State: H - Depth: 2 - Heuristic: 1 - Path cost 5
State: D - Depth: 1 - Heuristic: 2 - Path cost 4
State: A - Depth: 0 - Heuristic: 0 - Path cost 0
```

Looking at the graph of the exercise, it can been seen that we have found the
cheapest solution. We notice that the total path cost, is lesser than the
"greedy best-first" solution. However it must also be noted that A* expands many
more nodes than the greedy best-first solution. In fact it expands 13 nodes.


## Weighted A*

We choose to bias in favour of the heuristic (it estimates the cost of reaching
goal from node), as it is admissible (it does not overestimate the cost of
reaching the goal). We say that $h(n)$ dominates $h_1(n)$ if $h$ is better
(expands fewer nodes) than $h_1$ for all nodes $n$.  The idea of a weighted
search is to have a more efficient search, biasing in favour of the best
(dominant) heuristic. We inflate this by $\alpha$. The cost of this will be at
most $\alpha$ times the optimal solution.

We pick $\alpha = 5$

```
Expanded notes:3
Solution path:
State: L - Depth: 3 - Heuristic: 0 - Path cost 10
State: H - Depth: 2 - Heuristic: 1 - Path cost 5
State: D - Depth: 1 - Heuristic: 2 - Path cost 4
State: A - Depth: 0 - Heuristic: 0 - Path cost 0
```

We pick $\alpha = 1.5$

```
Expanded notes:10
Solution path:
State: L - Depth: 3 - Heuristic: 0 - Path cost 10
State: H - Depth: 2 - Heuristic: 1 - Path cost 5
State: D - Depth: 1 - Heuristic: 2 - Path cost 4
State: A - Depth: 0 - Heuristic: 0 - Path cost 0
```

# A* on the Vacuum Cleaner

The solution path of the A*:

```
Expanded notes:3
Solution path:
State: D - Depth: 0 - Heuristic: 0 - Path cost 3
State: C - Depth: 0 - Heuristic: 1 - Path cost 2
State: B - Depth: 0 - Heuristic: 2 - Path cost 1
State: A - Depth: 0 - Heuristic: 3 - Path cost 0
```

