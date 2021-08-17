#!/usr/bin/env python
# coding: utf-8

# # Controle de versão

# ## Objetivos
# 
# - Entender o que um Sistema de Controle Versões (SCV) e o versionamento de código
# - Compreender benefícios de SCVs para arquivos diversos (reprodutibilidade, auditabilidade, compartilhamento, entre outros)
# - Ter uma visão geral sobre os SCVs mais comuns
# - Entender o funcionamento do SCV _git_, bem como o workflow _stage_- _commit_- _push_.
# - Compreender comandos básicos para criação e gerenciamento de repositórios locais e remotos

# ## Introdução

# > Controle de versão é a _abordagem sistemática para registrar alterações realizadas em um arquivo ou conjunto de arquivos ao longo do tempo_. 
# 
# - Daremos uma visão geral sobre _sistemas de controle de versão_ (SCVs), do inglês _control version systems_;
# - Meios eficientes de gerir arquivos em repositórios remotos;
# - Noções de _Git_.

# ## Benefícios de um SCV
# 
# - Reprodutibilidade
# 
# - Auditabilidade
# 
# - Historicidade
# 
# - Sincronia
# 
# - Compartilhamento

# ## Exemplos de SCVs 
# 
# Podem ser baseados em interface gráfica ou em linha de comando. Exemplos:
# 
# - _Google Drive_: suíte de soluções bem conhecida;
# - _Dropbox_: repositório de arquivos com versionamento automático;
# - _Overleaf_: ferramenta para escrever artigos científicos com sistema embutido de versão;
# - _HackMD_: ferramenta colaborativa para documentação.

# - _Bazaar_
# - _Git_
# - _Mercurial_
# - _Subversion_
# - _SVN_

# Neste curso, aprenderemos sobre o _Git_. O _Git_ surgiu em 2005 para ser um sistema SCV:
# 
# - rápido;
# - eficiente;
# - com suporte ao desenvolvimento não-linear (_multibranching_);
# - completamente distribuído e 
# - capaz de manipular grandes projetos.

# ## Processo de versionamento
# 
# O _workflow_ de um SCV ocorre, em geral, nas seguintes etapas básicas:
# 
# 1. Criar arquivos
# 2. Manipular arquivos (alterar, deletar, adicionar)
# 3. Atribuir o estado (_status_) dos arquivos 

# - A atribuição do _status_ é o que se define por _versão_ em um determinado tempo. 
# - Nos SCVs populares, versão é também chamada de _checkpoint_, _commit_ ou _time-point_. 
# - Para o _Git_, o _commit_ é a submissão de uma modificação de arquivo (nova versão de si).

# ### _Masters_ e _branches_
# 
# O desenvolvimento de códigos pode ser ilustrado como uma planta (caule + ramos). 
# 
# - Caule (_master_): "linha-mestra"  do código;
# - Ramos (_branches_):  são as melhorias (_features_) que incorporamos ao código com o tempo. 

# - A ideia de uma ou mais _branches_ é permitir que um programador trabalhe em múltiplas _features_ ao mesmo tempo e decida, posteriormente, se as _branches_ poderão ser fundidas na _master_ ou não. 

# - Este processo é conhecido como "fusão" (_merge_). 
# - A _master_, por si, é chamada de _master branch_ => desenvolvimento _linear_. 
# - Quando _branches_ adicionais coexistem => desenvolvimento _não-linear_.

# ### _Master branch_
# 
# <img src="../figs/04/branch-linear.png">

# ### _Branches_
# 
# <img src="../figs/04/branch-nonlinear.png">

# ## Usando o _git_ 
# 
# Para começar, apontemos uma sutil diferença: 
# 
# - _Git_: é um SCV para gerenciar o histórico de códigos-fonte.
# - _GitHub_: serviço de hospedagem para repositórios _Git_.

# - Enquanto outros SCVs lidam com as "mudanças" feitas em cada arquivo ao longo do tempo, o _Git_ trata-os como um conjunto de imagens de um sistema de arquivos em miniatura.

# - Toda vez que alteramos versões (_commit_), o _Git_ basicamente "tira uma foto de todos os arquivos e armazena uma referência para esse conjunto de arquivos". 

# - Para ser eficiente, se os arquivos não são alterados, o _Git_ não armazena o arquivo novamente, mas um link para o arquivo idêntico anterior já armazenado. Então, o _Git_ lida com _fluxo de estado dos arquivos_. 

# <img src="../figs/04/scv-delta.png" >
# 
# Fluxo dos arquivos no tempo para um SCV usual e para o _Git_.

# <img src="../figs/04/scv-git.png" >
# 
# Armazenamento de arquivos como _snapshots_ (estado dos arquivos"). Fonte: Pro Git Book.

# ### Estados de arquivos
# 
# - Um repositório _git_ pode ser criado por inicialização em um diretório ou por clonagem de um repositório existente. 
# - O processo geral do _Git_ é baseado em três etapas: _Alterar > Preparar > Enviar_. 

# - Em um diretório local, arquivos são criados, modificados, então admitidos a uma área de preparação (_stage area_) e, posteriormente, enviados (_commit_) a um estado de "nova versão". 
# -  Para submetê-los a um repositório remoto, "empurramos" (_push_) os arquivos para sincronizá-los com o repositório local.

# ### Comandos básicos
# 
# - Para inicializar um novo repositório:
# 
# ```
# git init
# ```

# - Para adicionar arquivos à área de preparação:
# 
# ```
# git add
# ```

# - Para enviar arquivos à nova versão:
# 
# ```
# git commit
# ```

# - Para saber o estado dos arquivos:
# 
# ```
# git status
# ```

# - Para gerar o histórico de mudanças:
# 
# ```
# git log
# ```

# <img src="../figs/04/git-commands.png">
# 
# Quadro de estado de arquivos e comandos do _Git_.
# 

# ### Boas práticas do _commit_
# 
# - Escrever mensagem:
# 
# ```none
# git commit -m "Modificação realizada"
# ```

# - Configurar editor preferido 
# 
# ```none
# git config --global core.editor "editor_preferido"
# ```

# As mensagens de um _commit_ devem seguir algumas diretrizes:
# 
# 1. Dar significado: escreva mensagens objetivas, diretas e significativas.
# 2. Resumir as alterações: um modelo sugerido é: 
#     - 1a. linha: escreva um título com até 50 caracteres.
#     - 2a. linha: espaçamento.
#     - 3a. linha em diante: corpo da mensagem contendo o detalhamento das alterações. 

# 3. Usar o tempo verbal no presente: em geral, usamos o tempo verbal no indicativo ou no imperativo, ou mesmo gerúndio para especificar o título de um _commit_. Por exemplo:
#     - Fazendo algo... (_Doing, adding, including this_...)
#     - Faz algo... (_Do, add, include this_...)

#     
# 4. Especificar arquivos: use `git add arq1 arq2 ...` para especificar os arquivos específicos relacionados ao _commit_.
# 
# - Em Python, podemos usar _len('titulo')_ para contar se os o objeto _str_ 'titulo' possui 50 caracteres ou menos.

# Exemplificamos abaixo dois tipos de mensagens que podem acompanhar um _commit_:
# 
# - Mensagem inadequada
# 
# ```none
# "Estou alterando o sinal de + para -."
# ```

# - Mensagem adequada
# 
# ```none
# "Corrige operação aritmética.
# 
# Corrige símbolo de adição ('+') para subtração ('-') 
# na expressão 'a + b' da fórmula utilizada no cálculo do XLMX."
# ```

# Em inglês, uma mensagem equivalente seria: 
# 
# ```none
# "Fix arithmetic operator.
# 
# Replaces symbol '+' with '-' at the expression 'a + b' in the formula to compute the XLMX. 
# ```

# - Para ignorar arquivos de serem rastreados, criamos um arquivo chamado `.gitignore` e neles acrescentamos todos os demais que não devem ser rastreados. 

# - Por exemplo, as instruções abaixo servem para criar o arquivo `.gitignore` e adicionar o arquivo _ignore.txt_ para não ser rastreável.
# 
# ```bash
# touch .gitignore; echo "ignore.txt" > .gitignore; cat .gitignore
# ```

# ### Recuperação e comparação
# 
# - Para criar um novo _commit_ que reverte as mudanças feitas na última versão a um estado anterior:
# 
# ```none
# git revert HEAD
# ```
# - A partir do histórico de mudanças obtido por `git log`, podemos reverter o projeto inteiro para uma versão anterior especificando o SHA do projeto:

# ```none
# git checkout SHA
# ```
# - No caso de recuperar a versão anterior de um único arquivo, especificamos o arquivo com:

# ```none
# git checkout SHA -- file
# ```

# 
# [[SHA]](https://en.wikipedia.org/wiki/Secure_Hash_Algorithms) (_Secure Hash Algorithm_) é um conjunto de algoritmos desenvolvidos pelo americano National Institute of Standards and Technology (NIST) para encriptar arquivos e atribuir-lhes uma identidade para finalidades de verificação. SHA é um tipo de CHF (_cryptographic hash function_).

# **Exemplo:** 2 _commits_ realizados em um projeto. 
# - O ponteiro (_HEAD_) mostra que o _commit_ com SHA `553ae56fb180ff630ba4026cbc1deb212e4efd42` é o estado mais atual do projeto. 
# - Para retornar o projeto ao estado imediatamente anterior, podemos fazer `git checkout 431d0e589e7366dc21d0e18144f72b67d6b4a148`.  

# ```none
# commit 553ae56fb180ff630ba4026cbc1deb212e4efd42 (HEAD -> master)
# Author: Gustavo Oliveira <gustavo.oliveira@ci.ufpb.br>
# Date:   Tue Mar 16 16:06:50 2021 -0300
# 
#     Fix ex5. Required to modify convertInputUnits to see pressure.
# 
# commit 431d0e589e7366dc21d0e18144f72b67d6b4a148
# Author: Gustavo Oliveira <gustavo.oliveira@ci.ufpb.br>
# Date:   Tue Mar 16 14:24:03 2021 -0300
# 
#     ex5 removed files.
# ```

# - Para comparar duas versões de arquivo podemos usar 
# 
# ```
# git diff
# ```
#  Entender o que está sendo comparado
#         - observar as indicações
#     - Comparar somente arquivos relevantes

# ### Trabalhando com _branches_
# 
# - _Branches_ são abertas para incorporar novos elementos, funcionalidades ou componentes em um projeto de maneira a não interferir no tronco do projeto, que deve permanecer estável ao longo do tempo. 
# - São também usadas para evitar rupturas acidentais que danifiquem a operação normal das componentes de projeto.

# - Para criar uma nova _branch_, usamos: 
# 
# ```none
# git checkout -b nome_da_branch
# ```

# - Para navegar entre as _branches_:
# 
# ```none
# git checkout nome_da_branch
# ```

# - Para listar todas as _branches_ existentes:
# 
# ```none
# git branch
# ```

# - Para deletar completamente uma branch:
# 
# ```none
# git branch -D nome_da_branch
# ```

# ### Fusão
# 
# - Para integrar as modificações propostas em uma _branch_ na _branch master_ realizamos uma espécie de "fusão". 
# - Por exemplo, para fundir uma _branch_ de origem, digamos _branch_A_, em outra de destino, digamos _branch_B_, primeiro devemos levar o ponteiro para a origem _branch_A_ com:

# ```none
# git checkout branch_A
# ```
# Em seguida, a fundimos na _branch_B_ com: 
# 
# ```none
# git merge branch_B
# ```

# #### Conflitos 
# 
# - Se, por exemplo, um mesmo arquivo for alterado na _branch_A_, mas não na _branch_B_, ao tentar fundi-las, uma incompatibilidade existirá, de maneira que um erro por conflito de versões será produzido. 
# 
# - Para corrigir incompatibilidades, as partes modificadas do arquivo devem ser equalizadas ou substituídas por um novo arquivo. Em seguida, um novo _commit_ deve ser submetido. Eventualmente, para descatar uma fusão, usamos:
# 
# ```none
# git merge --abort
# ```

# ##### Ferramentas para resolver conflitos 
# 
# Algumas ferramentas que ajudam a resolver conflitos gerados por _merge_ estão disponíveis no mercado, tais como 
# 
# - [KDiff3](http://kdiff3.sourceforge.net/)
# - [Beyond Compare](https://www.scootersoftware.com/)
# - [Meld](http://meldmerge.org/) e 
# - [P4Merge](https://www.perforce.com/products/helix-core-apps/merge-diff-tool-p4merge). 

# Para definir a ferramenta padrão para fusão, fazemos:
# 
# ```none
# git config --global merge.tool name_of_the_tool
# ```
# e a lançamos com: 
# 
# ```none
# git mergetool
# ```

# #### Boas práticas 
# 
# Para trabalhar efetivamente com _branches_, algumas boas práticas recomendadas são:
# 
# - Manter a _master_ limpa;
# - Adicionar apenas uma nova _feature_ por _branch_;
# - Usar nomes razoáveis para as _branches_.

# ### Integração com repositórios
# 
# Repositórios remotos são hoje amplamente utilizados como meios de hospedagem e compartilhamento de código, entre os quais estão o _GitHub_, _GitLab_ e o _Bitbucket_. Todavia, é possível que qualquer um crie seu próprio repositório em um servidor web (veja, por exemplo, este [link](https://opensource.com/life/16/8/how-construct-your-own-git-server-part-6)). 
# 
# - A seguir, damos exemplos de como utilizar o _GitHub_. Para realizar a comunicação entre um repositório local com seu homólogo remoto, ou vice-versa.

# Para clonar um repositório remoto localmente, o comando se parece com:
# 
# ```
# git clone https://github.com/user/repo.git
# ```
# 
# onde _user_ é o nome do usuário no _GitHub_ e _repo_ é o nome do repositório.

# - Para atualizar um repositório local tomando como base um remoto:
# 
# ```
# git pull
# ```
# Neste caso, é necessário que o histórico de modificações também seja compatível entre ambos.

# - Para submeter versões após um _commit_ para o repositório remoto, utilizamos 
# 
# ```
# git push
# ```
# 
# > No jargão da computação, _repo_ é uma redução de repositório.
# 

# #### Vinculando o repositório local com o remoto
# 
# Para que tenhamos um repositório local em sincronia com um remoto, podemos realizar os seguintes passos: 
# 
# - Inicialização e versionamento
# 
# ```none
# cd icd
# git init
# git add .
# git commit
# ```
# Acima, `icd` é o diretório onde o projeto está localizado em nosso disco local. Em seguida, inicializamos o rastreamento, adicionamos todos os arquivos contidos no diretório e atribuímos a versão. 

# - Vinculação remota 
# 
# Nesta etapa, fazemos a vinculação com o repositório remoto no _GitHub_ e "empurramos" os arquivos para lá:
# 
# ```none
# git remote add origin https://github.com/user/repo.git
# git push - u origin master
# ```

# - Atualização local
# 
# Caso alteremos os arquivos diretamente no _GitHub_, podemos atualizar o repositório local com: 
# 
# ```none
# git pull
# ```

# ### _Pull requests_
# 
# Caso queiramos contribuir com um projeto cuja propriedade seja de outro usuário, podemos requisitar acesso a ele no _GitHub_ com _pull requests_.
# 
# Suponhamos que 3 desenvolvedores atuam em um projeto em 3 branches distintas. Se um deles fizer uma modificação e submetê-la à _branch master_ sem que os outros 2 acompanhem em tempo real, ambos podem atualizar suas _branches_ com
# 
# ```
# git pull origin master
# ```

# ### _Forks_ 
# 
# Um _fork_ é o ato de _aforquilhar_ ("prender com forquilha ou garfo") um projeto, no sentido de copiar o repositório de um usuário no GitHub para você. O repositório original "forkado" é chamado de _upstream_.

# Para trabalhar com a sua cópia "forkada", siga os seguintes passos: 
# 
# - Clone o _repo_ aforquilhado localmente:
# 
# ```none
# git clone git@github.com/seu_user/forked_repo.git
# ```

# - Adicione o _upstream_ à sua lista de repositórios remotos para receber as mudanças submetidas no _repo_ original:
# 
# ```none
# git remote add upstream https://github.com/upstream_user/original_repo.git
# ```

# - Verifique se ele foi, de fato adicionado: 
# 
# ```none
# git remote -v
# ```

# - Atualize o _repo_ aforquilhado trazendo do original as mudanças e _commits_ mais recentes, bem como todas as _branches_ (fazer uma "juntada"):
# 
# ```none
# git fetch upstream
# ```

# - Liste todas as _branches_, incluindo as do _upstream_:
# 
# ```none
# git branch -va
# ```

# - Direcione o ponteiro para a sua _master branch_:
# 
# ```none
# git checkout master
# ```

# ### Tutorial interativo do _Git_
# 
# Descrever em palavras o que os comandos _git_ realizam concretamente pode ser um pouco impreciso. A ferramenta 
# [Learn Git Branching](https://learngitbranching.js.org/) foi criada com o propósito de ensinar o _git_ por meio de tutoriais interativos. Com ela, você pode praticar e entender comandos e simular o comportamento de um repositório real.

# ## Controle de versão para dados
# 
# - Ferramentas para que lidam com controle de versão de grandes arquivos passaram a ser desenvolvidas. 
# - Elas permitem que grandes dados sejam adicionados a repositórios e tenham seus estados controlados. 
# - Algumas dessas ferramentas são:
#     - [CyberDuck](https://cyberduck.io)
#     - [DataLad](https://www.datalad.org)
#     - [_Git LFS_](https://git-lfs.github.com/)
#     - [_git-annex_](https://git-annex.branchable.com/)

# Exemplos de ferramentas de _cloud computing_ para gestão de grandes arquivos e controle de dados são: 
# 
# - [Alibaba Cloud](https://www.alibabacloud.com)
# - [AWS CLI](https://aws.amazon.com/cli/)
# - [Google Cloud](https://cloud.google.com)
# - [Microsoft Azure](https://azure.microsoft.com/en-us/)

# ## Exercícios
# 
# - Criar repositório para o curso e organizá-lo como um projeto.
# - Praticar comandos do _git_ na _sandbox_ do [Learn Git Branching](https://learngitbranching.js.org/).

# ## Referências 
# 
# - [[GitHub Docs]](https://docs.github.com/en)
# 
# - [[Learn Git with Bitbucket]](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)
# 
# - [[Pro Git Book]](https://git-scm.com/book/en/v2)
# 
# - [[The Turing Way]](https://the-turing-way.netlify.app/welcome.html)
