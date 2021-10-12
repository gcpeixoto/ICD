#!/usr/bin/env python
# coding: utf-8

# ## Questionário 41 (Q41)

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

# **Questão 1.** No _dataset_ [enem2019.xlsx](https://github.com/gcpeixoto/ICD/blob/main/database/enem2019.xlsx), estão disponíveis as notas médias por estado obtidas nas provas do ENEM 2019. A partir da série que contém a média das notas da prova de Ciências Humanas, converta os valores para inteiro, faça uma distribuição de frequências e calcule a amplitude _h_ dos intervalos de classe, se divididos uniformemente. Marque a alternativa que corresponde ao valor correto de _h_ e à classe cuja frequência é 3.
# 
# A. _h_ = 8 e [499,509)
# 
# B. _h_ = 10 e [499,509)
# 
# C. _h_ = 9 e [509,519)
# 
# D. _h_ = 10 e [509,519)

# <hr>
# 
# ## Gabarito
# 
# Alternativa **B**

# In[2]:


import pandas as pd
import numpy as np


# In[4]:


df = pd.read_excel("../database/enem2019.xlsx")
df = df.set_index("Estado")
df.head()


# In[27]:


# Coluna a ser avaliada
dados = df['Média da nota da prova de Ciências Humanas'].apply(lambda x: int(x))
dados.sort_values().head()


# In[14]:


# binning usando np.ceil
def binning(d,rule='standard'):       
    
    if isinstance(d,list): d = np.array(d)
    n = len(d)            
    
    if rule == 'standard':
        if n <= 25: K = 5
        else: K = int(np.ceil(np.sqrt(n)))
            
    if rule == 'sturges': 
        K = int(np.ceil(1 + 3.22*np.log10(n)))

    return K


# In[15]:


K1,K2 = binning(dados,rule='standard'), binning(dados,rule='sturges'); 
K1,K2


# In[16]:


R = np.max(dados) - np.min(dados)
h = np.ceil(R/K1);R,h


# In[17]:


bin_ = [np.min(dados) + i*h.astype('int') for i in range(K1+1)];bin_


# In[21]:


f_r = pd.cut(dados, bins=bin_, right=False)
f = f_r.value_counts()

for a in f.items():
    if a[1] == 3:
        interval = (a[0])
        
f'Resposta esperada: h = {h} // {interval}'


# <hr>
# 
# **Questão 2.** Considerando a série que contém a média das notas da prova de Matemática apenas para os estados nordestinos, assinale a alternativa que corresponde ao valor médio aproximado dessas médias, a mediana e a moda, se houver.
# 
# A. 504.27, 502.84, unimodal
# 
# B. 505.27, 502.84, 9
# 
# C. 504.27, 502.84, amodal
# 
# D. 504.27, 503.84, 8

# <hr>
# 
# ## Gabarito 
# 
# **Alternativa C**

# In[76]:


nordeste = ["AL","BA","CE","MA","PB","PE","PI","RN","SE"]

dados2 = df.loc[nordeste,'Média da nota da prova de Matemática']
dados2 = dados2.sort_values()

if len(dados2.mode()) > 1:
    Mo = 'amodal' 
else:
    Mo = np.round(dados2.mode(),2)

f'Resposta esperada: {np.round(dados2.mean(),2)}, {np.round(dados2.median(),2)}, {Mo}'


# <hr>
# 
# **Questão 3.** Levando em conta a série que contém as médias das notas da prova de Redação apenas para os estados nordestinos, assinale a alternativa correta quanto ao quartil em que o estado da Paraíba se encontrou nesta prova.
# 
# A. 4-quartil
# 
# B. 3-quartil
# 
# C. 2-quartil
# 
# D. 1-quartil
# 

# <hr>
# 
# ## Gabarito
# Alternativa **B**

# In[86]:


def quartil(a):
    for a in dados3.quantile([0.0,0.25,0.50,0.75,1]).items():
        if a[1] == dados3.PB:

            if a[0] <= 0.25:
                print("Está no primeiro quartil")  

            elif a[0] <= 0.50:
                print("Está no segundo quartil")

            elif a[0] <= 0.75:
                print("Está no terceiro quartil")

            else:
                print("Está no quarto quartil")


# In[87]:


dados3 = df.loc[nordeste,'Média da nota da prova de redação']
dados3 = dados3.sort_values()
quartil(dados3)

