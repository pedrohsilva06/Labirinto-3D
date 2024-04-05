import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

class Labirinto:
    def __init__(self):
        self.labirinto = np.random.randint(-100, 101, size=(10, 10, 10))
        self.visitados = []
        self.total_coletado = 0
        self.max_coletas = 2000

    def coletar_guloso(self, xi, yi, zi, xf, yf, zf):
        self.visitados = [(xi, yi, zi)]
        self.total_coletado += self.labirinto[xi][yi][zi]

        while self.total_coletado < self.max_coletas:
            if xi == xf and yi == yf and zi == zf:
                break

            vizinhos = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dz in [-1, 0, 1]:
                        if abs(dx) + abs(dy) + abs(dz) == 1:
                            x, y, z = xi + dx, yi + dy, zi + dz
                            if 0 <= x < 10 and 0 <= y < 10 and 0 <= z < 10 and (x, y, z) not in self.visitados:
                                vizinhos.append((x, y, z))

            if not vizinhos:
                break

            max_valor = -101
            proximo = None
            for x, y, z in vizinhos:
                if self.labirinto[x][y][z] > max_valor:
                    max_valor = self.labirinto[x][y][z]
                    proximo = (x, y, z)

            xi, yi, zi = proximo
            self.visitados.append((xi, yi, zi))
            self.total_coletado += self.labirinto[xi][yi][zi]

    def plotar_labirinto(self, xi, yi, zi, xf, yf, zf):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(xi, yi, zi, c='green', marker='o', label='Inicial')
        ax.scatter(xf, yf, zf, c='red', marker='o', label='Final')

        for i in range(len(self.visitados) - 1):
            xi, yi, zi = self.visitados[i]
            xf, yf, zf = self.visitados[i + 1]
            ax.plot([xi, xf], [yi, yf], [zi, zf], c='black')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        
        plt.show()
        

if __name__ == '__main__':
    while True:
        lab = Labirinto()
        xi, yi, zi = np.random.randint(0, 10, size=3)
        xf, yf, zf = np.random.randint(0, 10, size=3)
        while (xi, yi, zi) == (xf, yf, zf):
            xi, yi, zi = np.random.randint(0, 10, size=3)
            xf, yf, zf = np.random.randint(0, 10, size=3)

        lab.coletar_guloso(xi, yi, zi, xf, yf, zf)
        print("Valor total coletado:", lab.total_coletado)
        lab.plotar_labirinto(xi, yi, zi, xf, yf, zf)
        plt.close()