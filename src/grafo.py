from functools import total_ordering
import numpy as np
from collections import defaultdict
import time

class Grafo:
  def __init__(self):
    self.adjacency_list = defaultdict(list) 
    self.ordem = 0
    self.tamanho = 0

  def adiciona_vertice(self, rotulo):
    isValid = True
    
    for adjacency in self.adjacency_list:
      if rotulo.replace(" ", "") == adjacency:
        isValid = False
        break

    if not isValid: 
      return
      
    self.ordem += 1
    self.adjacency_list[rotulo.replace(" ", "")]
    return self.adjacency_list

  def adiciona_aresta(self, u,  v,  peso):
    isDuplicated = False

    if len(self.adjacency_list) > 0 and len(self.adjacency_list[u]) > 0:
      index = 0
      for adjacency in self.adjacency_list[u]:
        if adjacency[0] == v:
            list_adjacency = list(self.adjacency_list[u][index])
            list_adjacency[1] += 1
            self.adjacency_list[u][index] = tuple(list_adjacency)
            isDuplicated = True

        index += 1

    if not isDuplicated:
      self.adjacency_list[u].append((v, peso)) 

    return self.adjacency_list    

  def tem_aresta(self, u, v):
    if len(self.adjacency_list[u]) == 0:
      return False
    
    if len(self.adjacency_list[u][v]) > 0:
      return True
    else:
      return False

  def total_vertices(self):
    return self.ordem

  def total_arestas(self):
    total_edges = 0

    for vertex in self.adjacency_list:
      for edge in vertex:
        total_edges += 1

    return total_edges

  def peso(self, u, v):
    peso = ""
    
    for aresta in self.adjacency_list[u]:
      if v in aresta:
        peso = aresta

    if peso == "": 
      #print(f"\n Sem aresta entre {u} e {v}") 
      return

    #print(f"Peso da aresta entre {u} e {v} = {peso[1]}")
    return peso[1]
    
  def grafo_e_euleriano(self):
    isEulerian = True

    for vertex in self.adjacency_list:
      if not self.grau(vertex) % 2:
        isEulerian = False

    return isEulerian

  def grau(self, u):
    return len(self.adjacency_list[u])


  def grau_entrada(self, vertice):
    lista = []
    for vertex in self.adjacency_list:
      for adj in self.adjacency_list[vertex]:
        if adj[0] == vertice:
          lista.append(vertex)

    return len(lista)

  def quantidade_grau_entrada(self):
    print("\n")
    lista = []
    for vertex in self.adjacency_list:
      quant_vertice = self.grau_entrada(vertex)
      lista.append([quant_vertice, vertex])

    lista.sort(reverse=True)
    novaLista = []
    for item in lista:
      novaLista.append([item[1], item[0]])

    return print("20 indiv??duos com maior grau de entrada", novaLista[:20])


  def grau_saida(self, u):
    return len(self.adjacency_list[u])
    
  def quantidade_grau_saida(self):
    lista = []
    for vertex in self.adjacency_list:
      quant_vertice = self.grau_saida(vertex)
      lista.append([quant_vertice, vertex])

    lista.sort(reverse=True)
    novaLista = []
    for item in lista:
      novaLista.append([item[1], item[0]])

    return print("20 indiv??duos com maior grau de saida", novaLista[:20])


  def grau_saida(self, u):
    return len(self.adjacency_list[u])
    
  def get_quantidade_grau_saida(self):
    lista = []
    for vertex in self.adjacency_list:
      quant_vertice = self.grau_saida(vertex)
      lista.append([quant_vertice, vertex])

    lista.sort(reverse=True)
    return print("20 maiores grau de saida", lista[:20])


  def imprime_lista_adjacencias(self):
 
    for i in self.adjacency_list:
      print(f"\n{i}: ")

      j = 0
      while j < len(self.adjacency_list[i]):
        print(f"\b | {self.adjacency_list[i][j]} -> \n", end="")
        j += 1

  def warshall(self):

    matrizAlcancabilidade = np.zeros((self.ordem, self.ordem))
    for i in range(self.ordem):
        for j in range(self.ordem):
          if self.matrizAdjacencias[i][j] != np.inf:
            matrizAlcancabilidade[i][j] = 1

    print(f"M_0:\n {matrizAlcancabilidade}")

    for k in range(self.ordem):
      for i in range(self.ordem):
        for j in range(self.ordem):
          print(f"M[{i}, {j}] <-- M[{i}, {j}] or (M[{i}, {k}] and M[{k}, {j}])")
          matrizAlcancabilidade[i][j] = matrizAlcancabilidade[i][j] or (matrizAlcancabilidade[i][j] and matrizAlcancabilidade[i][j])
          #print(f"M[{i}, {j}] <-- M[{i}, {j}] or (M[{i}, {k}] and M[{k}, {j}])")
      print(f"M_{k+1}: \n {matrizAlcancabilidade} \n")


  def possuiCaminho(self, u, v):
    matrizAlcancabilidade = self.warshall()
    if matrizAlcancabilidade[u][v]:
      return True
    else:
      return False
  
  def get_adjacent(self, u):
    adjacencias = []
    i = 0
    
    if len(self.adjacency_list[u]) != 0:
      while i < len(self.adjacency_list[u]):
        adjacencias.append(self.adjacency_list[u][i][0])
        i += 1

    return adjacencias


  def percorre_largura(self, initialNode, nodeOfInterest):
    start_time = time.time()
    visited = []
    queue = []     
    visited.append(initialNode)
    queue.append(initialNode)

    while len(queue) != 0:
      currentNode = queue.pop(0)

      for neighbour in self.adjacency_list[currentNode]:
        if neighbour[0] == nodeOfInterest:
          finish_time = time.time()
          period = (finish_time - start_time)
          print(f"Tempo de execu????o: {round(period, 4)}s")
          print(f"V??rtices visitados entre {initialNode} e {nodeOfInterest}: ")
          return visited
        else:
          if neighbour not in visited:
            visited.append(neighbour[0])
            queue.append(neighbour[0])
    
    if len(self.adjacency_list[initialNode]) == 0 or nodeOfInterest not in visited:
      return f"O v??rtice {nodeOfInterest} n??o pode ser alcan??ado a partir de {initialNode}"
        
  def vertices_a_x_arestas(self, x, u):
    vertexList = self.adjacency_list[u]
    vertexList = vertexList[:x]
    position = 1

    print(f"\nV??rtices a uma dist??ncia de {x} arestas de {u}: ")
    for vertex in vertexList:
      print(f"\t{position}. {vertex}")
      position += 1

    return vertexList


  def percorre_em_profundidade(self, u, visited, stack):
    currentVertex = u
    visited.append(u)
    isFinish = False

    while((len(visited) != self.ordem) and isFinish == False):
      count = 0
      
      if currentVertex not in stack:
        stack.append(currentVertex)

      if len(self.adjacency_list[currentVertex]) == 0:
        stack.pop()
        if len(stack) == 0: break
        currentVertex = stack[len(stack) - 1]
        continue

      for neighbour in self.adjacency_list[currentVertex]:
        if neighbour[0] in visited:
          if count == (len(self.adjacency_list[currentVertex]) - 1):
            stack.pop()
            if len(stack) == 0: 
              isFinish = True
              break

            currentVertex = stack[len(stack) - 1]
            break

        count += 1

        if neighbour[0] not in visited:
          visited.append(neighbour[0])
          currentVertex = neighbour[0]
          break

    return visited

  def x_alcanca_y_profundidade(self, x, y):
    start_time = time.time()
    visitedList = self.percorre_em_profundidade(x, [], [])
    finish_time = time.time()
    period = (finish_time - start_time)

    if y not in visitedList:
      print(f"\n{x} n??o alcan??a {y} em profundidade")
      return
    else:
      print(f"\n{x} alcan??a {y} em profundidade em {period}s")
      print("Caminho percorrido:")

    position = 1

    for visited in visitedList:
      print(f"\t|{position}: {visited}")
      position += 1
      if visited == y:
        break

  def imprime_maior_caminho_minimo(self):
    caminho_minimo = self.maior_caminho_minimo()
    position = 1

    print(f"\nMaior caminho minimo possui tamanho {len(caminho_minimo)}:")

    for vertex in caminho_minimo:
      print(f"\t| {position}. {vertex}")
      position += 1

  def maior_caminho_minimo(self):
    maiorCaminhoMinimo = []
    for vertex in self.adjacency_list:
      for second_vertex in self.adjacency_list:
        menor_caminho_vertex = self.Dijkstra(vertex, second_vertex)

        if len(menor_caminho_vertex) > len(maiorCaminhoMinimo):
          maiorCaminhoMinimo = menor_caminho_vertex
       
    return maiorCaminhoMinimo

  def Dijkstra(self, source_node, target_node):
    visited = []
    caminho = []
    current_node = source_node

    while len(visited) < self.ordem:
      adjacent_node = current_node
      current_visited = []
      peso = ""

      #caso o n?? n??o tenha n??s adjacentes para o la??o
      if len(self.adjacency_list[adjacent_node]) == 0:
        break

      for node in self.adjacency_list[adjacent_node]:
        node_weight = node[1]
        node_name = node[0]

        #verifica se o n?? foi visitado, se foi, adiciona o n?? em um array
        #para verificar posteriormente se todos os seus n??s adjacentes foram 
        #visitados, para n??o causar um loop infinito
        if node_name in visited:
          current_visited.append(node)
          continue

        #pega o menor peso entre os n??s adjacentes
        if peso == "" or node_weight < peso:
          peso = node_weight
          current_node = node_name

      #Se todos os n??s adjacentes foram visitados, para o while
      if len(current_visited) == len(self.adjacency_list[adjacent_node]):
        break

      caminho.append(current_node)
      visited.append(current_node)
      
      #se for o n?? alvo para a execu????o e retorna o caminho
      if current_node == target_node:
        break

    return caminho