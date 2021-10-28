#!/usr/bin/env python
# coding: utf-8

# ## Questionário 43 (Q43)

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

# Para responder este questionário, utilize o banco de dados [brasileirao2021.csv](https://github.com/gcpeixoto/ICD/blob/main/database/brasileirao2021.csv). Fonte: [[CBF]](https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a).
# 
# **Obs.:** use o _dataset_ do repositório Git e não o do site da CBF, visto que este é atualizado após cada jogo.
# 
# <br>
# 
# **Questão 1.** Utilizando o método de _z-scores_ e o _dataset_, identifique todos os times cuja pontuação superou a média do campeonato e assinale a alternativa correta quanto às posições que ocupavam no ranque do Brasileirão 2021 no momento em que o _dataset_ havia sido gerado.
# 
# A. 1a. a 6a.
# 
# B. 3a. a 5a.
# 
# C. 1a. a 9a.
# 
# D. 2a. a 8a.

# <hr>
# 
# ## Gabarito
# 
# Alternativa **C**

# In[13]:


#Dataset e tratamento dos dados
import pandas as pd 
import numpy as np

# Fonte: https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a"
brasileiro_2021 = pd.read_csv('../database/brasileirao2021.csv')
brasileiro_2021 = brasileiro_2021.drop(columns=['%','Recentes','Próx'])


# In[14]:


#Função do Z-Score
def zScore(df,colname):
    s = df[colname]
    return (s - s.mean())/s.std(ddof=0)


# In[15]:


#Filtrando as colunas que iremos utilizar e indexando
df_pts_j = brasileiro_2021.filter(['Posição', 'PTS', 'J']).set_index('Posição')

#Criando o df com o dados do z-score
l = {}
for c in df_pts_j.columns:    
    l[c + ':Z-score'] = zScore(df_pts_j,c)


df_zscore = pd.DataFrame(l)

#Verificando quais são > 0
print("Todos os times que tem a pontuação acima da média:\n\n")
for i in range(len(df_zscore)):
    
    if (df_zscore['PTS:Z-score'][i] > 0):
        print(df_zscore.index[i])
    
    else:
        continue


# <hr>
# 
# **Questão 2.** O _dataset_ descreve o desempenho de cada time através de marcadores clássicos do futebol, a saber: Pontos (_PTS_), Jogos (_J_), Vitórias (_V_), Empates (_E_), Derrotas (_D_), Gols Marcados (Pró) (_GP_), Gol Sofridos (Contra) (_GC_), Saldo de Gols (_SG_), Cartões Amarelos (_CA_) e Cartões Vermelhos (_CV_).
# 
# Considerando $X$ a série correspondente a _PTS_, determine as variáveis correspondentes às séries $Y_1$ e $Y_2$, tais que, $\text{cov}(X,Y_1)$ seja a maior covariância positiva e $\text{cov}(X,Y_2)$ seja a maior covariância negativa.
# 
# 
# A. _J_ e _V_
# 
# B. _GP_ e _GC_
# 
# C. _SG_ e _GP_
# 
# D. _SG_ e _GC_
# 

# <hr>
# 
# ## Gabarito
# 
# Alternativa **D**

# In[16]:


# covariância
def cov(df,colname1,colname2):
    s1,s2 = df[colname1],df[colname2]
    return np.dot( s1 - s1.mean(), s2 - s2.mean() )/(len(s1)-1)


# In[17]:


brasileiro_2021.head()


# In[18]:


def stats(db, col_alvo):
    l=np.ones(len(db.columns[2:]))
    for _ in range(len(db.columns[2:])):
        l[_] = (cov(db,col_alvo,str(db.columns[_+2])))
        
    return l


# In[19]:


covariance = stats(brasileiro_2021, "PTS")
brasileiro_2021.columns[np.argmax(covariance)+2] + " / " + brasileiro_2021.columns[np.argmin(covariance)+2]


# **Questão 3.** Tomando todas as séries do _DataFrama_ de _GM_ em diante, identifique aquela que possui a mais forte correlação positiva com _E_ e aquela que possui a mais forte correlação negativa com _V_, respectivamente.
# 
# A. GP / GC
# 
# B. CV / GP
# 
# C. CA / GC
# 
# D. SG / GC

# <hr>
# 
# ## Gabarito
# 
# Alternativa **C**

# In[20]:


def corr1(db, col_alvo):
    l = np.ones(len(db.columns[6:]))
    for _ in range(len(db.columns[6:])):

        l[_] = db[[col_alvo, str(db.columns[_+6])]].corr()[1:][col_alvo].values[0]
        print(f"{str(db.columns[_+6])}: {l[_]}")
        
    return l


# In[21]:


newdf = brasileiro_2021.columns[6:]


# In[22]:


corr2 = corr1(brasileiro_2021, "E");corr2


# In[23]:


corr3 = corr1(brasileiro_2021, "V"); corr3


# In[24]:


brasileiro_2021.columns[np.argmax(corr2)+6] + " / " + brasileiro_2021.columns[np.argmin(corr3)+6]

