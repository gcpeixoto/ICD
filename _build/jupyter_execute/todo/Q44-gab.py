#!/usr/bin/env python
# coding: utf-8

# ## Questionário Q44

# Orientações: 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-a à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# 
# <hr>

# In[41]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import scipy as sp
np.set_printoptions(suppress=True)


# **Questão 1.** O _dataset_ [covid19-weekly-trends-in-europe](https://github.com/gcpeixoto/ICD/blob/main/database/covid19-weekly-trends-in-europe.csv) contém tendências semanais de casos de Covid-19 em diferentes países da Europa com referência ao dia 8 de novembro de 2021. Separe a série correspondente ao número de casos nos últimos 7 dias (_Cases in the last 7 days_) entre países pertencentes à União Europeia (_UE_) e não pertencentes à UE (_non-UE_). Assinale a alternativa que associa corretamente o grupo de países ao valor do coeficiente de Pearson.
# 
# A. _non-UE_: 620983827.08
# 
# B. _UE_: 620983827.08
# 
# C. _UE_: 750983827.02
# 
# D. _non-UE_: 8290903184.71

# <hr>
# 
# ## Gabarito
# 
# Alternativa **D**

# This Dataset contains Weekly trends of COVID-19 in different regions of Europe as on November 08, 2021.

# In[2]:


db = pd.read_csv("COVID-19_WEEKLY_TRENDS_IN_EUROPE.csv")
db = db.set_index("Country, Other")
db


# In[3]:


UE = pd.read_html("https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population")
UE = UE[0].dropna()
UE


# In[4]:


#Tem que tratar pois não tem Cyprus no nosso dataset
UE_ = []
out_UE = []
db.index
for i in db.index:
    if i in UE["Country"].values:
        
        UE_.append(i)
    else:
        out_UE.append(i)


# In[5]:


#lista de poíses da união européia presente no dataset
UE_


# In[6]:


#Paises que estão no nosso dataset mas não são da União européia
out_UE


# In[7]:


UE_db = db.loc[UE_]
out_UE_db = db.loc[out_UE]


# In[8]:


# coeficiente de pearson
def p(x):
    return 3*( x.mean() - x.median() )*x.std()


# In[9]:


pp = np.array([p(UE_db['Cases in the last 7 days']), p(out_UE_db['Cases in the last 7 days'])])

p_list = ['Dentro da União Europeia', 'Fora da União Européia']

p_list[np.argmax(pp)],pp


# In[10]:


f'Resposta esperada: {p_list[np.argmax(pp)]} //{pp.max()}'


# <hr>
# 
# **Questão 2.** Analise as seguintes distribuições normais aleatórias:
# 
# ```{figure} ../figs/q/q-44-1.png
# ---
# width: 400px
# name: q44-1
# ---
# ```
# 
# Assinale a alternativa em que as curvas aparecem em ordem crescente de desvio padrão.
# 
# A. (A, B, C, D)
# 
# B. (B, A, D, C)
# 
# C. (B, A, C, D)
# 
# D. (A, B, D, C)

# <hr>
# 
# ## Gabarito
# Alternativa **C** 
# 
# ## LEMBRAR DE CONFERIR O GABARITO DESSA QUESTÃO PROFESSOR
# 

# In[47]:


plt.figure(figsize = (10,5))
#distribuições

dn1 = sp.random.normal(2,10,300);
dn2 = sp.random.normal(-20,5,300);
dn3 = sp.random.normal(40,40,300);
dn4 = sp.random.normal(100,27,300);

#mu = 2 // sigma = 10
count, bins, ignored = plt.hist(dn1, 30, density=True, alpha=0.5,label = 'Curva A')
plt.plot(bins, 1/(10 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 2)**2 / (2 * 10**2) ),linewidth=1.5, color='b')


#mu = -20 // sigma = 5
count, bins, ignored = plt.hist(dn2, 30, density=True, alpha=0.5,label = 'Curva B')
plt.plot(bins, 1/(5 * np.sqrt(2 * np.pi)) * np.exp( - (bins - (-20))**2 / (2 * 5**2) ),linewidth=1.5, color='orange')


#mu = 40 // sigma = 40
count, bins, ignored = plt.hist(dn3, 30, density=True, alpha=0.5, label = 'Curva C')
plt.plot(bins, 1/(40 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 40)**2 / (2 * 40**2) ),linewidth=1.5, color='g')

#mu = 100 // sigma = 27
count, bins, ignored = plt.hist(dn4, 30, density=True, alpha=0.5, label = 'Curva D')
plt.plot(bins, 1/(27 * np.sqrt(2 * np.pi)) * np.exp( - (bins - 100)**2 / (2 * 27**2) ),linewidth=1.5, color='r')

plt.legend(loc=1);
plt.xticks([])
plt.yticks([-10])
#plt.savefig('../figs/q/q44-1.png')


# In[17]:


sum(dn3)>sum(dn4)


# <hr>
# 
# **Questão 3.** O código
# 
# ```python
# import numpy as np, from scipy.stats import norm
# N, band = 100, 0.5
# 
# np.random.seed(2)
# X = np.concatenate(
#     (np.random.normal(0, 1, int(0.3 * N)),
#      np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]
# Xp = np.linspace(-5, 10, 1000)[:, np.newaxis]
# 
# dens = 0.3*norm(0,1).pdf(Xp[:, 0]) + 0.7*norm(5,1).pdf(Xp[:, 0])
# ```
# gera a distribuição sombreada `dens` apresentada nas figuras de (a) a (d) abaixo. 
# 
# ```{figure} ../figs/q/q-44-2.png
# ---
# width: 400px
# name: q44-2
# ---
# ```
# Com base nos _kernels_ disponíveis na classe `KernelDensity`
# do módulo _scikit-learn_, assinale a alternativa que melhor preeche as lacunas na sentença:
# 
# *"O kernel ______ aproxima a distribuição em ______, ao passo que o kernel ______ aproxima a distribuição mostrada em ______."*
# 
# 
# A. 'linear' / (a) / 'gaussian' / (d)
# 
# B. 'linear' / (b) / 'tophat' / (a)
# 
# C. 'epanechnikov' / (c) / 'linear' / (d)
# 
# D. 'gaussian' / (b) / 'epanechnikov' / (c)

# <hr>
# 
# ## Gabarito
# 
# Alternativa **C**

# In[13]:



from sklearn.neighbors import KernelDensity
from scipy.stats import norm
N = 100 # amostras
band = 0.5 # largura de banda

np.random.seed(2)
X = np.concatenate(
    (np.random.normal(0, 1, int(0.3 * N)),
     np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]
Xp = np.linspace(-5, 10, 1000)[:, np.newaxis]

true_dens = 0.3 * norm(0,1).pdf(Xp[:, 0]) + 0.7 * norm(5, 1).pdf(Xp[:, 0])

# gaussian
kde_gaus = KernelDensity(kernel='gaussian', bandwidth=band).fit(X)
log_dens_gaus = kde_gaus.score_samples(Xp)

# tophat
kde_tophat = KernelDensity(kernel='tophat', bandwidth=band).fit(X)
log_dens_tophat = kde_tophat.score_samples(Xp)

# epanechnikov
kde_epanechnikov = KernelDensity(kernel='epanechnikov', bandwidth=band).fit(X)
log_dens_epanechnikov = kde_epanechnikov.score_samples(Xp)

# linear
kde_linear = KernelDensity(kernel='linear', bandwidth=band).fit(X)
log_dens_linear = kde_linear.score_samples(Xp)

plt.subplot(221)
plt.fill_between(Xp[:,0],true_dens,alpha=0.3)
plt.plot(Xp[:,0],np.exp(log_dens_gaus),c='#ed3411')
plt.xticks([]); plt.yticks([]);
plt.title('(a)')

plt.subplot(222)
plt.fill_between(Xp[:,0],true_dens,alpha=0.3)
plt.plot(Xp[:,0],np.exp(log_dens_tophat),c='#ed3411')
plt.xticks([]); plt.yticks([]);
plt.title('(b)')

plt.subplot(223)
plt.fill_between(Xp[:,0],true_dens,alpha=0.3)
plt.plot(Xp[:,0],np.exp(log_dens_epanechnikov),c='#ed3411')
plt.xticks([]); plt.yticks([]);
plt.title('(c)')

plt.subplot(224)
plt.fill_between(Xp[:,0],true_dens,alpha=0.3)
plt.plot(Xp[:,0],np.exp(log_dens_linear),c='#ed3411')
plt.xticks([]); plt.yticks([-10]);
plt.title('(d)');
#plt.savefig('../figs/q/q44-2.png')

