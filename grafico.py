import matplotlib.pyplot as plt

class Grafico():
    def barra(x,y):
        fig, ax = plt.subplots()
        #fig, ax = plt.subplots(figsize=(15, 6))
        ax.barh(x,y)
        ax.set_xlabel('Ocorrência de Fatalidades')
        ax.set_title('Espécie da Ave por ocorrência de Fatalidade')
        plt.show()
