#!/usr/bin/env python
# coding: utf-8

# ## Questionário 72 (Q72)
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
# >Um ataque hacker ao portal do Governo Federal foi identificado após se descobrir na página https://www.gov.br/economia/pt-br/assuntos/processo-eletronico-nacional/conteudo/barramento-de-servicos/relacao-dos-orgaos-e-entidades, associada ao Ministério da Economia, que as _cache keys_ embutidas em alguns links resultavam em uma chave com 6 blocos de 4 dígitos que permitia o acesso furtivo a dados sigilosos.
# >
# >A atividade criminosa funcionava da seguinte forma:
# >
# >1. O hacker coletou cada _cache key_ existente no cabeçalho do arquivo .HTML dessa página exatamente nas vinculações aos arquivos .CSS. A _cache key_ é um número hexadecimal de 32 dígitos que aparece em um elemento `<link>`. No exemplo 
# >```html
# ><link href="https://www.gov.br/economia/ ... cachekey-dac9630aec642a428cd73f4be0a03569.css"  ... />,
# >```
# > a cache key é o número `dac9630aec642a428cd73f4be0a03569`.
# > 2. O hacker usava a _cache key_ como entrada para uma função decriptadora e obtinha um número de 4 dígitos.
# > 3. Juntando as 6 _cache keys_ contidas na página, ele determinava uma sequência do tipo ####.####.####.####.####.####, que era usada para quebrar _firewalls_ e acessar os arquivos sigilosos.
# >
# 
# Como especialista, você frustrou o ataque do hacker usando a função de decriptação dada por:
# ```python
# def decrypt(Hash):
#     return sum(map(lambda x: ord(x),Hash)),
# ```
# onde `Hash` é uma _cache key_. Por exemplo:
# 
# ```python
# print(decrypt('dac9630aec642a428cd73f4be0a03569'))
# 2280
# ```
# 
# 
# _Obs.:_ o relato acima é fictício.

# **Questão 1.** Utilize raspagem de dados para coletar as 6 _cache keys_ contidas na página e determinar as 6 quádruplas que quebram o _firewall_ e assinale a alternativa que contém todas as quádruplas corretas, independentemente da ordem das _cache keys_ que os determinam.
# 
# A. 2184.1999.2200.1090.2215.2175
# 
# B. 1090.1999.2169.2215.2175.2184
# 
# C. 2091.2169.1999.2184.2215.2175
# 
# D. 2175.1999.2184.2215.1090.1010

# ## GABARITO 
# 
# Alternativa **C**.

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.gov.br/economia/pt-br/assuntos/processo-eletronico-nacional/conteudo/barramento-de-servicos/relacao-dos-orgaos-e-entidades')
bs = BeautifulSoup(html.read(),'html.parser')

cachekeys = []
for a in bs.head.find_all('link',href=True):
    href = a.get('href')
    if re.search('cachekey',href):
        cachekeys.append(href.split('cachekey-')[-1].split('.')[0])

# função de decriptação
def decrypt(Hash):
    return sum(map(lambda x: ord(x),Hash))

d = {decrypt(c):c for c in cachekeys}   
d


# **Questão 2.** No corpo do arquivo HTML da página em questão, existem diversas âncoras (elementos da árvore DOM com a tag `<a>...</a>` com URLs que apontam para outros endereços no domínio do Ministério da Economia. Assinale a alternativa correta para o número de links contidos em `<body>` que iniciam pela raiz `https://www.gov.br/economia/pt-br`.
# 
# A. 502
# 
# B. 499 
# 
# C. 400
# 
# D. 380

# ## GABARITO
# 
# Alternativa **B**.

# In[2]:


gov_economia_links = []
for a in bs.body.find_all('a',href=True):
    href = a.get('href')    
    if re.search('(https://www.gov.br/economia/pt-br)',href):
        gov_economia_links.append(href)
        
len(gov_economia_links)        


# **Questão 3.** Marque a alternativa correta para o número de descendentes de `<body>` na árvore DOM correspondente ao arquivo HTML da página em questão.
# 
# A. 5821
# 
# B. 6000
# 
# C. 5800
# 
# D. 5994

# ## GABARITO
# 
# Alternativa **A**.

# In[3]:


k = 0
for _ in bs.body.descendants:
    k += 1
k    

