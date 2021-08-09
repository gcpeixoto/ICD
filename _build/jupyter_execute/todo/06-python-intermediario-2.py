#!/usr/bin/env python
# coding: utf-8

# # Python Intermediário: Parte 2

# ## Funções
# 
# O conceito de "função" é conhecido por nós como algo que produz uma saída (_output_) a partir de uma entrada (_input_). Matematicamente, podemos representar este processo como $y= f(x)$. Por exemplo, uma impressora jato de tinta ao receber uma folha de papel em branco ($x$) aciona seus mecanismos de impressão ($f$) e produz uma folha impressa ($y$).  
# 
# Em Python, funções são utilizadas praticamente da mesma forma, em que zero ou mais entradas retornam uma saída correspondente. Funções são fundamentais para organizar e reutilizar código, sempre que uma tarefa tenha de ser executada repetidamente. Toda função é um _objeto de primeira classe_. Isto essencialmente significa que ela pode ser: i) atribuída a uma variável ou elemento em uma estrutura de dado; ii) passada como argumento para outra função; iii) retornada como resultado de uma função.
# 
# ### Tipos de funções 
# 
# Neste curso, separaremos as funções em três grupos:
# 
# - _predefinidas_ (_built-in functions_): aquelas pré-existentes no _core_ da linguagem ou em outros módulos;
# - _regulares_ (_user-defined functions_): aquelas definidas por você;
# - _anônimas_ (_lambdas_): funções, em geral, criadas por você que não exigem um nome; 

# #### Funções predefinidas
# 
# Exploraremos exemplos com funções _built-in_ do _core_ Python. Em particular, cobriremos: `hex`, `bin`

# **Exemplos:** funções predefinidas do _core_ da linguagem.

# In[32]:


# built-in functions
hex(1234),bin(345),round(12.3456,3)


# Discussão: 
# 
# - `hex` converte um número para hexadecimal, indicada pelo prefixo `0x`.
# 
# - `bin` converte um número para hexadecimal, indicada pelo prefixo `0b`.
# 
# - `round(x,n)` arredonda um número `x` em `n` dígitos de precisão. Se `n < 0`, retorna `0.0`. 

# In[262]:


# built-in function
for i in range(6000,7000,100):
    print(chr(i),end=',')


# Discussão: 
# 
# - `chr` retorna o caracter Unicode correspondente ao número inteiro passado no intervalo [0,1114111].

# **Exemplo**: somando números em uma lista.

# In[242]:


sum(range(100)), sum([])


# Discussão: 
# - `sum` é uma função predefinida aplicável a sequências iteráveis.
# - Se o iterável for vazio, `sum` retorna zero.
# - No exemplo anterior, somamos os números de 0 a 100 e aplicamos a função a uma lista vazia.

# **Exemplo**: número de elementos em iteráveis.

# In[247]:


# no. de elementos
len([1,4,5])


# In[249]:


# conta keys
len({'a':1,'b':2})


# In[246]:


# lembre da unicidade
# 3 elementos no conjunto
len({1,3,1,2})


# In[254]:


# conta caracteres
len('nome')


# #### Funções regulares
# 
# Funções regulares, como dissemos, possuem um nome definido pelo usuário. Vejamos alguns exemplos.

# **Exemplos:** funções regulares e uso de funções.

# In[70]:


def cm_to_inch(x):
    """converte número de centímetros para polegadas"""
    return 2.45*x


# Comentários: 
# 
# - Funções regulares são declaradas com a _keyword_ `def` e valores de retorno com a _keyword_ `return`.

# In[71]:


# chamada simples
cm_to_inch(23)


# In[73]:


# atribuindo em objeto
cmi = cm_to_inch


# In[232]:


# usando como argumento de outra função
def fn(n,f):
    """Calcula f(n) dados n e uma função f."""
    return f(n)

fn(2,cm_to_inch)


# In[233]:


# docstring da função
fn.__doc__


# Parâmetros de funções podem assumir um argumento padrão que pode ser modificado sempre que necessário. 
# 
# **Exemplos:**

# In[101]:


# 'BEGIN' é valor padrão
def line(title='BEGIN'):
    print(title.center(20,'-'))


# In[105]:


# especificação não necessária
line()


# In[104]:


# alterando padrão
line('HEAD')


# **Exemplo:** função com argumentos posicionais.

# In[220]:


# função com 2 argumentos posicionais
def upper_len(s,cut):
    if isinstance(s,str): # checa se é str
        print(':: ' + s.upper()[:cut],sep=',')
    else:
        pass # não faz nada


# In[229]:


from random import randint

abc = ['alfa', 'bravO', 'chARlie', 230, 111.222]

# fatiamento aleatório
for s in abc:
    upper_len(s,randint(0,7)) 


# Comentários: 
# 
# - Esta função aceita strings, formatam-nas em maiúsculas e  imprime-as fatiadas até o índice `cut`, determinado aleatoriamente.
# - Note que nada é impresso para entradas que são números.
# - A função possui dois argumentos posicionais, isto é que obedecem às posições especificadas.
# - Se as posições dos argumentos forem alteradas, o sentido da função muda.

# In[196]:


# Nada faz porque o primeiro 
# parâmetro deixou de ser str
for s in abc:
    upper_len(randint(1,3),s) 


# **Exemplo:** especificando argumentos com _keywords_.

# In[192]:


# declaração com 3 keywords
def triple(x=0,y=0,z=0):
    return x*y*z


# In[193]:


# padrão
triple()


# In[197]:


# sem declarar keywords
triple(2,3,4)


# In[199]:


# declarando uma keyword
triple(3,4,z=4)


# In[200]:


# erro!
triple(x=3,4,4)


# Discussão: 
# - Argumentos com _keyword_ devem vir **após** os argumentos posicionais, se houver algum.

# In[202]:


# declaração com 1 posicional e 2 keywords
def triple_2(x,y=0,z=0):
    return x*y*z


# In[209]:


triple_2(2,y=5,z=3)


# In[210]:


triple_2(2,5,z=3)


# In[212]:


# declaração com 2 posicionais e 1 keyword
def triple_3(x,y,z=0):
    return x*y*z


# In[216]:


triple_3(3,1,2)


# In[217]:


triple_3(3,1,z=2)


# #### Funções anônimas
