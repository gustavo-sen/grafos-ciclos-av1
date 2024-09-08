import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Dicionário para armazenar a lista de adjacência
grafo = {}

def connect_node(start_node, end_node=''):
    # Adiciona o nó de destino ao grafo e ao dicionário se ele não existir
    if end_node and end_node not in grafo:
        grafo[end_node] = []
        G.add_node(end_node)

    # Adiciona o nó de início ao grafo e ao dicionário se ele não existir
    if start_node not in grafo:
        grafo[start_node] = []
        G.add_node(start_node)

    # Adiciona a aresta
    if end_node:
        grafo[start_node].append(end_node)
        grafo[end_node].append(start_node)  # Atualiza a lista de adjacência de end_node
        G.add_edge(start_node, end_node)

def remove_node(node_name):
    if node_name not in grafo:
        print(f"Node {node_name} not found")
        return
    
    # Remove as arestas associadas ao nó
    for neighbor in grafo[node_name]:
        G.remove_edge(node_name, neighbor)
        grafo[neighbor].remove(node_name)
    
    # Remove o nó do grafo e do dicionário
    G.remove_node(node_name)
    del grafo[node_name]

    print(f"Node {node_name} removed")

# Adicionar nós e arestas
connect_node('A', 'B')
connect_node('A', 'C')
connect_node('B', 'C')

# Exibir o grafo
nx.draw(G, with_labels=True)
plt.show()

# Remover um nó
remove_node('B')

# Exibir o grafo atualizado
nx.draw(G, with_labels=True)
plt.show()