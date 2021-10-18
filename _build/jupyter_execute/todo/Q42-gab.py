#!/usr/bin/env python
# coding: utf-8

# ## Questionário 42 (Q42)

# 
# 
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

# **Questão 1.** No _dataset_ [enem2019.xlsx](https://github.com/gcpeixoto/ICD/blob/main/database/enem2019.xlsx), estão disponíveis as notas médias por estado obtidas nas provas do ENEM 2019. Supondo que _x_ é a diferença entre a amplitude da quantidade de inscritos na região Sudeste e a amplitude da quantidade de inscritos na região Norte, e que _y_ é o desvio médio para a série da quantidade total de inscritos de ensino médio público apenas para os estados do sul, assinale a alternativa que corretamente expressa os valores de _x_ e _y_,  nesta sequência.
# 
# **Obs.:** considere apenas a parte inteira do desvio médio.
# 
# A. 149465 e 5690
# 
# B. 169265 e 6593
# 
# C. 149465 e 0
# 
# D. 173921 e 2

# ## GABARITO
# 
# $n =$ **_Quantidade de inscritos da região_**
# 
# $\overline{X}$ = **_Média do total de inscritos de Ensino Público_**
# 
# $X_i$ = $Estado_i$ 
# 
# Alterei o **n** e o desvio da média; alterei o **n** que deveria ser para evitar que os alunos apenas usem _.mad()_ e realizem de fato o desvio médio
# 
# Alternativa **C**
# 
# <hr>

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_excel("../database/enem2019.xlsx")
df = df.set_index("Estado")
df.head()


# In[3]:


norte0 = ["AC","AP","AM","PA","RO","RR","TO"]
alvos = ["Quantidade de Inscritos"]
nortedf = df.loc[norte0,alvos]
sudeste0 = ["ES","MG","RJ","SP"]
sudestedf = df.loc[sudeste0,alvos]


# In[4]:


R_norte = nortedf.values.max() - nortedf.values.min()
R_sudeste = sudestedf.values.max() - sudestedf.values.min()
R_dif = R_sudeste - R_norte


# In[5]:


alvos = ["Quantidade de Inscritos","Total de inscritos de Ensino Médio Público","Total de inscritos de Ensino Médio Privado"]
sul0 = ["PR","RS","SC"]
suldf = df.loc[sul0,alvos]
n = sum(suldf["Quantidade de Inscritos"])
media = suldf["Total de inscritos de Ensino Médio Público"].mean()
DM = sum((suldf["Total de inscritos de Ensino Médio Público"] - media)/n)
f'Resultado esperado: {R_dif} // {DM}'


# <hr>
# 
# **Questão 2.** Calcule o percentual _p_ de inscritos para o ENEM 2019 provenientes do ensino privado de todos os Estados em relação ao total de inscritos no exame, bem como o valor do quociente _v/V_, onde _v_ é a variância para a série do total de inscritos provenientes do ensino público e _V_ a variância para a série do total de inscritos provenientes do ensino privado. Assinale a alternativa correta para _p_ e _v/V_.
# 
# A. 11.4% e 34.48
# 
# B. 15% e 33.45
# 
# C. 12.5% e 36.78
# 
# D. 13.54% e 34.6

# <hr>
# 
# ## GABARITO
# 
# Alternativa **A**

# In[6]:


#RESPOSTA CERTA A)

df4 = df.filter(["Quantidade de Inscritos", "Total de inscritos de Ensino Médio Público", "Total de inscritos de Ensino Médio Privado"])

p = (df4["Total de inscritos de Ensino Médio Privado"].sum() / df4["Quantidade de Inscritos"].sum())*100
v = df4["Total de inscritos de Ensino Médio Público"].var() / df4["Total de inscritos de Ensino Médio Privado"].var()

print("{:.2f}% é a porcentagem do total de inscritos no ENEM do Ensino Médio Privado" .format(p))
print("{:.2f} é o quociente da variância do Total de inscritos de Ensino Médio Público sob o Total de inscritos de Ensino Médio Privado" .format(v))


# <hr>

# **Questão 3.** Defina a nota média $N(x)$ de cada região brasileira $x$ como a média das notas $N_i$ de cada uma das $Q$ grandes áreas de conhecimento que constam da prova do ENEM 2019, isto é,
# 
# $$N(x) =  \frac{ \sum_{i=1}^Q N_i(x)}{Q},$$
# 
# e assinale a alternativa cujas regiões detém o primeiro e o segundo maiores valores de desvio padrão.
# 
# A. Nordeste e Sudeste
# 
# B. Sudeste e Nordeste
# 
# C. Norte e Sul
# 
# D. Sul e Centro-Oeste

# <hr>
# 
# ## GABARITO
# 
# Na verdade é apenas o desvio padrão da nota de cada região.
# 
# Alternativa **B**

# In[7]:


df2 = df.iloc[:,4:]


# In[8]:


nordeste0 = ["AL","BA","CE","MA","PB","PE","PI","RN","SE"]
centro_oeste0 = ["GO","MT","MS","DF"]
norte1 = df2.loc[norte0]
sudeste1 = df2.loc[sudeste0]
nordeste1 = df2.loc[nordeste0]
centro_oeste1 = df2.loc[centro_oeste0]
sul1 = df2.loc[sul0]
df3 = pd.DataFrame({"Nordeste": nordeste1.mean(), "Sudeste":sudeste1.mean(), "Centro-Oeste":centro_oeste1.mean(),
                   "Norte": norte1.mean(), "Sul":sul1.mean()},index=nordeste1.mean().index)


# In[9]:


df3.head()


# In[11]:


df4 = pd.concat([df3.mean(),df3.std()], axis=1)
df4.columns=['Média', 'Desvio padrão']
df4.sort_values(by='Desvio padrão',ascending=False)

