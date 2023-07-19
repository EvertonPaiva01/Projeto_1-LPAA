#------Instanciando a classe para gerar os gráficos------#
import matplotlib.pyplot as plt

class Grafico():
    def __init__(self) -> None:
        pass

#------Gerando gráfico de Barra com orientação Horizontal------#
    def barrah(x,y,title,xlabel):
        fig, ax = plt.subplots()
        #fig, ax = plt.subplots(figsize=(15, 6))
        ax.barh(x, y, color='#1f77b4', edgecolor='black')
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel(xlabel)
        plt.yticks(size=7,fontweight='bold')
        plt.show()


#------Gerando gráfico de Barra com orientação Vertical------#
    def barra(x,y,title,xlabel):
        fig, ax = plt.subplots()
        bars = ax.bar(x, y, color='#1f77b4', edgecolor='black')
        # Adicionar os valores acima das colunas de forma suave
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=8)

        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel(xlabel)
        plt.show()

