#!/usr/bin/env python
# coding: utf-8

# ## Questionário 73 (Q73)
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

# Para responder às questões, leia o texto introdutório a seguir.
# 
# >Diversos países firmam acordos bilaterais com o intuito de fortalecer interesses mútuos. Uma rede multinacional da qual o Brasil faz parte começou a ser modelada por cientistas de dados a partir de um grafo não dirigido em que os _nós_ do grafo representam os países, renomeados segundo o código Alpha-3 do padrão [IBAN](https://www.iban.com/country-codes), e as _arestas_ representam a existência de um acordo bilateral.
# > A figura abaixo mostra, por exemplo, um subgrafo dessa rede formado por Áustria (AUS), Bélgica (BEL), Brasil (BRA), Noruega (NOR) e Estados Unidos (USA).
# ```{figure} ../figs/q/q73.png
# ---
# width: 660px
# name: rede
# ---
# Exemplo de rede de países que mantêm acordos bilaterais.
# ```
# > O arquivo `paises-acordo-bilateral.txt` contém, implicitamente, a lista de conexões que formam o grafo da rede inteira, as quais são determinadas por pares do tipo `x,y`, onde `x` e `y` são nomes de países não padronizados. Por exemplo, o par `China,Norway` indica que há um acordo bilateral entre China e Noruega.
# 
# >*Obs.:* acesse o arquivo [aqui](https://github.com/gcpeixoto/ICD/tree/main/database/paises-acordo-bilateral.txt).

# **Questão 1.** Faça a raspagem da tabela de códigos de países disponíveis na página [IBAN](https://www.iban.com/country-codes) para recuperar os códigos Alpha-3 para cada país contido na lista de arestas e crie um segundo arquivo chamado `paises-acordo-bilateral-IBAN.txt`. Use o módulo `networkx` e a função `read_edgelist` para construir o grafo da rede multinacional. Em seguida, assinale a alternativa correta para a tupla (número de nós, número de arestas) que você encontrou. Sugestão: use as funções `get_table_head` e `get_table_body` criadas no capítulo do livro de ICD sobre _Raspagem de dados_.
# 
# A. (14, 60)
# 
# B. (16, 62)
# 
# C. (12, 56)
# 
# D. (14, 66)

# ## GABARITO
# 
# Alternativa **D**.

# 
# 

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import networkx as nx

html = urlopen('https://www.iban.com/country-codes')
bs = BeautifulSoup(html.read(),'html.parser')

# extrai cabeçalho
def get_table_head(t):
    '''Lê objeto tabela e extrai header para lista'''
    res = []
    thead = t.find('thead')
    th = thead.find_all('th')
    for f in th:
        res.append(f.getText().strip())
    return res

t_header = get_table_head(bs.body)

# extrai linhas
def get_table_body(t):
    res = []
    tbody = t.find('tbody')
    tr = tbody.find_all('tr')
    for row in tr:
        this_row = []
        row_fields = row.find_all('td')
        for f in row_fields:
            this_row.append(f.getText().strip())
            res.append(this_row)
    return res

r = get_table_body(bs.body)
# DataFrame
iban = pd.DataFrame(r,columns=t_header).drop_duplicates().drop(columns=['Alpha-2 code','Numeric']).reset_index(drop=True)


# In[2]:


f = open('../database/paises-acordo-bilateral.txt','r')
g = open('../database/paises-acordo-bilateral-IBAN.txt','w')

for i in f.readlines():
    p1,p2 = i.strip().split(',') 
    p1 = iban[iban['Country'] == p1]['Alpha-3 code'].values
    p2 = iban[iban['Country'] == p2]['Alpha-3 code'].values
    p1,p2 = p1[0],p2[0]
    s = p1 + ',' + p2 + '\n'
    g.write(s)

f.close()
g.close()


# In[3]:


G = nx.read_edgelist('../database/paises-acordo-bilateral-IBAN.txt',delimiter=',')
Gsub = nx.subgraph(G,['AUT','USA','BRA','BEL',''])
nx.draw_networkx(Gsub,with_labels=True)


# In[4]:


G.number_of_nodes(),G.number_of_edges()


# **Questão 2.** A _centralidade de grau_ `deg`, calculada para cada nó do grafo completo pelo módulo `networkx`, pode ser interpretada, para este estudo de caso, como uma medida relativa da pré-disposição de um país para se abrir à globalização. Neste sentido, calcule `deg` e assinale a opção cujo país é o mais **fechado** ao fenômeno da globalização.
# 
# A. CHN 
# 
# B. NLD
# 
# C. IND
# 
# D. ZAF

# ## GABARITO
# 
# Alternativa **D**.

# In[5]:


# minima deg é ZAF
deg = nx.degree_centrality(G)
deg = {k: v for k, v in sorted(deg.items(), key=lambda item: item[1],reverse=True)}
deg


# **Questão 3.** Semelhantemente à interpretação da questão anterior, a _centralidade de intermediação_ `bet` fornece uma medida relativa de quão boa é a confiança e respeitabilidade diplomática de um país para a concretização de acordos. Calcule `bet` e assinale a opção cujo país é o mais respeitado para intermediar acordos.
# 
# A. AUT
# 
# B. GBR
# 
# C. USA
# 
# D. ISR

# ## GABARITO
# 
# Alternativa **C**.

# In[6]:


# maxima bet é USA
bet = nx.betweenness_centrality(G)
bet = {k: v for k, v in sorted(bet.items(), key=lambda item: item[1],reverse=True)}
bet


# In[7]:


get_ipython().system('rm ../database/paises-acordo-bilateral-IBAN.txt')

