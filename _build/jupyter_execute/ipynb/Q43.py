#!/usr/bin/env python
# coding: utf-8

# ## Questionário 43 (Q43)

# 
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

# Para responder este questionário, utilize o banco de dados [brasileirao2021.csv](https://github.com/gcpeixoto/ICD/blob/main/database/brasileirao2021.csv). Fonte: [[CBF]](https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a).
# 
# **Obs.:** use o _dataset_ do repositório Git e não o do site da CBF, visto que este é atualizado após cada jogo.
# 
# <br>
# 
# **Questão 1.** Utilizando o método de _z-scores_ e o _dataset_, identifique todos os times cuja pontuação superou a média do campeonato e assinale a alternativa correta quanto às posições que ocupavam no ranque do Brasileirão 2021 no momento em que o _dataset_ havia sido gerado.
# 
# A. 1a. a 6a.
# 
# B. 3a. a 5a.
# 
# C. 1a. a 9a.
# 
# D. 2a. a 8a.

# **Questão 2.** O _dataset_ descreve o desempenho de cada time através de marcadores clássicos do futebol, a saber: Pontos (_PTS_), Jogos (_J_), Vitórias (_V_), Empates (_E_), Derrotas (_D_), Gols Marcados (Pró) (_GP_), Gol Sofridos (Contra) (_GC_), Saldo de Gols (_SG_), Cartões Amarelos (_CA_) e Cartões Vermelhos (_CV_).
# 
# Considerando $X$ a série correspondente a _PTS_, determine as variáveis correspondentes às séries $Y_1$ e $Y_2$, tais que, $\text{cov}(X,Y_1)$ seja a maior covariância positiva e $\text{cov}(X,Y_2)$ seja a maior covariância negativa.
# 
# 
# A. _J_ e _V_
# 
# B. _GP_ e _GC_
# 
# C. _SG_ e _GP_
# 
# D. _SG_ e _GC_
# 

# **Questão 3.** Considere o _DataFrame_ processado para a resolução da Questão 2. Entre as 
# séries Gols Marcados (Pró) (_GP_), Gol Sofridos (Contra) (_GC_), Saldo de Gols (_SG_), Cartões Amarelos (_CA_) e Cartões Vermelhos (_CV_), identifique a que possui a mais forte correlação positiva com _E_ e a que possui a mais forte correlação negativa com _V_, respectivamente. Assinale a alternativa correta.
# 
# A. _GP_ e _GC_
# 
# B. _CV_ e _GP_
# 
# C. _CA_ e _GC_
# 
# D. _SG_ e _GC_
