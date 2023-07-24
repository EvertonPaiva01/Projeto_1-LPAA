"""
Projeto 1 de LPAA - Análise e Exploração de Dados 
Aircraft Wildlife Strikes, 1990-2015

@author: EvertonPaiva01

"""

#Importando as bibliotecas que serão utilizadas no projeto
import numpy as np
import re
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

pomba = df['Incident Year'].loc[(df['Species Name'] == 'MOURNING DOVE')].value_counts().sort_index()
#Grafico.plot(pomba.index,pomba.values,'Acidentes causados pela MOURNING DOVE\n ao longo dos Anos','Ano')

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
#--- Qual espécie de ave causou mais danos aos aviões

# Verificando a especie que colidiu mais vezes com aeronaves 
especies = df["Species Name"]
qtd_colisao_especies=especies.value_counts()


#--Removendo dados com baixa frequencia foram retirados da análise (cerca de 2%)

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

# Grafico da analise qualitativa
#Grafico.pie(qualitativa,'Especies envolvidas com maior frequência\n em colisões com aeronaves',label,'')

#--Analisando as especies conhecidas que afetam as aeronaves
especies_conhecidas = ["MOURNING DOVE", "GULL","KILLDEER", "AMERICAN KESTREL","BARN SWALLOW"]
especies_conhecidas = especies[especies.isin(especies_conhecidas)]
#print(especies_conhecidas.value_counts())

label2 = especies_conhecidas.value_counts().keys()
 
#Grafico.pie(especies_conhecidas.value_counts(),'Especies que mais colidem com aeronaves',label2,'')


#----------------------------------------------Análise QUALITATIVA ----------------------------------------------------------------------#
#--Parte que são mais propensa a danos em colisões com animais

#Selecionando o cabeçalho do dataset para coletar os dados de dados e colisões de forma automática
atributos = list(df.columns)
dano_x=[]
colisao_x=[]
dano=".*Damage$"
colisao=".*Strike$"
for i in atributos:
    if (re.match(dano, i)):
        dano_x.append(i)
    elif (re.match(colisao, i)):
        colisao_x.append(i)

#Removendo a coluna Aircraft Damage
dano_x=dano_x[1:]

#Selecionando os valores contidos nas células referentes as colunas filtradas anteriormente
dano_y=[]
colisao_y=[]
for i in colisao_x:
    colisao_y.append(df[i].sum())

for i in dano_x:
    dano_y.append(df[i].sum())

#Gráfico das maiores partes danificadas nas aeronaves
#Grafico.barra2(dano_x,dano_y,'Partes danificadas na aeronave','')

#Gráfico das partes atingidas nas aeronaves
#Grafico.barra2(colisao_x,colisao_y,'Partes atingidas na aeronave','')

#--Partes mais danificadas em fução da colisão
dano_por_colisao=[]
partes=[]
for i in range(0,len(colisao_x)):
    dano_por_colisao.append((dano_y[i]/colisao_y[i])*100)
    partes.append(colisao_x[i][:-7])

Grafico.barra2(partes,dano_por_colisao,'Partes mais danificadas em fução da colisão (%)','sim')
