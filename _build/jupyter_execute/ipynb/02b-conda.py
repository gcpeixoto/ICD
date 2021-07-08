#!/usr/bin/env python
# coding: utf-8

# # _Crash course_ de _conda_

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
# - Seu objetivo é fornecer suporte à rápida instalação, desinstalação e atualização de pacotes
# 
# - Embora criado para Python, hoje pode ser aplicado a softwares escritos em R, Ruby, Lua, Java, Javascript, C++ etc.
# 
# - Atualmente, há cerca de 7500 pacotes gerenciados no repositório [repo.anaconda.com](http://repo.anaconda.com) que são mantidos pela empresa Anaconda Inc.

# ### Benefícios do _conda_ para cientistas de dados
# 
# - Fornece pacotes pré-construídos que evitam a necessidade de lidar com compiladores ou saber como configurar uma ferramenta específica;
# 
# - Gerencia instalações de ferramentas que são mais difíceis de instalar (como TensorFlow) com apenas um passo;
# 
# - Permite que você forneça seu ambiente a outras pessoas em diferentes plataformas, assim oferecendo suporte à reprodutibilidade de fluxos de trabalho de pesquisa;
# 
# - Permite o uso de outras ferramentas de gerenciamento de pacotes, tais como _pip_, dentro de ambientes _conda_ onde uma biblioteca ou ferramentas ainda não foram empacotadas para _conda_;
# 
# - Fornece bibliotecas e ferramentas de ciência de dados comumente usadas, tais como _R_, _NumPy_, _SciPy_ e _TensorFlow_. Estes são construídos usando bibliotecas específicas de hardware otimizadas (como MKL da Intel, ou CUDA da NVIDIA) que aceleram o desempenho sem alterações de código.

# ## Conceitos fundamentais
# 
# - Anaconda: distribuição de código aberto, alto desempenho e otimizada para Python e R.
# 
# - Anaconda Cloud: repositório de pacotes hospedado na web (nuvem)
# 
# - Anaconda Navigator: interface gráfica incluída na distribuição para fácil gestão de pacotes, ambientes e canais.
# 
# - Canal: local dos repositórios onde o _conda_ procura por pacotes. Pode ser um repositório público, na web, ou privado, dentro da universidade, em uma empresa, na sua casa, etc.
# 
# - _conda_: gerenciador de pacotes e ambientes que vem incluído na distribuição.
# 
# - _conda environment_ (Ambiente): diretório que contém uma coleção específica de pacotes e dependências que pode ser administrado separadamente. Por exemplo, é possível manter um ambiente Python 2 e Python 3 totalmente isolados sem que um interfira em outro.
# 
# - _conda package_ (Pacote): arquivo comprimido que contém todos os elementos necessários para o funcionamento de um software: bibliotecas, módulos, executáveis e componentes.
# 
# - _conda repository_ (Repositório, ou _repo_): o repositório em nuvem mantido pela Anaconda.
# 
# - Miniconda: é uma versão menor da distribuição que inclui apenas pacotes essenciais, tais como `conda`, `pip`, `zlib` e outros considerados básicos. Pode ser expandido pela instalação de pacotes adicionais.
# 
# - _noarch package_ (Pacote independente de arquitetura): pacote que não contém nada específico à arquitetura de um sistema e que pode ser instalado em qualquer plataforma. `noarch` constitui um subdiretório em um canal.
# 
# - Repositório: qualquer local onde ativos de software são armazenados e podem ser baixados ou recuperados para instalação e uso em computadores.
# 
# 
# ```{note}
# Se você é novo com Python ou conda, recomenda-se instalar a distribuição _Anaconda_ (inteira) em vez da _Miniconda_, embora mais tempo e espaço em disco sejam necessários. A distribuição padrão requer cerca de 3 Gb de espaço em disco, ao passo que a _Miniconda_ ocupa em torno de 400 Mb.
# ```

# ## Comandos fundamentais
# 
# A lista a seguir não é exaustiva e contempla os comandos `conda` mais frequentes. Baseia-se na [[Conda Cheat Sheet]](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
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
# |`conda activate AMB`|ativa o ambiente de nome AMB|
# |`conda activate /caminho/para/amb`|ativa um ambiente dado seu local|
# |`conda deactivate`|desativa o ambiente ativo|
# |`conda list`|lista todos os pacotes do ambiente ativo|
# |`conda list --name AMB`|lista todos os pacotes do ambiente AMB|
# |`conda remove --name AMB --all`|deleta todo o ambiente AMB|
# |`conda create --clone AMB --name NAMB`|faz um clone NAMB de AMB|
# |`conda env export --name AMB > amb.yml`|exporta configurações de AMB em um arquivo YAML|
# |`conda env create --file amb.yml`|cria AMB a partir de configurações contidas em um arquivo YAML|
# 
# ```{note}
# YAML (acrônimo para "YAML Ain't Markup Language") é uma linguagem de serialização de dados legível por humanos comumente usada para organizar arquivos de configuração. É utilizada em múltiplas linguagens. Veja [[YAML]](https://yaml.org).
# ```
# 
# ```{warning}
# `conda activate` e `conda deactivate` somente funcionam a partir das versões 4.6 do `conda`. Para versões anteriores, no Windows usa-se `activate`/`deactivate` e no macOS, usa-se `source activate`/`source deactivate`.
# ```

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

# ```{note}
# A lista de canais padrão utilizadas pela distribuição fica armazenada no arquivo oculto `.condarc`. A partir do caderno interativo, execute o comando `!cat ~/.condarc` para uma visão geral do conteúdo do arquivo `.condarc`.
# ```

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

# ```{tip}
# Em muitos casos, opções de comandos que são precedidas por 2 hífens (`--`) podem ser abreviadas para apenas 1 hífen e a primeira letra da opção. Então, `--name` e `-n`, bem como `--envs` e `-n` são opções equivalentes.
# ```

# ## Exemplos
# 
# - Criar ambiente chamado "dataScience" com versão Python 3.8 contendo os pacotes numpy, versão 1.19.1, e pandas, mais atual no repositório Anaconda.
# 
# ```bash
# conda create --name dataScience python=3.8 numpy=1.19.1 pandas
# ```
# 
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
# 
# ```bash
# # ativamos um novo ambiente chamado 'lecture'
# (base) gustavo@GloryCrown ICD % conda activate lecture
# (lecture) gustavo@GloryCrown ICD %
# ```
# 
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
# 
# - Criar arquivo YAML para construção de ambiente personalizado
# 
#     - Abra seu editor de texto preferido (sugestão: no Windows, `notepad++`; no Linux, `gedit`; no macOS, `TextEdit`);
#     - Salve o arquivo como `icd.yml`;
#     - Personalize o seu ambiente (use o modelo a seguir); 
#     - Use o comando `conda env create -f icd.yml` para criar o ambiente;
#     - Verifique se o ambiente foi criado corretamente com `conda env list`. Você deve ver algo como: 
#     
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

# ```{tip}
# Quando você precisar atualizar o seu ambiente de ciência de dados, seja porque necessita de um pacote novo, ou porque encontrou um pacote melhor, basta atualizar o conteúdo do arquivo `icd.yml` e então executar o seguinte comando: `conda env update --file icd.yml --prune`. A opção `--prune` faz com que o conda remova dependêncaias que não forem mais necessárias.
# ```

# ## Desempenho do _conda_
# 
# A instalação de pacotes pode tornar-se lenta por uma variedade de motivos: processamento de metadados, velocidade de internt, verificação de dependências, etc. À medida que o número de pacotes disponíveis aumenta, a busca que o _conda_ realiza pode perdurar por mais tempo. 
# 
# Caso ao tentar instalar um pacote haja lentidão, há algumas questões a analisar. Verifique se há dependências instaladas via `pip`; se os canais estão disponíveis; se o pacote que você está tentando instalar está disponível. 
# 
# Para melhorar o desempenho consulte recomendações [aqui](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/conda-performance.html#improving-conda-performance).
# 
# ```{hint}
# Trabalhar com ambientes menores e dedicados é sempre melhor e mais rápido do que ter ambientes grandes, que são bem mais difíceis de gerenciar. Para ganhar desempenho, reduza a complexidade de seus ambientes.
# ```

# ## Exercícios
# 
# - Usando o `conda`, crie um novo ambiente de trabalho para o curso chamado `icd`.
# - Ative o novo ambiente e instale:
#     - o pacote `numpy` em sua versão mais recente;
#     - o pacote `scipy` na versão 1.6.0;
# - Execute o comando `conda list ncurses`. Qual é a resposta? Ele está instalado? Qual é a versão?
# - Use um comando para buscar informações sobre a versão mais recente do pacote `sympy`. Quantas e quais são as suas dependências?
# - Desinstale o pacote `scipy`. Quantos pacotes permaneceram em seu ambiente?
# - Desinstale o pacote `numpy`. Algum pacote ainda permaneceu em seu ambiente? Por quê?
# - Desative o ambiente `icd` e delete-o completamente.
# - Crie um novo ambiente personalizado `icd` a partir de um arquivo YAML.
