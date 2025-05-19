from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from collections import deque 
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):
        
    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {"X-Y", "X-Z", ...}
        Onde X, Z e W são vértices no grafo que não têm uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        nao_adjacentes = set()
        vertices = [v.rotulo for v in self.vertices]
         
        # Cria um conjunto com todos os pares adjacentes
        adjacentes = set()
        for aresta in self.arestas.values():
            v1 = aresta.v1.rotulo
            v2 = aresta.v2.rotulo
            adjacentes.add(frozenset([v1, v2]))

        # Compara todos os pares possíveis
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                par = frozenset([vertices[i], vertices[j]])
                if par not in adjacentes:
                    nao_adjacentes.add(f"{vertices[i]}-{vertices[j]}")
        
        return nao_adjacentes

    def ha_laco(self):
        for a in self.arestas.values():
            if a.v1 == a.v2:
                return True
        return False

    def grau(self, V=''):
        '''


        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()
        grau = 0
        for a in self.arestas.values():
            if a.v1.rotulo == V:
                grau += 1
            if a.v2.rotulo == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas_vistas = set()
        for a in self.arestas.values():
            v1 = a.v1.rotulo
            v2 = a.v2.rotulo
            par = frozenset([v1, v2])
            if par in arestas_vistas:
                return True
            arestas_vistas.add(par)
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()
        resultado = []
        for rotulo, aresta in self.arestas.items():
            if aresta.v1.rotulo == V or aresta.v2.rotulo == V:
                resultado.append(rotulo)
        return resultado

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for i in range(len(self.vertices)):
            for j in range(i + 1, len(self.vertices)):
                v1 = self.vertices[i].rotulo
                v2 = self.vertices[j].rotulo
                conectado = False
                for a in self.arestas.values():
                    if (a.v1.rotulo == v1 and a.v2.rotulo == v2) or (a.v1.rotulo == v2 and a.v2.rotulo == v1):
                        conectado = True
                        break
                if not conectado:
                    return False
        return True
    
    def dfs(self, V=''):
        '''
        Executa uma busca em profundidade (DFS) recursiva a partir do vértice V.
        Retorna um objeto MeuGrafo representando a árvore DFS.
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        grafo_dfs = MeuGrafo()
        grafo_dfs.adiciona_vertice(V)
        visitados = set()

        def dfs_recursiva(u):
            
            visitados.add(u)
            for aresta in self.arestas.values():
                v1 = aresta.v1.rotulo
                v2 = aresta.v2.rotulo

                if v1 == u and v2 not in visitados:
                    grafo_dfs.adiciona_vertice(v2)
                    grafo_dfs.adiciona_aresta(aresta.rotulo, v1, v2)

                    dfs_recursiva(v2)
                    
                elif v2 == u and v1 not in visitados:
                    grafo_dfs.adiciona_vertice(v1)
                    grafo_dfs.adiciona_aresta(aresta.rotulo, v2, v1)

                    dfs_recursiva(v1)


        dfs_recursiva(V)

        return grafo_dfs

