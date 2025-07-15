import heapq

def dijkstra(graph, start):
    # Distance to all nodes from start; initialized to infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue: (distance_from_start, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we've already found a better path
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If new path is shorter, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
# Graph: adjacency list format
# Each node maps to a list of (neighbor, weight) tuples
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Find shortest paths from 'A'
shortest_paths = dijkstra(graph, 'A')

print(shortest_paths)
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
