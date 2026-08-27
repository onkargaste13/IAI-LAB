import heapq

# Graph: node -> [(neighbor, cost)]
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('D', 2), ('C', 3)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 1)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 1), ('I', 2)],
    'I': [('G', 3), ('H', 2), ('E', 5), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic values h(n) from the image
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

def a_star(start, goal):
    # (f, g, current_node, path)
    priority_queue = [
        (heuristic[start], 0, start, [start])
    ]

    visited = set()

    while priority_queue:

        f, g, current, path = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            return path, g

        # Check neighbours
        for neighbour, cost in graph[current]:

            if neighbour not in visited:

                new_g = g + cost
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float('inf')


# Start = A, Goal = J
path, cost = a_star('A', 'J')

print("Path:", " -> ".join(path))
print("Total Cost:", cost)