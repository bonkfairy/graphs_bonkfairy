def bfs(graph, start):
    """Breadth First Search"""
    visited = set()
    queue = [start]
    result = []
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            result.append(node)
            if node in graph:
                queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    
    return result

def dfs(graph, start):
    """Depth First Search"""
    visited = set()
    result = []
    
    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result