from meu_grafo_lista_adj_nao_dir import MeuGrafo

g = MeuGrafo()

g.adiciona_vertice("1")
g.adiciona_vertice("2")
g.adiciona_vertice("3")
g.adiciona_vertice("4")
g.adiciona_vertice("5")

g.adiciona_aresta('a1', '1', '3')
g.adiciona_aresta('a2', '1', '4')
g.adiciona_aresta('a3', '1', '5')
g.adiciona_aresta('a4', '5', '2')


print(g.eh_arvore())
