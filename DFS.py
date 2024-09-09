
def hasLoop(grafo):
    # Inicializa variáveis
    tempo = 0
    cor = {}  
    descoberta = {}  
    termino = {}  
    predecessor = {}  
    
    # Variável para detectar ciclos
    ciclo = False

    # Inicializa todos os vértices
    for vertice in grafo:
        cor[vertice] = 'branco'  # Todos começam como brancos
        predecessor[vertice] = None  

    # Percorre todos os vértices
    for vertice in grafo:
        if cor[vertice] == 'branco':
            if dfs_visit(grafo, vertice, cor, descoberta, termino, predecessor, tempo):
                return True
    
    return False


def dfs_visit(grafo, vertice, cor, descoberta, termino, predecessor, tempo):
    cor[vertice] = 'cinza'  # Vértice está sendo descoberto
    tempo += 1
    descoberta[vertice] = tempo  # Tempo de descoberta
    
    # Explora cada adjacente
    for adjacente in grafo[vertice]:
        if cor[adjacente] == 'branco': 
            predecessor[adjacente] = vertice
            if dfs_visit(grafo, adjacente, cor, descoberta, termino, predecessor, tempo):
                return True
        elif cor[adjacente] == 'cinza':
            # Um ciclo é detectado se você voltar a um nó "cinza"
            return True       
    
    cor[vertice] = 'preto'  # Vértice terminado
    tempo += 1
    termino[vertice] = tempo  # Tempo de término
    return False  # Nenhum ciclo detectado

