#!/usr/bin/env python
# coding: utf-8

# ## Questionário Q44

# Orientações: 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-a à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# 
# <hr>

# **Questão 1.** O _dataset_ [covid19-weekly-trends-in-europe](https://github.com/gcpeixoto/ICD/blob/main/database/covid19-weekly-trends-in-europe.csv) contém tendências semanais de casos de Covid-19 em diferentes países da Europa com referência ao dia 8 de novembro de 2021. Separe a série correspondente ao número de casos nos últimos 7 dias (_Cases in the last 7 days_) entre países pertencentes à União Europeia (_UE_) e não pertencentes à UE (_non-UE_). Assinale a alternativa que associa corretamente o grupo de países ao valor do coeficiente de Pearson.
# 
# A. _non-UE_: 620983827.08
# 
# B. _UE_: 620983827.08
# 
# C. _UE_: 750983827.02
# 
# D. _non-UE_: 8290903184.71

# <hr>
# 
# **Questão 2.** Analise as seguintes distribuições normais aleatórias:
# 
# ```{figure} ../figs/q/q44-1.png
# ---
# width: 600px
# name: q44-1
# ---
# ```
# 
# Assinale a alternativa em que as curvas aparecem em ordem crescente de desvio padrão.
# 
# A. (A, B, C, D)
# 
# B. (B, A, D, C)
# 
# C. (B, A, C, D)
# 
# D. (A, B, D, C)

# <hr>
# 
# **Questão 3.** O código
# 
# ```python
# import numpy as np, from scipy.stats import norm
# N, band = 100, 0.5
# 
# np.random.seed(2)
# X = np.concatenate(
#     (np.random.normal(0, 1, int(0.3 * N)),
#      np.random.normal(5, 1, int(0.7 * N))))[:, np.newaxis]
# Xp = np.linspace(-5, 10, 1000)[:, np.newaxis]
# 
# dens = 0.3*norm(0,1).pdf(Xp[:, 0]) + 0.7*norm(5,1).pdf(Xp[:, 0])
# ```
# gera a distribuição sombreada `dens` apresentada nas figuras de (a) a (d) abaixo. 
# 
# ```{figure} ../figs/q/q44-2.png
# ---
# width: 600px
# name: q44-2
# ---
# ```
# Com base nos _kernels_ disponíveis na classe `KernelDensity`
# do módulo _scikit-learn_, assinale a alternativa que melhor preeche as lacunas na sentença:
# 
# *"O kernel ______ aproxima a distribuição em ______, ao passo que o kernel ______ aproxima a distribuição mostrada em ______."*
# 
# 
# A. _'linear'_ / (a) / _'gaussian'_ / (d)
# 
# B. _'linear'_ / (b) / _'tophat'_ / (a)
# 
# C. _'epanechnikov'_ / \(c\) / _'linear'_ / (d)
# 
# D. _'gaussian'_ / (b) / _'epanechnikov'_ / \(c\)
