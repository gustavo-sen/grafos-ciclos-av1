from graph import *
from DFS import *
create_plot()

while True:
    command = input("Adicionar (A), Remover (R), Conectar (C), Sair (X): ").strip().upper()

    if command == 'A':
        node_name = input("Nome do nó: ").strip().capitalize()
        if node_name:
            connect_node(node_name)
    elif command == 'R':
        node_name = input("Nome do nó a ser removido: ").strip().capitalize()
        if node_name: 
            remove_node(node_name)
    elif command == "C":
        start_node = input("Nome do nó inicial: ").strip().capitalize()
        end_node = input("Nome do nó final: ").strip().capitalize()
        if start_node and end_node: 
            connect_node(start_node, end_node)
    elif command == "X":
        plt.ioff() 
        plt.close()
        break
    else:
        print("Comando inválido. Tente novamente.")

    print(grafo)
    print("É cíclico: ", hasLoop(grafo)) 
    update_plot()  