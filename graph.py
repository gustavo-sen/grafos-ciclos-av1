import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Dicionário para armazenar a lista de adjacência
grafo = {}

def create_plot():
    plt.figure(figsize=(8, 6))  # Define o tamanho da figura
    pos = nx.spring_layout(G)  # Posição dos nós
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, 
            edge_color='gray', arrows=True, arrowsize=20)
    plt.title("Grafo Atual")
    plt.ion()  # Ativa o modo interativo
    plt.show()

def update_plot():
    plt.clf()  # Limpa a figura atual
    pos = nx.spring_layout(G)  # Recalcula a posição dos nós
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, 
            edge_color='gray', arrows=True, arrowsize=20)
    plt.title("Grafo Atualizado")
    plt.draw()  # Redesenha a figura
    plt.pause(0.1)  # Pausa para permitir a visualização

def connect_node(start_node, end_node=''):
    
    # Adiciona o nó de início ao grafo e ao dicionário se ele não existir
    if start_node not in grafo:
        grafo[start_node] = []
        G.add_node(start_node)    
    
    # Adiciona o nó de destino ao grafo e ao dicionário se ele não existir
    if end_node != '' and end_node not in grafo:
        grafo[end_node] = []
        G.add_node(end_node)

    # Adiciona a aresta
    if end_node and end_node not in grafo[start_node]:
        grafo[start_node].append(end_node)
        G.add_edge(start_node, end_node)


def remove_node(node_name):
    if node_name not in grafo:
        print(f"Node {node_name} not found")
        return
    
    # Remove todas as arestas que têm o nó como destino
    for other_node in grafo:
        if node_name in grafo[other_node]:
            G.remove_edge(other_node, node_name)
            grafo[other_node].remove(node_name)

    # Remove o nó do grafo e do dicionário
    G.remove_node(node_name)
    del grafo[node_name]

    print(f"Node {node_name} removed")
