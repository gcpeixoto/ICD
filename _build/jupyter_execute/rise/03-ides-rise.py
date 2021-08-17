#!/usr/bin/env python
# coding: utf-8

# # Ambientes de desenvolvimento e computação interativa

# ## IDEs para ciência de dados
# 
# Um IDE (_Integrated Development Environment_) é um software que facilita programadores para o desenvolvimento de softwares. 
# 
# Funcionalidades básicas de um IDE: 
# 
# 1. edição de texto
# 2. interpretação/compilação automatizada
# 3. depuração

# ### Alguns IDEs comumente usados
# 
# - [Sublime](https://www.sublimetext.com)
# - [Spyder](https://www.spyder-ide.org)
# - [Atom](https://atom.io/packages/data-atom)
# - [Visual Studio](https://code.visualstudio.com)
# - [PyCharm](https://www.jetbrains.com/pycharm/)
# - [Jupyter Notebooks](https://jupyter.org)
# - [Jupyter Lab](http://jupyterlab.io)
# - [Wing](https://wingware.com)

# ### Exemplo de uso: Spyder 5.0
# 
# <img src="../figs/03/spyder-screenshot.png" width="700px">

# > Não existe "o melhor IDE". A escolha depende do gosto pessoal, da necessidade e dos objetivos. Qualquer que seja a sua opção, algum tempo deve ser gasto no entendimento das funcionalidades de cada um e na organização do _workflow_ individual.  
# 

# ### Completação de código inteligente
# 
# - Ferramentas ajudam a aumentar a produtividade
# - A maioria dos IDEs acima possuem completação de código 
# - Este nicho tem se tornado bem específico
# - Exemplos de ferramentas para completação de código:
#     - [Kite](https://www.kite.com)
#     - [Codota](https://www.codota.com)
#     - [Jedi](https://jedi.readthedocs.io/en/latest/docs/features.html#type-hinting)
#     - [Finisher](https://github.com/slobdell/Finisher)

# ## Cadernos interativos
# 
# - A computação interativa torna a interação entre pessoas e máquinas mais dialógica e fácil
# 
# - Hoje, _cadernos interativos_ são quase indispensáveis para um cientista de dados

# ###  O Projeto [[Jupyter]](http://jupyter.org)
# 
# - Iniciado em 2014, lançou a proposta dos chamados _notebooks_:
# 
# - Permite que textos, códigos e elementos gráficos sejam integrados em uma espécie de caderno "vivo". 
# 
# - _Jupyter notebooks_ são interfaces baseadas em _web_ onde podemos executar códigos 
# 
# - Diferentes linguagens possíveis desde que alteremos os _kernels_. 
# 
# - Para Python, ele dispõe do tradicional _kernel_ _IPython_.

# ### JupyterLab
# 
# - Interface de nova geração para o _Jupyter_
# - Capacidade para:
#     - editar texto
#     - avaliar código
#     - pré-visualização de gráficos, figuras, tabelas e muito mais
# - Depuração ou funcionalidades específicas alcançadas por meio de _extensões_

# #### Instalação
# 
# Usando `conda`, o _JupyterLab_ pode ser instalado pelo comando:
# 
# ```bash
# conda install -c conda-forge jupyterlab
# ```

# #### Inicialização 
# 
# Inicialize pelo _Anaconda Navigator_ ou pela linha de comando usando:
# 
# ```
# jupyter-lab
# ```
# 
# O ambiente será aberto em seu navegador _web_ padrão em um endereço similar a:
# 
# ```
# http(s)://<server:port>/<lab-location>/lab
# 
# ```
# 
# Para lançar o Jupyter Notebook padrão, use menu _Help > Launch Classic Notebook_.

# #### Elementos da interface
# 
# - Área de trabalho principal
# - Barra lateral esquerda
#     - Navegador de arquivos
#     - Lista de kernels em execução
#     - Paleta de comandos
#     - Inspetor
#     - Lista de abas
# - Barra de menus

# #### Workspace
# 
# Cada sessão do _JupyterLab_ reside em um _workspace_, cujas variáveis podem ser dinamicamente alteradas. 

# #### Funções de URL úteis
# 
# - Reset do workspace: adicione `?reset` na URL. 
# 
# Exemplo:
# ```
# http://127.0.0.1:8889/lab/tree/ICD/teste.ipynb?reset
# ```
# 
# - Clonar o workspace atual para outro chamado _copia_: adicione `?clone=copia`
# ```
# http://127.0.0.1:8889/lab/tree/ICD/teste.ipynb?clone=copia
# ```

# #### Estrutura de um arquivo _.ipynb_
# 
# O formato oficial de um _Jupyter Notebook_, com extensão _.ipynb_ é construído sobre uma estrutura JSON.
# 
# 
# [[JSON]](https://www.json.org/json-en.html) - JavaScript Object Notation, é um formato de intercâmbio de dados baseado em um subconjunto da linguagem JavaScript.

# Em seu maior nível, o arquivo é um dicionário que contém algumas chaves, tais como: 
# 
# - `metadata` (dict)
# - `nbformat` (int)
# - `nbformat_minor` (int)
# - `cells` (list)

# Abaixo, temos um exemplo da estrutura JSON de um arquivo _.ipynb_.
# 
# ```json
# {
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.8.8"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 5
# }
# ```

# Uma célula de texto deste material por exemplo é, no formato JSON, exibida como: 
# 
# ```json
#  {
#    "cell_type": "markdown",
#    "id": "93e25ab1-2a8a-4baf-9bcf-a72057aa908f",
#    "metadata": {},
#    "source": [
#     "### Estrutura de um arquivo `.ipynb`\n",
#     "\n",
#     "O formato oficial de um _Jupyter Notebook_, com extensão `.ipynb` é construído sobre uma estrutura JSON.\n",
#     "\n",
#     "```{note}\n",
#     "[[JSON]](https://www.json.org/json-en.html) - JavaScript Object Notation, é um formato de intercâmbio de dado baseado em um subconjunto da linguagem JavaScript.\n",
#     "```"
#    ]
#   }
# ```

# Os principais elementos são:
# 
# - `cell_type`: tipo de célula.
# - `id`: identificador (único) de uma célula. É um objeto `str` de comprimento 1-64.
# - `metadata`: opções que controlam o comportamento da célula.
# - `source`: conteúdo da célula.

# Entretanto, outros elementos podem estar presentes. Um exemplo de célula de código que retorna um erro é dado a seguir: 
# 
# ```json
#  {
#    "cell_type": "code",
#    "execution_count": 5,
#    "metadata": {},
#    "outputs": [
#     {
#      "ename": "SyntaxError",
#      "evalue": "unexpected EOF while parsing (<ipython-input-5-ef2d20508391>, line 1)",
#      "output_type": "error",
#      "traceback": [
#       "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-5-ef2d20508391>\"\u001b[0;36m, line \u001b[0;32m1\u001b[0m\n\u001b[0;31m    2 - 98*( 7/3\u001b[0m\n\u001b[0m                ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
#      ]
#     }
#    ],
#    "source": [
#     "2 - 98*( 7/3"
#    ]
#   },
# ```

# #### Formatos de saída de células 
# 
# Diferentes tipos de arquivo podem ter uma saída renderizada de modo enriquecido. 
# 
# Por exemplo:

# - Visualizando código HTML

# In[17]:


import IPython.display as dpl

dpl.display(dpl.HTML('<h>Isto é um título</h2> <hr> é <sup>H</sup>ML</h1>'))


# - Visualizando código JSON

# In[18]:


dpl.display(dpl.JSON({"a":'b',"meta":[1,2]}))


# - Visualizando vídeo do YouTube

# In[21]:


dpl.display(dpl.YouTubeVideo("fn3KWM1kuAw",width=500,height=400))   


# - Visualizando áudio 

# In[25]:


# teste descomentando
#dpl.Audio(url="https://www.bands.army.mil/music/play.asp?TheArmySong2013_BandAndChorus.mp3",autoplay=False)


# - Visualizando imagem

# In[26]:


dpl.Image('http://www.google.fr/images/srpr/logo3w.png') 


# #### Depuração
# 
# - _JupyterLab_ > 3.0 vem munido de depurador, mas é necessário _kernel_ que o suporte. 
# 
# - Alguns conhecidos são: 
#     - [xeus-python](https://github.com/jupyter-xeus/xeus-python)
#     - [xeus-robot](https://github.com/jupyter-xeus/xeus-robot)

# - Melhor maneira de ter suporte à depuração:
#     - Criar um ambiente novo, chamado, digamos `jb`, contendo JupyterLab 3.0 e um desses _kernels_
# 
# - Exemplo:
# ```bash
# conda create -n jd -c conda-forge jupyterlab=3 xeus-python
# conda activate jd
# ```
# - O _kernel_ pode ser habilitado via navegador ou seletor de núcleo. 

# - Experimente um ambiente com depuração [aqui](https://mybinder.org/v2/gh/blink1073/jupyter-ide-demo/stable?urlpath=/lab/tree/index.ipynb)

# #### Extensões
# 
# - O _JupyterLab_ é um ambiente extensível 
# - Pode ser customizado ou melhorado
# - Extensões incluem:
#     - temas
#     - visualizadores
#     - editores
#     - renderizadores. 
#     
# - Adicionam itens ao menu, à paleta de comandos ou configurações

# #### Instalação de extensões
# 
# - Podem ser de dois tipos: originais e pré-construídas. 
# - Extensões pré-construídas são mais fáceis de gerenciar
#     - Instaláveis usando o gerenciador de extensões: `jupyter-labextension install`
# 
# > Verifique requisito de instalação: `node-js` > 12.0.0
# 
# ```
# conda install nodejs -c conda-forge --repodata-fn=repodata.json
# ```
# 
# Adicionalmente, elas podem ser instaladas usando o painel lateral esquerdo. 

# ### Extensões recomendadas para cientistas de dados
# 
# - JupyterLab drawio: `jupyterlab-drawio`
# - JupyterLab plotly: `@jupyterlab/plotly-extension`
# - JupyterLab Github: `@jupyterlab/github`
# - JupyterLab bokeh: `jupyterlab_bokeh`
# - JupyterLab chart editor: `jupyterlab-chart-editor`
# 
# Para instalar use: `jupyter-labextension install EXT`, substituindo _EXT_ por um dos nomes acima.

# ### Exercício recomendado
# 
# - Configure seu ambiente de trabalho com IDE ou Jupyter Notebook, com seus temas e extensões de preferência.
