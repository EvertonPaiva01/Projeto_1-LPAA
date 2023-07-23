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

#Grafico.plot(ano.index,ano.values,'Evolução dos aceidentes ao longo dos Anos','Ano')


#-----------------------------------Locais onde ocorre mais colisões----------------------------------------------------------------------#
#Dicionario que armazenará locais e valores das colisões
colisoes = {}
for col in df.columns:
    col_sep = col.split(' ')
    #No col cada termo que trata de colisão, o Strike aparece na segunda posição [1]
    if len(col_sep) > 1 and col_sep[1] == 'Strike':
        colisoes[col_sep[0]] = df[col_sep[0] + ' Damage'].sum() / df[col].sum()                        

#Grafico.barra(list(colisoes.keys()),list(colisoes.values()),'Alta ocorrência de colisão (%)','')

#----------------------------------------------Análise QUALITATIVA ----------------------------------------------------------------------#
# Verificando a especie que colidiu mais vezes com aeronaves 
especies = df["Species Name"]
qtd_colisao_especies=especies.value_counts()


#---------------------Removendo dados com baixa frequencia foram retirados da análise (cerca de 2%)-------------------------------------#

#Selecionando dados com ocorrência acima de 2.000 (duas mil) colisões:
qtd_colisao_especies=qtd_colisao_especies[qtd_colisao_especies>4000]

#Total de Colisões
total_colisoes = df['Species Name'].count()

#Baixa ocorrência
baixa_ocorrencia = total_colisoes - qtd_colisao_especies.sum()

qualitativa = list(qtd_colisao_especies.values)
qualitativa.append(baixa_ocorrencia)

label = list(qtd_colisao_especies.keys())
label.append('Baixa Ocorrência')

Grafico.pie(qualitativa,'Especies envolvidas com maior frequência\n em colisões com aeronaves',label,'')


#https://www.kaggle.com/code/ronymayukh/vital-data-visualisation