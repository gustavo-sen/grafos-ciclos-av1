def hasLoop(graph):
    visited = set()
    stack = set()
    
    for current_node in graph:
        if current_node not in visited:     # Se não visitado
            visited.add(current_node)       # Visito o nó
            stack.add(current_node)         # Adiciono no processamento stack

            for adjacent_node in graph.get(current_node):   # Para cada nó adjacente visite-os
                if adjacent_node not in visited:            # Se nao foi visitado,
                    visited.add(adjacent_node)              # Adicionar em stack
                    stack.add(adjacent_node)                # Adicionar em stack
                elif adjacent_node in stack:                # se ele é adjacente e ja estava em análise há ciclo
                    return True                             
    return False
