import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Labirinto:
    def __init__(self):
        self.labirinto = np.random.randint(-100, 101, size=(10, 10, 10))
        self.visitados = []
        self.max_coletas = 1000
        self.maior_valor = -float('inf')
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

    def coletar_backtracking(self, xi, yi, zi, xf, yf, zf, valor_atual=0, coletas=0):
        print(f"Posição atual: ({xi}, {yi}, {zi})")

        if coletas >= self.max_coletas:
            print("Número máximo de coletas excedido!")
            return

        if (xi, yi, zi) in self.visitados:
            print("Posição já visitada.")
            return

        if xi == xf and yi == yf and zi == zf:
            if valor_atual > self.maior_valor:
                self.maior_valor = valor_atual
                self.visitados.append((xi, yi, zi))
                print(f"Posição final encontrada: ({xi}, {yi}, {zi})")
            return

        if 0 <= xi < 10 and 0 <= yi < 10 and 0 <= zi < 10:
            self.visitados.append((xi, yi, zi))
            valor_atual += self.labirinto[xi][yi][zi]
            coletas += 1

            if valor_atual > self.maior_valor:
                self.maior_valor = valor_atual

            self.ax.clear()
            for x, y, z in self.visitados:
                self.ax.scatter(x, y, z, c='black')
            self.ax.scatter(xi, yi, zi, c='red', marker='o')
            self.ax.set_xlabel('X')
            self.ax.set_ylabel('Y')
            self.ax.set_zlabel('Z')
            self.ax.set_title(f'Total coletado até agora: {valor_atual}\nTotal de coletas até agora: {coletas}')
            plt.pause(0.1)

            print(f"Valor coletado: {self.labirinto[xi][yi][zi]}")
            print(f"Total coletado até agora: {valor_atual}")
            print(f"Total de coletas até agora: {coletas}")

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dz in [-1, 0, 1]:
                        if abs(dx) + abs(dy) + abs(dz) == 1:
                            self.coletar_backtracking(xi + dx, yi + dy, zi + dz, xf, yf, zf, valor_atual, coletas)

    def plotar_labirinto(self):
        plt.show()

if __name__ == '__main__':
    lab = Labirinto()
    lab.coletar_backtracking(0, 0, 0, 9, 9, 9)
    print("Maior valor coletado:", lab.maior_valor)
    lab.plotar_labirinto()