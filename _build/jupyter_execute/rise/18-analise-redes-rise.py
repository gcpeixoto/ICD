#!/usr/bin/env python
# coding: utf-8

# # Análise de redes

# - _Rede_ (_network_) é uma forma de organizar e representar dados discretos. 
# - Redes diferem da forma tabular (linhas e colunas) e funcionam com base em dois conceitos:
# 
# 1. _entidades_, ou _atores_, ou ainda _nós_, e
# 2. _relacionamentos_, ou _links_, ou _arcos_, ou ainda, _conexões_.
# 
# - Casualmente, o conceito de _rede_ se confunde com o conceito matemático de _grafo_.
# - Notação $G(V,E)$ para designar um grafo genérico $G$ com um conjunto $V$ de vértices e um conjunto $E$ de arestas.

# ## Redes complexas
# 
# - Barateamento dos recursos de computação no final do século XX
# - Demanda de problemas complexosa;
# - Evolução da _análise de redes complexas_ (_complex network analysis_, ou CNA)
# - No século XXI, percebemos um interesse explosivo em CNA. 

# Aplicações:
# 
# - transporte: planejamento de malhas ferroviárias, rodovias e conexões entre cidades;
# - sociologia: entender pessoas, comportamento, interação em redes sociais, orientações de pensamento e preferências;
# - energia: linhas de transmissão de energia elétrica;
# - biologia: redes de transmissão de doenças infecciosas;
# - ciência: núcleos de pesquisa mais influentes;

# ## O módulo `networkx`
# 
# Pontos positivos
# 
# - facilidade de instalação;
# - ampla documentação no [site oficial](https://networkx.org);
# - extenso conjunto de funções e algoritmos;
# - versatilidade para lidar com redes de até 100.000 nós.

# In[37]:


import networkx as nx


# ### Criação de grafos não dirigidos

# Em seguida vamos criar um grafo $G$ _não dirigido_. Isso significa que o sentido da aresta é irrelevante. Contudo, vale comentar que há situações em que o sentido da aresta importa. Neste caso, diz-se que o grafo é _dirigido_.

# In[58]:


# cria grafo não dirigido com 4 vértices

# inicializa
G = nx.Graph() 

# adiciona arestas explicitamente
G.add_edge(1,2) 
G.add_edge(1,3)
G.add_edge(2,3)
G.add_edge(3,4)


# Em seguida, visualizamos o grafo com `draw_networkx`.

# In[59]:


nx.draw_networkx(G) 


# ### Adição e deleção de nós e arestas

# Podemos adicionar nós indvidualmente ou por meio de uma lista, bem como usar _strings_ como nome.

# In[60]:


G.add_node('A')   
G.add_nodes_from(['p',99,'Qq'])
G.add_node('Mn') # nó adicionado por engano
nx.draw_networkx(G) 


# Podemos fazer o mesmo com arestas sobre nós existentes ou não existentes.

# In[61]:


G.add_edge('A','p') # aresta individual
G.add_edges_from([(1,99),(4,'A')]) # aresta por lista (origem, destino)
G.add_edge('Mn','no') # 'no' não existente
nx.draw_networkx(G) 


# Nós e arestas podem ser removidos de maneira similar.

# In[62]:


G.remove_node('no')
G.remove_nodes_from(['Qq',99,'p'])
nx.draw_networkx(G)


# In[63]:


G.remove_edge(1,2)
G.remove_edges_from([('A',4),(1,3)])
nx.draw_networkx(G)


# Para remover todas os nós e arestas do grafo, mas mantê-lo criado, usamos `clear`.

# In[64]:


G.clear()


# Verificamos que não há nós nem arestas:

# In[65]:


len(G.nodes()), len(G.edges)


# Para deletá-lo completamente, podemos fazer:

# In[66]:


del G


# ### Criação de grafos aleatórios

# Podemos criar um grafo aleatório de diversas formas. Com `random_geometric_graph`, o grafo de _n_ nós uniformemente aleatórios fica restrito ao "cubo" unitário de dimensão `dim` e conecta quaisquer dois nós _u_ e _v_ cuja distância entre eles é no máximo `raio`.

# In[77]:


# 30 nós com raio de conexão 0.2
n = 30
raio = 0.2
G = nx.random_geometric_graph(n,raio,dim=2)
nx.draw_networkx(G)


# In[82]:


# 30 nós com raio de conexão 5
n = 30
raio = 5
G = nx.random_geometric_graph(n,raio,dim=2)
nx.draw_networkx(G)


# In[84]:


# 12 nós com raio de conexão 1.15
n = 12
raio = 1.15
G = nx.random_geometric_graph(n,raio,dim=2)
nx.draw_networkx(G)


# In[102]:


# 12 nós com raio de conexão 0.4
n = 12
raio = 0.4
G = nx.random_geometric_graph(n,raio,dim=2)
nx.draw_networkx(G)


# ### Impressão de listas de nós e de arestas
# 
# Podemos acessar a lista de nós ou de arestas com:

# In[107]:


G.nodes()


# In[109]:


G.edges()


# Notemos que as arestas são descritas por meio de tuplas (_origem_,_destino_).

# Se especificarmos `data=True`, atributos adicionais são impressos. Para os nós, vemos `pos` como a posição espacial.

# In[110]:


print(G.nodes(data=True))


# No caso das arestas, nenhum atributo existe para este grafo. Contudo, em grafos mais complexos, é comum ter _capacidade_ e _peso_ como atributos. Ambas são relevantes em estudos de _fluxo_, em que se associa a arestas uma "capacidade" de transporte e um "peso" de relevância.

# In[18]:


print(G.edges(data=True))


# ### Criação de redes a partir de arquivos: estudo de caso Facebook
# 
# Um modo conveniente de criar redes é ler diretamente um arquivo contendo informações sobre a conectividade. 
# 
# O _dataset_ que usaremos a partir deste ponto em diante corresponde a uma rede representando a amizade entre usuários reais do Facebook. 
# 
# Cada usuário é representado por um vértice e um vínculo de amizade por uma aresta. Os dados são anônimos.
# 
# Carregamos o arquivo _.txt_ com `networkx.read_edgelist`.

# In[112]:


fb = nx.read_edgelist('../database/fb_data.txt')
len(fb.nodes), len(fb.edges)


# Vemos que esta rede possui 4039 usuários e 88234 vínculos de amizade. Você pode plotar o grafo para visualizá-lo, porém pode demorar um pouco...

# ## Propriedades relevantes
# 
# Vejamos algumas propriedades de interesse de redes e grafos.

# ### Grau
# 
# O _grau_ de um nó é o número de arestas conectadas a ele. Assim, o grau médio da rede do Facebook acima pode ser calculado por:

# In[20]:


fb.number_of_edges()/fb.number_of_nodes()


# In[113]:


# outra forma
fb.size()/fb.order()


# Ambos os resultados mostram que cada usuário nesta rede tem pelo menos 21 amizades.

# In[ ]:





# ### Caminho
# 
# _Caminho_ é uma sequencia de nós conectados por arestas contiguamente. O _caminho mais curto_ em uma rede é o menor número de arestas a serem visitadas partindo de um nó de origem _u_ até um nó de destino _v_.
# 
# A seguir, plotamos um caminho formado por 20 nós.

# In[144]:


Gpath = nx.path_graph(35)
nx.draw_networkx(Gpath)


# ### Componente
# 
# Um grafo é _conexo_ se para todo par de nós, existe um caminho entre eles. Uma _componente conexa_, ou simplesmente _componente_ de um grafo é um subconjunto de seus nós tal que cada nó no subconjunto tem um caminho para todos os outros.
# 
# Podemos encontrar todas as componentes da rede do Facebook usando `connected_componentes`. Entretanto, o resultado final é um objeto _generator_. Para acessarmos as componentes, devemos usar um iterador.

# In[148]:


cc = nx.connected_components(fb)

# varre componentes e imprime os primeiros 5 nós
for c in cc:
    print(list(c)[0:5])


# Uma vez que há apenas uma lista impressa, temos que a rede do Facebook, na verdade, é uma componente única. De outra forma,

# In[149]:


# há apenas 1 componente conexa, a própria rede
nx.number_connected_components(fb)


# ### Subgrafo
# 
# _Subgrafo_ é um subconjunto dos nós de um grafo e todas as arestas que os conectam. Para selecionarmos um _subgrafo_ da rede Facebook, usamos `subgraph`. Os argumentos necessários são: o grafo original e uma lista dos nós de interesse. Abaixo, geramos uma lista aleatória de `ng` nós.

# In[189]:


from numpy.random import randint
# número de nós do subgrafo
ng = 40
# identifica nós (nomes são strings)
nodes_to_get = randint(1,fb.number_of_nodes(),ng).astype(str)
# extrai subgrafo
fb_sub = nx.subgraph(fb,nodes_to_get)
# plota
nx.draw_networkx(fb_sub)


# Se fizermos alguma alteração no grafo original, pode ser que o número de componentes se altere. Vejamos:

# In[191]:


# copia grafo
fb_less = fb.copy()

# remove o nó '0'
fb_less.remove_node('0')

# novas componentes
nx.number_connected_components(fb_less)


# Neste exemplo, a retirada de apenas um nó do grafo original resultou em 19 componentes, com número variável de elementos.

# In[193]:


ncs = []
for c in nx.connected_components(fb_less):
    ncs.append(len(c))


# In[28]:


# número de componentes em ordem
sorted(ncs,reverse=True)


# ## Métricas de centralidade
# 
# A _centralidade_ de um nó mede a sua importância relativa no grafo. Em outras palavras, nós mais "centrais" tendem a ser considerados os mais influentes, privilegiados ou comunicativos.
# 
# Em uma rede social, por exemplo, um usuário com alta centralidade pode ser um _influencer_, um político, uma celebridade, ou até mesmo um malfeitor. Há diversas _métricas de centralidade_ disponíveis. Aqui veremos as 4 mais corriqueiras.
# 
# Vamos calcular as centralidades de um subgrafo da rede do Facebook. Primeiro, extraímos um subgrafo menor.

# In[194]:


# número de nós do subgrafo
ng = 400

# identifica nós (nomes são strings)
nodes_to_get = randint(1,fb.number_of_nodes(),ng).astype(str)

# extrai subgrafo
fb_sub_c = nx.subgraph(fb,nodes_to_get)


# ### Centralidade de grau (_degree centrality_)
# 
# - Definida pelo número de arestas de um nó;

# In[221]:


import matplotlib.pyplot as plt

# centralidade de grau
deg = nx.degree_centrality(fb_sub_c)
nx.draw_networkx(fb_sub_c,
                 with_labels=False,
                 node_color=list(deg.values()),
                 alpha=0.6,
                 cmap=plt.cm.afmhot)


# ### Centralidade de intermediação (_betweeness centrality_)
# 
# = Definida pelo número de vezes em que o nó é visitado ao tomarmos o caminho mais curto entre um par de nós distintos deste. Esta centralidade pode ser imaginada como uma "ponte" ou "pedágio".

# In[222]:


# centralidade de intermediação
bet = nx.betweenness_centrality(fb_sub_c)
nx.draw_networkx(fb_sub_c,
                 with_labels=False,
                 node_color=list(bet.values()),
                 alpha=0.6,
                 cmap=plt.cm.afmhot)


# ### Centralidade de proximidade (_closeness centrality_)
# 
# Definida pelo inverso da soma das distâncias do nó de interesse a todos os outros do grafo. Ela quão "próximo" o nó é de todos os demais. Um nó com alta centralidade é aquele que, grosso modo, "dista por igual" dos demais.

# In[226]:


# centralidade de proximidade
cln = nx.closeness_centrality(fb_sub_c)
nx.draw_networkx(fb_sub_c,
                 with_labels=False,
                 node_color=list(cln.values()),
                 alpha=0.6,
                 cmap=plt.cm.afmhot)


# ### Centralidade de autovetor (_eigenvector centrality_)
# 
# Definida pelo escore relativo para um nó tomando por base suas conexões. Conexões com nós de alta centralidade aumentam seu escore, ao passo que conexões com nós de baixa centralidade reduzem seu escore. De certa forma, ela mede como um nó está conectado a nós influentes.

# In[233]:


# centralidade de autovetor
eig = nx.eigenvector_centrality(fb_sub_c)
nx.draw_networkx(fb_sub_c,
                 with_labels=False,
                 node_color=list(eig.values()),
                 alpha=0.6,
                 cmap=plt.cm.afmhot)


# ## Layouts de visualização
# 
# Podemos melhorar a visualização das redes alterando os layouts. O exemplo a seguir dispõe o grafo em um layout melhor, chamado de `spring`. Este layout acomoda a posição dos nós iterativamente por meio de um algoritmo especial. Além disso, a centralidade de grau está normalizada no intervalo [0,1] e escalonada. 
# 
# Com o novo plot, é possível distinguir "comunidades", sendo os maiores nós os mais centrais.

# In[235]:


from numpy import array
pos_fb = nx.spring_layout(fb_sub_c,iterations = 50)

nsize = array([v for v in deg.values()])
nsize = 500*(nsize - min(nsize))/(max(nsize) - min(nsize))
nodes = nx.draw_networkx_nodes(fb_sub_c, pos = pos_fb, node_size = nsize)
edges = nx.draw_networkx_edges(fb_sub_c, pos = pos_fb, alpha = .1)


# Um layout aleatório pode ser plotado da seguinte forma:

# In[35]:


pos_fb = nx.random_layout(fb_sub_c)
nx.draw_networkx(fb_sub_c,pos_fb,with_labels=False,alpha=0.5)

