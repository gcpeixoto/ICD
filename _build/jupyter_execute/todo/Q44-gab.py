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

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# **Questão 1.** O _dataset_ 
# [covid19-weekly-trends-in-europe.csv](https://github.com/gcpeixoto/ICD/blob/main/database/covid19-weekly-trends-in-europe.csv?raw=true) contém as tendências semanais de casos de Covid-19 em diferentes regiões da Europa registradas em 8 de novembro de 2021. 
# 
# E tendo os dados da média móvel de mortes do brasil em 7 dias, partindo do dia 3 (quarta-feira), até o dia 8 (Segunda-feira):
# 
# |Data   |Dia    |	Mortes|
# |:---   |:----: |     ---:
# |03/11	|Quarta |	225   |
# |04/11	|Quinta |	227   |
# |05/11	|Sexta  |	230   |
# |06/11	|Sabado |	237   |
# |07/11	|Domingo|   232   |
# |08/11	|Segunda|   235   |
# |09/11	|Terça  |   243   |
# 
# Fonte: [Portal G1](https://g1.globo.com/saude/coronavirus/noticia/2021/11/09/brasil-completa-uma-semana-com-media-movel-abaixo-de-250-vitimas-diarias-de-covid-total-se-aproxima-de-610-mil.ghtml).
# 
# Dito isso, faça sua função para calcular a distribuição acumulativa entre as mortes em 7 dias por COVID nas diferentes regiões da Europa e o valor mortes do brasil em cada um dos 7 dias acima, guarde em um array e informe qual dia tem a maior probabilidade de ser encontrada.
# 
# Posteriormente, separe os países da união europeia (apenas o que estão no dataset) e os que não estão na UE, e avaliando os casos dos ultimos 7 dias dessas (Cases in the last 7 days) dentre as duas regiões que vc selecionou informe qual é mais assimétricamente distribuido.
# 
# Assinale de maneira respectiva a alternativa correta:
# 
# A. Segunda // Fora da União Européia
# 
# B. Terça // Dentro da União Européia
# 
# C. Quarta // Dentro da União Européia
# 
# D. Segunda // Dentro da União Européia
# 
# E. Terça // Fora da União Européia
# 
# 

# <hr>
# 
# ## Gabarito
# 
# Alternativa **E**

# This Dataset contains Weekly trends of COVID-19 in different regions of Europe as on November 08, 2021.

# In[2]:


dia = ['Quarta','Quinta','Sexta', 'Sabado','Domingo','Segunda','Terça']
date = ['03/11','04/11','05/11','06/11','07/11','08/11','09/11']
deaths = [225,227,230,237,232,235,243]
brasil_deaths_weakly = pd.DataFrame({"Dia":dia,"Mortes":deaths}, index = date)
brasil_deaths_weakly


# In[3]:


db = pd.read_csv("COVID-19_WEEKLY_TRENDS_IN_EUROPE.csv")
db = db.set_index("Country, Other")
db


# In[4]:


UE = pd.read_html("https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population")
UE = UE[0].dropna()
UE


# In[5]:


#Tem que tratar pois não tem Cyprus no nosso dataset
UE_ = []
out_UE = []
db.index
for i in db.index:
    if i in UE["Country"].values:
        
        UE_.append(i)
    else:
        out_UE.append(i)


# In[6]:


#lista de poíses da união européia presente no dataset
UE_


# In[7]:


#Paises que estão no nosso dataset mas não são da União européia
out_UE


# In[8]:


UE_db = db.loc[UE_]
out_UE_db = db.loc[out_UE]


# In[9]:


# implementação da CDF
def CDF(t,x):
    c = 0 # contagem
    
    for ti in t: # cada valor na amostra
        if ti <= x:
            c += 1
    prob = c / len(t) # probabilidade
    return prob


# In[10]:


cdfs = np.array([CDF(db['Deaths in the last 7 days'], brasil_deaths_weakly['Mortes'][_]) for _ in range (len(brasil_deaths_weakly['Mortes']))])


# In[11]:


day = brasil_deaths_weakly['Dia'][np.argmax(cdfs)]


# In[12]:


# coeficiente de pearson
def p(x):
    return 3*( x.mean() - x.median() )*x.std()


# In[13]:


pp = np.array([p(UE_db['Cases in the last 7 days']), p(out_UE_db['Cases in the last 7 days'])])

p_list = ['Dentro da União Europeia', 'Fora da União Européia']

p_list[np.argmax(pp)]


# In[14]:


f'Resposta esperada: {day} //  {p_list[np.argmax(pp)]}'


# **Questão 2.** Calcule e plote uma distribuição exponencial do zero com os valores head da coluna "Weekly Death % Change" do DataFrame.

# In[15]:



import pandas as pd
import scipy as sp
import seaborn as sb


#DataFrame
df = db

#Criando um vetor valores de 0 a 0.3 com 300 pontos
X = np.linspace(0, 0.3, 300)

#Cores para plotar o gráfico
colors = ['black','red','blue','green','orange','cyan']


# In[16]:


#RESOLUÇÃO:


#Captando os valores head do dataframe
lamb = []
for i in range(len(df.head())):
    lamb.append(df["Weekly Death % Change"][i])
    
#Distribuição exponencial
fs = []
for i in range(len(lamb)):
    f = lamb[i]*np.exp(-1.0*lamb[i]*X)
    fs.append(f)

#Plotando o gráfico
for i in range(len(lamb)):
    plt.plot(X,fs[i],color=colors[i],label=r'$\lambda$='+str(lamb[i]))

plt.xlabel('X')
plt.ylabel(r'f(X,$\lambda$)')
plt.legend()
plt.tight_layout()


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

# In[39]:


import numpy as np
import matplotlib.pyplot as plt 
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


# In[ ]:




