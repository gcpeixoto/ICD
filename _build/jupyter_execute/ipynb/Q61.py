#!/usr/bin/env python
# coding: utf-8

# ## Questionário 61 (Q61)

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

# **Questão 1.** Observe os gráficos abaixo e julgue os itens a seguir.
# 
# ```{figure} ../figs/q/q61.png
# ---
# width: 600px
# name: convex
# ---
# ```
# 
# i) existe uma função convexa entre as quatro plotadas.
# 
# ii) uma entre as funções plotadas possui convexidade parcial.
# 
# iii) duas entre as funções plotadas não são convexas.
# 
# Assinale a alternativa correta:
# 
# A. São corretos i) e ii), apenas.
# 
# B. Apenas i) é correto.
# 
# C. São corretos i) e iii), apenas.
# 
# D. n.d.a.

# **Questão 2.** A função a seguir simula a curva do _potencial de ação_ de uma membrana:
# 
# $$P(x) = \dfrac{1.0}{(x - 0.5)^2 + 0.01} - \dfrac{1.0}{(x - 0.8)^2 + 0.04} - 70.$$
# 
# Use computação simbólica para calcular uma aproximação para $P'(x=0)$ e assinale a alternativa correta.
# 
# A. -67.62
# 
# 
# B. 0.25
# 
# 
# C. 11.33
# 
# 
# D. 0.00
# 
# Nota: Use `sympy.subs(x,x0)`.

# **Questão 3.** Considere a função
# 
# $$f(x) =  - \dfrac{1}{e^x \text{sen}(6x)},$$
# 
# definida no domínio $[-0.5,-0.1]$. Assinale a alternativa correta:
# 
# A. $f(x)$ não é convexa e $f'(x) = -\frac{e^{x}}{\text{sen}{\left(6 x \right)}} + \frac{6 e^{- x} \cos{\left(6 x \right)}}{\text{sen}^{2}{\left(6 x \right)}}$
# 
# B. $f(x)$ é convexa e $f'(x) = \frac{e^{- x}}{\text{sen}{\left(6 x \right)}} + \frac{6 e^{- x} \cos{\left(6 x \right)}}{\text{sen}^{2}{\left(6 x \right)}}$
# 
# C. $f(x)$ não é convexa e $f'(x) = \frac{e^{x}}{\text{sen}{\left(6 x \right)}} + \frac{6 e^{- x} \cos{\left(6 x \right)}}{\text{sen}^{2}{\left(6 x \right)}}$
# 
# D. $f(x)$ é convexa e $f'(x) = -\frac{e^{- x}}{\text{sen}{\left(6 x \right)}} + \frac{6 e^{- x} \cos{\left(6 x \right)}}{\text{sen}^{2}{\left(6 x \right)}}$
