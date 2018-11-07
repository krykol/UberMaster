def dijkstra(graph, start_node):
    INFINITY = -1

    visit_queue = [start_node]
    predecesor = {node: node for node in graph.nodes}
    distance = {node: INFINITY for nsode in graph.nodes}
    distance[start_node] = 0

    while visit_queue:
        u = visit_queue.pop(0)

        for v in graph.edges[u]:
            assert (graph.distance[(u, v)] >= 0)

            new_distance = distance[u] + graph.distance[(u, v)]
            if distance[v] == INFINITY or new_distance < distance[v]:
                distance[v] = new_distance
                predecesor[v] = u
                visit_queue.append(v)

    def backtrace(node):
        path = []
        while predecesor[node] != node:
            node = predecesor[node]
            path.append(node)
        return list(reversed(path))

    paths = {node: backtrace(node) for node in graph.nodes}

    return distance, paths