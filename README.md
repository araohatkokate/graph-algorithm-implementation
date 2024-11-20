# Graph Algorithms Implementation

This repository contains implementations of the following graph algorithms as part of an assignment:

1. **Topological Sort**: Orders vertices of a Directed Acyclic Graph (DAG) such that for every directed edge `u -> v`, vertex `u` appears before `v`.
2. **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
3. **Kruskal's Algorithm**: Finds the Minimum Spanning Tree (MST) of a graph using a greedy approach.


## Algorithms

### 1. Topological Sort
- **Input**: Number of nodes and a list of directed edges.
- **Output**: A valid topological ordering of the nodes.
- **Key Features**:
  - Implemented using Kahn's Algorithm.
  - Detects cycles in the graph.

### 2. Depth-First Search (DFS)
- **Input**: A graph (adjacency list) and a starting node.
- **Output**: Nodes visited in DFS order.
- **Key Features**:
  - Recursive implementation.
  - Prints the traversal path.

### 3. Kruskal's Algorithm
- **Input**: Number of nodes and a list of edges with weights.
- **Output**: Minimum Spanning Tree (MST) and its cost.
- **Key Features**:
  - Uses Union-Find for cycle detection.
  - Finds the MST of a weighted graph.

## Requirements

- Python 3.8 or higher
- Libraries: `pytest` (for testing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name ```
2. Install pytest for testing:
```bash
pip install pytest
```
## Usage
1. Run the algorithm individually:
```bash
python filename.py
```
2. Test the algorithms using
 ```bash
 pytest
 ```
3. Test individual algorithms using
```bash
pytest filename.py
```

   






