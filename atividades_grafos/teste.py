from meu_grafo_lista_adj_nao_dir import MeuGrafo

GrafoTeste = MeuGrafo()

GrafoTeste.adiciona_vertice("J")
GrafoTeste.adiciona_vertice("K")
GrafoTeste.adiciona_vertice("C")
GrafoTeste.adiciona_vertice("B")
GrafoTeste.adiciona_vertice("A")
GrafoTeste.adiciona_vertice("L")
GrafoTeste.adiciona_vertice("M")

GrafoTeste.adiciona_aresta("a1", "J", "K")
GrafoTeste.adiciona_aresta("a2", "J", "M")
GrafoTeste.adiciona_aresta("a3", "J", "L")
GrafoTeste.adiciona_aresta("a4", "J", "A")
GrafoTeste.adiciona_aresta("a5", "J", "C")

GrafoTeste.ha_laco()  