import heapq

def BFS(graph, heuristics, start, goal):
    priority_queue = [(heuristics[start], start, [start])] 
    visited = set()
    
    while priority_queue:
        current_heuristic, current_node, path = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return path
            
        if current_node not in visited:
            visited.add(current_node)
            
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    heapq.heappush(priority_queue, (heuristics[neighbor], neighbor, new_path))
                    
    return None

if __name__ == "__main__":
    example_graph={
        'A' : ['B', 'C'],
        'B' : ['D', 'E'],
        'C' : ['F'],
        'D' : [],
        'E' : ['F']
    }
    
    example_heuristics = {
        'A' : 6,
        'B' : 4,
        'C' : 5,
        'D' : 3,
        'E' : 1,
        'F' : 0
    }
    
    start_node = 'A'
    goal_node = 'F'
    
    result_path = BFS(example_graph, example_heuristics, start_node, goal_node)
    
    if result_path:
        print(f"Path found : {' -> '.join(result_path)}")
    else:
        print("No path could be found to the goal.")
