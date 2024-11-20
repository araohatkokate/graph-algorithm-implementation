import pytest
from depth_first_search import dfs

def test_dfs_traversal(capsys):
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [3]
    }
    dfs(graph, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 0 1 3"

def test_dfs_single_node(capsys):
    graph = {
        0: []
    }
    dfs(graph, 0)
    captured = capsys.readouterr()
    assert captured.out.strip() == "0"

def test_dfs_disconnected_graph(capsys):
    graph = {
        0: [1],
        1: [],
        2: [3],
        3: []
    }
    dfs(graph, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "2 3"
