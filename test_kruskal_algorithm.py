import pytest
from kruskal_algorithm import kruskal

def test_kruskal_simple_graph():
    num_nodes = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    mst, mst_cost = kruskal(num_nodes, edges)
    expected_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
    expected_cost = 19
    assert mst == expected_mst
    assert mst_cost == expected_cost

def test_kruskal_disconnected_graph():
    num_nodes = 4
    edges = [
        (0, 1, 10),
        (2, 3, 5)
    ]
    mst, mst_cost = kruskal(num_nodes, edges)
    expected_mst = [(2, 3, 5), (0, 1, 10)]
    expected_cost = 15
    assert mst == expected_mst
    assert mst_cost == expected_cost

def test_kruskal_single_node():
    num_nodes = 1
    edges = []
    mst, mst_cost = kruskal(num_nodes, edges)
    assert mst == []
    assert mst_cost == 0
