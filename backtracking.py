import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


class Labirinto:
    def __init__(self):
        self.labirinto = np.random.randint(-100, 101, size=(10, 10, 10))
        self.visitados = set()
        self.max_coletas = 1000
        self.maior_valor = -float('inf')
        self.caminho_final = []
        self.caminho_temporario = []

        # Preparação para animação
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def backtracking(self, xi, yi, zi, xf, yf, zf, valor_atual=0):
        if not (0 <= xi < 10 and 0 <= yi < 10 and 0 <= zi < 10):
            return False

        if (xi, yi, zi) in self.visitados or valor_atual <= self.maior_valor - self.labirinto[xi][yi][zi]:
            return False

        valor_atual += self.labirinto[xi][yi][zi]
        self.caminho_temporario.append((xi, yi, zi))

        if xi == xf and yi == yf and zi == zf:
            if valor_atual > self.maior_valor:
                self.maior_valor = valor_atual
                self.caminho_final = list(self.caminho_temporario)
            self.caminho_temporario.pop()
            return True

        self.visitados.add((xi, yi, zi))

        direcoes = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                    (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        random.shuffle(direcoes)

        for dx, dy, dz in direcoes:
            if self.backtracking(xi + dx, yi + dy, zi + dz, xf, yf, zf, valor_atual):
                self.caminho_temporario.pop()
                return True

        self.caminho_temporario.pop()
        return False

    def plotar_labirinto(self, frame):
        self.ax.clear()
        for i, (xi, yi, zi) in enumerate(self.caminho_final[:frame + 1]):
            cor = 'red' if i == frame else ('green' if i == 0 else 'black')
            self.ax.scatter(xi, yi, zi, c=cor, marker='o')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        plt.draw()
        plt.pause(0.01)


if __name__ == '__main__':
    lab = Labirinto()
    lab.backtracking(0, 0, 0, 9, 9, 9)
    print(f"Maior valor coletado: {lab.maior_valor}")
    # Animar
    ani = FuncAnimation(lab.fig, lab.plotar_labirinto,
                        frames=len(lab.caminho_final), repeat=False)
    plt.show()
