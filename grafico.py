#------Instanciando a classe para gerar os gráficos------#
import matplotlib.pyplot as plt

class Grafico():
    def __init__(self) -> None:
        pass

#------Gerando gráfico de Barra com orientação Horizontal------#
    def barrah(x,y,title,xlabel):
        fig, ax = plt.subplots()

        # Gráfico de barra Vertial
        ax.barh(x, y, color='#1f77b4', edgecolor='black')

        # Título e rótulo do eixo x
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel(xlabel)
        plt.yticks(size=7,fontweight='bold')
        plt.show()


#------Gerando gráfico de Barra com orientação Vertical------#
    def barra(x,y,title,xlabel):
        fig, ax = plt.subplots()
        #Variável que recebe o gráfico de barra
        bars = ax.bar(x, y, color='#1f77b4', edgecolor='black')

        # Adiciona os valores acima das colunas
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height + 2, f'{height}', ha='center', va='bottom', fontsize=8)
            
        # Título e rótulo do eixo x
        ax.set_title(title, fontsize=16, fontweight='bold')
        ax.set_xlabel(xlabel)

        # Exibir o gráfico
        plt.show()

    def plot(x,y,title,xlabel):
            fig, ax = plt.subplots()
            # Plotar o gráfico de linhas
            ax.plot(x, y)

            # Adicionar os valores acima de cada pico
            for i in range(len(x)):
                #percorre os anos e plota os valores em cada pico do gráfico
                if x[i] in [1990,1995,2000,2005,2010,2013,2014,2015]:
                    ax.text(x[i], y[i], f'{y[i]}', ha='center', va='bottom', fontsize=7, fontweight='bold')

            # Título e rótulo do eixo x
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel(xlabel)

            # Ajustar o espaço para evitar cortar as legendas
            #plt.tight_layout()

            # Exibir o gráfico
            plt.show()      