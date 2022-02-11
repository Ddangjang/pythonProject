def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited