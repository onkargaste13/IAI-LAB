import heapq

# Graph
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3)],
    'C': [('E', 2)],
    'D': [('G', 2)],
    'E': [('G', 3)],
    'G': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 2,
    'E': 3,
    'G': 0
}

def a_star(start, goal):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g

        for neighbour, cost in graph[current]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbour]

                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float('inf')


# Start and Goal
path, cost = a_star('A', 'G')

print("Path:", " -> ".join(path))
print("Total Cost:", cost)