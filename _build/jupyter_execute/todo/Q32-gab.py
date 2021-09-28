#!/usr/bin/env python
# coding: utf-8

# ## Questiónario Q32 - Pandas Data Frames
# 
# Monitor: Vladimir Yuri

# ## Questão 1
# 
# ### Para criar uma Data Frame utilizamos a função pd.DataFrame()
# 
# #### Marque a alternativa verdadeira sobre os parâmetros da função pd.DataFrame()

# a. (dados, index, colums) = o parâmetro "index" rotula as linhas do DataFrame.
# 
# b. (dados, columns, lines) = "dados" serão os dados utilizados para vizualizar no DataFrame.
# 
# c. (dados, index, colums) = o parâmetro "columns" printa somente as colunas do DataFrane.
# 
# d. (index, columns, dados) = "index" se refere aos índices do DataFrame.
# 
# RESPOSTA CORRETA: A

# ## Questão 2
# 
# ### Quais são as funções utilizadas para vizualizar respectivamente as cinco primeiras e cinco últimas de um Data Frame chamado "data_frame"?
# 

# a. data_frame.begin() e data_frame.last()
# 
# b. data_frame.head() e data_frame.last()
# 
# c. data_frame.head() e data_frame.tail()
# 
# d. data_frame.first(5) e data_frame.tail()
# 
# RESPOSTA CORRETA: C

# ## Questão 3
# 
# ### Três carros saíram de João Pessoa - PB e foram enviados para 3 localidades diferentes. 
# 
# #### Carro 1 para Bahia(848 Km) e gastou 7h e 30 min.
# #### Carro 2 para Fortaleza(728 Km) e gastou 10h.
# #### Carro 3 para Sergipe(640 Km) e gastou 9h e 30 min.
# 
# ### Crie um DataFrame com esses dados, depois crie uma nova coluna com a Velocidade Média de cada carro e crie um programa para printar o carro que teve a Velocidade Média mais alta.

# a. Carro 2 = 125,06 Km/h
# 
# a. Carro 1 = 113,06 Km/h
# 
# c. Carro 1 = 115,45 Km/h
# 
# d. Carro 3 = 110,8 Km/h

# In[30]:


# RESOLUÇÃO:

import numpy as np
import pandas as pd

carros_distancia = pd.Series({'Carro 1': 848, 'Carro 2': 728, 'Carro 3': 640}, name = "Distancia")
carros_tempo = pd.Series({'Carro 1': 7.5, 'Carro 2': 10, 'Carro 3': 9.5}, name = "Velocidade")

carros_dict = {'Distancia': carros_distancia, 'Velocidade': carros_tempo}

carros_dataframe = pd.DataFrame(carros_dict)

carros_dataframe["Km/h"] = carros_dataframe["Distancia"]/carros_dataframe["Velocidade"]

for i in range(len(carros_dataframe)):
    
    if(carros_dataframe["Km/h"][i] > maior):
        maior = carros_dataframe["Km/h"][i]
        
        
print(maior)

# RESPOSTA CORRETA: A


# In[ ]:




