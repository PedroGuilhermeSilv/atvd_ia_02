from collections import deque

class Ambiente:
    def __init__(self, grafo):
        self.grafo = grafo
    
    def get_vizinhos(self, estado):
        return self.grafo[estado]

class Agente:
    def __init__(self, ambiente, estado_inicial, objetivo):
        self.ambiente = ambiente
        self.estado_inicial = estado_inicial
        self.objetivo = objetivo
    
    def buscar_objetivo(self):
        fila = deque([(self.estado_inicial, [self.estado_inicial])])
        visitados = set()

        while fila:
            estado_atual, caminho = fila.popleft()
            if estado_atual == self.objetivo:
                return caminho
            
            if estado_atual not in visitados:
                visitados.add(estado_atual)
                vizinhos = self.ambiente.get_vizinhos(estado_atual)
                for vizinho in vizinhos:
                    fila.append((vizinho, caminho + [vizinho]))
        
        return None

# Exemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

ambiente = Ambiente(grafo)
agente = Agente(ambiente, 'A', 'F')
caminho = agente.buscar_objetivo()

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Não foi possível encontrar um caminho para o objetivo.")
