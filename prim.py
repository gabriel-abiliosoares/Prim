import networkx as nx
import heapq

def ler_grafo(caminho):
    G = nx.Graph()  # não direcionado (obrigatório para Prim)

    with open(caminho, 'r') as f:
        for linha in f:
            u, v, peso = linha.strip().split()
            G.add_edge(u, v, weight=float(peso))

    return G

def prim(G, inicio):
    T = set([inicio])   # vértices na árvore
    F = []              # arestas da árvore
    custo = 0

    n = len(G.nodes)

    while len(T) < n:
        valor = float('inf')
        vaux = None
        vnovo = None

        # percorre todos os vértices já na árvore
        for vk in T:
            # percorre todos os vértices fora da árvore
            for vi in G.nodes:
                if vi not in T:
                    # verifica se existe aresta entre vk e vi
                    if G.has_edge(vk, vi):
                        peso = G[vk][vi]['weight']

                        if peso < valor:
                            valor = peso
                            vaux = vk
                            vnovo = vi

        # adiciona a melhor aresta encontrada
        if vnovo is None:
            raise ValueError("Grafo não é conectado!")

        custo += valor
        T.add(vnovo)
        F.append((vaux, vnovo, valor))

    return F, custo


grafo = input("Qual o nome do arquivo do grafo? ")
G = ler_grafo(grafo)

inicio = list(G.nodes)[0]

mst, custo = prim(G, inicio)

print("Arestas da árvore mínima :")
for u, v, p in mst:
    print(f"{u} -> {v} (peso: {p})")

print("\nCusto total:", custo)