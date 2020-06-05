from src.implementations.graphs.representations.graph_directed import Digraph


def topologically_sort(graph) -> [int]:
    """Implements
    https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
    Returns topologically sorted list of vertices in adj list.
    Assumes adj_list is a maximally-connected Directed Acyclic Graph (DAG)
    """
    visited_vertices = [False for v in range(graph.v())]
    postorder = []
    for v in range(graph.v()):
        if not visited_vertices[v]:
            _dfs_with_postorder_tracking(v, graph, visited_vertices, postorder)
    return list(reversed(postorder))


def _dfs_with_postorder_tracking(v, graph, visited: list, postorder: list):
    # Perform dfs on reverse graph and track postorder of visited vertices
    visited[v] = True
    for w in graph.adj(v):
        if visited[w]:
            raise Exception('Graph is cyclic - cannot be topologically sorted')
        _dfs_with_postorder_tracking(w, graph, visited, postorder)
    postorder.append(v)


if __name__ == '__main__':
    DG = Digraph(7)
    edges = [
        (0, 1),
        (1, 2),
        (1, 3),
        (0, 4),
        (4, 5),
        (4, 6)
    ]
    for (v, w) in edges:
        DG.add_edge(v, w)
    print(DG)

    topologically_sorted = topologically_sort(DG)

    assert topologically_sorted == [0, 4, 6, 5, 1, 3, 2]
    print(f'Topologically sorted: {topologically_sorted}')

    """Expect the following to raise error because the graph is cyclic"""
    # DG2 = Digraph(10)
    # edges = [
    #     (0, 9),
    #     (0, 8),
    #     (0, 7),
    #     (1, 2),
    #     (1, 1),
    #     (2, 6),
    #     (2, 9),
    #     (9, 2),
    #     (3, 5),
    #     (6, 9),
    #     (7, 8),
    #     (8, 0),
    #     (0, 8)
    # ]
    # for (v, w) in edges:
    #     DG2.add_edge(v, w)
    # print(DG2)
    # print(f'Topologically sorted: {topologically_sort(DG2)}')
