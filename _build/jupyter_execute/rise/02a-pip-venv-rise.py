#!/usr/bin/env python
# coding: utf-8

# # Pacotes e ambientes virtuais com _pip_ e _venv_

# ## Objetivos
# 
# - Dar visão geral sobre gerenciadores de pacote e ambientes virtuais
# - Aprender a utilizar o _pip_ e o _venv_ para gerenciar a instalação de pacotes, dependências e ambientes
# - Compreender comandos do _pip_ e do _venv_, e praticá-los em terminal

# ## Ambientes virtuais
# 
# > Locais isolados do resto do sistema operacional (daí o nome "virtual") onde podemos instalar pacotes sem que estes interfiram nos demais pacotes configurados globalmente.

# ### Vantagens
# 
# Algumas vantagens de se trabalhar com ambientes virtuais são: 
# 
# - Impedir conflitos de versão
# - Facilidade para reprodução e instalação
# - Execução independente de acesso privilegiado

# ## Gerenciamento de pacotes e ambientes
# 
# - **Boa prática:** instalar "pacotes" em ambientes virtuais. 
# - Pacotes como "habilidades" e "especializações" a um programa. 
# - Falaremos um pouco sobre o _pip_ e o _venv_.

# ### _pip_ 
# 
# - Infinidade de pacotes no [PyPi](https://pypi.org) - _Python Package Index_
# - Uma das maneiras mais fáceis de instalar pacotes PyPi é usar o gerenciador de pacotes _pip_.
# 
# > Precisa de uma especialidade? Confira se já não existe no PyPi. Não reinvente a roda!

# - Verificar instalação

# In[2]:


# no sistema operacional, remover o !
get_ipython().system('pip --version')


# - Verificar lista de pacotes instalados

# In[3]:


get_ipython().system('pip list ')


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

# - Comandos de interesse: _install_, _uninstall_, _search_. 
# 
# - Exemplo:
# ```python
# pip install lxml
# ```
# Instala a biblioteca _lxml_, globalmente! 
# 
# > Todavia, isso pode ser uma má escolha se você trabalhar com múltiplos projetos e versões como explicado anteriormente. 

# Como evitar potenciais conflitos de versão e imcompatibilidades? 
#     
# **Ambientes virtuais!**

# ### _venv_
# 
# - Integrado na versão Python 3.3 [PEP 405](https://www.python.org/dev/peps/pep-0405/)
# - Melhoria do [_virtualenv_](https://virtualenv.pypa.io/en/stable/) para Python 2

# Nesta seção: 
# 
# - Etapas essenciais do trabalho com _venv_ através da linha de comando:
#     - Criação e configuração do ambiente virtual
#     - Instalação e gestão de pacotes no ambiente virtual
#     - Salvamento e replicação do ambiente virtual

# #### Criação e configuração do ambiente virtual
# 
# Vamos supor que o nosso ambiente virtual seja chamado de `icd`. Para criá-lo, fazemos o seguinte:

# In[18]:


get_ipython().system('python3 -m venv icd')


# Um diretório _icd_ é criado no diretório a partir do qual o comando foi executado contendo outros diretórios.

# In[19]:


get_ipython().system('ls -l icd')


# - _lib_: diretório de pacotes independentes
# - _bin_: diretório com ferramentas de inicialização e interrupção do ambiente

# Para ativar o ambiente, fazemos:
source icd/bin/activate
# A ativação do ambiente produzirá uma mudança no terminal, tal como: 
# note o prefixo icd
(icd) (base) gustavo@GloryCrown
# #### Instalação e gestão de pacotes no ambiente virtual
# 
# - Uma vez ativado o ambiente, você está isolado do sistema global
# - Vamos instalar os seguintes pacotes para o curso:
#     - _numpy_
#     - _scipy_
#     - _sympy_
#     - _matplotlib_
#     - _pandas_
#     - _seaborn_

# Antes de prosseguir, vamos verificar o que há no ambiente.
# lista os pacotes no ambiente puro
pip list(icd) (base) gustavo@GloryCrown ipynb % pip list
Package    Version
---------- -------
pip        19.2.3
setuptools 41.2.0
# Como vemos, há apenas dois pacotes no ambiente. Agora, podemos proceder à instalação dos pacotes requisitados.
# 
# Se necessário, atualize o _pip_ com `pip install --upgrade pip`.
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
# #### Salvamento e replicação do ambiente virtual
# 
# - Interesse em manter o AV? 
# - Natural "salvar" o seu estado para replicá-lo em outro lugar (ex. outro usuário)
# - Como fazer? 
#     - Usar _freeze_ e redirecionar os pacotes para um arquivo de requisitos: `requirements.txt`.
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
# O arquivo de requisitos permite:
# 
# - Indicar restrição para versões dos pacotes
#     - Exemplo: `_numpy>=1.14.1_`
# - _upgrade_ total de uma só vez para todos os pacotes
#     - Exemplo: `pip install --upgrade -r requirements.txt`

# Finalmente, para excluir o ambiente, basta desativá-lo e posteriormente deletar o seu conteúdo.

# ## Outras opções para  "separação" virtual de ambientes
# 
# - Contêinerização com _Docker_ ou _Kubernetes_
# - Máquinas virtuais (_virtual machines_)
# - Gerenciamento de ambientes com _conda_, _miniconda_, _pipenv_, 
