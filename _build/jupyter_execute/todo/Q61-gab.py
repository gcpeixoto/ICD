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

# In[2]:


import sympy as sym
from sympy import Symbol, pprint
import numpy as np
import matplotlib.pyplot as plt 


# **Questão 1.** Observe a figura abaixo e julgue os itens a seguir.
# 
# ```{figure} ../figs/q/q61.png
# ---
# width: 300px
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
# Assinale a alternativa correta.
# 
# A. São corretos i) e ii), apenas.
# 
# B. Apenas i) é correto.
# 
# C. São corretos i) e iii), apenas.
# 
# D. n.d.a.

# In[7]:


plt.figure(figsize=(14,4))
plt.subplot(141)
x1 = np.linspace(-10, 10, 100)
plt.plot(np.sin(x1),c='r')
plt.xticks([]); plt.yticks([]);
plt.title('(a)')

plt.subplot(142)
x2 = np.linspace(-2, 2, 100)
plt.plot(x2, np.exp(x2)*10*np.sin(6*x2))
plt.xticks([]); plt.yticks([]);
plt.title('(b)')

plt.subplot(143)
x3 = np.arange(-100, 100, 1)
plt.plot(x3, x3**2, c='orange')
plt.xticks([]); plt.yticks([]);
plt.title('(c)')

plt.subplot(144)
x4 = np.arange(-100, 0, 1)
plt.plot(x4, x4**3,c='m')
plt.xticks([]); plt.yticks([]);
plt.title('(d)')


plt.show()


# <hr>
# 
# ## Gabarito
# Alternativa **A**

# <hr>
# 
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

# In[3]:


x1 = np.random.normal(0,1,10)


# In[4]:


#Gráfico da função
plt.plot((1.0/(x1-0.5)**2)-1.0/((x1-0.8)**2 +0.04) - 70 , label='$P(x)$', c='g');
plt.legend()
plt.title('Potencial de ação de uma membrana')
plt.show()
#plt.savefig("../figs/q/q61-2.png'")


# <hr>
# 
# ## Gabarito
# Alternativa **C**

# In[9]:


x = sym.symbols('x')
p = (1.0/((x-0.5)**2+0.01))-1.0/((x-0.8)**2 +0.04) - 70 


# In[10]:


p


# In[73]:


dp = sym.diff(p,x)
dp.subs(x,0)


# <hr>

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

# <hr>
# 
# ## Gabarito
# Alternativa **B**.

# In[81]:


# domínio
a,b = -0.5,-0.1
x = sym.symbols('x')
c = 6 

# função e valores
f = -1/(sym.exp(x)*sym.sin(c*x))

df = f.diff(x)

dom = np.linspace(a,b)
plt.plot(dom, -1/(np.exp(dom)*np.sin(c*dom)));


# In[ ]:




