"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
Aircraft Wildlife Strikes, 1990-2015

@author: EvertonPaiva01

"""

#Importando as bibliotecas que serão utilizadas no projeto
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Carregando o arquivo dataset
df = pd.read_csv(r'D:/POLI - UPE\2023.1\LPAA\dataset\database.csv')

# Especie das aves
especie_ave = np.array(df['Species Name'].loc[(df['Fatalities'] > 0)])

#Tratando o nome das Aves
aves = np.char.replace(especie_ave.astype(str), 'UNKNOWN ', '')

#Ocorrência de Fatalidade
fatalidade = np.array(df['Fatalities'].loc[(df['Fatalities'] > 0)])
legenda = list(aves)

plt.figure(figsize=(18, 8))
plt.barh(aves,fatalidade.astype(int))
plt.ylabel('Número de Fatalidades')
plt.title('Fatalidades/Ave')
plt.legend(legenda)
plt.show()