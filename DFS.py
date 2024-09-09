tempo = 0
ciclo = False
cor = {}  
descoberta = {}  
termino = {}  
predecessor = {}  

def hasLoop(grafo):
    global ciclo
    for vertice in grafo:
        cor[vertice] = 'branco'  # Todos começam como brancos
        predecessor[vertice] = None  
    for vertice in grafo:
        if cor[vertice] == 'branco':
            ciclo = dfs_visit(grafo, vertice)
    return ciclo


def dfs_visit(grafo, vertice):
    global tempo, ciclo
    cor[vertice] = 'cinza'  # Vértice está sendo descoberto
    tempo += 1
    descoberta[vertice] = tempo  # Tempo de descoberta
    
    # Explora cada adjacente
    for adjacente in grafo[vertice]:
        if cor[adjacente] == 'branco': 
            predecessor[adjacente] = vertice
            dfs_visit(grafo, adjacente)
        elif cor[adjacente] == 'cinza':
            ciclo = True       
    
    cor[vertice] = 'preto'  # Vértice terminado
    tempo += 1
    termino[vertice] = tempo  # Tempo de término
    return ciclo