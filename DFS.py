def dfs(current_node, graph, visited, processing):
    # Marcar o nó como visitado e adicioná-lo à pilha de recursão
    visited.add(current_node)
    processing.add(current_node)
    
    # Explora vizinhos do no atual
    for adjacent_node in graph.get(current_node, []):
        if adjacent_node not in visited:                            # Verifica se o nó já foi visitado
            if dfs(adjacent_node, graph, visited, processing):      # Chamada recursiva para visitar o próximo nó
                return True                                         # Retorna verdadeiro se a chamada detectar um loop
        elif adjacent_node in processing:                           # Verifica se o nó visitado está em processo, detectando assim o loop
            return True                                             # Retorna Verdadeiro se houver loop
    
    processing.remove(current_node)                                 # Remover o nó da pilha ao final da exploração
    return False

def hasLoop(graph):
    visited = set()
    processing = set()
    # Verificar todos os nós para cobrir grafos desconexos
    for current_node in graph:
        if current_node not in visited:
            if dfs(current_node, graph, visited, processing) == True:
              return True

    # se chegou aqui é porque não achou ciclos
    return False


