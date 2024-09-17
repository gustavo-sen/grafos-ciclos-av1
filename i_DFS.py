def hasLoop(graph):
    visited = set()       # Conjunto para nós completamente visitados
    processing = set()    # Conjunto para nós sendo processados (na pilha)

    for start_node in graph:
        if start_node not in visited:
            # Usar uma pilha para DFS iterativo
            node_stack = [(start_node, None)]  # (nó atual, nó pai)

            while node_stack:
                current_node, parent = node_stack[-1]

                # Se o nó já está na pilha de processamento, há um ciclo
                if current_node in processing:
                    return True
                
                # Se o nó não foi visitado, processar
                if current_node not in visited:
                    visited.add(current_node)
                    processing.add(current_node)

                    # Adicionar vizinhos à pilha de DFS
                    has_unvisited_adjacent = False
                    for adjacent_node in graph.get(current_node, []):
                        if adjacent_node not in visited:
                            node_stack.append((adjacent_node, current_node))
                            has_unvisited_adjacent = True
                        elif adjacent_node in processing:
                            # Ciclo detectado
                            return True
                    
                    # Se o nó não tem mais vizinhos não visitados, removê-lo da pilha de processamento
                    if not has_unvisited_adjacent:
                        processing.remove(current_node)
                        node_stack.pop()

                else:
                    # Se já foi visitado, remover da pilha de processamento
                    processing.remove(current_node)
                    node_stack.pop()

    return False

# Exemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A']  # Ciclo: A → B → C → A
}

print(hasLoop(graph))
