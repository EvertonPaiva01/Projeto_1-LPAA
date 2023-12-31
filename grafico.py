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

#------Gerando gráfico de Barra com orientação Vertical------#
    def barra2(x,y,title,realce):
        fig, ax = plt.subplots()
        # Ordenar os dados com base nas alturas (do menor para o maior)
        x_sorted, y_sorted = zip(*sorted(zip(x, y), key=lambda pair: pair[1]))

        #Variável que recebe o gráfico de barra
        #bars = ax.bar(x, y, color='#1f77b4', edgecolor='black')
        bars = ax.bar(x_sorted, y_sorted, color='#1f77b4', edgecolor='black')

        # Adiciona os valores acima das colunas
        for bar in bars:
            height = bar.get_height()
            get_value_bar = bar.get_x() + bar.get_width() / 2
            ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height:.0f}', ha='center', va='bottom', fontsize=8)

        #Criando um destaque para o valor mais significativo do gráfico
        if realce == 'sim':
        # Encontrando o índice da maior coluna
            indice_maior_coluna = y_sorted.index(max(y_sorted))

            # Definindo a cor vermelha para a maior coluna
            bars[indice_maior_coluna].set_color('red')

        # Título e rótulo do eixo x
        ax.set_title(title, fontsize=16, fontweight='bold')
        plt.xticks(rotation=90,fontsize=8)
        
        # Exibir o gráfico
        plt.show()

#------Gerando gráfico de linha------#
    def plot(x,y,title,xlabel):
            fig, ax = plt.subplots()
            # Plotar o gráfico de linhas
            ax.plot(x, y)

            # Adicionar os valores acima de cada pico
            for i in range(len(x)):
                #percorre os anos e plota os valores em cada pico do gráfico da lista dos anos
                if x[i] in [1990,1995,2000,2005,2010,2013,2014,2015]:
                    ax.text(x[i], y[i], f'{y[i]}', ha='center', va='bottom', fontsize=7, fontweight='bold')

            # Título e rótulo do eixo x
            ax.set_title(title, fontsize=16, fontweight='bold')
            ax.set_xlabel(xlabel)

            # Ajustar o espaço para evitar cortar as legendas
            #plt.tight_layout()

            # Exibir o gráfico
            plt.show()      
    
#------Gerando gráfico de pizza------#
    def pie(x,title,label,legenda):
        nomes = label
        #cores=['#4F6272', '#B7C3F3', '#DD7596', '#8EB897']
        cores=['#4F6272', '#B7C3F3', '#DD7596', '#8EB897','#FFB6C1', '#98FB98', '#B0E0E6', '#FFFF99', '#DDA0DD', '#FFDAB9', '#AFEEEE', '#E6E6FA']
        fig, ax = plt.subplots()
        plt.rcParams['figure.figsize'] = (11,7)
        ax.pie(x,wedgeprops={"linewidth": 1, "edgecolor": "black"}, autopct='%1.1f%%',textprops={'color': 'black'},colors=cores,labels=nomes)
        ax.set_title(title, fontsize=16, fontweight='bold')
        if legenda != '':
            plt.legend(legenda)
        plt.show()

#------Gerando gráfico de dispersão------#
    def dispersao(x,y,title,xlabel,ylabel):
        plt.scatter(x,y,c='k')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.show()
