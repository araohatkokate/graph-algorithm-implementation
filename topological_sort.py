from collections import defaultdict, deque

def topological_sort(num_nodes, edges):
    # Create adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * num_nodes
    
    # Populate the graph
    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1
    
    # Collect all nodes with in-degree 0
    zero_in_degree = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    topo_order = []
    
    while zero_in_degree:
        current = zero_in_degree.popleft()
        topo_order.append(current)
        
        # Decrease in-degree of neighbors
        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)
    
    # Check if there was a cycle
    if len(topo_order) != num_nodes:
        raise ValueError("Graph is not a DAG, topological sort not possible")
    
    return topo_order

# Test case for Topological Sort
num_nodes = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print("Topological Sort:", topological_sort(num_nodes, edges))
