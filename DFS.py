
def hasLoop(graph):
    def dfs(node):
        # Marcar o nó como visitado e adicioná-lo à pilha de recursão
        visited.add(node)
        rec_stack.add(node)
        
        # Explorar todos os vizinhos
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                # Se o vizinho está na pilha de recursão, encontramos um ciclo
                return True
        
        # Remover o nó da pilha de recursão ao final da exploração
        rec_stack.remove(node)
        return False
    
    visited = set()
    rec_stack = set()
    
    # Verificar todos os nós para cobrir grafos desconexos
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False
