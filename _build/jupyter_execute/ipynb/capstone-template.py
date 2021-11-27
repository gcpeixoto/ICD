#!/usr/bin/env python
# coding: utf-8

# # Relátorio de Projeto Final (Modelo)
# 
# **Introdução à Ciência de Dados - Prof. Gustavo Oliveira - Semestre 202Y/0X**
# 
# **Equipe:** 
# 
# - Euclides de Alexandria, 'euclides.alexandria@nome.edu.br'
# - Rei Henrique VII, 'henry@eu.com'
# - Cosme de Médici, 'cmedici@yuhh.com.br'
# 
# _Nota_: altere Y (1,2,3,...) e X (1 ou 2) correspondentemente na identificação de ano/semestre.
# 
# <hr>

# ## Resumo
# 
# Escreva em uma ou duas sentenças, no máximo, a finalidade do relatório. 
# 
# Exemplo: 
# 
# >Aplicamos a técnica de _heatmap_ para destacar o potencial para produção de biogás na região Nordeste. 

# ## Descrição do problema
# 
# Descreva o problema a ser tratado em até 3 parágrafos. (O quê?)
# 
# Exemplo: 
# 
# > O crescimento populacional associado aos hábitos de consumo modernos são fatores consideráveis para o aumento do lixo produzido nas cidades. Resíduos sólidos são tratados de diversas formas, tais como reciclagem, incineração e aterro sanitário (REFERÊNCIA 1, ANO). 
# >
# > Em geral, nos aterros sanitários, os compostos orgânicos podem ser tratados por processos termoquímicos ou bioquímicos que geram o biogás. Embora algumas cidades da região Nordeste possuam dados sobre o volume produzido de matéria orgânica semanalmente, não houve até o momento nenhuma análise sobre o potencial de geração de biogás nos aterros sanitários municipais (REFERÊNCIA 2, ANO). 
# >
# > A questão central que buscamos responder é: _podemos construir um mapa de calor sobre a região Nordeste pelo qual possamos, rapidamente, visualizar o potencial de geração de biogás nos municípios?_ 

# ## Metodologia de solução

# Descreva a metodologia utilizada para resolver o problema proposto. (Como?)
# 
# Exemplo: 
# 
# > Para resolver o problema proposto, usamos a seguinte metodologia:
# > 1. Coleta de dados nos sites das companhias de limpeza urbana responsáveis pela coleta de lixo em 200 municípios da região Nordeste distribuídos conforme a tabela abaixo: 
# > |Estado|No. de municípios|
# > |---|---|
# > |AL|5|
# > |BA|11|
# > |CE|7|
# > |MA|2|
# > |PB|135|
# > |PE|12|
# > |PI|6|
# > |RN|9|
# > |SE|3|
# > 2. Limpeza e processamento dos dados utilizando os módulos _pandas_, _numpy_ e _statsmodels_ para construir DataFrames contendo os parâmetros mais relevantes de análise. A seguir, mostramos um recorte de um dos DataFrames apresentando o volume de compostos orgânicos produzidos por estado (`VCOPS`) e o potencial de biogás médio por estado (`POTBIOGM`).
# 
# |    | NELU                                           | COD   | UF   |   VCOPS (m3) |   POTBIOGM (fraction) |
# |---:|:-----------------------------------------------|:------|:-----|-------------:|---------------------:|
# |  0 | DKX Engenharia                                 | DKX   | PE   |      65000   |                0.443 |
# |  1 | Modal Soluções em Limpeza                      | MOD   | AL   |      21234.1 |                0.211 |
# |  2 | Soft Clean                                     | SFC   | RN   |      42109.8 |                0.112 |
# |  3 | Autarquia Especial Municipal de Limpeza Urbana | EMLUR | PB   |      87772.3 |                0.652 |
# 
# > 3. Definição da expressão de `POTBIOG`, cujo valor varia entre 0 e 1.
# >
# > 4. Plotagem dos mapas de calor de `POTBIOG` utilizando o módulo _geopandas_.
# >
# > O código a seguir resume os passos fundamentais executados.

# <hr>
# 
# ### Potencial de biogás no Nordeste
# 
# *Notas:* 
# 
# - **os dados produzidos nesta análise são fictícios e não devem ser usados para pesquisa!**
# - para reproduzir este código, é necessário instalar o módulo [`geopandas`](https://geopandas.org/en/stable/index.html), preferencialmente em novo ambiente virtual;
# - os mapas do Brasil estão disponíveis como arquivos .SHP [aqui](https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_BRA_shp.zip'), do site [GADM](https://gadm.org/download_country.html). Consulte política de uso!

# ```python
# import geopandas as geo
# from matplotlib.pyplot import title, subplots
# from numpy.random import normal
# 
# from warnings import filterwarnings
# filterwarnings('ignore')
# ```

# ### Definição de _helper functions_

# ```python
# # biogas potential (POTBIOG) simulator 
# def simulate_POTBIOG(state_name,mean,sigma):
#     state = bra2[bra2['NAME_1'] == state_name]
#     state['POTBIOG'] = normal(mean,sigma,size=len(state))
#     return state
# 
# # plot POTBIOG per state
# def plotfig(UF,state_name):
#     fig, ax = subplots(figsize=(12,8))
#     f = lambda x: x.plot(ax=ax,column='POTBIOG',cmap='Reds',legend=True)
#     f(UF)
#     title(state_name)
#     ax.set_xticks([])
#     ax.set_yticks([]);
# ```

# ### Carregamento de dados
# 
# Baixe o .zip localmente e carregue a partir do diretório ou use métodos robustos do _geopandas_ para raspagem da web.

# ```python
# # local directory on your computer
# local_dir = '/Users/gustavo/Downloads/'
# 
# # level 1 shape file
# bra = geo.read_file(local_dir + 'gadm36_BRA_shp/gadm36_BRA_1.shp')
# 
# # level 2 shape file
# bra2 = geo.read_file(local_dir + 'gadm36_BRA_shp/gadm36_BRA_2.shp')
# 
# # NE region mask
# mask = (bra['NAME_1'] == 'Alagoas') | \
#        (bra['NAME_1'] == 'Bahia') | \
#        (bra['NAME_1'] == 'Ceará') | \
#        (bra['NAME_1'] == 'Maranhão') | \
#        (bra['NAME_1'] == 'Pernambuco') | \
#        (bra['NAME_1'] == 'Piauí') | \
#        (bra['NAME_1'] == 'Paraíba') | \
#        (bra['NAME_1'] == 'Rio Grande do Norte') | \
#        (bra['NAME_1'] == 'Sergipe')
# 
# # NE state limits
# NE = bra[mask]
# 
# # simulate values for 4 states: AL, PB, PE, and RN
# AL = simulate_POTBIOG('Alagoas',0.211,0.05)
# PB = simulate_POTBIOG('Paraíba',0.652,0.06)
# PE = simulate_POTBIOG('Pernambuco',0.443,0.1)
# RN = simulate_POTBIOG('Rio Grande do Norte',0.112,0.08)
# 
# # to have POTBIOG's merged distribution
# # check for artifacts!!!
# ALL = AL.merge(PB,how='outer')
# ALL = ALL.merge(PE,how='outer')
# ALL = ALL.merge(RN,how='outer')
# 
# # plot figure for all NE region
# fig, ax = subplots(figsize=(12,8))
# NE.plot(ax=ax,edgecolor='k',facecolor='gray',alpha=0.3)
# ALL.plot(ax=ax,column='POTBIOG',cmap='Reds',legend=True)
# ax.set_xticks([])
# ax.set_yticks([]);
# title('Potencial de Biogás - Região NE')
# 
# # plot figures per state of interest    
# for a,b in [(AL,'Potencial de Biogás - AL'),
#             (PB,'Potencial de Biogás - PB'),
#             (PE,'Potencial de Biogás - PE'),
#             (RN,'Potencial de Biogás - RN')]:
#     plotfig(a,b)
# ```
# <hr>

# ## Resultados, análise e discussão
# 
# Adicione gráficos, figuras, tabelas e informações necessárias (E aí?)
# 
# Exemplo:
# 
# >A partir dos dados coletados, obtivemos os mapas de calor
# abaixo para o potencial de biogás (`POTBIOG`). 
# ```{figure} ../figs/capstone-template/potbiog-ne.png
# ---
# width: 330px
# name: potbiog-ne
# ---
# POTBIOG - NE.
# ```
# 
# ```{figure} ../figs/capstone-template/potbiog-al.png
# ---
# width: 330px
# name: potbiog-al
# ---
# POTBIOG - AL.
# ```
# 
# ```{figure} ../figs/capstone-template/potbiog-pb.png
# ---
# width: 330px
# name: potbiog-pb
# ---
# POTBIOG - PB.
# ```
# 
# ```{figure} ../figs/capstone-template/potbiog-pe.png
# ---
# width: 330px
# name: potbiog-pe
# ---
# POTBIOG - PE.
# ```
# 
# ```{figure} ../figs/capstone-template/potbiog-rn.png
# ---
# width: 330px
# name: potbiog-rn
# ---
# POTBIOG - RN.
# ```
# 
# >Verifica-se que os valores se distribuem de maneira heterogênea na região estudada, mas o POTBIOG do estado da Paraíba é superior aos demais.

# ## Referências bibliográficas
# 
# Registre todas as referências utilizadas no formato utilizado no template do mini-artigo. Referências incluem:
# 
# - Livro
# - Artigo
# - Site
# - Post
# - etc.

# ### Ajuda (esta seção não deve ser incluída no relatório!)

# Recursos para aprender como escrever o relatório. Caso queira fazer algo e não saiba, pergunte ao professor. Se ele souber, orientará como fazer.
# 
# - O que é Markdown?: [link](https://pt.wikipedia.org/wiki/Markdown)
# 
# - Dicas rápidas de Markdown: [link](https://www.markdownguide.org/cheat-sheet/)
# 
# - Editor online para aprender Markdown: [link](https://stackedit.io/app#)
# 
# - Como inserir texto, imagens e tabelas em notebooks: [link](https://www.earthdatascience.org/courses/intro-to-earth-data-science/file-formats/use-text-files/format-text-with-markdown-jupyter-notebook/)
