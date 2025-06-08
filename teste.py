from meu_grafo_matriz_adj_nao_dir import MeuGrafo

g = MeuGrafo()

g.adiciona_vertice("A")
g.adiciona_vertice("B")
g.adiciona_vertice("C")
g.adiciona_vertice("D")

g.adiciona_aresta('a1', 'B', 'B')
g.adiciona_aresta('a2', 'D', 'C')
g.adiciona_aresta('a3', 'D', 'C')


print(g.eh_completo())