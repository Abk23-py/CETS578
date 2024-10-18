
import heapq

def shortest_path(graph, start):
    # Create a priority queue to hold nodes to be processed
    queue = [(0, start)]

    # Create a dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Create a dictionary to store the previous node in the shortest path
    previous = {node: None for node in graph}

    while queue:
        # Get the node with the shortest distance from the queue
        current_distance, current_node = heapq.heappop(queue)

        # If we've already found a shorter path to this node, skip it
        if current_distance > distances[current_node]:
            continue

        # For each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the distance to the neighbor through the current node
            distance = current_distance + weight

            # If this path is shorter than the previous shortest path, update the distances and previous node
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Build the shortest path by backtracking from the end node
    path = []
    current_node = 'D'  # Change this to the end node
    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]
    path.reverse()

    # Print the shortest path and its length
    print("Shortest path:", path)
    print("Length:", distances['D'])  # Change this to the end node

    # Print the assigned value at each vertex
    print("Assigned values:")
    for node, distance in distances.items():
        print(node, distance)
        
#Example
graph = {
    'A': {'B': 6, 'C':8 },
    'B': {'C': 3, 'D': 5},
    'C': {'D': 4},
    'D': {}
}

shortest_path(graph, 'A')


