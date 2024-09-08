# Grafo representado como um dicionário de listas de adjacências
grafo = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': ['A', 'C'],
    'E': ['F','G'],
    'F':['B'],
    'G':['F','D']
}



# Inicialização de variáveis
tempo = 0
ciclo = False
cor = {}  
descoberta = {}  
termino = {}  
predecessor = {}  


def dfs(grafo):
    
    for vertice in grafo:
        cor[vertice] = 'branco'  # Todos começam como brancos
        predecessor[vertice] = None  

    for vertice in grafo:
        if cor[vertice] == 'branco':
            dfs_visit(vertice)


def dfs_visit(vertice):
    global tempo, ciclo
    cor[vertice] = 'cinza'  # Vértice está sendo descoberto
    tempo += 1
    descoberta[vertice] = tempo  # Tempo de descoberta
    
    # Explora cada adjacente
    for adjacente in grafo[vertice]:
        if cor[adjacente] == 'branco': 
            predecessor[adjacente] = vertice
            dfs_visit(adjacente)
        elif cor[adjacente] == 'cinza':
            ciclo = True
    
    cor[vertice] = 'preto'  # Vértice terminado
    tempo += 1
    termino[vertice] = tempo  # Tempo de término

def adicionar_no(grafo, no1, no2):
    grafo[no1] = no2

# Executa o DFS no grafo
dfs(grafo)

# Saída dos tempos de descoberta e término

print("\nTempos de descoberta e término:")
for vertice in grafo:
    print(f"{vertice}: {descoberta[vertice]}/{termino[vertice]}")

if ciclo:
    print("tem ciclo")
else:
    print("não tem ciclo")


