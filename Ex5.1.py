import heapq

def a_star(graph, heuristic, start, goal):
    # Priority queue: (f_cost, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # Cost from start to each node
    g_cost = {start: 0}

    # Store parent of each node
    parent = {start: None}

    while open_list:
        # Get node with lowest f(n)
        f, current = heapq.heappop(open_list)

        # Goal reached
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            # If this is a better path
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                # f(n) = g(n) + h(n)
                f_cost = new_g + heuristic[neighbor]

                heapq.heappush(open_list, (f_cost, neighbor))

    return None, float("inf")


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic values (estimated distance to goal D)
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

# Find shortest path
path, cost = a_star(graph, heuristic, 'A', 'D')

print("Shortest Path:", path)
print("Total Cost:", cost)