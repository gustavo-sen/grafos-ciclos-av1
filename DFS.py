def dfs(node, graph, visited, stack):
    # Marcar o nó como visitado e adicioná-lo à pilha de recursão
    visited.add(node)
    stack.add(node)
    
    # Explorar todos os vizinhos
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if dfs(neighbor, graph, visited, stack):
                return True
        elif neighbor in stack:
            # Se o vizinho está na pilha de recursão, encontramos um ciclo
            return True
    
    # Remover o nó da pilha de recursão ao final da exploração
    stack.remove(node)
    return False

def hasLoop(graph):
    visited = set()
    stack = set()
    
    # Verificar todos os nós para cobrir grafos desconexos
    for node in graph:
        if node not in visited:
            if dfs(node, graph, visited, stack):
                return True
    
    return False

