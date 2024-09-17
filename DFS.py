def dfs(current_node, graph, visited, stack):
    # Marcar o nó como visitado e adicioná-lo à pilha de recursão
    visited.add(current_node)
    stack.add(current_node)
    
    # Explora vizinhos do no atual
    for adjacent_node in graph.get(current_node, []):
        if adjacent_node not in visited:
            if dfs(adjacent_node, graph, visited, stack):
                return True
        elif adjacent_node in stack:
            return True
        # Remover o nó da pilha ao final da exploração
    stack.remove(current_node)
    return False

def hasLoop(graph):
    visited = set()
    stack = set()
    # Verificar todos os nós para cobrir grafos desconexos
    for current_node in graph:
        if current_node not in visited:
            if dfs(current_node, graph, visited, stack) == True:
              return True

    # se chegou aqui é porque não achou ciclos
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']  # Ciclo: A → B → C → A
}

print(hasLoop(graph)) 