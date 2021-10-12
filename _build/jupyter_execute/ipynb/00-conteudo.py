#!/usr/bin/env python
# coding: utf-8

# # Apresentação do curso

# ## Conteúdo
# 
# ### Introdução
# 
# - [Introdução à Ciência de Dados](01-introducao.ipynb)
# 
# ### Unidade 1 
# 
# #### Parte 1
# 
# - [Pacotes e ambientes virtuais com _pip_ e _venv_](02a-pip-venv.ipynb)
# - [_Crash course_ de _conda_](02b-conda.ipynb)
# - [Ambientes de desenvolvimento e computação interativa](03-ides.ipynb)
# - [Controle de versão](04-cvs-git.ipynb)
# 
# #### Parte 2
# 
# - [Python intermediário - I](05-python-intermediario.ipynb)
# - [Python intermediário - II](06-python-intermediario-2.ipynb)
# - [Python intermediário - III](07-python-intermediario-3.ipynb)
# - [Computação vetorizada](08a-computacao-vetorizada.ipynb)
# - [Álgebra Linear Computacional básica](08b-alc.ipynb)
# - [Plotagem e formatação de gráficos](09-plotagem-matplotlib.ipynb)
# 
# ### Unidade 2
# 
# #### Parte 3
# 
# - [Manipulação de dados - I](10a-pandas-series.ipynb)
# - [Manipulação de dados - II](10b-pandas-dataframe.ipynb)
# - [Manipulação de dados - III](10c-pandas-agrupamento.ipynb)
# 
# #### Parte 4
# 
# - [Estatística Descritiva](11-estatistica-descritiva.ipynb)
# - [Correlação](12-correlacao.ipynb)
# <!-- - [Regressão](13-regressao.ipynb) -->
# 
# ### Unidade 3
# 
# _Coming soon..._
# 
# ## Avaliação
# 
# ### Questionários
# 
# - Unidade 1: Parte 2
#     - [Questionário 21](Q21.ipynb)
#     - [Questionário 22](Q22.ipynb)
#     - [Questionário 23](Q23.ipynb)
#     - [Questionário 24](Q24.ipynb)
#     - [Questionário 25](Q25.ipynb)
# - Unidade 2: Parte 3
#     - [Questionário 31](Q31.ipynb)
#     - [Questionário 32](Q32.ipynb)    
# - Unidade 2: Parte 4
#     - [Questionário 41](Q41.ipynb)    
# 
# #### Conceito
# 
# Cada questionário possui 3 questões em formato _única escolha_ (vide orientações em seu cabeçalho) e procura avaliar a compreensão dos conceitos.
# 
# #### Avaliação 
# 
# A nota atribuída ao questionário é calculada da seguinte forma: 
# 
# - 1 acerto: nota 3
# - 2 acertos: nota 6
# - 3 acertos: nota 10
# 
# Entretanto, as respostas devem ser comprovadas por meio de um arquivo .IPYNB **único** utilizado para codificar as soluções. Neste sentido, adotam-se os seguintes comportamentos e fatores de redução de nota, no que couber:
# 
# - _O arquivo foi enviado, mas a extensão difere de .IPYNB?_ A nota do questionário será reduzida em 30%.
# - _Foram enviados mais de um arquivo .IPYNB com questões separadas?_ A nota do questionário será reduzida em 50%.
# - _O questionário foi respondido, mas o arquivo .IPYNB correspondente não foi enviado?_ A nota do questionário será reduzida em 70%.
# 
#     
# ### Mini-Artigos
# 
# #### Conceito 
# 
# Mini-artigos são textos escritos pelos alunos que complementam o estudo dos tópicos propostos durante o curso. Eles devem ter no máximo 2 páginas e estar em conformidade com o modelo (_template_) proposto.
# 
# #### Avaliação
# 
# Os mini-artigos podem ter temas genéricos e assumirem formato discursivo, narrativo ou instrucional (tutorial) relativos à ciência de dados. Entretanto, espera-se que haja um caráter minimamente técnico.
# 
# Uma nota de 0 a 10 é atribuída ao mini-artigo a partir da média aritmética de notas parciais que consideram os 4 critérios (dimensões) a seguir:
# 
# - **C1: Originalidade/Tecnicalidade:** avalia capacidade de expor tema com originalidade e caráter técnico.
# - **C2: Atualidade/Criatividade:** avalia se o tema é de relevância para a atualidade e se há novidade criativa.
# - **C3: Apresentação/Visual:** avalia organização e estrutura do texto, qualidade de figuras, tabelas e dados em geral.
# - **C4: Linguagem/Correção:** avalia o uso da linguagem perante a norma culta, ortografia, coesão e coerência.
# 
# Para cada critério, duas perguntas devem ser respondidas de maneira binária (sim/não), consoante a seguinte estrutura e pesos, onde $P_{ij}$ é a $j$-ésima pergunta associada ao critério $i$.
# 
# - P<sub>11</sub>: O tema escolhido para o artigo é original? (peso 0,5)
# - P<sub>12</sub>: O artigo pode ser classificado como técnico? (peso 0,5)
# - P<sub>21</sub>: O tema é relevante na atualidade?	(peso 0,4)
# - P<sub>22</sub>: A escolha do tema reflete criatividade, i.e., novidade não considerada em aula? (peso 0,6)
# - P<sub>31</sub>: A formatação do artigo está de acordo com o template fornecido? (peso 0,5)
# - P<sub>32</sub>: Os elementos gráficos são legíveis, com boa resolução e bem dispostos? (peso 0,5)
# - P<sub>41</sub>: O texto do artigo obedece à norma culta? (peso 0,5)
# - P<sub>42</sub>: O texto possui poucos erros ortográficos, coerência e coesão razoáveis? (peso 0,5)	
# 
# #### Fluxo de processamento
# 
# O processo de avaliação do mini-artigo seguirá o seguinte fluxo: 
# 
# 1. Mini-artigo é escrito e renomeado para o seguinte modelo: `<YYYY-SS> - Short Paper - A<p> - <Name> <Surname> - <Title>`, onde `YYYY` é o ano corrente, `SS` o semestre acadêmico corrente (01 ou 02), `p` é o dígito correspondente à parte do curso (vide divisão de unidades e partes), `Name` é o primeiro nome do(a) discente, `Surname` seu último sobrenome e `Title` o título do artigo. **Atenção:** altere apenas os caracteres confinados por `< >`. O nome do arquivo deve resultar em algo como: `2021-01> - Short Paper - A2 - Isaac Newton - Análise do módulo os`. 
# 2. Mini-artigo é submetido à avaliação via SIGAA dentro do prazo estipulado.
# 3. Mini-artigo é avaliado segundo os 4 critérios e a nota é atribuída. 
# 4. Comentários com recomendações são adicionados no PDF para finalidades de correção.
# 5. Mini-artigo revisado recebe sufixo `Reviewed`, é encriptado por senha e devolvido ao(à)  discente (consultar arquivo .ZIP disponível no SIGAA). 
# 6. Discente baixa o mini-artigo revisado eo desbloqueia (senha: últimos 4 dígitos de sua matrícula).   
# 7. Discente acata ou não as sugestões propostas. Se sim, faz as alterações devidas no texto.
# 8. Discente renomeia o arquivo PDF substituindo o sufixo `Reviewed` por `Final`.
# 9. Se concordar, discente ressubmete o arquivo PDF do mini-artigo em sua versão final via SIGAA para registro no banco de dados de mini-artigos do curso de ICD. 
# 10. Mini-artigo é disponibilizado online permanentemente através de site do curso (ou do professor) para consulta e referência de demais discentes.
# 
# **Observação:** a submissão para a versão `Final` só será considerada para quem enviou o mini-artigo original dentro do prazo estipulado no programa. Logo, envios posteriores não serão aceitos. 
# 
# #### Template 
# 
# Para elaborar os mini-artigos avaliativos, pode-se usar o template em formato .ODT disponibilizado <a href="https://github.com/gcpeixoto/ICD/blob/main/templates/short-paper/odt/main.odt" download="https://github.com/gcpeixoto/ICD/blob/main/templates/short-paper/odt/main.odt"> aqui </a>, mas recomenda-se, preferencialmente, o uso do template LaTeX disponibilizado <a href="https://github.com/gcpeixoto/ICD/tree/main/templates/short-paper/tex"> aqui </a>.
# 
# **Atenção:** não altere a formatação do template, sob pena de ter a pontuação reduzida! Obedeça o esquema de cores, fontes, etc.
# 
# ### Projeto Final
# 
# _Coming soon..._
# 
# ### Fórmulas de cálculo
# 
# - Nota da parte: $N_{p} = 0,5A_p + \sum_{i} x_i \, Q_{pi}$
#     - $A_p$: nota do mini-artigo associado à parte $p$
#     - $Q_{pi}$: questionário $i$ da parte $p$
#     - $x_{i}$: peso do questionário $Q_{pi}$ (igual para todos, com $\sum_i x_{i} = 0,5.$
#   
# - Nota da unidade: $N_u = \frac{1}{P}\sum_{p=1}^P N_p$
#     - $P$: número de partes
# 
# - Nota final: $N_{f} = \sum_{u=1}^4 0,1N_{u} + 0,6 NPF$
#     - $NPF$: nota do projeto final
#     
# #### Repositório de arquivos
# 
# - [Projeto _Cadernos de ICD_](cadernos-icd.ipynb)

# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Parte 1
# 
# 01-introducao
# 02a-pip-venv
# 02b-conda
# 03-ides
# 04-cvs-git
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Parte 2
# 
# 05-python-intermediario
# 06-python-intermediario-2
# 07-python-intermediario-3
# 08a-computacao-vetorizada
# 08b-alc
# 09-plotagem-matplotlib
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Parte 3
# 
# 10a-pandas-series
# 10b-pandas-dataframe
# 10c-pandas-agrupamento
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Parte 4
# 
# 11-estatistica-descritiva
# 12-correlacao
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Questionários
# 
# Q21
# Q22
# Q23
# Q24
# Q25
# Q31
# Q32
# Q41
# ```
# 
# 
# ```{toctree}
# :hidden:
# :titlesonly:
# :caption: Cadernos de ICD
# 
# cadernos-icd
# ```
# 
