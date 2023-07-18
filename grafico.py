import matplotlib.pyplot as plt

class Grafico():
    def barrah(x,y,title,xlabel):
        fig, ax = plt.subplots()
        #fig, ax = plt.subplots(figsize=(15, 6))
        ax.barh(x,y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        plt.yticks(size=8)
        plt.show()

    def barra(x,y,title,xlabel):
        fig, ax = plt.subplots()
        ax.bar(x,y)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        plt.show()