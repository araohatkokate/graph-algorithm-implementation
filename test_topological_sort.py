from topological_sort import topological_sort

def is_valid_topological_order(order, num_nodes, edges):
    # Create a map of positions for quick lookup
    position = {node: index for index, node in enumerate(order)}
    
    # Verify all edges follow the topological order
    for u, v in edges:
        if position[u] >= position[v]:
            return False
    return True

def test_topological_sort_simple():
    num_nodes = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    result = topological_sort(num_nodes, edges)
    assert is_valid_topological_order(result, num_nodes, edges), "Invalid topological order"

def test_topological_sort_disconnected():
    num_nodes = 4
    edges = [(0, 1), (2, 3)]
    result = topological_sort(num_nodes, edges)
    assert is_valid_topological_order(result, num_nodes, edges), "Invalid topological order for disconnected graph"

