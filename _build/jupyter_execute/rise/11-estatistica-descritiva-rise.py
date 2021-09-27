#!/usr/bin/env python
# coding: utf-8

# # Estatística Descritiva

# Neste capítulo, apresentaremos vários métodos desenvolvidos para *Series* e *DataFrames* relacionados à Estatística Descritiva.
# 
# Começaremos importando as bibliotecas *pandas* e *numpy*.

# In[1]:


import numpy as np
import pandas as pd


# ## Distribuição de Frequência
# 
# Uma distribuição de frequência é uma tabela que contém um resumo dos dados obtido em uma amostra. A distribuição é organizada em formato de tabela e cada entrada da tabela contém a frequência dos dados em um determinado intervalo, ou em um grupo.

# Abaixo vemos um exemplo simplificado de tabela de distribuição de frequência:
# 
# | Alturas em metros | Número dos Alunos | 
# | :-------------: |:-------------:| 
# |1,50 $|-$ 1,60   | 5 | 
# | 1,60 $|-$ 1,70   | 15     |   
# | 1,70 $|-$ 1,80   | 17      |   
# | 1,80 $|-$ 1,90    | 3      |   
# | Total    | 40      |

# ### Construção de uma distribuição de frequência
# 
# Para ilustrar como se constrói uma distribuição de frequência, vamos considerar um exemplo específico. Suponha que uma pesquisa foi feita e o seguinte conjunto de dados foi obtido:
# 
# * **Dados Brutos**: 24-23-22-28-35-21-23-33-34-24-21-25-36-26-22-30-32-25-26-33-34-21-31-25-31-26-25-35-33-31.
# 
# 

# In[2]:


dados = [24,23,22,28,35,21,23,33,34,24,21,25,36,26,22,30,32,25,26,33,34,21,31,25,31,26,25,35,33,31]


# #### Rol de dados
# 
# A primeira coisa a fazer é ordenar os dados do menor para o maior, formando o *rol de dados*:
# 
# * **Rol de dados**: 21-21-21-22-22-23-23-24-25-25-25-25-26-26-26-28-30-31-31-31-32-33-33-33-34-34-34-35-35-36.

# In[3]:


np.sort(dados)


# #### Amplitude Total
# 
# Em seguida, calculamos a *amplitude total*, ou seja, o maior valor obtido na amostra subtraído do menor
# valor obtido na amostra:
# 
# * **Amplitude Total**: R = 36-21 = 15.

# In[4]:


R = np.max(dados) - np.min(dados); R


# #### Tamanho Amostral
# 
# Vamos calcular agora o tamanho amostral, ou seja, o número de observações obtidas na amostra.
# 
# * **Tamanho Amostral**: n = 30.
# 

# In[5]:


n = len(dados); n


# Para *Series* e *DataFrames* o método `count()` retorna a total de valores.

# In[6]:


n = pd.Series(dados).count(); n


# #### Número de Classes
# 
# Dividiremos a amostra em uma quantidade de grupos que formarão os intervalos. Cada grupo é chamado de *classe*. Assim, definiremos o *número de classes* a ser considerado na tabela de *distribuição de frequência*:
# 
# * **Número de Classes**: K.
#     * K=5 para $n\leq 25$ e $K\approx \sqrt{n}$, para $n>25$. 
#     * Fórmula de Sturges: $K\approx 1+3,22\log n$. 
# 
# Logo, pela primeira regra temos $K=\sqrt{30}\approx 5,48 \approx 6$, e pela segunda regra 
# $K\approx 1+3,22\log 30\approx 5,75 \approx 6.$ Desta forma, em ambos os casos temos $K=6$, que será o valor considerado.
# 

# Número de classes padrão:

# In[7]:


if n<25:
    K = 5
else:
    K = np.ceil(np.sqrt(n))
K


# Número de classes fórmula de Sturges:

# In[8]:


KFS = np.ceil( 1 + 3.22*np.log10(n)); KFS


# #### Amplitude das Classes
# 
# O próximo passo é saber o comprimento de cada intervalo a ser considerado, ou seja, calcular a amplitude de cada classe. Queremos que todas as classes tenham a mesma amplitude e portanto, temos:
# 
# * **Amplitude das Classes**: $h=\frac{R}{K}=\frac{15}{6}=2,5\approx 3$.

# In[9]:


h = np.ceil(R/K); h


# #### Limites das Classes
# 
# Agora definimos os *limites das classes*. Para tanto, começamos com o menor valor obtido da amostra, ou equivalentemente, o primeiro valor do *rol de dados*, e vamos somando a amplitude para definir cada limite de intervalo:
#     
# | Classes |    
# | :-------------:
# | 21 $|-$ 24 |
# | 24 $|-$ 27 |  
# | 27 $|-$ 30 |  
# | 30 $|-$ 33 | 
# | 33 $|-$ 36 |  
# | 36 $|-$ 39 | 

# In[10]:


bins = [np.min(dados) + i*h.astype('int') for i in range(K.astype('int')+1)]; bins


# #### Frequência dos Dados
# 
# * Agora, calculamos as frequências dos dados em cada intervalo e, chamada também de *frequência absoluta*. E finalmente montamos a tabela de *Distribuição de Frequência*.
# 
# | Classes |   Frequência |
# | :-------------:| :-------------:|
# | 21 $|\!-$ 24 | 7 |
# | 24 $|\!-$ 27 | 9 |  
# | 27 $|\!-$ 30 | 1 |  
# | 30 $|\!-$ 33 | 5 | 
# | 33 $|\!-$ 36 | 7 | 
# | 36 $|\!-$ 39 | 1 | 

# No *pandas*, a função `cut` cria classes a partir dos dados e o método `value_counts()` cria uma tabela de frequências. Combinando os dois obtemos uma *Distribuição de Frequência*.

# In[11]:


pd.cut(dados, bins=bins, right=False).value_counts() 


# Neste ponto, definiremos algumas funções para ajudar-nos a automatizar a criação de uma tabela de frequências.

# In[12]:


def n_classes(dados: pd.Series, tipo='Padrão'):
    n_obs = len(dados)
    if tipo=='Padrão':
        return 5 if n_obs<25 else np.ceil(np.sqrt(n_obs)).astype(int)
    if tipo=='Sturges':
        return (1 + np.ceil(np.log2(n_obs))).astype(int)

def amplitude_classes(dados: pd.Series, tipo='Padrão', arredondar=True):
    amplitude = np.ceil((dados.max() - dados.min())/n_classes(dados, tipo=tipo))     if arredondar else (dados.max() - dados.min())/n_classes(dados, tipo=tipo)
    return amplitude

def construir_tabela(dados, tipo='Padrão', direita=False, arredondar=True):
    dados_series = pd.Series(dados)
    n_class = n_classes(dados_series, tipo=tipo)
    amp_class = amplitude_classes(dados_series, tipo=tipo, arredondar=arredondar)
    bins = [dados_series.min() + i*amp_class for i in range(n_class+1)]
    return pd.cut(dados_series, bins=bins, right=direita).value_counts(sort=False).rename('Frequência')

def formatar_intervalos(intervalos, prec, direita=False):   
    fechado = 'right' if direita else 'left'
    return [pd.Interval(left=np.round(intervalo.left,prec), 
                        right=np.round(intervalo.right,prec), closed=fechado) for intervalo in intervalos]


# In[13]:


def dist_freq(dados, tipo='Padrão', prec=2, direita=False, arredondar=True, exibir_total=True):    
    df_dist_freq = pd.DataFrame(construir_tabela(dados, tipo=tipo, direita=direita, arredondar=arredondar))
    df_dist_freq.index = formatar_intervalos(df_dist_freq.index.array, prec, direita=direita)
    df_dist_freq.index = df_dist_freq.index.rename('Classes')
    if exibir_total:
        total_dist = pd.DataFrame({'Frequência':df_dist_freq['Frequência'].sum()}, index=['Total'])
        total_dist.index = total_dist.index.rename('Classes')
        df_dist_freq = pd.concat([df_dist_freq, total_dist])
    return  df_dist_freq.query('Frequência>0')


# Exemplos:

# In[14]:


dist_freq(dados)


# Exemplo com números aleatórios.

# In[15]:


z=np.random.normal(0,1,200)
dist_freq(z)


# In[16]:


np.min(z)


# In[17]:


np.max(z)


# ## Medidas de Posição
# 
# As medidas de posição são valores que representam a tendência de concentração dos dados observados. As mais importantes são as _medidas de tendência central_.  As três medidas de tendência central mais utilizadas são: *média*, *moda* e *mediana*.

# ### Média
# 
# É um valor que representa uma característica do conjunto de dados. Essa característica é tal que a soma dos dados é preservada. A média é obtida a partir de todos os elementos da distribuição e do tamanho da amostra.
# 
# *Notação*: representamos a média de um conjunto de dados por $\overline{X}$. Calculamos a média aritmética pela fórmula:
# $$\overline{X}=\sum_{i=1}^{n}\frac{X_i}{n}.$$
# 

# 
# Para *Series* e *DataFrames* o método `mean()` retorna a média dos valores.

# In[18]:


pd.Series(dados).mean()


# #### Média para dados agrupados em intervalos
# 
# No caso em que temos os dados agrupados em intervalos, utilizamos a frequência e o ponto médio de cada classes para calcular a média pela fórmula:
# $$\overline{X}=\sum_{i=1}^{K}\frac{F_i\cdot pm_i}{n},$$
# onde $K$ é o número de classes, $F_i$ é a frequência da $i$-ésima classe e $pm_i$ é o ponto médio da $i$-ésima classe.

# In[19]:


dist_freq_pm = dist_freq(dados, exibir_total=False)
intervalos = dist_freq_pm.index.array
dist_freq_pm['Ponto Médio'] = [(intervalo.left+intervalo.right)/2 for intervalo in intervalos]
dist_freq_pm


# In[20]:


media = (dist_freq_pm['Frequência']*dist_freq_pm['Ponto Médio']).sum()/dist_freq_pm['Frequência'].sum()
media


# In[21]:


def media_dist_freq(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
    intervalos = d_freq.index.array
    d_freq['Ponto Médio'] = [(intervalo.left+intervalo.right)/2 for intervalo in intervalos]
    return (d_freq['Frequência']*d_freq['Ponto Médio']).sum()/d_freq['Frequência'].sum()


# In[22]:


media_dist_freq(dist_freq(dados))


# In[23]:


media_dist_freq(dist_freq(z))


# ### Moda
# 
# Definimos a moda de um conjunto de dados como o valor mais frequente deste conjunto. 
# 
# *Notação*: representamos a moda de um conjunto de dados por $Mo$.
# 
# *Exemplo*:
# 
# * 1, 2, 4, 5 e 8 - não existe valor mais frequente - não existe moda (Amodal).
# * 2, 2, 3, 7 e 8 - $Mo$ = 2 (Unimodal).
# * 1, 1, 10, 5, 5, 8, 7, 2 - $Mo$ = 1 e 5 (Bimodal). 
# 
# Para Series e DataFrames o método `mode()` retorna a moda dos valores.

# In[24]:


pd.Series(dados).mode()


# In[25]:


pd.Series(z).mode()


# ##### Moda em dados agrupados em intervalos
# 
# Neste caso, utiliza-se a fórmula de Czuber identificando a *classe modal*, isto é, a classe com a maior frequencia.
# 
# $${\rm Mo}=l_{\rm Mo} + \left[\frac{h(F_{\rm Mo} - F_{\rm ant})}{2 F_{\rm Mo}-(F_{\rm ant}+F_{\rm pos})} \right],$$
# onde:
# 
# - $l_{\rm Mo}$ é o limite inferior da *classe modal*,
# 
# - $h$ é a amplitude intervalar,
# 
# - $F_{\rm Mo}$ é a frequência da *classe modal*,
# 
# - $F_{\rm ant}$ é a frequência da classe anterior à *classe modal*,
# 
# - $F_{\rm pos}$ é a frequência da classe posterior à classe modal.
# 
# 

# Aqui, definiremos algumas funções para automatizar processos.

# In[26]:


def encontra_indices_modais(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
    d_temp = d_freq.reset_index()['Frequência']
    return ((d_temp[d_temp == d_temp.max()]).index).to_numpy()

def encontra_freq_anterior(d_freq):
    idx_modal = encontra_indices_modais(d_freq).astype('float')
    idx_anterior = idx_modal-1
    idx_anterior[idx_anterior<0] = np.nan
    freq_anterior = d_freq['Frequência'].iloc[idx_anterior[~np.isnan(idx_anterior)]].to_numpy()
    if(np.isnan(idx_anterior[0])):
        freq_anterior = np.insert(freq_anterior,0,0)
    return freq_anterior

def encontra_freq_posterior(d_freq):
    idx_modal = encontra_indices_modais(d_freq).astype('float')
    n_classes = d_freq.shape[0]
    idx_posterior = idx_modal+1
    idx_posterior[idx_posterior >= n_classes] = np.nan
    freq_posterior = d_freq['Frequência'].iloc[idx_posterior[~np.isnan(idx_posterior)]].to_numpy()
    if(np.isnan(idx_posterior[-1])):
        freq_posterior = np.append(freq_posterior,0)
    return freq_posterior

def moda_dist_freq(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
        d_freq.index = d_freq.index.array.astype(pd.arrays.IntervalArray)
    idx_modal = encontra_indices_modais(d_freq)
    h = d_freq.index.array[0].right-d_freq.index.array[0].left
    lMo = d_freq.index.array[idx_modal].left.array
    FMo = d_freq.iloc[idx_modal]['Frequência'].array
    FPos = encontra_freq_posterior(d_freq)
    FAnt = encontra_freq_anterior(d_freq)
    return lMo + (h*(FMo-FAnt))/(2*FMo - (FAnt+FPos))


# In[27]:


moda_dist_freq(dist_freq(z))


# In[28]:


moda_dist_freq(dist_freq(dados))


# ### Mediana
# 
# Definimos a mediana de um conjunto de dados como o valor que divide o *rol de dados* em duas partes com a mesma quantidade de dados.
# 
# *Notação:* representamos a mediana de um conjunto de dados por $Md$.
# 
# O *elemento mediano*, $E_{\rm  Md}$, aponta o local no *rol de dados* onde a mediana está localizada.  A mediana será o valor assumido na posição $E_{\rm  Md}$. 
# 
# Se o tamanho amostral $n$ é ímpar, temos que $E_{\rm  Md} = \frac{(n+1)}{2}$. Por outro lado, se par, teremos dois valores possíveis para o elemento mediano: $\frac{n}{2}$ e $\frac{n}{2}+1$. Neste caso a mediana será a média dos valores assumidos nestas posições.

# * Exemplos:
# 
#     * 1, 2, 4, 5, 8. Como $n$ é ímpar, temos $E_{\rm  Md} = 3$, e $Md = 4$.
# 
#     * 2, 2, 3, 7, 8, 10. Aqui $n$ é par, assim $E_{\rm  Md,1} = \frac{6}{2} = 3$ e  $E_{\rm Md,2} = \frac{6}{2}+1 = 4$. Daí ${ Md} = \frac{3+7}{2} = 5$.
#     
# * Para Series e DataFrames o método `median()` retorna a mediana dos valores.

# In[29]:


pd.Series(dados).median()


# In[30]:


pd.Series(z).median()


# ##### Mediana em dados agrupados em intervalos
# 
# Neste caso, utilizamos $E_{\rm Md} = \frac{n}{2}$ independentemente de $n$ ser par ou ímpar. A *classe mediana* é a primeira classe tal que $F_{\rm ac} \geq E_{\rm Md}$.

# Definimos a *mediana* pela fórmula
# 
# $${\rm Md} = l_{\rm Md} + h\left[ \frac{E_{\rm Md} - F_{\rm ac,ant}}{F_{\rm Md}}\right],$$
# 
# onde,
# 
# $l_{\rm Md}$ é o limite inferior da *classe mediana*,
# 
# $h$ é a amplitude do intervalo,
# 
# $F_{\rm ac,ant}$ é a frequência acumulada da classe anterior à *classe mediana*,
# 
# $F_{\rm Md}$ é a frequência da *classe mediana*.

# Para *Series* e *DataFrames*, o método `cumsum()` retorna a soma acumulada dos valores.

# In[31]:


d_freq_temp = dist_freq(dados, exibir_total=False)
d_freq_temp['Freq Acumulada'] = d_freq_temp['Frequência'].cumsum()
d_freq_temp


# In[32]:


def mediana_dist_freq(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
        d_freq.index = d_freq.index.array.astype(pd.arrays.IntervalArray)
    n_obs = d_freq['Frequência'].sum()
    h = d_freq.index.array[0].right-d_freq.index.array[0].left
    d_freq['Freq Acumulada'] = d_freq['Frequência'].cumsum()
    lMd = (d_freq[d_freq['Freq Acumulada'] >= n_obs/2].iloc[0]).name.left
    EMd = n_obs/2
    FMd = d_freq[d_freq['Freq Acumulada'] >= n_obs/2].iloc[0]['Frequência']
    if (d_freq['Freq Acumulada'] < n_obs/2).any():
        FAcAnt = d_freq[d_freq['Freq Acumulada'] < n_obs/2].iloc[-1]['Freq Acumulada']
    else:
        FAcAnt = 0
    return lMd + h*(EMd-FAcAnt)/FMd


# In[33]:


mediana_dist_freq(dist_freq(z))


# In[34]:


mediana_dist_freq(dist_freq(dados))


# ## Medidas de Dispersão
# 
# 
# As medidas de dispersão medem o grau de variabilidade dos elementos de uma distribuição. O valor zero indica ausência de dispersão. A dispersão aumenta à medida que aumenta o valor da medida de dispersão. As principais Medidas de Dispersão: *amplitude*, *desvio médio*, *variância*, *desvio padrão*.

# Motivação para as medidas de dispersão
# 
# |Alunos||| Notas||| Média|
# |:--:|:--:|:--:|:--:|:--:|:--:|:--:|
# |Antônio|5|5|5|5|5|5|
# |João |6|4|5|4|6|5|
# |José |10|5|5|5|0|5|
# |Pedro |10|10|5|0|0|5|
# 
# Observa-se que:
# 
# * As notas de Antônio não variaram;
# 
# * As notas de João variaram menos do que as notas de José;
# 
# * As notas de Pedro variaram mais do que as notas de todos os outros alunos.

# #### Amplitude
# 
# A amplitude nos fornece uma idéia do campo de variação dos elementos. Mais precisamente, ela fornece a maior variação possível dos dados. A amplitude é dada pela fórmula:
# $$R = X_{\max} -  X_{\min},$$
# onde $X_{\max}$ é o máximo dos valores nos dados e $X_{\min}$ é o mínimo dos valores nos dados.
# 
# Para *Series* e *DataFrames* os métodos `max()` e `min()` retornam respectivamente o máximo e mínimo dos valores.

# In[35]:


R = pd.Series(dados).max()-pd.Series(dados).min(); R


# ### Desvio Médio
# 
# Para medir a dispersão dos dados em relação a média, é interessante analisar os desvios em torno da média, isto é, fazer a análise dos desvios:
# 
# $$
# d_i=(X_i-\overline{X}).
# $$
# 
# Porém, a soma de todos os desvios é igual a zero, como podemos verificar com
# $$
# \sum_{i=1}^{n} d_i= \sum_{i=1}^{n} (X_i-\overline{X})= \sum_{i=1}^{n}X_i-\sum_{i=1}^{n}\overline{X}=\sum_{i=1}^{n}X_i-{n}\overline{X}=
# $$
# 
# $$
# =\sum_{i=1}^{n}X_i-n\frac{\sum_{i=1}^{n}X_i}{n}= \sum_{i=1}^{n}X_i-\sum_{i=1}^{n}X_i=0.
# $$

# Logo, será preciso encontrar uma maneira de se trabalhar com os desvios sem que a soma dê zero. Dessa forma, define-se o *desvio médio*.
# 
# *Notação:* representamos o *desvio médio* de um conjunto de dados por $DM$.
# 
# Portanto, definimos o *desvio médio* pela fórmula:
# $$
# DM=\sum_{i=1}^{n} \frac{|d_i|}{n}= \sum_{i=1}^{n} \frac{|X_i-\overline{X}|}{n}.
# $$
# 
# Para *Series* e *DataFrames* o método `mad()` retorna a *desvio médio* dos valores.

# In[36]:


pd.Series(dados).mad()


# In[37]:


pd.Series(z).mad()


# ##### Desvio médio em dados agrupados em intervalos
# 
# No caso em que temos os dados agrupados em intervalos, utilizamos a frequência e o ponto médio de cada classe para calcular a *desvio médio* pela fórmula:
# 
# $$
# DM=\sum_{i=1}^{K} \frac{|d_i|\cdot F_i}{n}= \sum_{i=1}^{K} \frac{|pm_i-\overline{X}|\cdot F_i}{n},
# $$
# 
# onde $K$ é o número de classes, $F_i$ é a frequência da $i$-ésima classe e  $pm_i$ é o ponto médio da $i$-ésima classe.

# In[38]:


def dm_dist_freq(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
    intervalos = d_freq.index.array
    d_freq['Ponto Médio'] = [(intervalo.left+intervalo.right)/2 for intervalo in intervalos]
    return (d_freq['Frequência']*np.abs(d_freq['Ponto Médio'] - 
                                  media_dist_freq(d_freq))).sum()/(d_freq['Frequência'].sum())


# In[39]:


dm_dist_freq(dist_freq(dados))


# In[40]:


dm_dist_freq(dist_freq(z))


# **Observações**:
# 
# * A *amplitude* não mede bem a dispersão dos dados porque usam-se apenas os valores extremos em vez de todos os elementos da distribuição. 
# 
# * O *desvio médio* é mais vantajoso que a *amplitude*, visto que leva em consideração todos os valores da distribuição e é menos sensível a *outliers*.
# 
# * No entanto, *desvio médio* não é tão frequentemente empregado no ajuste de modelos, pois não apresenta propriedades matemáticas interessantes, porém é bastante utilizado na validação e comparação de modelos.

# ### Variância
# 
# A *variância* é a medida de dispersão mais utilizada. É o quociente entre a soma dos quadrados dos desvios e o número de elementos. Assim, temos a seguinte fórmula para *variância populacional*:
# 
# $$
# \sigma^2=\sum_{i=1}^{N} \frac{d_i^2}{N}= \sum_{i=1}^{N} \frac{(X_i-\overline{X})^2}{N},
# $$
# 
# onde $\sigma^2$ indica a variância populacional (lê-se "sigma ao quadrado" ou "sigma dois"). Neste caso, $\overline{X}$ e $N$ na formúla representam a média populacional e o tamanho populacional, respectivamente.

# ### Variância Amostral
# 
# Temos a seguinte definição de *variância amostral*:
# 
# $$
# S^2=\sum_{i=1}^{n} \frac{d_i^2}{n-1}= \sum_{i=1}^{n} \frac{(X_i-\overline{X})^2}{n-1}.
# $$
# 
# Para *Series* e *DataFrames* o método `var()` retorna a *variância amostral* dos valores. 

# In[41]:


pd.Series(dados).var()


# In[42]:


pd.Series(z).var()


# ##### Variância amostral em dados agrupados em intervalos
# 
# No caso em que temos os dados agrupados em intervalos, utilizamos a frequência e o ponto médio de cada classe para calcular a *variância* pela fórmula:
# 
# $$
# S^2=\sum_{i=1}^{K} \frac{d_i^2\cdot F_i}{n-1}= \sum_{i=1}^{K} \frac{(pm_i-\overline{X})^2\cdot F_i}{n-1}.
# $$
# 
# onde $K$ é o número de classes, $F_i$ é a frequência da $i$-ésima classe e  $pm_i$ é o ponto médio da $i$-ésima classe.

# In[43]:


def var_dist_freq(d_freq):
    if(type(d_freq.index.array).__name__ != 'IntervalArray'):
        d_freq = d_freq.head(-1).copy()
    intervalos = d_freq.index.array
    d_freq['Ponto Médio'] = [(intervalo.left+intervalo.right)/2 for intervalo in intervalos]
    return (d_freq['Frequência']*(d_freq['Ponto Médio'] - 
                                  media_dist_freq(d_freq))**2).sum()/(d_freq['Frequência'].sum()-1)


# In[44]:


var_dist_freq(dist_freq(dados))


# In[45]:


var_dist_freq(dist_freq(z))


# ### Desvio Padrão
# 
# Temos também outra medida de dispersão, que é a raiz quadrada da variância, chamada de *desvio padrão*. Assim,
# 
# $$
# \sigma = \sqrt{\sigma^2} \quad \hbox{é o desvio desvio padrão populacional}
# $$
# 
# e
# 
# $$
# S = \sqrt{S^2} \quad \hbox{é o desvio desvio padrão amostral.}
# $$
# 
# Para o cálculo do *desvio padrão*, deve-se, primeiramente, determinar o valor da variância e, em seguida, extrair a raiz quadrada desse resultado.
# 
# Para *Series* e *DataFrames* o método `std()` retorna o *desvio padrão* dos valores. 

# In[46]:


pd.Series(dados).std()


# In[47]:


np.sqrt(pd.Series(dados).var())


# In[48]:


pd.Series(z).std()


# In[49]:


np.sqrt(pd.Series(z).var())


# #### Desvio Padrão para dados agrupados em intervalos

# In[50]:


def dp_dist_freq(d_freq):
    return np.sqrt(var_dist_freq(d_freq))


# In[51]:


dp_dist_freq(dist_freq(dados))


# In[52]:


dp_dist_freq(dist_freq(z))


# ## Resumo Estatístico de uma *Serie* ou *DataFrame*
# 
# Para obtermos um resumo estatístico de uma *Series* ou *DataFrame* do *pandas*, utilizamos o método `describe`. O método `describe` exclui observações ausentes por padrão.

# Exemplos:

# In[53]:


pd.Series(dados).describe()


# In[54]:


pd.DataFrame(z).describe()


# **Observações**
# 
# * Se as entradas da *Series* não forem numéricas, o método `describe` retornará uma tabela contendo as quantidades de valores únicos, qual o valor mais frequente e qual a quantidade de elementos do valor mais frequente.
# 
# * No caso de um *DataFrame* que contenha colunas numéricas e colunas não-numéricas, o método `describe` só irá considerar as colunas numéricas.

# Exemplos:

# In[55]:


serie_ex1 = pd.Series(['a','b','c','d','e','f','g','h','i','j'])
serie_ex2 = pd.Series(range(10))


# In[56]:


serie_ex1.describe()


# In[57]:


serie_ex2.describe()


# Exemplo:

# In[58]:


df_exemplo = pd.concat([serie_ex1, serie_ex2], axis=1)


# In[59]:


df_exemplo


# Exemplo:

# In[60]:


df_exemplo.describe()


# **Observação**: Podemos controlar o que será considerado no `describe` utilizando os argumentos `include` ou `exclude`. No caso, devemos colocar como argumento uma lista contendo os tipos a serem incluídos ou excluídos. Existem vários tipos que podem ser considerados para serem incluídos ou excluídos. Para uma lista dos tipos disponíveis, consulte a documentação da função `select_dtypes()`.

# Exemplos:

# In[61]:


df_exemplo.describe(exclude='number')


# In[62]:


df_exemplo.describe(include='object')


# Exemplo:

# In[63]:


df_exemplo.describe(include='all')

