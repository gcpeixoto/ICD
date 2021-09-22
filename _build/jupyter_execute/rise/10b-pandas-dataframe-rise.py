#!/usr/bin/env python
# coding: utf-8

# # Manipulação de dados - II

# ## *DataFrames*
# 
# O *DataFrame* é a segunda estrutura basilar do *pandas*. Um *DataFrame*:
# - é uma tabela, ou seja, é bidimensional;
# - tem cada coluna formada como uma *Series* do *pandas*;
# - pode ter *Series* contendo tipos de dado diferentes.

# In[145]:


import numpy as np
import pandas as pd


# ## Criação de um *DataFrame*

# O método padrão para criarmos um *DataFrame* é através de uma função com mesmo nome.
# 
# ```python
# df_exemplo = pd.DataFrame(dados_de_interesse, index = indice_de_interesse, 
#                           columns = colunas_de_interesse)
# ```

# Ao criar um *DataFrame*, podemos informar
# - `index`: rótulos para as linhas (atributos *index* das *Series*).
# - `columns`: rótulos para as colunas (atributos *name* das *Series*).

# No _template_, `dados_de_interesse` pode ser
# 
# * um dicionário de:
#   * *arrays* unidimensionais do *numpy*;
#   * listas;
#   * dicionários;
#   * *Series* do *pandas*.
# * um *array* bidimensional do *numpy*;
# * uma *Series* do *Pandas*;
# * outro *DataFrame*.

# ### *DataFrame* a partir de dicionários de *Series*
# 
# Neste método de criação, as *Series* do dicionário não precisam possuir o mesmo número de elementos. O *index* do *DataFrame* será dado pela **união** dos *index* de todas as *Series* contidas no dicionário.

# Exemplo:

# In[148]:


serie_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22}, name="Idade") 


# In[149]:


serie_Peso = pd.Series({'Ana':55, 'João': 80, 'Maria': 62, 'Pedro': 67, 'Túlio': 73}, name="Peso")


# In[150]:


serie_Altura = pd.Series({'Ana':162, 'João': 178, 'Maria': 162, 'Pedro': 165, 'Túlio': 171}, name="Altura")


# In[151]:


dicionario_series_exemplo = {'Idade': serie_Idade, 'Peso': serie_Peso, 'Altura': serie_Altura}


# In[152]:


df_dict_series = pd.DataFrame(dicionario_series_exemplo) 


# In[154]:


df_dict_series  


# > Compare este resultado com a criação de uma planilha pelos métodos usuais. Veja que há muita flexibilidade para criarmos ou modificarmos uma tabela.
# 
# Vejamos exemplos sobre como acessar intervalos de dados na tabela.

# In[159]:


pd.DataFrame(dicionario_series_exemplo, index=['João','Ana','Maria'])


# In[164]:


pd.DataFrame(dicionario_series_exemplo, index=['Ana','Maria'], columns=['Altura','Peso'])


# Neste exemplo, adicionamos a coluna `IMC`, ainda sem valores calculados.

# In[166]:


pd.DataFrame(dicionario_series_exemplo, index=['Ana','Maria','Paula'], 
             columns=['Peso','Altura','IMC'])


# In[167]:


df_exemplo_IMC = pd.DataFrame(dicionario_series_exemplo, 
             columns=['Peso','Altura','IMC'])


# Agora, mostramos como os valores do IMC podem ser calculados diretamente por computação vetorizada sobre as *Series*.

# In[168]:


df_exemplo_IMC['IMC'] = round(df_exemplo_IMC['Peso']/(df_exemplo_IMC['Altura']/100)**2,2)


# In[13]:


df_exemplo_IMC


# ### *DataFrame* a partir de dicionários de listas ou *arrays* do *numpy*
# 
# Neste método de criação, os *arrays* ou as listas **devem** possuir o mesmo comprimento. Se o *index* não for informado, o *index* será dado de forma similar ao do objeto tipo *Series*.

# Exemplo com dicionário de listas:

# In[169]:


dicionario_lista_exemplo = {'Idade': [20,19,21,22,20],
                            'Peso': [55,80,62,67,73],
                            'Altura': [162,178,162,165,171]}


# In[15]:


pd.DataFrame(dicionario_lista_exemplo)


# Mais exemplos:

# In[170]:


pd.DataFrame(dicionario_lista_exemplo, index=['Ana','João','Maria','Pedro','Túlio'])


# Exemplos com dicionário de *arrays* do *numpy*:

# In[171]:


dicionario_array_exemplo = {'Idade': np.array([20,19,21,22,20]),
                            'Peso': np.array([55,80,62,67,73]),
                            'Altura': np.array([162,178,162,165,171])}


# In[18]:


pd.DataFrame(dicionario_array_exemplo)


# Mais exemplos:

# In[172]:


pd.DataFrame(dicionario_array_exemplo, index=['Ana','João','Maria','Pedro','Túlio'])


# ### *DataFrame* a partir de uma *Series* do *pandas*
# 
# Neste caso, o *DataFrame* terá o mesmo *index* que a *Series* do *pandas* e apenas uma coluna.

# In[173]:


series_exemplo = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20})


# In[174]:


pd.DataFrame(series_exemplo)


# Caso a *Series* possua um atributo `name` especificado, este será o nome da coluna do *DataFrame*.

# In[175]:


series_exemplo_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}, name="Idade")


# In[176]:


pd.DataFrame(series_exemplo_Idade)


# ### *DataFrame* a partir de lista de *Series* do *pandas*
# 
# Neste caso, a entrada dos dados da lista no *DataFrame* será feita por linha.

# In[177]:


pd.DataFrame([serie_Peso, serie_Altura, serie_Idade]) 


# Podemos corrigir a orientação usando o método `transpose`.

# In[180]:


pd.DataFrame([serie_Peso, serie_Altura, serie_Idade]).transpose()


# ### *DataFrame* a partir de arquivos
# 
# Para criar um *DataFrame* a partir de um arquivo, precisamos de funções do tipo `pd.read_FORMATO`, onde `FORMATO` indica o formato a ser importado.

# Os formatos mais comuns são: 
# 
# * *csv* (comma-separated values), 
# * *xls* ou *xlsx* (formatos do Microsoft Excel),
# * *hdf5* (comumente utilizado em *big data*), 
# * *json* (comumente utilizado em páginas da internet).

# As funções para leitura correspondentes são: 
# * `pd.read_csv`, 
# * `pd.read_excel`, 
# * `pd.read_hdf`, 
# * `pd.read_json`, 
# 
# respectivamente.

# De todas elas, a função mais utilizada é `read_csv`. Ela possui vários argumentos. Vejamos os mais utilizados:
# 
# * `file_path_or_buffer`: o endereço do arquivo a ser lido. Pode ser um endereço da internet.
# * `sep`: o separador entre as entradas de dados. O separador padrão é `,`.
# * `index_col`: a coluna que deve ser usada para formar o *index*. O padrão é `None`. Porém pode ser alterado para outro. Um separador comumente encontrado é o `\t` (TAB).
# * `names`: nomes das colunas a serem usadas. O padrão é `None`.
# * `header`: número da linha que servirá como nome para as colunas. O padrão é `infer` (ou seja, tenta deduzir automaticamente). Se os nomes das colunas forem passados através do `names`, então `header` será automaticamente considerado como `None`.  

# **Exemplo:** considere o arquivo `../database/exemplo_data.csv` contendo:
# 
# ```
# ,coluna_1,coluna_2
# 2020-01-01,-0.4160923582996922,1.8103644347460834
# 2020-01-02,-0.1379696602473578,2.5785204825192785
# 2020-01-03,0.5758273450544708,0.06086648807755068
# 2020-01-04,-0.017367186564883633,1.2995865328684455
# 2020-01-05,1.3842792448510655,-0.3817320973859929
# 2020-01-06,0.5497056238566345,-1.308789022968975
# 2020-01-07,-0.2822962331437976,-1.6889791765925102
# 2020-01-08,-0.9897300598660013,-0.028120707936426497
# 2020-01-09,0.27558240737928663,-0.1776585993494299
# 2020-01-10,0.6851316082235455,0.5025348904591399
# ``` 
# 
# Para ler o arquivo acima basta fazer:

# In[26]:


df_exemplo_0 = pd.read_csv('../database/exemplo_data.csv')


# In[27]:


df_exemplo_0


# No exemplo anterior, as colunas receberam nomes corretamentes exceto pela primeira coluna que gostaríamos de considerar como *index*. Neste caso fazemos:

# In[28]:


df_exemplo = pd.read_csv('../database/exemplo_data.csv', index_col=0)


# In[29]:


df_exemplo


# #### O método *head* do *DataFrame*
# 
# O método `head`, sem argumento, permite que visualizemos as 5 primeiras linhas do *DataFrame*.

# In[30]:


df_exemplo.head()


# Se for passado um argumento com valor `n`, as `n` primeiras linhas são impressas.

# In[31]:


df_exemplo.head(2)


# In[32]:


df_exemplo.head(7)


# #### O método `tail` do *DataFrame*
# 
# O método `tail`, sem argumento, retorna as últimas 5 linhas do *DataFrame*.

# In[33]:


df_exemplo.tail()


# Se for passado um argumento com valor `n`, as `n` últimas linhas são impressas.

# In[34]:


df_exemplo.tail(2)


# In[35]:


df_exemplo.tail(7)


# ## Atributos de *Series* e *DataFrames*
# 
# Atributos comumente usados para *Series* e *DataFrames* são:
# 
# * `shape`: fornece as dimensões do objeto em questão (*Series* ou *DataFrame*) em formato consistente com o atributo `shape` de um *array* do *numpy*.
# * `index`: fornece o índice do objeto. No caso do *DataFrame* são os rótulos das linhas.
# * `columns`: fornece as colunas (apenas disponível para *DataFrames*) 

# In[36]:


df_exemplo.shape


# In[37]:


serie_1 = pd.Series([1,2,3,4,5])


# In[38]:


serie_1.shape


# In[39]:


df_exemplo.index


# In[40]:


serie_1.index


# In[41]:


df_exemplo.columns


# Se quisermos obter os dados contidos nos *index* ou nas *Series* podemos utilizar a propriedade `.array`.

# In[42]:


serie_1.index.array


# In[43]:


df_exemplo.columns.array


# Se o interesse for obter os dados como um `array` do *numpy*, devemos utilizar o método `.to_numpy()`.
# 
# Exemplo:

# In[44]:


serie_1.index.to_numpy()


# In[45]:


df_exemplo.columns.to_numpy()


# O método `.to_numpy()` também está disponível em *DataFrames*:

# In[46]:


df_exemplo.to_numpy()


# A função do *numpy* `asarray()` é compatível com *index*, *columns* e *DataFrames* do *pandas*:

# In[47]:


np.asarray(df_exemplo.index)


# In[48]:


np.asarray(df_exemplo.columns)


# In[49]:


np.asarray(df_exemplo)


# ### Informações sobre as colunas de um *DataFrame*
# 
# Para obtermos uma breve descrição sobre as colunas de um *DataFrame* utilizamos o método `info`.
# 
# Exemplo:

# In[50]:


df_exemplo.info()


# ## Criando arquivos a partir de *DataFrames*
# 
# Para criar arquivos a partir de *DataFrames*, basta utilizar os métodos do tipo `pd.to_FORMATO`, onde `FORMATO` indica o formato a ser exportado e supondo que a biblioteca *pandas* foi importada com `pd`.

# Com relação aos tipos de arquivo anteriores, os métodos para exportação correspondentes são:
# * `.to_csv` ('endereço_do_arquivo'), 
# * `.to_excel` ('endereço_do_arquivo'), 
# * `.to_hdf` ('endereço_do_arquivo'), 
# * `.to_json`('endereço_do_arquivo'), 
# 
# onde `endereço_do_arquivo` é uma `str` que contém o endereço do arquivo a ser exportado.

# Exemplo:
#     
# Para exportar para o arquivo `exemplo_novo.csv`, utilizaremos o método `.to_csv` ao *DataFrame* `df_exemplo`:

# In[51]:


df_exemplo.to_csv('../database/exemplo_novo.csv')


# ### Exemplo COVID-19 PB

# Dados diários de COVID-19 do estado da Paraíba:
# 
# *Fonte: https://superset.plataformatarget.com.br/superset/dashboard/microdados/*

# In[52]:


dados_covid_PB = pd.read_csv('https://superset.plataformatarget.com.br/superset/explore_json/?form_data=%7B%22slice_id%22%3A1550%7D&csv=true', 
                             sep=',', index_col=0)


# In[53]:


dados_covid_PB.info()


# In[54]:


dados_covid_PB.head()


# In[55]:


dados_covid_PB.tail()


# In[56]:


dados_covid_PB['estado'] = 'PB'


# In[57]:


dados_covid_PB.head()


# In[58]:


dados_covid_PB.to_csv('../database/dadoscovidpb.csv')


# ### Índices dos valores máximos ou mínimos
# 
# Os métodos `idxmin()` e `idxmax()` retornam o *index* cuja entrada fornece o valor mínimo ou máximo da *Series* ou *DataFrame*. Se houver múltiplas ocorrências de mínimos ou máximos, o método retorna a primeira ocorrência.
# 
# Vamos recriar um *DataFrame* genérico.

# In[59]:


serie_Idade = pd.Series({'Ana':20, 'João': 19, 'Maria': 21, 'Pedro': 22, 'Túlio': 20}, name="Idade")
serie_Peso = pd.Series({'Ana':55, 'João': 80, 'Maria': 62, 'Pedro': 67, 'Túlio': 73}, name="Peso")
serie_Altura = pd.Series({'Ana':162, 'João': 178, 'Maria': 162, 'Pedro': 165, 'Túlio': 171}, name="Altura")


# In[60]:


dicionario_series_exemplo = {'Idade': serie_Idade, 'Peso': serie_Peso, 'Altura': serie_Altura}


# In[61]:


df_dict_series = pd.DataFrame(dicionario_series_exemplo)


# In[62]:


df_dict_series


# Assim, podemos localizar quem possui menores idade, peso e altura.

# In[63]:


df_dict_series.idxmin()


# De igual forma, localizamos quem possui maiores idade, peso e altura.

# In[64]:


df_dict_series.idxmax()


# **Exemplo:** Aplicaremos as funções `idxmin()` e `idxmax()` aos dados do arquivo `data/exemplo_data.csv` para localizar entradas de interesse.

# In[65]:


df_exemplo = pd.read_csv('../database/exemplo_data.csv', index_col=0); df_exemplo


# In[66]:


df_exemplo = pd.DataFrame(df_exemplo, columns=['coluna_1','coluna_2','coluna_3'])


# Inserimos uma terceira coluna com dados fictícios.

# In[67]:


df_exemplo['coluna_3'] = pd.Series([1,2,3,4,5,6,7,8,np.nan,np.nan],index=df_exemplo.index)
df_exemplo


# Os *index* correspondentes aos menores e maiores valores são datas, evidentemente.

# In[68]:


df_exemplo.idxmin()


# In[69]:


df_exemplo.idxmax()


# ### Reindexação de *DataFrames*
# 
# No *pandas*, o método `reindex`
# 
# * reordena o *DataFrame* de acordo com o conjunto de rótulos inserido como argumento;
# * insere valores faltantes caso um rótulo do novo *index* não tenha valor atribuído no conjunto de dados;
# * remove valores correspondentes a rótulos que não estão presentes no novo *index*.

# Exemplos:

# In[70]:


df_dict_series.reindex(index=['Victor', 'Túlio', 'Pedro', 'João'], columns=['Altura','Peso','IMC'])


# ## Remoção de linhas ou colunas de um *DataFrame*
# 
# Para remover linhas ou colunas de um *DataFrame* do *pandas* podemos utilizar o método `drop`. O argumento `axis` identifica o eixo de remoção: `axis=0`, que é o padrão, indica a remoção de uma ou mais linhas; `axis=1` indica a remoção de uma ou mais colunas.

# Nos exemplos que segue, note que novos *DataFrames* são obtidos a partir de `df_dict_series` sem que este seja sobrescrito.

# In[71]:


df_dict_series.drop('Túlio') # axis=0 implícito 


# In[72]:


df_dict_series.drop(['Ana','Maria'], axis=0)


# In[73]:


df_dict_series.drop(['Idade'], axis=1)


# ### Renomeando *index* e *columns*
# 
# O método `rename` retorna uma cópia na qual o *index* (no caso de *Series* e *DataFrames*) e *columns* (no caso de *DataFrames*) foram renomeados. O método aceita como entrada um dicionário, uma *Series* do *pandas* ou uma função.

# Exemplo:

# In[74]:


serie_exemplo = pd.Series([1,2,3], index=['a','b','c'])


# In[75]:


serie_exemplo


# In[76]:


serie_exemplo.rename({'a':'abacaxi', 'b':'banana', 'c': 'cebola'})


# Exemplo:

# In[77]:


df_dict_series


# In[78]:


df_dict_series.rename(index = {'Ana':'a', 'João':'j', 'Maria':'m', 'Pedro':'p','Túlio':'t'},
                     columns = {'Idade':'I', 'Peso':'P','Altura':'A'})


# No próximo exemplo, usamos uma *Series* para renomear os rótulos.

# In[79]:


indice_novo = pd.Series({'Ana':'a', 'João':'j', 'Maria':'m', 'Pedro':'p','Túlio':'t'})


# In[80]:


df_dict_series.rename(index = indice_novo)


# Neste exemplo, usamos a função `str.upper` (altera a `str` para "todas maiúsculas") para renomear colunas.

# In[81]:


df_dict_series.rename(columns=str.upper)


# ## Ordenação de *Series* e *DataFrames*
# 
# É possível ordenar ambos pelos rótulos do *index* (para tanto é necessário que eles sejam ordenáveis) ou por valores nas colunas. 
# 
# O método `sort_index` ordena a *Series* ou o *DataFrame* pelo *index*. O método `sort_values` ordena a *Series* ou o *DataFrame* pelos valores (escolhendo uma ou mais colunas no caso de *DataFrames*). No caso do *DataFrame*, o argumento `by` é necessário para indicar qual(is) coluna(s) será(ão) utilizada(s) como base para a ordenação.

# Exemplos:

# In[82]:


serie_desordenada = pd.Series({'Maria': 21, 'Pedro': 22, 'Túlio': 20, 'João': 19, 'Ana':20}); 
serie_desordenada


# In[83]:


serie_desordenada.sort_index() # ordenação alfabética


# Mais exemplos:

# In[84]:


df_desordenado = df_dict_series.reindex(index=['Pedro','Maria','Ana','Túlio','João'])


# In[85]:


df_desordenado


# In[86]:


df_desordenado.sort_index()


# Mais exemplos:

# In[87]:


serie_desordenada.sort_values()


# In[88]:


df_desordenado.sort_values(by=['Altura']) # ordena por 'Altura'


# No caso de "empate", podemos utilizar outra coluna para desempatar.

# In[89]:


df_desordenado.sort_values(by=['Altura','Peso']) # usa a coluna 'Peso' para desempatar


# Os métodos `sort_index` e `sort_values` admitem o argumento opcional `ascending`, que permite inverter a ordenação caso tenha valor `False`.

# In[90]:


df_desordenado.sort_index(ascending=False)


# In[91]:


df_desordenado.sort_values(by=['Idade'], ascending=False)


# ## Comparação de *Series* e *DataFrames*
# 
# *Series* e *DataFrames* possuem os seguintes métodos de comparação lógica: 
# 
# - `eq` (igual);
# - `ne` (diferente);
# - `lt` (menor do que);
# - `gt` (maior do que);
# - `le` (menor ou igual a); 
# - `ge` (maior ou igual a)
# 
# que permitem a utilização dos operadores binários `==`, `!=`, `<`, `>`, `<=` e `>=`, respectivamente. As comparações são realizadas em cada entrada da *Series* ou do *DataFrame*.

# > **Observação**: Para que esses métodos sejam aplicados, todos os objetos presentes nas colunas do *DataFrame* devem ser de mesma natureza. Por exemplo, se um *DataFrame* possui algumas colunas numéricas e outras com *strings*, ao realizar uma comparação do tipo `> 1`, um erro ocorrerá, pois o *pandas* tentará comparar objetos do tipo `int` com objetos do tipo `str`, assim gerando uma incompatibilidade.
# 
# Exemplos:

# In[92]:


serie_exemplo


# In[93]:


serie_exemplo == 2


# De outra forma:

# In[94]:


serie_exemplo.eq(2)


# In[95]:


serie_exemplo > 1


# Ou, na forma funcional:

# In[96]:


serie_exemplo.gt(1)


# In[97]:


df_exemplo > 1


# > **Importante:** Ao comparar *np.nan*, o resultado tipicamente é falso:

# In[98]:


np.nan == np.nan


# In[99]:


np.nan > np.nan


# In[100]:


np.nan >= np.nan


# Só é verdadeiro para indicar que é diferente:

# In[101]:


np.nan != np.nan


# Neste sentido, podemos ter tabelas iguais sem que a comparação usual funcione:

# In[102]:


# 'copy', como o nome sugere, gera uma cópia do DataFrame
df_exemplo_2 = df_exemplo.copy() 


# In[103]:


(df_exemplo == df_exemplo_2)


# O motivo de haver entradas como `False` ainda que `df_exemplo_2` seja uma cópia exata de `df_exemplo` é a presença do `np.nan`. Neste caso, devemos utilizar o método `equals` para realizar a comparação.

# In[104]:


df_exemplo.equals(df_exemplo_2)


# ## Os métodos `any`, `all` e a propriedade `empty`
# 
# O método `any` é aplicado a entradas booleanas (verdadeiras ou falsas) e retorna *verdadeiro* se existir alguma entrada verdadeira, ou *falso*, se todas forem falsas. O método `all` é aplicado a entradas booleanas e retorna *verdadeiro* se todas as entradas forem verdadeiras, ou *falso*,  se houver pelo menos uma entrada falsa. A propriedade `empty` retorna *verdadeiro* se a *Series* ou o *DataFrame* estiver vazio, ou *falso* caso contrário.

# Exemplos:

# In[105]:


serie_exemplo


# In[106]:


serie_exemplo_2 = serie_exemplo-2; 
serie_exemplo_2


# In[107]:


(serie_exemplo_2 > 0).any()


# In[108]:


(serie_exemplo > 1).all()


# Este exemplo reproduz um valor `False` único.

# In[109]:


(df_exemplo == df_exemplo_2).all().all()


# In[110]:


serie_exemplo.empty


# Mais exemplos:

# In[111]:


(df_exemplo == df_exemplo_2).any()


# In[112]:


df_exemplo.empty


# In[113]:


df_vazio = pd.DataFrame()


# In[114]:


df_vazio.empty


# ## Seleção de colunas de um *DataFrame*
# 
# Para selecionar colunas de um *DataFrame*, basta aplicar *colchetes* a uma lista contendo os nomes das colunas de interesse.

# No exemplo abaixo, temos um *DataFrame* contendo as colunas `'Idade'`, `'Peso'` e `'Altura'`. Selecionaremos `'Peso'` e `'Altura'`, apenas.

# In[115]:


df_dict_series[['Peso','Altura']]


# Se quisermos selecionar apenas uma coluna, não há necessidade de inserir uma lista. Basta utilizar o nome da coluna:

# In[116]:


df_dict_series['Peso']


# Para remover colunas, podemos utilizar o método `drop`.

# In[117]:


df_dict_series.drop(['Peso','Altura'], axis=1)


# ### Criação de novas colunas a partir de colunas existentes
# 
# Um método eficiente para criar novas colunas a partir de colunas já existentes é `eval`. Neste método, podemos utilizar como argumento uma *string* contendo uma expressão matemática envolvendo nomes de colunas do *DataFrame*.

# Como exemplo, vamos ver como calcular o IMC no *DataFrame* anterior:

# In[118]:


df_dict_series.eval('Peso/(Altura/100)**2')


# Se quisermos obter um *DataFrame* contendo o IMC como uma nova coluna, podemos utilizar o método `assign` (sem modificar o *DataFrame* original):

# In[119]:


df_dict_series.assign(IMC=round(df_dict_series.eval('Peso/(Altura/100)**2'),2))


# In[120]:


df_dict_series # não modificado


# Se quisermos modificar o *DataFrame* para incluir a coluna IMC fazemos:

# In[121]:


df_dict_series['IMC']=round(df_dict_series.eval('Peso/(Altura/100)**2'),2)


# In[122]:


df_dict_series # modificado "in-place"


# ## Seleção de linhas de um *DataFrame*
# 
# Podemos selecionar linhas de um *DataFrame* de diversas formas diferentes. Veremos agora algumas dessas formas.
# 
# Diferentemente da forma de selecionar colunas, para selecionar diretamente linhas de um *DataFrame* devemos utilizar o método `loc` (fornecendo o *index*, isto é, o rótulo da linha) ou o `iloc` (fornecendo a posição da linha):

# Trabalharemos a seguir com um banco de dados atualizado sobre a COVID-19. Para tanto, importaremos o módulo `datetime` que nos auxiliará com datas.

# In[123]:


import datetime


# In[124]:


dados_covid_PB = pd.read_csv('https://superset.plataformatarget.com.br/superset/explore_json/?form_data=%7B%22slice_id%22%3A1550%7D&csv=true', 
                             sep=',', index_col=0)

# busca o banco na data D-1, visto que a atualização
# ocorre em D
ontem = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d') 


# In[125]:


dados_covid_PB.head(1)


# Podemos ver as informações de um único dia como argumento. Para tanto, excluímos a coluna `'Letalidade'` (valor não inteiro) e convertemos o restante para valores inteiros:

# In[126]:


dados_covid_PB.loc[ontem].drop('Letalidade').astype('int')


# Podemos selecionar um intervalo de datas como argumento (excluindo letalidade):

# In[127]:


dados_covid_PB.index = pd.to_datetime(dados_covid_PB.index) # Convertendo o index de string para data
dados_covid_PB.loc[pd.date_range('2021-02-01',periods=5,freq="D")].drop('Letalidade',axis=1) 
                #função pd.date_range é muito útil para criar índices a partir de datas.


# Podemos colocar uma lista como argumento:

# In[128]:


dados_covid_PB.loc[pd.to_datetime(['2021-01-01','2021-02-01'])]


# Vamos agora examinar os dados da posição 100 (novamente excluindo a coluna letalidade e convertendo para inteiro):

# In[129]:


dados_covid_PB.iloc[100].drop('Letalidade').astype('int')


# Podemos colocar um intervalo como argumento:

# In[130]:


dados_covid_PB.iloc[50:55].drop('Letalidade', axis=1).astype('int') 


# ### Seleção de colunas com `loc` e `iloc`
# 
# Podemos selecionar colunas utilizando os métodos `loc` e `iloc` utilizando um argumento adicional.

# In[131]:


dados_covid_PB.loc[:,['casosNovos','obitosNovos']]


# In[132]:


dados_covid_PB.iloc[:,4:6] # fatiamento na coluna


# ### Seleção de linhas e colunas específicas com `loc` e `iloc`

# Usando o mesmo princípio de *fatiamento* aplicado a *arrays* do numpy, podemos selecionar linhas e colunas em um intervalo específico de forma a obter uma subtabela.

# In[133]:


dados_covid_PB.iloc[95:100,4:6]


# Neste exemplo um pouco mais complexo, buscamos casos novos e óbitos novos em um período específico e ordenamos a tabela da data mais recente para a mais antiga.

# In[134]:


dados_covid_PB.loc[pd.date_range('2020-04-06','2020-04-10'),['casosNovos','obitosNovos']].sort_index(ascending=False)


# Suponha que o peso de Ana foi medido corretamente, mas registrado de maneira errônea no *DataFrame* `df_dict_series` como 55.

# In[135]:


df_dict_series


# Supondo que, na realidade, o valor é 65, alteramos a entrada específica com um simples `loc`. Em seguida, atualizamos a tabela.

# In[136]:


df_dict_series.loc['Ana','Peso'] = 65

df_dict_series = df_dict_series.assign(IMC=round(df_dict_series.eval('Peso/(Altura/100)**2'),2)) # O IMC mudou


# In[137]:


df_dict_series


# ### Seleção de linhas através de critérios lógicos ou funções
# 
# Vamos selecionar quais os dias em que houve mais de 40 mortes registradas:

# In[138]:


dados_covid_PB.loc[dados_covid_PB['obitosNovos']>40]


# Selecionando os dias com mais de 25 óbitos e mais de 1500 casos novos:

# In[139]:


dados_covid_PB.loc[(dados_covid_PB.obitosNovos > 25) & (dados_covid_PB.casosNovos>1500)]


# **Obs**.: Note que podemos utilizar o nome da coluna como um atributo.

# Vamos inserir uma coluna sobrenome no `df_dict_series`:

# In[140]:


df_dict_series['Sobrenome'] = ['Silva', 'PraDo', 'Sales', 'MachadO', 'Coutinho']
df_dict_series


# Vamos encontrar as linhas cujo sobrenome termina em "do". Para tanto, note que a função abaixo retorna `True` se o final é "do" e `False` caso contrário.
# 
# ```python
# def verifica_final_do(palavra):
#     return palavra.lower()[-2:] == 'do'
# ```
# **Obs**.: Note que convertemos tudo para minúsculo.

# Agora vamos utilizar essa função para alcançar nosso objetivo:

# In[141]:


# 'map' aplica a função lambda a cada elemento da *Series*
df_dict_series['Sobrenome'].map(lambda palavra: palavra.lower()[-2:]=='do') 


# In[142]:


# procurando no df inteiro
df_dict_series.loc[df_dict_series['Sobrenome'].map(lambda palavra: palavra.lower()[-2:]=='do')]


# Vamos selecionar as linhas do mês 2 (fevereiro) usando `index.month`:

# In[143]:


dados_covid_PB.loc[dados_covid_PB.index.month==2].head()


# ### Seleção de linhas com o método *query*
# 
# Similarmente ao método `eval`, ao utilizarmos `query`, podemos criar expressões lógicas a partir de nomes das colunas do *DataFrame*.

# Assim, podemos reescrever o código
# 
# ```python
# dados_covid_PB.loc[(dados_covid_PB.obitosNovos>25) & 
#                    (dados_covid_PB.casosNovos>1500)]
# ```
# como

# In[144]:


dados_covid_PB.query('obitosNovos>25 and casosNovos>1500') # note que 'and' é usado em vez de '&'

