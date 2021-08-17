#!/usr/bin/env python
# coding: utf-8

# # _Crash course_ de _conda_

# ## Objetivos
# 
# - Aprender a utilizar o _conda_ para gerenciar a instalação de pacotes, dependências e ambientes; 
# - Entender conceitos de distribuição, módulo e repositório;
# - Compreender comandos do _conda_ e praticá-los em terminal;

# ## Pré-requisitos
# 
# - [Instalação](https://docs.anaconda.com/anaconda/install/) da distribuição Anaconda (recomenda-se Python 3.x);
# - Acesso simples a um terminal ou ao _Anaconda Prompt_;

# ## Introdução
# 
# - _conda_ é um gerenciador de pacotes, dependências e ambientes para múltiplas linguagens;
# 
# - Pacote de código aberto executável em Windows, macOS e Linux;
# 
# > Objetivo: fornecer suporte à rápida instalação, desinstalação e atualização de pacotes
# 
# - Hoje, ~ 7500 pacotes no [repo.anaconda.com](http://repo.anaconda.com)!

# ### Benefícios do _conda_ para cientistas de dados
# 
# - Pacotes pré-construídos: evitam compiladores ou configurações específicas
# 
# - Gestão: instalações mais difíceis com apenas um passo;
# 
# - Reprodutibilidade: Permite que você forneça seu ambiente a outras pessoas em diferentes plataformas;

# ## Conceitos fundamentais
# 
# - Anaconda: distribuição de código aberto, alto desempenho e otimizada para Python e R.
# 
# - Anaconda Cloud: repositório de pacotes hospedado na web (nuvem)
# 
# - Anaconda Navigator: interface gráfica incluída na distribuição para fácil gestão de pacotes, ambientes e canais.

# - Canal: local dos repositórios onde o _conda_ procura por pacotes. Pode ser um repositório público, na web, ou privado, dentro da universidade, em uma empresa, na sua casa, etc.

# - _conda_: gerenciador de pacotes e ambientes que vem incluído na distribuição.

# - _conda environment_ (Ambiente): diretório que contém uma coleção específica de pacotes e dependências que pode ser administrado separadamente. Por exemplo, é possível manter um ambiente Python 2 e Python 3 totalmente isolados sem que um interfira em outro.

# - _conda package_ (Pacote): arquivo comprimido que contém todos os elementos necessários para o funcionamento de um software: bibliotecas, módulos, executáveis e componentes.

# - _conda repository_ (Repositório, ou _repo_): o repositório em nuvem mantido pela Anaconda.

# - Miniconda: é uma versão menor da distribuição que inclui apenas pacotes essenciais, tais como `conda`, `pip`, `zlib` e outros considerados básicos. Pode ser expandido pela instalação de pacotes adicionais.

# - _noarch package_ (Pacote independente de arquitetura): pacote que não contém nada específico à arquitetura de um sistema e que pode ser instalado em qualquer plataforma. `noarch` constitui um subdiretório em um canal.

# - Repositório: qualquer local onde ativos de software são armazenados e podem ser baixados ou recuperados para instalação e uso em computadores.

# ## Comandos fundamentais
# 
# Ver [[Conda Cheat Sheet]](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
# 
# Aqui, dividiremos os comandos nos seguintes grupos: 
# 
# 1. informação e atualização
# 2. ambientes
# 3. pacotes e canais
# 4. adicionais

# ### Comandos para manutenção e atualização
# 
# |comando|o que faz?|
# |---|---|
# |`conda --version` ou `conda -V`|verifica se conda está instalado |
# |`conda info`|verifica instalação e versão do conda|
# |`conda update -n base conda`|atualiza o gerenciador para a versão atual|
# |`conda update conda`|idem|
# |`conda update anaconda`|atualiza todos os pacotes da distribuição para versões estáveis|

# ### Comandos para trabalhar com ambientes
# 
# |comando|o que faz?|
# |---|---|
# |`conda create --name AMB python=3.x "PKG1>v.s" PKG2`|cria novo ambiente com nome "AMB" para funcionar com a versão Python 3.x e instala neste ambiente os pacotes PKG1 e PKG2, sendo o primeiro na versão específica "v.s" e o outro a estável mais atual|

# |comando|o que faz?|
# |---|---|
# |`conda activate AMB`|ativa o ambiente de nome AMB|
# |`conda activate /caminho/para/amb`|ativa um ambiente dado seu local|
# |`conda deactivate`|desativa o ambiente ativo|

# |comando|o que faz?|
# |---|---|
# |`conda list`|lista todos os pacotes do ambiente ativo|
# |`conda list --name AMB`|lista todos os pacotes do ambiente AMB|

# |comando|o que faz?|
# |---|---|
# |`conda remove --name AMB --all`|deleta todo o ambiente AMB|
# |`conda create --clone AMB --name NAMB`|faz um clone NAMB de AMB|

# |comando|o que faz?|
# |---|---|
# |`conda env export --name AMB > amb.yml`|exporta configurações de AMB em um arquivo YAML|
# |`conda env create --file amb.yml`|cria AMB a partir de configurações contidas em um arquivo YAML|

# > YAML (acrônimo para "YAML Ain't Markup Language") é uma linguagem de serialização de dados legível por humanos comumente usada para organizar arquivos de configuração. É utilizada em múltiplas linguagens. Veja [[YAML]](https://yaml.org).

# >`conda activate` e `conda deactivate` somente funcionam a partir das versões 4.6 do `conda`. Para versões anteriores, no Windows usa-se `activate`/`deactivate` e no macOS, usa-se `source activate`/`source deactivate`.
# 

# ### Comandos para trabalhar com pacotes e canais
# 
# |comando|o que faz?|
# |---|---|
# |`conda search PCT=2.8 "PCT [version='>=2.8,<3.2']"`|procura pelo pacote PCT nos canais configurados cuja versão esteja no intervalo 2.8 <= v < 3.2|
# |`conda install PCT`|instala o pacote PCT, se disponível|
# |`conda install -c CH PCT`|instala o pacote AMB a partir do canal CH|
# |`conda install PCT==4.1.0`|instala o PCT com a versão especificada (4.1.0)|
# |`conda install "PCT[version='3.1.0\|3.1.1']"`|instala pacote com uma das versões especificadas (OU)|
# |`conda install "PCT>3.1,<3.5" `|instala uma das das versões do pacote especificadas (E)|

# ### Comandos adicionais
# 
# |comando|o que faz?|
# |---|---|
# |`conda search AMB --info`|fornece informação detalhada sobre o pacote AMB|
# |`conda clean --all`|remove pacotes inutilizados|
# |`conda uninstall PCT --name AMB`|remove o pacote PCT do ambiente AMB|
# |`conda update --all --name AMB`|atualiza todos os pacotes do ambiente AMB|
# |`conda install --yes PCT1 PCT2`|instala pacotes sem exigir prompt do usuário|
# |`conda -h`|para obter ajuda sobre os comandos disponíveis do gerenciador|

# ## Exemplos
# 
# - Criar ambiente chamado "dataScience" com versão Python 3.8 contendo os pacotes numpy, versão 1.19.1, e pandas, mais atual no repositório Anaconda.
# 
# ```bash
# conda create --name dataScience python=3.8 numpy=1.19.1 pandas
# ```

# - Alternar entre ambientes
# 
# Abaixo, vamos reproduzir a mudança de um ambiente para outro em um Z Shell apontando para a pasta _ICD_ e mostrar que o pacote `scipy` está instalado em um ambiente, mas não em outro.
# 
# 
# ```bash
# # no ambiente 'base', procuramos pelo pacote 'scipy'
# (base) gustavo@GloryCrown ICD % conda list scipy
# ```
# ```
# # packages in environment at /Users/gustavo/opt/anaconda3:
# #
# # Name                    Version                   Build  Channel
# scipy                     1.6.2            py38hd5f7400_1
# ```

# ```bash
# # ativamos um novo ambiente chamado 'lecture'
# (base) gustavo@GloryCrown ICD % conda activate lecture
# (lecture) gustavo@GloryCrown ICD %
# ```

# ```bash
# # dentro do ambiente 'lecture', procuramos pelo pacote 'scipy'
# (lecture) gustavo@GloryCrown ICD % conda list scipy
# ```
# 
# ```
# # packages in environment at /Users/gustavo/opt/anaconda3/envs/lecture:
# #
# # Name                    Version                   Build  Channel
# ```

# Nada é mostrado, significando que o pacote `scipy` está indisponível no ambiente `lecture`. Enfim, desativamos o ambiente ativo.
# 
# ```bash
# # desativamos 'lecture' e voltamos para 'base'
# (lecture) gustavo@GloryCrown ICD % conda deactivate
# (base) gustavo@GloryCrown ICD %
# ```

# - Criar arquivo YAML para construção de ambiente personalizado
# 
#     - Abra seu editor de texto preferido (sugestão: no Windows, `notepad++`; no Linux, `gedit`; no macOS, `TextEdit`);
#     - Salve o arquivo como `icd.yml`;
#     - Personalize o seu ambiente (use o modelo a seguir); 
#     - Use o comando `conda env create -f icd.yml` para criar o ambiente;
#     - Verifique se o ambiente foi criado corretamente com `conda env list`. Você deve ver algo como: 

# ```    
# (base) gustavo@GloryCrown ICD % conda env list
# # conda environments:
# #
# base                  *  /Users/gustavo/opt/anaconda3
# icd                      /Users/gustavo/opt/anaconda3/envs/icd
# ``` 

# ```yaml
# # Conteúdo do arquivo  "icd.yaml" 
# # para construir o ambiente 'icd'
# name: icd # nome do ambiente
# channels: # lista de canais a utilizar
#   - defaults # canais padrão
#   - conda-forge
# dependencies: # pacotes dependentes
#   - numpy
#   - scipy
#   - sympy
#   - matplotlib
#   - pandas
#   - seaborn  
# ```   
