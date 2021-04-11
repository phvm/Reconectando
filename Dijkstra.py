def main():
    class Grafo:
        def __init__(self, vertices):
            self.V = vertices
            self.grafo = {}

        def inserir(self, vert1, vert2, peso):
            if not self.grafo[vert1]:
                self.grafo[vert1] = {}
            if not self.grafo[vert2]:
                self.grafo[vert2] = {}
            self.grafo[vert1][vert2] = peso
            self.grafo[vert2][vert1] = peso

        def dijkstra(self, src, dest):
            men_dist = {}
            antecessor = {}
            nao_visitado = self.grafo
            infinito = float("inf")
            caminho = []
            for node in nao_visitado:
                men_dist[node] = infinito
            men_dist[src] = 0

            while nao_visitado:
                minNode = None
                for node in nao_visitado:
                    if minNode is None:
                        minNode = node
                    elif men_dist[node] < men_dist[minNode]:
                        minNode = node

                for filho, peso in self.grafo[minNode].items():
                    if peso + men_dist[minNode] < men_dist[filho]:
                        men_dist[filho] = peso + men_dist[minNode]
                        antecessor[filho] = minNode
                nao_visitado.pop(minNode)

            atual = dest
            while atual != src:
                try:
                    caminho.insert(0, atual)
                    atual = antecessor[atual]
                except KeyError:
                    print(str(dest) + " não é alcançavel por " + str(src))
                    break
            caminho.insert(0, src)
            if men_dist[dest] != infinito:
                print("O menor caminho é: ", end="")
                print(*caminho, sep=" ")


if __name__ == '__main__':
    main()