#!/usr/bin/env python
# coding: utf-8

# ## Questionário 32 (Q32)

# Orientações: 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-o à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# 
# <hr>

# In[1]:


import pandas as pd
import numpy as np


# **Questão 1.** Marque a alternativa cujas funções são as utilizadas para imprimir as 4 primeiras e as 6 últimas linhas, respectivamente, de um _DataFrame_ `d`, tal que  `len(d) = 20`.
# 
# A. `df.head(6)`, `df.tail(4)`
# 
# B. `df.head(-6)`, `df.tail(4)`
# 
# C. `df.head(-16)`, `df.tail(6)`
# 
# D. `df.tail(-6)`, `df.tail(4)`

# <hr>
# 
# ## Gabarito
# 
# Alternativa **C**.

# In[2]:


d1 = dict(zip([chr(i) for i in range(97,107)],range(0,10)))
d2 = dict(zip([chr(i) for i in range(65,75)],range(11,21)))
df = pd.DataFrame({'d':d1,'e':d2})
df.head(-16),df.tail(6)


# <hr>
# 
# **Questão 2** No dia 01/08/2021, três veículos saíram de João Pessoa - PB (JPA) com destino a três cidades de outros estados com distâncias (em quilômetros) e durações de viagem (em horas) em relação à origem dadas pelo quadro abaixo. 
# 
# | Veículo | Estado    |Distância de JPA (km) | Duração (h) |
# |--------:|:----------|-----------------:|:-------------|
# |  VW Gol | Bahia     |              848 | 7,5          |
# |  BMW Z4 | Ceará     |              728 | 10           |
# |Chery QQ | Sergipe   |              640 | 9,5          |
# 
# Tendo chegado ao destino, verificou-se por meio de um sistema de monitoramento que às 13:45h desse mesmo dia, todos os veículos haviam registrado no velocímetro uma velocidade igual à velocidade média calculada para o percurso. Entretanto, a partir desse instante, o sistema mostrou que os veículos haviam acelerado de tal forma que, às 13:47h, a velocidade média havia aumentado em 12% de seu valor. 
# 
# Construa um _DataFrame_ `df` que calcule as velocidades e acelerações dos veículos – em unidades de metro e segundo – nos instantes de interesse e defina as variáveis a seguir:
# 
# - `a = df.loc['VW Gol']['Vel. inicial (m/s)']`
# 
# - `b = df.loc['BMW Z4']['Vel. final (m/s)']`
# 
# - `c = df.loc['Chery QQ']['Aceleração (m/s2)']`
# 
# Então, assinale a alternativa que corresponde à tupla `(a,b,c)`, com aproximação de duas casas decimais. 
# 
# A. (10.12, 20.20, 0.01)
# 
# B. (18.71, 20.96, 0.03)
# 
# C. (20.22, 22.65, 0.02)
# 
# D. (31.41, 22.65, 0.02)

# <hr>
# 
# ## Gabarito
# 
# Alternativa **D**:

# In[12]:


del df
import datetime

d = pd.Series({'Veículo': 'VW Gol','Cidade': 'Bahia', 'Distância (km)': 848, 'Duração (h)': 7.5})
e = pd.Series({'Veículo': 'BMW Z4','Cidade': 'Fortaleza', 'Distância (km)': 728, 'Duração (h)': 10})
f = pd.Series({'Veículo': 'Chery QQ','Cidade': 'Sergipe', 'Distância (km)': 640, 'Duração (h)': 9.5})

df = pd.DataFrame({0:d,1:e,2:f}).transpose()
df['Vel. média (km/h)'] = (df['Distância (km)']/df['Duração (h)']).apply(lambda x: round(x,2)) 
df['Vel. média (m/s)'] = (df['Distância (km)']/df['Duração (h)']/3.6).apply(lambda x: round(x,2)) 

# velocidade no trecho
prop = 0.12
df['Vel. inicial (m/s)'] = df['Vel. média (m/s)']
df['Vel. final (m/s)'] = np.round((1.0 + prop)*df['Vel. média (m/s)'],2)

# tempo
t0 = datetime.datetime(year=2021,month=8,day=1,hour=13,minute=45)
tf = datetime.datetime(year=2021,month=8,day=1,hour=13,minute=47)
deltaT = (tf-t0).total_seconds()

df['Tempo inicial'] = t0
df['Tempo final'] = tf
df['Delta t (s)'] = deltaT

# aceleração no trecho
df['Aceleração (m/s2)'] = np.round((df['Vel. final (m/s)'] - df['Vel. inicial (m/s)'])/deltaT,2)
df = df.set_index('Veículo')
df


# In[13]:


a=df.loc['VW Gol']['Vel. inicial (m/s)']
b=df.loc['BMW Z4']['Vel. final (m/s)']
c=df.loc['Chery QQ']['Aceleração (m/s2)']
a,b,c


# <hr>
# 
# **Questão 3.** O _dataset_ encontrado no arquivo [flights.csv](https://github.com/gcpeixoto/ICD/blob/main/database/flights.csv?raw=true) (_Box & Jenkins arline data_) registra a quantidade de passageiros transportados por uma companhia aérea entre 1949 e 1960.
# 
# Utilizando agrupamentos, determine: 
# 
# - `y`: o ano em que o maior número de passageiros foi transportado;
# - `p`: o total de passageiros transportados no ano `y`;
# - `m1, m2, m3`: os 3 meses que, na média, transportaram os maiores números de passageiros ao longo desses anos (TOP 3);
# 
# Assinale a alternativa que corresponde aos valores corretos dessas variáveis na seguinte ordem: `y`, `p`, `(m1,m2,m3)`.

# a. 1957, 4421, (Jul, Ago, Set)
# 
# b. 1960, 5714, (Jul, Ago, Jun)
# 
# c. 1960, 5714, (Nov, Fev, Jan)
# 
# d. 1951, 2042, (Ago, Set, Out)

# <hr>
# 
# ## Gabarito
# 
# Alternativa **B**.
# 

# In[7]:


del df
# RESOLUÇÃO:
df = pd.read_csv("../database/flights.csv")
df_year_soma = df[['year', 'passengers']].groupby(["year"]).sum()
df_year_soma.loc[df_year_soma.idxmax()]


# In[6]:


df[["month","passengers"]].groupby(["month"]).mean().sort_values(by='passengers',ascending=False)

