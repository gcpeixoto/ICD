#!/usr/bin/env python
# coding: utf-8

# # Pacotes e ambientes virtuais com _pip_ e _venv_

# ## Objetivos
# 
# - Dar visão geral sobre gerenciadores de pacote e ambientes virtuais;
# - Aprender a utilizar o _pip_ e o _venv_ para gerenciar a instalação de pacotes, dependências e ambientes; 
# - Compreender comandos do _pip_ e do _venv_, e praticá-los em terminal

# ## Ambientes virtuais

# Ambientes virtuais são locais isolados do resto do sistema operacional (daí o nome "virtual") onde podemos instalar pacotes sem que estes interfiram nos demais pacotes configurados globalmente.
# 
# ### Vantagens
# 
# Algumas vantagens de se trabalhar com ambientes virtuais são: 
# 
# - _Impedir conflitos de versão:_ suponha que o projeto A no qual você trabalha dependa de uma biblioteca que está na versão X. Então, dentro de alguns meses, você inicia um outro projeto B que depende de uma versão mais nova que X da mesma biblioteca e a atualiza. O projeto B funciona maravilhosamente bem, mas o A para de funcionar porque não suporta outra versão além da X. Conclusão: um conflito de versões!
# - _Facilidade para reproduzir e instalar:_ uma vez que você tiver controle sobre as versões exatas necessárias para que seu projeto funcione, torna-se fácil para outros usuários reproduzir o projeto construindo-o e instalando o que for necessário.
# - _Execução independente de acesso privilegiado:_ com um ambiente virtual, um usuário que se encontra em uma rede na qual ele não tem acesso como administrador para instalar programas livremente, é possível executar projetos sem ter acesso em nível de _root_.

# ## Gerenciamento de pacotes e ambientes

# Em geral, instalamos "pacotes" em ambientes virtuais. Pacotes podem ser comparados à concessão de habilidades e especializações a um programa. Logo, é necessário que compreendamos como gerimos a instalação de pacotes antes de criarmos ambientes virtuais. Aqui, falaremos um pouco sobre o _pip_ e o _venv_.
# 
# 

# ### _pip_ 
# 
# A comunidade Python disponibiliza uma infinidade de pacotes em um local remoto chamado [PyPi](https://pypi.org), que significa _Python Package Index_. Uma das maneiras mais fáceis de instalar pacotes Python de terceiros disponíveis na PyPi é usar o gerenciador de pacotes chamado _pip_.
# 
# ```{hint}
# Está precisando de uma especialidade para seu programa? Confira se o que você precisa já não existe na PyPi. Não reinvente a roda!
# ```

# - Verificar instalação

# In[2]:


# no sistema operacional, remover o !
get_ipython().system('pip --version ')


# - Verificar lista de pacotes instalados

# In[10]:


get_ipython().system('pip list')


# - Imprimir informações sobre um pacote listado

# In[12]:


get_ipython().system('pip show alabaster')


# - Para atualizar o _pip_ para uma versão mais nova
# 
# ```python
# python -m pip install --upgrade pip
# ```

# - Para ajuda do _pip_
# 
# ```python
# pip -h
# ```

# Comandos de interesse são _install_, _uninstall_, e _search_. Entretanto, quando fazemos algo como 
# 
# ```python
# pip install lxml
# ```
# para instalar a biblioteca _lxml_, por exemplo, o _pip_ a instalará globalmente em seu computador. Todavia, isso pode ser uma má escolha se você trabalhar com múltiplos projetos e versões como explicado anteriormente. Para evitar potenciais conflitos de versão e imcompatibilidades, podemos criar ambientes virtuais com o _venv_.

# ### _venv_
# 
# O módulo _venv_ passou a ser integrado na versão Python 3.3 e é intensamente discutido no [PEP 405](https://www.python.org/dev/peps/pep-0405/). Ele surgiu como uma melhoria do módulo anterior [_virtualenv_](https://virtualenv.pypa.io/en/stable/), criado para Python 2, e com uma promessa de confiabilidade superior de isolamento. Por padrão, ele já vem instalado.
# 
# Nesta seção, abordaremos as etapas essenciais do trabalho com _venv_, que deverão ser realizadas através da linha de comando, a saber:
# 
# - Criação e configuração do ambiente virtual
# - Instalação e gestão de pacotes no ambiente virtual
# - Salvamento e replicação do ambiente virtual

# #### Criação e configuração do ambiente virtual
# 
# Vamos supor que o nosso ambiente virtual seja chamado de `icd`. Para criá-lo, fazemos o seguinte:

# In[18]:


get_ipython().system('python3 -m venv icd')


# Um diretório _icd_ é criado no diretório a partir do qual o comando foi executado contendo outros diretórios.

# In[19]:


get_ipython().system('ls -l icd')


# A estrutura mostra que: 
# 
# - _lib_: é um diretório de pacotes independentes
# - _bin_: é um diretório com as ferramentas de inicialização e interrupção do ambiente

# Para ativar o ambiente, fazemos:
source icd/bin/activate
# A ativação do ambiente produzirá uma mudança no terminal, tal como: 
# note o prefixo icd
(icd) (base) gustavo@GloryCrown
# #### Instalação e gestão de pacotes no ambiente virtual
# 
# Uma vez ativado o ambiente, você está isolado do sistema global para instalar pacotes. Vamos agora realizar a instalação dos seguintes pacotes, úteis para o nosso curso:
# 
# - _numpy_
# - _scipy_
# - _sympy_
# - _matplotlib_
# - _pandas_
# - _seaborn_

# Antes de prosseguir, vamos verificar o que há no ambiente.
# lista os pacotes no ambiente puro
pip list(icd) (base) gustavo@GloryCrown ipynb % pip list
Package    Version
---------- -------
pip        19.2.3
setuptools 41.2.0
# Como vemos, há apenas dois pacotes no ambiente. Agora, podemos proceder à instalação dos pacotes requisitados.
# 
# ```{warning}
# Se necessário, atualize o _pip_ com `pip install --upgrade pip`.
# ```
# instala pacotes com pip
pip install numpy scipy sympy matplotlib pandas seaborn
# Para verificar se todos os pacotes foram instalados, fazemos:
# lista pacotes após instalação
pip list(icd) (base) gustavo@GloryCrown ipynb % pip list
Package         Version
--------------- -------
cycler          0.10.0
kiwisolver      1.3.1
matplotlib      3.4.2
mpmath          1.2.1
numpy           1.21.0
pandas          1.3.0
Pillow          8.3.1
pip             21.1.3
pyparsing       2.4.7
python-dateutil 2.8.1
pytz            2021.1
scipy           1.7.0
seaborn         0.11.1
setuptools      41.2.0
six             1.16.0
sympy           1.8
# Como podemos ver, não apenas os pacotes requisitados são instalados, mas também uma série de pacotes dependentes adicionais, tais como _mpmath_ e _six_.

# #### Salvamento e replicação do ambiente virtual
# 
# Depois de termos estabelecido um ambiente virtual complexo, se houver interesse em mantê-lo para uso futuro, é natural que "salvemos" o seu estado para que possamos replicá-lo em outro lugar, ou permitir que outro usuário aproveite nossa configuração para construir o ambiente. 
# 
# Há uma maneira muito interessante de fazer isto, que se resume em usar o comando _freeze_ e redirecionar os pacotes do ambiente para um arquivo de requisitos que chamaremos de `requirements.txt`.
# salva a configuração do ambiente em 'requirements.txt'
pip freeze > requirements.txt
# Se analisarmos o conteúdo do arquivo `requirements.txt`, veremos algo como:
(icd) (base) gustavo@GloryCrown ipynb % cat requirements.txt
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.4.2
mpmath==1.2.1
numpy==1.21.0
pandas==1.3.0
Pillow==8.3.1
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2021.1
scipy==1.7.0
seaborn==0.11.1
six==1.16.0
sympy==1.8
# A replicação do nosso ambiente _icd_ em outro computador, por exemplo, pode então ser feita da seguinte forma:
# instala pacotes a partir de arquivo de requisitos em ambiente pré-ativado
pip install -r requirements.txt
# Se quisermos desinstalar todos os pacotes de uma só vez, podemos fazer algo como:
# desinstala pacotes no ambiente a partir de arquivo de requisitos com confirmação
pip uninstall -r requirements.txt -y
# Uma vez desinstalados, se listarmos novamente os pacotes no ambiente, veríamos exatamente o que tínhamos no início:
(icd) (base) gustavo@GloryCrown ipynb % pip list
Package    Version
---------- -------
pip        21.1.3
setuptools 41.2.0
# O arquivo de requisitos permite-nos realizar mais algumas coisas de maneira eficiente: 
# 
# - Se alterarmos o símbolo de `=` para `>=` em algum pacote, indicaremos uma restrição para versões dos pacotes, mas ampliaremos a possibilidade. Por exemplo, _numpy>=1.14.1_ indicar que qualquer versão igual ou acima de 1.14.1 seria possível para o _numpy_.
# - Se aplicarmos um comando como `pip install --upgrade -r requirements.txt`, forçaremos um _upgrade_ total de uma só vez para todos os pacotes do ambiente.

# Finalmente, para excluir o ambiente, basta desativá-lo e posteriormente deletar o seu conteúdo.

# ## Outras opções 
# 
# Há várias formas disponíveis hoje em dia para alcançar a "separação" virtual de ambientes. Algumas opções que você pode estudar mais a respeito são:
# 
# - Contêinerização com _Docker_ ou _Kubernetes_
# - Máquinas virtuais (_virtual machines_)
# - Gerenciamento de ambientes com _conda_, _miniconda_, _pipenv_, 
# 
# Veremos mais à frente como gerenciar pacotes e ambientes com um rápido curso sobre _conda_.

# ## Referências 
# 
# - [[PyPA]](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
# 
# - [[venv]](https://docs.python.org/3/library/venv.html)
# 
# - [[virtualenv]](https://docs.python-guide.org/dev/virtualenvs/)
# 
# - [[pipenv]](https://python.land/virtual-environments/pipenv)
