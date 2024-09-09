from graph import *
from DFS import *
create_plot()

while True:
    command = input("Adicionar (A), Remover (R), Conectar (C), Sair (X): ").strip().upper()

    if command == 'A':
        node_name = input("Nome do nó: ").strip()
        if node_name:
            connect_node(node_name)
    elif command == 'R':
        node_name = input("Nome do nó a ser removido: ").strip()
        if node_name: 
            remove_node(node_name)
    elif command == "C":
        start_node = input("Nome do nó inicial: ").strip()
        end_node = input("Nome do nó final: ").strip()
        if start_node and end_node: 
            connect_node(start_node, end_node)
    elif command == "X":
        plt.ioff() 
        plt.show() 
        break
    else:
        print("Comando inválido. Tente novamente.")

    update_plot()  
    print("Tem loop?:", dfs(grafo)) 