"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
Aircraft Wildlife Strikes, 1990-2015

@author: EvertonPaiva01

"""

#Importando as bibliotecas que serão utilizadas no projeto
import numpy as np
from grafico import Grafico
from dados import Dados

#Tratando dados NaN
df = Dados.tratados()

#-----------------------------------Colisão de Aves com Aeronave---------------------------------------------------------------------------#
# Especie das aves
especie_ave = np.array(df['Species Name'].loc[(df['Fatalities'] > 0) & (df['Species Name'] != 'WHITE-TAILED DEER')])

#Ocorrência de Fatalidade
fatalidade = np.array(df['Fatalities'].loc[(df['Fatalities'] > 0) & (df['Species Name'] != 'WHITE-TAILED DEER')])

# Aves que provocaram acidentes fatais
#Grafico.barrah(especie_ave,fatalidade.astype(int),'Espécie da Ave por ocorrência de Fatalidade','Ocorrência de Fatalidades')


#-----------------------------------Incidente ao longo dos Anos---------------------------------------------------------------------------#
#Ocorrência de acidentes ao longo dos Anos:
ano = df['Incident Year'].value_counts().sort_index()

#Grafico.barra(ano.index,ano.values,'Número de Acidentes ao longo dos Anos','Ano')


#-----------------------------------Locais onde ocorre mais colisões----------------------------------------------------------------------#
#Dicionario que armazenará locais e valores das colisões
colisoes = {}
for col in df.columns:
    col_sep = col.split(' ')
    #No col cada termo que trata de colisão, o Strike aparece na segunda posição [1]
    if len(col_sep) > 1 and col_sep[1] == 'Strike':
        colisoes[col_sep[0]] = df[col_sep[0] + ' Damage'].sum() / df[col].sum()                        

Grafico.barra(list(colisoes.keys()),list(colisoes.values()),'Alta ocorrência de colisão (%)','')
