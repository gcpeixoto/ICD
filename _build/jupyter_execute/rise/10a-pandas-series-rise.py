#!/usr/bin/env python
# coding: utf-8

# # Manipulação de dados - I

# ## A biblioteca _pandas_
# 
# - _pandas_ é uma biblioteca para leitura, tratamento e manipulação de dados em *Python* 
# - Funções similares as de softwares de planilhamento (ex. _Microsoft Excel_, _LibreOffice Calc_, _Apple Numbers_) 
# - Novas estruturas de dados que *pandas* introduz: *Series* e *DataFrames*
# - Para saber mais, veja a [página oficial](https://pandas.pydata.org/about/index.html) da biblioteca

# ## Visão geral 
# 
# - Um *DataFame* possui uma estrutura tabular
# - Suas colunas são vetores unidimensionais (*Series*) 
# - Suas linhas são rotuladas por um *index* 
# - Usaremos o *numpy* integrado com *pandas*

# In[34]:


import numpy as np
import pandas as pd


# ## *Series*
# 
# As *Series*:
#   * são vetores, ou seja, são *arrays* unidimensionais;
#   * possuem um *index* para cada entrada (e são muito eficientes para operar com base neles);
#   * podem conter qualquer um dos tipos de dados (`int`, `str`, `float` etc.).

# ### Criando um objeto do tipo *Series* 

# - O método padrão é utilizar a função *Series*:
# 
# ```python
# serie_exemplo = pd.Series(dados_de_interesse, index=indice_de_interesse)
# ```
# - `dados_de_interesse` pode ser:
#     * um dicionário (objeto do tipo `dict`);
#     * uma lista (objeto do tipo `list`);
#     * um objeto `array` do *numpy*;
#     * um escalar, tal como o número inteiro 1.
# 

# ### Criando *Series* a partir de dicionários

# In[35]:


dicionario_exemplo = {'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}


# In[36]:


pd.Series(dicionario_exemplo)


# - *index* obtido a partir das "chaves" dos dicionários 
# - ordem do *index* foi dada pela ordem de entrada no dicionário
# - podemos fornecer um novo *index* ao dicionário já criado

# In[43]:


pd.Series(dicionario_exemplo, index=['Maria', 'Maria', 'ana', 'Paula', 'Túlio', 'Pedro'])


# > Dados não encontrados são assinalados por um valor especial. O marcador padrão do *pandas* para dados faltantes é o `NaN` (*not a number*).

# ### Criando *Series* a partir de listas

# In[45]:


lista_exemplo = [1,2,3,4,5] 


# In[8]:


pd.Series(lista_exemplo)


# > Se os *index* não forem fornecidos, o *pandas* atribuirá automaticamente os valores `0, 1, ..., N-1`, onde `N` é o número de elementos da lista.

# ### Criando *Series* a partir de *arrays* do *numpy*

# In[46]:


array_exemplo = np.array([1,2,3,4,5])


# In[53]:


pd.Series(array_exemplo)


# ### Fornecendo um *index* na criação da *Series*
# 
# O total de elementos do *index* deve ser igual ao tamanho do *array*. Caso contrário, um erro será retornado.

# In[55]:


pd.Series(array_exemplo, index=['a','b','c','d','e','f'])


# In[61]:


pd.Series(array_exemplo, index=['a','b','c','d','e'])


# Além disso, não é necessário que que os elementos no *index* sejam únicos.

# In[13]:


pd.Series(array_exemplo, index=['a','a','b','b','c'])


# Um erro ocorrerá se uma operação que dependa da unicidade dos elementos no *index* for realizada, a exemplo do método `reindex`.

# In[64]:


series_exemplo = pd.Series(array_exemplo, index=['a','a','b','b','c']) 


# In[63]:


series_exemplo.reindex(['b','a','c','d','e']) # 'a' e 'b' duplicados na origem


# ### Criando *Series* a partir de escalares

# In[78]:


pd.Series(1, index=['a', 'b', 'c', 'd'])


# Neste caso, um índice **deve** ser fornecido!

# ### *Series* comportam-se como *arrays* do *numpy*
# 
# - Uma *Series* do *pandas* comporta-se como um *array* unidimensional do *numpy*. 
# - Pode ser utilizada como argumento para a maioria das funções do *numpy*. 
# - A diferença é que o *index* aparece.
# 

# In[92]:


series_exemplo = pd.Series(array_exemplo, index=['a','b','c','d','e'])


# In[93]:


series_exemplo[2]


# In[101]:


series_exemplo[:2]


# In[105]:


np.log(series_exemplo)


# Mais exemplos:

# In[112]:


serie_1 = pd.Series([1,2,3,4,5]); serie_2 = pd.Series([4,5,6,7,8])


# In[116]:


serie_1 + serie_2


# In[118]:


serie_1 * 2 - serie_2 * 3


# Assim como *arrays* do *numpy*, as *Series* do *pandas* também possuem atributos *dtype* (data type). 

# In[119]:


series_exemplo.dtype


# Se o interesse for utilizar os dados de uma *Series* do *pandas* como um *array* do *numpy*, basta utilizar o método `to_numpy` para convertê-la.

# In[122]:


series_exemplo.to_numpy()


# ### *Series* comportam-se como dicionários
# 
# Podemos acessar os elementos de uma *Series* através das chaves fornecidas no *index*.

# In[123]:


series_exemplo


# In[124]:


series_exemplo['a']


# Podemos adicionar novos elementos associados a chaves novas.

# In[126]:


series_exemplo['f'] = 6


# In[127]:


series_exemplo


# In[128]:


'f' in series_exemplo


# In[134]:


'g' in series_exemplo


# Neste examplo, tentamos acessar uma chave inexistente. Logo, um erro ocorre.

# In[32]:


series_exemplo['g']


# In[137]:


series_exemplo.get('g')


# Entretanto, podemos utilizar o método `get` para lidar com chaves que possivelmente inexistam e adicionar um `NaN` do *numpy* como valor alternativo se, de fato, não exista valor atribuído.

# In[144]:


series_exemplo.get('g',np.nan) 


# ### O atributo `name`
# 
# Uma *Series* do *pandas* possui um atributo opcional `name` que nos permite identificar o objeto. Ele é  bastante útil em operações envolvendo *DataFrames*.

# In[147]:


serie_com_nome = pd.Series(dicionario_exemplo, name = "Idade")


# In[149]:


serie_com_nome


# ### A função `date_range`
# 
# Em muitas situações, os índices podem ser organizados como datas. A função `data_range` cria índices a partir de datas. Alguns argumentos desta função são:
# 
# - `start`: `str` contendo a data que serve como limite à esquerda das datas. Padrão: `None`
# - `end`: `str` contendo a data que serve como limite à direita das datas. Padrão: `None`
# - `freq`: frequência a ser considerada. Por exemplo, dias (`D`), horas (`H`), semanas (`W`), fins de meses (`M`), inícios de meses (`MS`), fins de anos (`Y`), inícios de anos (`YS`) etc. Pode-se também utilizar múltiplos (p.ex. `5H`, `2Y` etc.). Padrão: `None`. 
# - `periods`: número de períodos a serem considerados (o período é determinado pelo argumento `freq`).

# Abaixo damos exemplos do uso de `date_range` com diferente formatos de data.

# In[181]:


pd.date_range(start='9/19/2021', freq='W', periods=10) 


# In[193]:


pd.date_range(start='2010-05-10', freq='Y', periods=10)


# In[202]:


pd.date_range('9/19/2021', freq='5H', periods=11)


# In[220]:


pd.date_range(start='2024-02-29', freq='365D', periods=9)


# O exemplo a seguir cria duas *Series* com valores aleatórios associados a um interstício de 10 dias.

# In[223]:


indice_exemplo = pd.date_range('2020-01-01', periods=10, freq='D')
serie_1 = pd.Series(np.random.randn(10),index=indice_exemplo)   
serie_2 = pd.Series(np.random.randn(10),index=indice_exemplo)

serie_1, serie_2

