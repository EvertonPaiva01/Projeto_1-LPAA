import pandas as pd

class Dados:
    def tratados():
        #Carregando o arquivo dataset
        dataset = pd.read_csv(r'D:/POLI - UPE\2023.1\LPAA\dataset\database.csv')
        return dataset.fillna(0)