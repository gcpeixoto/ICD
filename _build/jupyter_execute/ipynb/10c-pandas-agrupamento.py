#!/usr/bin/env python
# coding: utf-8

# # Manipulação de dados - III

# ## Agregação e agrupamento 

# ### Agregando informações de linhas ou colunas
# 
# Para agregar informações (p.ex. somar, tomar médias etc.) de linhas ou colunas podemos utilizar alguns métodos específicos já existentes em *DataFrames* e *Series*, tais como `sum`, `mean`, `cumsum` e `aggregate` (ou equivalentemente `agg`):

# In[1]:


import pandas as pd
import numpy as np

dados_covid_PB = pd.read_csv('https://superset.plataformatarget.com.br/superset/explore_json/?form_data=%7B%22slice_id%22%3A1550%7D&csv=true', 
                             sep=',', index_col=0)


# In[2]:


dados_covid_PB.agg(lambda vetor: np.sum(vetor))[['casosNovos','obitosNovos']].astype('int')


# Podemos conferir esta agregação resultante com o número de casos acumulados e óbitos acumulados

# In[3]:


dados_covid_PB.head()


# Isto também pode ser obtido utilizando o método `sum` de *DataFrames* e *Series*:

# In[4]:


dados_covid_PB[['casosNovos','obitosNovos']].sum()


# Podemos recriar a coluna `'obitosAcumulados'` com o método `cumsum` (soma cumulativa):

# In[5]:


dados_covid_PB.obitosNovos.sort_index().cumsum()


# ### Selecionando entradas distintas
# 
# Para selecionar entradas distintas utilizamos o método `drop_duplicate`. Aqui, para exemplificar, vamos utilizar o banco de dados oficial sobre COVID no Brasil:

# In[6]:


# pode levar um tempo para ler...
covid_BR = pd.read_excel('data/HIST_PAINEL_COVIDBR_18jul2020.xlsx')


# In[7]:


covid_BR.tail(3)


# In[8]:


# resumo da tabela
covid_BR.info()


# In[9]:


# todos os estados únicos
covid_BR.estado.drop_duplicates().array


# In[10]:


# ordena alfabeticamente
covid_BR.estado.drop_duplicates().dropna().sort_values().array


# ### Agrupando dados por valores em colunas e agregando os resultados
# 
# Vamos determinar uma coluna para agrupar. Consideraremos o *DataFrame* `covid_BR`e selecionaremos os estados *PB*, *PE*, *RJ* e *SP* para realizar análises agrupando os resultados por estados.

# In[11]:


covid_BR.query('estado in ["PB", "PE", "RJ", "SP"]')


# Inspecionando o conjunto de dados, observamos que os dados para estado são apresentados com o valor `NaN` para `codmun` e quando `codmun` possui um valor diferente de `NaN`, o resultado é apenas para o município do código em questão.
# 
# Como estamos interessados nos valores por estado, vamos selecionar apenas os dados com `codmun` contendo `NaN`.

# In[12]:


covid_estados = covid_BR.query('estado in ["PB", "PE", "RJ", "SP"]')
covid_apenas_estados = covid_estados.loc[covid_estados['codmun'].isna()]


# Vamos agora selecionar apenas as colunas de interesse. Para tanto, vejamos os nomes das colunas:

# In[13]:


covid_apenas_estados.columns


# In[14]:


covid_apenas_estados = covid_apenas_estados[['estado', 'data', 'casosNovos', 'obitosNovos']]


# A data parece ser o *index* natural, já que o *index* atual não representa nada. Observe que teremos *index* repetidos, pois teremos as mesmas datas em estados diferentes.

# In[15]:


covid_apenas_estados


# In[16]:


covid_apenas_estados = covid_apenas_estados.set_index('data')


# In[17]:


covid_apenas_estados


# ### Agrupando com o método *groupby*
# 
# Podemos escolher uma (ou mais colunas, incluindo o índice) para agrupar os dados. Ao agruparmos os dados, receberemos um objeto do tipo `DataFrameGroupBy`. Para vermos os resultados, devemos agregar os valores:

# In[18]:


covid_estados_agrupado = covid_apenas_estados.groupby('estado')


# In[19]:


covid_estados_agrupado.sum().rename({'casosNovos':'Casos Totais', 'obitosNovos':'Obitos Totais'},axis=1)


# Podemos agrupar por mais de uma coluna. Vamos fazer dois grupos. *grupo_1* formado por PB e PE e *grupo_2* formado por RJ e SP. Em seguida, vamos agrupar por grupo e por data:

# In[20]:


covid_estados_grupos = covid_apenas_estados.copy()
col_grupos = covid_estados_grupos.estado.map(lambda estado: 'grupo_1' if estado in ['PB','PE']
                                                  else 'grupo_2')
covid_estados_grupos['grupo'] = col_grupos


# In[21]:


covid_estados_grupos


# Agora vamos agrupar e agregar:

# In[22]:


covid_grupo_agrupado = covid_estados_grupos.groupby(['grupo','data'])


# In[23]:


covid_grupo_agrupado.sum()


# ### Mesclando *DataFrames* 
# 
# Vamos agora ver algumas formas de juntar dois ou mais *DataFrames* com *index* ou colunas em comum para formar um novo *DataFrame*.
# 

# #### Mesclando *DataFrames* através de concatenações
# 
# Concatenar nada mais é do que "colar" dois ou mais *DataFrames*. Podemos concatenar por linhas ou por colunas.
# 
# A função que realiza a concatenação é `concat`. Os dois argumentos mais utilizados são a lista de *DataFrames* a serem concatenados e `axis`, onde `axis = 0` indica concatenação por linha (um *DataFrame* "embaixo" do outro) e `axis=1` indica concatenação por coluna (um *DataFrame* ao lado do outro).

# Relembre do *DataFrame* `df_dict_series`:

# In[24]:


df_dict_series = pd.read_csv('data/df_dict_series.csv')


# Vamos criar um novo, com novas pessoas:

# In[25]:


serie_Idade_nova = pd.Series({'Augusto':13, 'André': 17, 'Alexandre': 45}, name="Idade")
serie_Peso_novo = pd.Series({'Augusto':95, 'André': 65, 'Alexandre': 83}, name="Peso")
serie_Altura_nova = pd.Series({'Augusto':192, 'André': 175, 'Alexandre': 177}, name="Altura")
serie_sobrenome = pd.Series({'Augusto':'Castro', 'André':'Castro', 'Alexandre':'Castro'}, name='Sobrenome')
dicionario_novo = {'Sobrenome':serie_sobrenome, 'Peso': serie_Peso_novo, 
                   'Idade': serie_Idade_nova, 'Altura': serie_Altura_nova}
df_novo = pd.DataFrame(dicionario_novo)
df_novo = df_novo.assign(IMC=round(df_novo.eval('Peso/(Altura/100)**2'),2))


# In[26]:


df_novo


# Agora vamos concatená-los:

# In[27]:


pd.concat([df_dict_series,df_novo]) 


# ### Concatenando por coluna
# 
# Para exemplificar vamos considerar os dados de COVID da Paraíba, selecionando casos novos e óbitos novos, e vamos obter dos dados do Brasil apenas os casos e óbitos diários do país, e vamos concatená-los por coluna.

# In[28]:


covid_PB_casos_obitos = dados_covid_PB[['casosNovos','obitosNovos']]


# Vamos tratar os dados do Brasil:

# In[29]:


covid_BR_casos_obitos = covid_BR.query('regiao=="Brasil"')
covid_BR_casos_obitos = covid_BR_casos_obitos.set_index('data')
covid_BR_casos_obitos = covid_BR_casos_obitos[['casosNovos','obitosNovos']].rename({
    'casosNovos':'casosBR', 'obitosNovos':'obitosBR'
}, axis=1)


# In[30]:


covid_PB_casos_obitos


# In[31]:


covid_BR_casos_obitos


# Vamos agora concatená-los por coluna:

# In[32]:


pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)


# Para um polimento final, vamos substituir os valores `NaN` que ocorreram antes do dia 13 de julho por 0. Para tanto, a forma ideal é utilizando o método `map`:

# In[33]:


dados_PB_BR = pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)
dados_PB_BR['casosNovos'] = dados_PB_BR.casosNovos.map(lambda caso: 0 if np.isnan(caso) else caso).astype('int')
dados_PB_BR['obitosNovos'] = dados_PB_BR.obitosNovos.map(lambda obito: 0 if np.isnan(obito) else obito).astype('int')
dados_PB_BR


# ### Mesclando *DataFrames* através de *joins*
# 
# Para realizar *joins* iremos utilizar a função `merge` do *pandas*. *joins* tomam duas tabelas, uma tabela à esquerda e uma à direita e retornam uma terceira tabela contendo a união das colunas das duas tabelas.

# Existem 4 tipos de *joins*:
# 
# * *left join*: Apenas irão aparecer os *index* (da linha) que existem na tabela à esquerda;
# * *right join*: Apenas irão aparecer os *index* (da linha) que existem na tabela à direita;
# * *inner join*: Apenas irão aparecer os *index* que existem nas duas tabelas;
# * *full join* ou *outer join*: irão aparecer todos os *index* das duas tabelas.

# Para exemplificar vamos considerar dois *DataFrames* (aqui teremos menos linhas, com nomes e dados fictícios). O primeiro *DataFrame* consistirá de nomes de alunos, CPF e matrícula da UFPB (*nome_cpf_mat*). O segundo *DataFrame* consistirá de nome, CPF e e-mail (*nome_cpf_email*). Nosso objetivo é criar um novo *DataFrame* contendo Nome, CPF, matrícula e e-mail.

# Temos ainda as seguintes situações:
# 
# - No *DataFrame* *nome_cpf_mat* existem alunos que não estão presentes no *nome_cpf_email*, pois não enviaram esta informação.
# 
# - No *DataFrame* *nome_cpf_email* existem alunos que não estão presentes no *nome_cpf_mat* pois estes não são alunos da UFPB.

# In[34]:


nome_cpf_mat = pd.read_csv('data/nome_cpf_mat.csv')
nome_cpf_email = pd.read_csv('data/nome_cpf_email.csv')


# Vamos agora examinar os *DataFrames*. Como são bem simples, basta realizar *prints* deles.

# In[35]:


nome_cpf_mat


# In[36]:


nome_cpf_email


# Tipicamente é bom possuir *index* únicos. Neste sentido, vamos definir o CPF como *index*:

# In[37]:


nome_cpf_mat = nome_cpf_mat.set_index('CPF')
nome_cpf_email = nome_cpf_email.set_index('CPF')


# Vamos agora realizar um **left** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos com matrícula irão aparecer):

# In[38]:


pd.merge(nome_cpf_mat, nome_cpf_email, how = 'left', on = ['Nome','CPF'])


# - Na opção *how* dizemos qual o tipo de *join* que queremos realizar. 
# 
# - Na opção *on* dizemos quais as colunas que existem em comum nos *DataFrames*.
# 
# Veja o que aconteceria se informássemos apenas que o *CPF* está presente nos dois *DataFrames*:

# In[39]:


pd.merge(nome_cpf_mat, nome_cpf_email, how = 'left', on = 'CPF')


# Observe que os nomes dos alunos que estão na segunda tabela ficam indeterminados na coluna *Nome_y*.

# Vamos agora realizar um **right** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos **com e-mail** irão aparecer):

# In[40]:


pd.merge(nome_cpf_mat, nome_cpf_email, how = 'right', on = ['Nome','CPF'])


# Vamos agora realizar um **inner** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, apenas alunos **com matrícula e com e-mail** irão aparecer):

# In[41]:


pd.merge(nome_cpf_mat, nome_cpf_email, how = 'inner', on = ['Nome','CPF'])


# Por fim, vamos agora realizar um **outer** ou **full** join com o *DataFrame* **nome_cpf_mat** ficando à esquerda (neste caso, **todos** os alunos irão aparecer):

# In[42]:


pd.merge(nome_cpf_mat, nome_cpf_email, how = 'outer', on = ['Nome','CPF'])


# ### Os métodos *apply*, *map* e *applymap*
# 
# A ideia é relativamente simples. Os três métodos são vetorizados e aplicam uma função ou uma substituição via dicionário de tal forma que:
# 
# * *apply* é realizado via linha ou coluna em um *DataFrame*;
# * *map* é aplicado a cada elemento de uma *Series*;
# * *applymap* é aplicado a cada elemento de um *DataFrame*.
# 
# Já vimos diversos exemplos de uso de `map`. Vejamos exemplos de `applymap` e `apply`.

# * Neste exemplo vamos retomar a concatenação entre os dados da Paraíba e do Brasil, porém iremos substituir *todos* os valores de `NaN` por zero, usando o métodp `applymap`.

# In[43]:


dados_PB_BR = pd.concat([covid_PB_casos_obitos, covid_BR_casos_obitos], axis=1)
dados_PB_BR.applymap(lambda valor: 0 if np.isnan(valor) else valor)


# Vamos utilizar `apply` para realizar a soma de casos e óbitos através de mais de uma forma

# In[44]:


dados_PB_BR.apply(lambda x: np.sum(x)).astype('int')


# Se quisermos realizar a operação por linhas, basta utilizar o argumento `axis=1`:

# In[45]:


dados_PB_BR.apply(lambda x: (x>0).all(), axis=1)

