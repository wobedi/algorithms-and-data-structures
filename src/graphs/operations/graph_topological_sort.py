def topologically_sort(graph):
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
    # perform dfs on reverse graph and track postorder of visited vertices
    visited[v] = True
    for w in graph.adj(v):
        if visited[w]:
            raise Exception('Graph is cyclic - cannot be topologically sorted')
        _dfs_with_postorder_tracking(w, graph, visited, postorder)
    postorder.append(v)
