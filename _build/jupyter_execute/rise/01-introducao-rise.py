#!/usr/bin/env python
# coding: utf-8

# # Aula 01 - Introdução à Ciência de Dados

# ## Indústria 4.0 / Sociedade 5.0
# 
# <!-- Figura -->
# <center>
#     <img src='../figs/01/society-5-industry-4.png' width=900px> </img>
# </center>
# 
# [Fonte](https://www.sphinx-it.eu/from-the-agenda-of-the-world-economic-forum-2019-society-5-0/)

# ## Ciência de Dados no Século XXI 
# 
# - Dados como matéria-prima: pessoas, empresas, governos, ciência
# - *Big Data*, *business intelligence*, *data analytics*,...
# 
# <!-- Figura -->
# <center>
#     <img src='../figs/01/11-pillars.png' width=600px> </img>
# </center>
# 
# [Fonte](https://knowledgecom.my/ir4.html)

# - *Ciência de dados*: nome razoável para denotar o aspecto científico dos dados
# - Contexto acadêmico: intersecta áreas, processos e pensamento científico
# - Modelo holístico não unificado 
# - Ciência de dados tem alta capilaridade e multidisciplinaridade

# ## Modelo em camadas
# 
# <!-- Figura -->
# <center>
#     <img src='../figs/01/cycle-ds.png' width=400px> </img>
# </center>

# ## Camada interna: interseção de áreas tradicionais 
# 
# - **Matemática/Estatística**: 
#  - modelos matemáticos
#  - análise e inferência de dados
#  - aprendizagem de máquina
# 
# - **Ciência da Computação/Engenharia de Software** 
#  - hardware/software
#  - projeto, armazenamento e segurança de dados
# 
# - **Conhecimento do Domínio/Expertise** 
#  - ramo de aplicação do conhecimento 
#  - *data reporting* e inteligência de negócios
#  - *marketing* e comunicação de dados

# ## Camada intermediária: processos da cadeia de dados
# 
# - Governança, curadoria
# - Armazenamento, reuso
# - Preservação, manutenção
# - Destruição, compartilhamento

# ## Camada externa: método científico
# *Soluções dirigidas por dados* (*data-driven solutions*) 
# 
# 1. **Definição do problema**: a "grande pergunta" 
# 
# 2. **Aquisição de dados**: coleta de toda informação disponível sobre o problema
# 
# 3. **Processamento de dados**, tratamento dos dados (limpeza, formatação e organização)

# 4. **Análise de dados**, mineração, agrupamento, clusterização, testes de hipótese e inferência
# 
# 5. **Descoberta de dados**, correlações, comportamentos distintivos, tendências claras, geração de conhecimento
# 
# 6. **Solução**, conversibilidade em produtos e ativos de valor agregado

# ### Exemplo: o caso da COVID-19
# 
# - Uma pergunta:
# > _A taxa de contágio do vírus em pessoas vivendo próximas de um centro comercial localizado em uma zona rural é menor do do que em pessoas vivendo próximas de um centro comercial localizado em uma zona urbana?_ 
# - Como delimitar a zona urbana? 

# - Centro comercial: 
#  - Conjunto de lojas de pequeno porte? 
#  - Feiras? 
#  - Circulação de 100 pessoas/h? 
#  
# - Bancos de dados: IBGE? DATASUS?

# ### Projetos de CD para a COVID-19
# 
# Mundo: 
# - *Coronavirus Resource Center*, John Hopkins University [[CRC-JHU]](https://coronavirus.jhu.edu/map.html)
# 
# Brasil: 
# - Observatório Covid-19 BR [[COVID19BR]](https://covid19br.github.io/index.html)
# - Observatório Covid-19 Fiocruz [[FIOCRUZ]](https://portal.fiocruz.br/observatorio-covid-19)
# - CoronaVIS-UFRGS [[CoronaVIS-UFRGS]](https://covid19.ufrgs.dev/dashboard/#/dashboard)
# - CovidBR-UFCG [[CovidBR-UFCG]](http://covid.lsi.ufcg.edu.br) 
# - [[LEAPIG-UFPB]](http://www.de.ufpb.br/~leapig/projetos/covid_19.html#PB)

# ## Cientista de dados x analista de dados x engenheiro de dados

# ### Cientista de dados
# 
# > _"**Cientista de dados** é um profissional que tem conhecimentos suficientes sobre necessidades de negócio, domínio do conhecimento, além de possuir habilidades analíticas, de software e de engenharia de sistemas para gerir, de ponta a ponta, os processos envolvidos no ciclo de vida dos dados."_
# 
# [[NIST 1500-1 (2015)]](https://bigdatawg.nist.gov/_uploadfiles/NIST.SP.1500-1.pdf)

# ### Ciência de dados
# 
# > _"**Ciência de dados** é a extração do conhecimento útil diretamente a partir de dados através de um processo de descoberta ou de formulação e teste de hipóteses."_ 
# 
# #### Informação não é sinônimo de conhecimento!
# 
# - Exemplo: de toda a informação circulante no seu Whatsapp por dia, que fração seria considerada útil e aproveitável? A resposta talvez seja um incrível "nada"... 
# 
# Portanto, ter bastante informação à disposição não significa, necessariamente, possuir conhecimento.

# ### Analista de dados
# 
# - _Analytics_ pode ser traduzido literalmente como "análise"
# - Segundo o documento NIST 1500-1, é definido como o "processo de sintetizar conhecimento a partir da informação". 
# 
# > _"**Analista de dados** é o profissional capaz de sintetizar conhecimento a partir da informação e convertê-lo em ativos exploráveis."_

# ### Engenheiro de dados
# 
# > _"**Engenheiro(a) de dados** é o(a) profissional que explora recursos independentes para construir sistemas escaláveis capazes de armazenar, manipular e analisar dados com eficiência e e desenvolver novas arquiteturas sempre que a natureza do banco de dados exigi-las."_

# Embora essas três especializações possuam características distintivas, elas são tratadas como partes de um corpo maior, que é a Ciência de Dados
# 
# - Ver [PROJETO EDISON](https://edison-project.eu), Universidade de Amsterdã, Holanda 
# - EDISON Data Science Framework [[EDSF]](https://edison-project.eu/sites/edison-project.eu/files/attached_files/node-5/edison2017poster02-dsp-profiles-v03.pdf)

# #### Quem faz o quê? 
# 
# Resumimos a seguir as principais tarefas atribuídas a cientistas, analistas e engenheiros(as) de dados com base em artigos de canais especializados:
# - [[DataQuest]](https://www.dataquest.io/blog/data-analyst-data-scientist-data-engineer/)
# - [[NCube]](https://ncube.com/blog/data-engineer-data-scientist-data-analyst-what-is-the-difference)
# - [[Medium]](https://medium.com/@gdesantis7/decoding-the-data-scientist-51b353a01443)
# - [[Data Science Academy]](http://datascienceacademy.com.br/blog/qual-a-diferenca-entre-cientista-de-dados-e-engenheiro-de-machine-learning/)
# - [[Data Flair]](https://data-flair.training/blogs/data-scientist-vs-data-engineer-vs-data-analyst/). 

# ##### Cientista de dados
# - Realiza o pré-processamento, a transformação e a limpeza dos dados;
# - Usa ferramentas de aprendizagem de máquina para descobrir padrões nos dados;
# - Aperfeiçoa e otimiza algoritmos de aprendizagem de máquina;
# - Formula questões de pesquisa com base em requisitos do domínio do conhecimento;
#    

# ##### Analista de dados
# - Analisa dados por meio de estatística descritiva;
# - Usa linguagens de consulta a banco de dados para recuperar e manipular a informação;
# - Confecciona relatórios usando visualização de dados; 
# - Participa do processo de entendimento de negócios;

# ##### Engenheiro(a) de dados
# - Desenvolve, constroi e mantém arquiteturas de dados;
# - Realiza testes de larga escala em plataformas de dados;
# - Manipula dados brutos e não estruturados;
# - Desenvolve _pipelines_ para modelagem, mineração e produção de dados
# - Cuida do suporte a cientistas e analistas de dados;

# #### Que ferramentas são usadas?
# 
# As ferramentas usadas por cada um desses profissionais são variadas e evoluem constantemente. Na lista a seguir, citamos algumas.

# ##### Cientista de dados
# - R, Python, Hadoop, Ferramentas SQL (Oracle, PostgreSQL, MySQL etc.)
# - Álgebra, Estatística, Aprendizagem de Máquina
# - Ferramentas de visualização de dados
#    

# ##### Analista de dados
# - R, Python, 
# - Excel, Pandas
# - Ferramentas de visualização de dados (Tableau, Infogram, PowerBi etc.)
# - Ferramentas para relatoria e comunicação 

# ##### Engenheiro(a) de dados
# - Ferramentas SQL e noSQL (Oracle NoSQL, MongoDB, Cassandra etc.)
# - Soluções ETL - Extract/Transform/Load (AWS Glue, xPlenty, Stitch etc.)
# - Python, Scala, Java etc.
# - Spark, Hadoop etc.

# ### A Matemática por trás dos dados

# #### *Bits*
# 
# Linguagem _binária_ (sequencias dos dígitos 0 e 1). Em termos de *bits*, a frase "Ciência de dados é legal!", por exemplo, é escrita como
# 
# `1000011110100111101010110111011000111101001110000110000011001001100101
# 1000001100100110000111001001101111111001110000011101001100000110110011001
# 01110011111000011101100100001`. 

# #### Dados 1D, 2D e 3D 
# 
# - Texto, som, imagem, áudio, vídeo...
# 
# - *Arrays*, vetores de dados e listas
# - *Dataframes* e planilhas
# - Matrizes (pixels, canais de cor)
# - Matrizes 3D (filmes, animações, FPS)

# ## Ferramentas computacionais do curso
# 
# - Python 3.x (onde x é um número de versão) como linguagem de programação. 
# - Linguagem interpretada
# - Alto nível

# ### _iPython_ e _Jupyter Notebook_ 
# 
# - [[iPython]](http://ipython.org): iniciado em 2001; interpretador Python para melhorar a interatividade com a linguagem. 
# - Integrado como um _kernel_ (núcleo) no projeto [[Jupyter]](http://jupyter.org), desenvolvido em 2014, permitindo textos, códigos e elementos gráficos sejam integrados em cadernos interativos. 
# - _Jupyter notebooks_ são interfaces onde podemos executar códigos em diferentes linguagens
# - _Jupyter_ é uma aglutinação de _Julia_, _Python_ e _R_, linguagens usuais para ciência de dados

# ### *Anaconda* 
# 
# - O [[Anaconda]](https://www.anaconda.com) foi iniciado em 2012 para fornecer uma ferramenta completa para o trabalho com Python. 
# - Em 2020, a [[Individual Edition]](https://www.anaconda.com/products/individual) é a mais popular no mundo com mais de 20 milhões de usuários. 
# - Leia o tutorial de instalação!

# ### *Jupyter Lab*
# 
# - Ferramenta que melhorou a interatividade do Jupyter
# - Este [[artigo]](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) discute as características do Jupyter Lab

# ### *Binder* 
# 
# - O projeto [[Binder]](https://mybinder.org) funciona como um servidor online baseada na tecnologia *Jupyter Hub* para servir cadernos interativos online.
# - Execução de códigos "na nuvem" sem a necessidade de instalações
# - Sessões temporárias

# ### *Google Colab* 
# 
# - O [[Google Colab]](http://colab.research.google.com) é um "misto" do _Jupyter notebook_ e _Binder_, 
# - Permite que o usuário use a infra-estrutura de computação de alto desempenho (GPUs e TPUS) da Google
# - Sincronização de arquivos com o Google Drive. 

# ### Ecossistema de módulos
# 
# - *numpy* (*NUMeric PYthon*): o *numpy* serve para o trabalho de computação numérica, operando fundamentalmente com vetores, matrizes e ágebra linear.
# 
# - *pandas* (*Python for Data Analysis*): é a biblioteca para análise de dados de Python, que opera *dataframes* com eficiência.

# - *sympy* (*SYMbolic PYthon*): é um módulo para trabalhar com matemática simbólica e cumpre o papel de um verdadeiro sistema algébrico computacional.
# 
# - *matplotlib*: voltado para plotagem e visualização de dados, foi um dos primeiros módulos Python para este fim.

# - *scipy* (*SCIentific PYthon*): o *scipy* pode ser visto, na verdade, como um módulo mais amplo que integra os módulos anteriores. Em particular, ele é utilizado para cálculos de integração numérica, interpolação, otimização  e estatística.
# 
# - *seaborn*: é um módulo para visualização de dados baseado no *matplotlib*, porém com capacidades visuais melhores. 
