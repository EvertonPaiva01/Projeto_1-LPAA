import matplotlib.pyplot as plt

class Grafico():
    def barra(x,y):
        plt.figure(figsize=(17, 8))
        plt.barh(x,y)
        plt.xlabel('Ocorrência de Fatalidades')
        plt.title('Fatalidades/Ave')
        plt.show()
