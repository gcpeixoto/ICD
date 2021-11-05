#!/usr/bin/env python
# coding: utf-8

# # Raspagem de dados

# _Raspagem de dados_ (_data scraping_), em seu sentido mais amplo, é um conceito aplicado à obtenção de dados de um certo programa a partir de outro de forma a extrair conteúdo de alto valor que sejam, prioritariamente, de fácil interpretação a humanos. Atualmente, a raspagem de dados é um sinônimo para _raspagem da web_ (_web scraping_), visto que a fonte mais ampla para coleta dados é a _web_. Então, o ato de "raspar" dados da _web_ equivale a utilizar scripts, programas ou APIs para obter dados relevantes de sites, páginas, blogs, repositórios, ou qualquer outro lugar acessível por conectividade e requisição.
# 
# Através da raspagem de dados, podemos, entre outras coisas,
# 
# - coletar preços de ativos do mercado financeiro em tempo real;
# - baixar históricos de sinistros em saúde pública, tais como os registros de casos durante a pandemia da Covid-19;
# - localizar matérias jornalísticas sobre um mesmo tema em diversos canais de comunicação;
# - encontrar o placar final de todos os jogos da NBA nos últimos 5 anos.
# 
# Durante o curso, você já lidou implicitamente com a raspagem de dados ao utilizar, por exemplo, a função `pandas.read_csv`, por exemplo, para realizar a leitura de um arquivo CSV hospedado em um site da internet. Neste capítulo, faremos uma breve introdução à raspagem de dados usando `BeautifulSoap`, um dos módulos Python mais populares para dissecar páginas da _web_, de maneira a ampliar a nossa compreensão acerca dessa área de conhecimento extremamente relevante para a ciência de dados.

# ## HTML 5

# A maioria das páginas da internet hoje são escritas em uma linguagem chamada _HTML_ (_HyperText Markup Language_), desenvolvida no início da década de 1990 como a linguagem básica da internet. O consórcio [W3C](www.w3.org) (_The World Wide Web Consortium_) é quem assegura os padrões abertos para desenvolvedores _web_. Desde 2014, a versão _HTML 5_ é a recomendada pela W3C para todos os criadores de sites. Em 2019, a W3C e a WHATWG assinaram um [acordo](https://www.w3.org/blog/news/archives/7753) para uniformizar o HTML, concluindo um [documento](https://html.spec.whatwg.org/#abstract) de especificações.
# 
# ```{note}
# Para saber mais sobre a história do HTML e do legado de Tim Berners-Lee, o inventor da World Wide Web (WWW), leia este [texto](https://www.w3.org/People/Raggett/book4/ch02.html).
# ```
# 
# Um documento HTML é estruturado por meio de _elementos_ enclausurados por um par de _tags_ e tem a seguinte aparência:
# 
# ```html
# <!DOCTYPE html>
# <html lang="pt-br">
#  <head>
#   <title>Introdução à Ciência de Dados</title>
#  </head>
#  <body>
#   <h1>Ciência de Dados no século XXI</h1>
#   <p>A História começa neste <a href="historia-icd.html">link</a>.</p>
#   <!-- comentário -->
#  </body>
# </html>
# ```
# No exemplo, `<head>` e `</head>` são exemplo de _tags_ de abertura e fechamento para a seção _head_ do documento. 

# ### A árvore DOM  
# 
# Os navegadores da web interpretam o código HTML e transformam em uma "árvore". Esta árvore caracteriza o modelo de objetos do documento, ou, formalmente, DOM (_Document Object Model_). Na forma de árvore DOM, o código acima tornar-se-ia algo como:
# 
# ```html
# |- DOCTYPE: html
# |- html lang="pt-br"
#    |- head
#    |  |- #text:
#    |  |- title
#    |  |  |- #text: Introdução à Ciência de Dados
#    |  |- #text:
#    |- #text:
#    |- body
#       |- #text:
#       |- h1
#       |  |- #text: Ciência de Dados no século XXI
#       |- #text:
#       |- p
#       |  |- #text: A História começa neste 
#       |  |- a href="historia-icd.html"
#       |     | #text: link
#       |  |- #text:
#       |- #comment: comentário
#       |- #text:
# ```      

# ### Tags
# 
# Existem diversas _tags_ disponíveis em HTML. A seguir listamos as que aparecem no código de exemplo anterior e sua descrição.
# 
# |Tag|Descrição|
# |---|---|
# |`<!DOCTYPE>` | define o tipo do documento|
# |`<html>` | define a raiz de um documento HTML|
# |`<head>` | enclausura os metadados (informações) sobre o documento|
# |`<title>` | define um título para o documento|
# |`<body>` | define o corpo do documento|
# |`<h1>` | define cabeçalho de primeiro nível (seção)|
# |`<p>` | define um parágrafo|
# |`<a>` | define um _hyperlink_ (ancoramento)|
# 
# ```{note}
# Um documento de referência para tags HTML está disponível [aqui](https://www.w3schools.com/TAGs/).
# ```

# #### Escrevendo HTML no Jupyter Notebook
# 
# Podemos escrever sintaxes de código HTML em um _Jupyter Notebook_ e renderizar a saída formatada usando o comando mágico `%%html` ou `IPython.display`. Por exemplo:

# In[1]:


get_ipython().run_cell_magic('html', '', '<!-- Nada aqui -->\n<h2>Brincando com <sup>H</sup><sub>T</sub><sup>M</sup>L!</h2>\n<p> Muito legal adicionar <b>negrito</b>, \n<i>itálico</i> emojis como <span> &#128540; </span> e \num <a href="none.html">link</a> para lugar algum!</p>')


# In[2]:


from IPython.display import HTML

HTML("<!-- Nada aqui --> <h2>Brincando com <sup>H</sup><sub>T</sub><sup>M</sup>L!</h2> <p> Muito legal adicionar <b>negrito</b>, <i>itálico</i> emojis como <span> &#128540; </span> e \
um <a href='none.html'>link</a> para lugar algum!</p>")


# ## APIs
# 
# A raspagem de dados pode ser otimizada através de uma _API_ (_Application Program Interface_). APIs são mecanismos (interfaces) que usam aplicativos de terceiros para realizar "conexões" e puxar dados. APIs são parecidas com módulos, mas não oferecem meramente um conjunto de funções, mas sim um programa capaz de operar com muitos dados. Embora uma API possa funcionar localmente (_offline_), sua utilidade para raspagem de dados é melhor exibida quando se conecta a aplicativos da web (_online_). 
# 
# Diversas instuições fornecem APIs para que desenvolvedores possam coletar dados. No início deste capítulo, mencionamos algumas aplicações de raspagem de dados. Algumas são possíveis apenas por meio de APIs. Google, Facebook, Twitter, Yahoo e Elsevier são algumas das empresas que fornecem APIs para aplicações em buscas na web, redes sociais, finanças e literatura científica. No Brasil, podemos citar como exemplos relevantes
# 
# - as [APIs da B3](https://www.b3.com.br/data/files/2B/41/CC/5D/10F42610D290A226790D8AA8/APIs-B3-Visao-Geral-versao-1.0.pdf) (Bolsa de Valores);
# - e as [APIs do Governo Federal](https://www.gov.br/conecta/catalogo/).
# 
# ```{note}
# Veja uma lista de APIs públicas neste [site](https://devresourc.es/tools-and-utilities/public-apis).
# ```

# ### Métodos HTTP
# 
# Na _web_, em geral lidamos com o HTTP (_HyperText Transfer Protocol_), isto é, um protocolo de comunicação entre clientes e servidores. Quando raspamos dados, eles são transferidos por meio de _requisições_ (_requests_) e _respostas_. Em geral, os quatro métodos mais comuns para transitar informações entre _browsers_ e servidores _web_ via HTTP são os seguintes:
# 
# - `GET`, para recuperar informação;
# - `POST`, para criar informação;
# - `PUT`, para atualizar informação;
# - `DELETE`, para deletar informação;
# 
# ```{note}
# Um padrão de projeto que pode ser usado para criar APIs web e integrar esses 4 métodos é o [REST](https://en.wikipedia.org/wiki/Representational_state_transfer),_Representational State Transfer_. Saiba mais [aqui](https://www.ibm.com/cloud/learn/rest-apis).
# ```

# ## JSON e XML
# 
# APIs utilizadas para raspagem de dados comumente retornam a informação em formato XML (_eXtensible Markup Language_), blocada em _tags_ ou JSON (_JavaScript Object Notation_), serializada. Embora JSON seja a escolha de APIs mais modernas, é importante ter em mente que muitos provedores de APIs as fornecem com saída XML. 
# 
# Um dos argumentos em favor de JSON é a economia de caracteres. Por exemplo, a estrutura XML 
# 
# ```xml
# <user><firstname>Juan</firstname><lastname>Hernandes</lastname><username>Fernandez</username></user>
# ```
# possui 100 caracteres.
# 
# A mesma informação, serializada em JSON, 
# 
# ```json
# {"user":{"firstname":"Juan","lastname":"Hernandes","username":"Fernandez"}}
# ```
# 
# com 75 caracteres, pouparia 25% do espaço.

# ## _Web crawlers_

# Rastreadores da web (_web crawlers_) são programas que indexam informações da rede a partir de várias fontes. Pelo fato de se comportarem como "espreitadores metódicos", eles também são conhecidos como _bots_, _aranhas_ ou _escutadores_ da rede. Eles trabalham de uma forma recursiva _ad infinitum_ puxando conteúdo de páginas e examinando-os.
# 
# _Crawlers_ são úteis para coleta de dados, porém baseiam-se em termos de serviço e conduta. Todo site público possui, de alguma forma, termos de serviço geridos por um administrador que declaram o que é permitido ao _crawler_ fazer ou não. Essas permissões (_allows_) ou restrições (_disallows_) estão expostas em arquivo chamado `robots.txt`. Qualquer site relevante possui um arquivo deste associado à sua URL. Para vê-lo, basta adicionar este nome após a URL do endereço. As restrições sobre _crawlers_ esbarram na fronteira da ética, principalmente no que diz respeito à raspagem de dados. Contudo, não discutiremos essas questões aqui.
# 
# Abaixo, mostramos o arquivo `robots.txt` para o site da UFPB.

# - Conteúdo de https://www.ufpb.br/robots.txt:
Sitemap: /sitemap.xml.gz
# Define access-restrictions for robots/spiders
# http://www.robotstxt.org/wc/norobots.html

# By default we allow robots to access all areas of our site 
# already accessible to anonymous users

User-agent: *
Disallow:

# Add Googlebot-specific syntax extension to exclude forms 
# that are repeated for each piece of content in the site 
# the wildcard is only supported by Googlebot
# http://www.google.com/support/webmasters/bin/answer.py?answer=40367&ctx=sibling

User-Agent: Googlebot
Disallow: /*sendto_form$
Disallow: /*folder_factories$
# Para outros exemplos, veja: 
# 
# - https://www.wikipedia.org/robots.txt
# 
# - https://www.google.com/robots.txt

# ## Bibliotecas para raspagem de dados
# 
# Existem muitos ferramentas, bibliotecas e _frameworks_ para raspagem de dados. Alguns exemplos são: _requests, _grab_, _scrapy_, _restkit_, _lxml_, _PDFMiner_. Neste capítulo, vamos dar enfoque ao módulo Python _BeautifulSoap_ e seus interpretadores (_parsers_).

# ### Vantagens de `BeautifulSoup`
# 
# Segundo o [site oficial](https://www.crummy.com/software/BeautifulSoup/), a `BeautifulSoup` 
# 
# - fornece métodos simples e expressões idiomáticas "Pythônicas" para navegar, pesquisar e modificar uma árvore de análise: um kit de ferramentas para dissecar um documento e extrair o que você precisa. 
# - converte automaticamente os documentos recebidos em Unicode e os documentos enviados em UTF-8. Você não tem que pensar em codificações, a menos que o documento não especifique uma codificação e a Beautiful Soup não consiga detectar uma. 
# - baseia-se em interpretadores (_parsers_) Python populares como _lxml_ e _html5lib_, permitindo que você experimente diferentes estratégias de análise para obter flexibilidade.
# 
# ```{note}
# A biblioteca BeautifulSoup foi assim denominada em homenagem a um poema de Lewis Carroll de mesmo nome em Alice no País das Maravilhas, em alusão à [Sopa de Tartaruga](https://www.triplov.com/contos/Alice-no-pais-das-maravilhas/capitulo_10.htm).
# ```

# ## Raspando dados do site da UFPB
# 
# Neste exemplo, faremos uma raspagem no site da UFPB para coletar a lista de cursos de graduação. Os passos a serem seguidos são:
# 
# 1. abrir uma requisição para a URL da PRG/UFPB;
# 2. coletar o HTML da página;
# 3. extrair o conteúdo da tabela de cursos na árvore DOM;
# 4. construir um _DataFrame_ cujas colunas devem conter: nome do curso, sede, modalidade, nome do(a) coordenador(a) e Centro de Ensino que administra o curso.
# 
# Entretanto, antes de produzirmos o _DataFrame_, faremos uma breve explanação sobre outras funcionalidades do módulo `BeautifulSoap`.

# Primeiramente, abriremos uma requisição com `urllib.request`.

# In[3]:


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://sigaa.ufpb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-graduacao')
bs = BeautifulSoup(html.read(),'html.parser')


# Neste ponto, criamos o objeto `bs` que contém a árvore DOM do documento HTML. Podemos acessar as partes do documento diretamente a partir das _tags_ `head`, `body`, `title` etc.

# In[4]:


# impressão na tela de head e body
# omitidas por serem grandes. 
# Teste em seu computador!
head = bs.head
body = bs.body
title = bs.title


# In[5]:


title


# Podemos puxar o conteúdo das _tags_ com `contents`.

# In[6]:


# é uma lista
title.contents


# In[7]:


# opera sobre str
title.contents[0].strip()


# Podemos navegar na árvore por meio das _tags_.

# In[8]:


head.link


# In[9]:


head.meta


# In[10]:


body.li


# In[11]:


body.span


# ### Navegação na árvore para baixo

# A árvore DOM é baseada em uma estrutura do tipo "_parents_/_children_". Um elemento pai pode ter um ou mais filhos e os elementos filhos podem também ter um ou mais filhos. Em termos de nível, os primeiros são _filhos diretos_.
# 
# - `contents` para encontrar filhas diretas como lista;
# - `children` para encontrar filhas diretas como iterador;
# - `descendants` para encontrar filhas diretas, filhas de filhas e assim por diante.

# In[12]:


type(body.contents)


# In[13]:


# iterador
for c in body.children:
    print(type(c))


# In[14]:


# itera sobre todos os descendentes
k = 1
for c in body.descendants:
    if k % 500 == 0:
        print(f'descendente {k}: {type(c)}',sep=':')
    k += 1


# Para navegar apenas em strings (já removendo espaços em branco) dentro de _tags_, podemos usar `stripped_strings`. Se quisermos considerar espaços, devemos usar apenas `strings`.

# In[15]:


# idenfica o campus sede em tabela 
campus = ('Areia','Bananeiras','Rio Tinto')
for s in body.tbody.stripped_strings:
    if s in campus:
        print(s,end=',')


# ### Navegação na árvore para baixo

# Inversamente, podemos acessar elementos "pai" (ou "mãe") a partir dos filhos com `parent`. 

# In[16]:


list(head.link.parent)[:4]


# Para iterar sobre os elementos "pai" (ou "mãe"), use `parents`. 

# In[17]:


for h in head.link.parents:
    print(type(h))


# ### Realizando buscas na árvore

# Funções de localização bastante úteis são `find_all` e `find`. Podemos aplicá-la passando como argumento uma _tag_

# In[18]:


body.find_all('td')[10:15]


# uma lista de _tags_

# In[19]:


body.find_all(['li','ul'])


# ou _tag_ e classe.
# 
# ```{note}
# _Classes_ dizem respeito ao estilo de formatação do arquivo HTML, que segue regras da linguagem [CSS](https://www.w3schools.com/css/default.asp).
# ```

# In[20]:


# busca <table data> com classe "subFormulario"
body.find_all('td',class_="subFormulario")[:3]


# Podemos também realizar buscas específicas por expressões regulares. Para isso, basta usar o módulo `re` e funções como `re.compile`.

# In[21]:


import re

body.find_all(string=re.compile('GRAD'))


# In[22]:


body.find_all(string=re.compile('CENTRO'))


# Se o resultado a ser localizado for único, podemos usar `find`.

# In[23]:


body.find(string=re.compile('Copyright'))


# ### Funções customizadas
# 
# Agora, implementaremos algumas funções customizadas para extrair o cabeçalho e o conteúdo da tabela de cursos do site da UFPB. Essas funções varrem a árvore DOM e coletam apenas as informações de interesse, transformando-as para listas.

# In[24]:


# extrai cabeçalhos
def get_table_head(t):
    '''Lê objeto tabela e extrai header para lista'''
    res = []
    thead = t.find('thead')
    th = thead.find_all('th')
    for f in th:
        res.append(f.getText().strip())
    return res

t_header = get_table_head(body.div)

t_header


# In[25]:


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

r = get_table_body(body.div)  


# ### Limpeza dos dados extraídos
# 
# Finalmente, construiremos o _DataFrame_ a partir das listas anteriores. Porém, precisamos realizar procedimento de preenchimento de dados e limpeza.
# 
# Note que a tabela original não traz os nomes dos cursos organizados por linha. Então, precisamos de uma coluna com o nome de cada Centro de Ensino organizado por curso.

# In[26]:


import pandas as pd

# cria DataFrame
df = pd.DataFrame(r,columns=t_header).drop_duplicates().reset_index(drop=True)
mask = df['Nome'].str.find('CENTRO') != -1
centros = df['Nome'].loc[mask]
idx = centros.index.values

# preenchimento
vals = []
for k in range(1,len(idx)):
    for i in range(max(idx)+1):
        if i >= idx[k-1] and i < idx[k]:
            vals.append(centros.iloc[k-1])
# extra
dx = len(df) - max(idx)
vals.extend(dx*[vals[-1]])


# limpa e renomeia
df['Centro'] = vals
df = df.drop(idx).rename(columns={"Nome": "Curso"}).reset_index(drop=True)


# In[27]:


df

