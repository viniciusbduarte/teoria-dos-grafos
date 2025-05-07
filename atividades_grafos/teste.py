from meu_grafo_lista_adj_nao_dir import MeuGrafo

GrafoTeste = MeuGrafo()

GrafoTeste.adiciona_vertice("A")
GrafoTeste.adiciona_vertice("B")
GrafoTeste.adiciona_vertice("C")
GrafoTeste.adiciona_vertice("D")

GrafoTeste.adiciona_aresta("a1", "A", "B")
GrafoTeste.adiciona_aresta("a2", "A", "C")
GrafoTeste.adiciona_aresta("a3", "A", "D")
GrafoTeste.adiciona_aresta("a4", "B", "C")
GrafoTeste.adiciona_aresta("a5", "B", "D")
GrafoTeste.adiciona_aresta("a6", "C", "D")


print("Vértices não adjacentes:", GrafoTeste.vertices_nao_adjacentes())  
print("Há laço?", GrafoTeste.ha_laco())                                   
print("Grau de A:", GrafoTeste.grau("A"))                                 
print("Há paralelas?", GrafoTeste.ha_paralelas())                         
print("Arestas sobre o vértice B:", GrafoTeste.arestas_sobre_vertice("B"))  
print("É completo?", GrafoTeste.eh_completo())  
