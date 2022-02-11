def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node)
    for adjacent_node in adjacent_graph[cur_node]:
        if adjacent_node not in visited_array:
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)