from meu_grafo_matriz_adj_dir import MeuGrafo

g = MeuGrafo()

g.adiciona_vertice("A")
g.adiciona_vertice("B")
g.adiciona_vertice("C")
g.adiciona_vertice("D")
g.adiciona_vertice("E")

g.adiciona_aresta('a1', 'A', 'B')
g.adiciona_aresta('a2', 'A', 'C')
g.adiciona_aresta('a3', 'C', 'D')
g.adiciona_aresta('a4', 'D', 'B')
g.adiciona_aresta('a5', 'B', 'D')
g.adiciona_aresta('a6', 'E', 'C')

h = MeuGrafo()

h.adiciona_vertice("A")
h.adiciona_vertice("B")
h.adiciona_vertice("C")
h.adiciona_vertice("D")

h.adiciona_aresta('a1', 'A', 'B')
h.adiciona_aresta('a2', 'B', 'C')
h.adiciona_aresta('a3', 'C', 'A')
h.adiciona_aresta('a4', 'C', 'D')



print(h.warshall())