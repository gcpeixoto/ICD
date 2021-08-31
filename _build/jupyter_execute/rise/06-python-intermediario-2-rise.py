#!/usr/bin/env python
# coding: utf-8

# # Python intermediário - II

# ## Funções
# 
# - Fundamentais para organizar e reutilizar código. 
# - Em Python, são _objetos de primeira classe_, i.e. podem ser:
#     1. atribuídas a uma variável ou elemento em uma estrutura de dado; 
#     2. passadas como argumento para outra função;
#     3. retornadas como resultado de uma função.

# ### Tipos de funções 
# 
# Neste curso, separaremos as funções em três grupos:
# 
# - _predefinidas_ (_built-in functions_): aquelas pré-existentes no _core_ da linguagem ou em outros módulos;
# - _regulares_ (_user-defined functions_): aquelas definidas por você que possuem um nome definido (UDFs);
# - _anônimas_ (_lambdas_): funções, em geral, criadas por você que não exigem um nome.

# #### Funções predefinidas
# 
# Exploraremos exemplos com funções _built-in_ do _core_ Python.

# In[49]:


# built-in functions
hex(1234),bin(345),round(12.3456,3)


# Discussão: 
# 
# - `hex` converte um número para hexadecimal, indicado pelo prefixo `0x`.
# 
# - `bin` converte um número para binário, indicado pelo prefixo `0b`.
# 
# - `round(x,n)` arredonda um número `x` em `n` dígitos de precisão. Se `n < 0`, retorna `0.0`. 

# In[58]:


# built-in function
for i in range(600,700,10):
    print(chr(i),end=',')


# Discussão: 
# 
# - `chr` retorna o caracter Unicode correspondente ao número inteiro passado, desde que esteja no intervalo [0,1114111].

# **Exemplo**: somando números em uma lista.

# In[61]:


sum(range(100)), sum([]) 


# Discussão: 
# - `sum` é uma função predefinida aplicável a sequências iteráveis.
# - Se o iterável for vazio, `sum` retorna zero.
# - No exemplo anterior, somamos os números de 0 a 100 e aplicamos a função a uma lista vazia.

# **Exemplo**: número de elementos em iteráveis.

# In[65]:


# no. de elementos
len([1,4,5])


# In[68]:


# conta keys
len({'a':1,'b':2}) 


# In[69]:


# lembre da unicidade
# 3 elementos no conjunto
len({1,3,1,2})


# In[71]:


# conta caracteres
len('nome')


# #### Funções regulares
# Possuem um nome definido pelo usuário.

# In[79]:


def cm_to_inch(x):
    """converte número de centímetros para polegadas"""
    return 2.45*x


# Comentários: 
# 
# - Funções regulares são declaradas com a _keyword_ `def` e valores de retorno com a _keyword_ `return`.

# In[93]:


# chamada simples
cm_to_inch(12.0)


# In[96]:


# atribuindo em objeto
cmi = cm_to_inch


# In[98]:


# usando como argumento de outra função
def fn(n,f):
    """Calcula f(n) dados n e uma função f."""
    return f(n)

fn(2,cm_to_inch)


# In[100]:


# docstring da função
fn.__doc__


# Parâmetros de funções podem assumir um argumento padrão que pode ser modificado sempre que necessário. 
# 
# **Exemplos:**

# In[133]:


# 'BEGIN' é valor padrão
def line(title='BEGIN'):
    print(title.center(21,'-'))    


# In[139]:


# especificação não necessária
line()


# In[138]:


# alterando padrão
line('HEAD')


# **Exemplo:** função com argumentos posicionais.

# In[227]:


# função com 2 argumentos posicionais
def upper_len(s,cut):
    if isinstance(s,str): # checa se é str
        print(':: ' + s.upper()[:cut],sep=',')
    else:
        pass # não faz nada


# In[206]:


from random import randint

abc = ['alfa', 'bravO', 'chARlie', 230, 111.222]

# fatiamento aleatório
for s in abc:
    upper_len(s,randint(0,7)) 


# Comentários: 
# - Função formatam strings em maiúsculas e  imprime-as fatiadas até o índice `cut`, determinado aleatoriamente.
# - Nada é impresso para entradas que são números.
# - A função possui dois argumentos posicionais
# - Se as posições dos argumentos forem alteradas, o sentido da função muda.

# In[228]:


# Nada faz porque o primeiro 
# parâmetro deixou de ser str
for s in abc:
    upper_len(randint(1,3),s)  


# **Exemplo:** especificando argumentos com _keywords_.

# In[229]:


# declaração com 3 keywords
def triple(x=0,y=0,z=0):
    return x*y*z


# In[230]:


# padrão
triple()


# In[231]:


# sem declarar keywords
triple(2,3,4)


# In[232]:


# declarando uma keyword
triple(3,4,z=4)


# In[235]:


# erro!
triple(x=3,4,4) 


# Discussão: 
# - Argumentos com _keyword_ devem vir **após** os argumentos posicionais, se houver algum.

# In[237]:


# declaração com 1 posicional e 2 keywords
def triple_2(x,y=0,z=0):
    return x*y*z


# In[238]:


triple_2(2,y=5,z=3)


# In[239]:


triple_2(2,5,z=3)


# In[240]:


# declaração com 2 posicionais e 1 keyword
def triple_3(x,y,z=0):
    return x*y*z


# In[241]:


triple_3(3,1,2)


# In[242]:


triple_3(3,1,z=2)


# ##### Escopos
# 
# Funções podem acessar variáveis em dois escopos: _global_ e _local_. O escopo global é aquele que está fora do escopo da função, enquanto o local é aquele determinado pela função.

# In[250]:


a = 0 # global
def test_vars(a):
    b = 1 # local    
    return a + b
    
print(test_vars(a)) 
print(b) # erro! b é local


# Comentários: 
# - A variável `a` é definida globalmente e foi utilizada como argumento de `test_vars`;
# - A variável `b` é definida localmente e, portanto, não pode ser acessada fora do escopo da função;
# - Um erro de "variável indefinida" é lançado por `print(b)`, visto que o escopo global não reconhece a variável `b`.

# In[252]:


def test_vars(a):
    global c     
    c = 1 # global
    return a + c
    
print(test_vars(a))
print(c) # ok! c é global


# Comentários: 
# - Neste caso, a `c` foi atribuído um valor no escopo local, porém ela foi declarada como global.
# - Para tornar uma variável dentro do escopo de uma função como global, usa-se a keyword `global`.
# - A impressão do valor de `c` no escopo global não retorna erro pela explicação anterior.

# > O uso indiscriminado de `global` não é encorajado. Quando a densidade do uso de `global` está alta, recomenda-se partir para uma abordagem de orientação a objetos e usar classes.

# #### Funções anônimas
# 
# - Uma função anônima não tem um nome explicitamente definido. 
# - Pode ser criada em apenas uma linha de código para executar uma tarefa específica.
# 
# > São baseadas na palavra-chave `lambda`, inspirada em uma área da ciência da computação chamada de cálculo-$\lambda$. Embora possam ser chamadas isoladamente, seu melhor uso é como argumento de uma função. 

# **Exemplo:**

# In[255]:


square = lambda x: x**2 
[square(x) for x in [2,3,4]]


# Comentários:
# 
# - `square` é um objeto `function` (verifique com `type(square)`.
# - Esta função anônima eleva um número passado ao quadrado.

# **Exemplo:**

# In[269]:


def op_to_list(lista,f):
    return [f(x) for x in lista]

op_to_list([2,3,4],lambda x: x**2)


# Discussão:
# - Esta construção produz um resultado equivalente ao anterior.
# - Neste exemplo, a função anônima é passada como argumento para ser aplicada à lista.

# **Exemplo:**

# In[270]:


# f(x) = x**3 - 4
op_to_list([2,3,4], lambda x: x**3 - 4)


# **Exemplo:**

# In[273]:


# separa nome e sobrenome, 
# e cria um user
op_to_list(['Aldo Bermudes',
            'Vicário Sempernaum',
            'Sebastian Folcher'], 
          lambda x: (x.split(' '),
                     x.lower().replace(' ','.')))


# > Nota: o abuso de _lambdas_ pode ser prejudicial à legibilidade de código. Use-as com moderação!

# **Exemplo:**

# In[277]:


frutas = ['melão','melancia','abacate',
          'morango','romã','banana']

sorted(frutas,key=lambda x: x[::-1])


# Discussão:
# - `x[::-1]`faz um swap na string;
# - A função _lambda_ passada como _key_ permite que os elementos da lista sejam ordenados com base na **soletração invertida** delas. 

# ### `map`
# 
# A função `map` serve para construir uma função que será aplicada a todos os elementos de uma sequência.

# **Exemplo:**

# In[279]:


list(map(lambda x: x**2,[2,3,4]))


# A conversão de `map` para um `list` é importante, pois o uso solitário de `map` produzirá uma resposta abstrata. 

# In[280]:


map(lambda x: x**2,[2,3,4]) 


# **Exemplo:**

# In[282]:


frutas = ['melão','melancia','abacate',
          'morango','romã','banana']

tuple(map(lambda x: x[::-1],frutas))


# Comentários:
# - O `map` é utilizado para realizar um swap nas strings.
# - Em seguida, realizamos uma conversão do `map` em um tupla.

# ### `filter`
# 
# - Podemos aplicar uma espécie de “filtro” para valores usando a função `filter`.
# - Em geral, definimos uma função _lambda_ para este propósito.

# In[377]:


from random import randint 

nums = []
for _ in range(15):
    nums.append(randint(0,30))

f = filter(lambda x: x < 20,nums)
list(f)


# #### Funções de ordem superior
# 
# - A partir da introdução de compreensões de lista, `map` e `filter` passaram a ser menos importantes. 
# 
# > `map`, `filter`, `reduce` e `apply` são funções de _ordem superior_. Todas são menos frequentes em Python 3 devido à aparição de métodos mais "modernos" para realizar o que elas fazem. 

# ### `args` e `kwargs`
# 
# - Úteis para construir uma função que requeira um número arbitrário de argumentos. 
# - Situação ocorre quando o usuário tem ampla liberdade para configurar algo. 
# - Desempacotamento por _star expression_. 

# Um resumo da aplicação delas é o seguinte:
# 
# - `*args` é **uma tupla** e utilizada para substituir um número arbitrário de argumentos posicionais.
# - `**kwargs`é **um dicionário** e utilizada para substituir um número arbitrário de _keywords_ e seus valores correspondentes.

# **Exemplo:** função que aceita um número arbitrário de argumentos de entrada.

# In[390]:


def media_arit(*vals):
    return sum(vals)/len(vals)

print(media_arit(1,3))
print(media_arit(1,2,4,5))
print(media_arit(1,2,4,5,7,9,10))


# Discussão:
# - `*vals` recebe, em cada caso, os argumentos de entrada. No primeiro caso, 2; no segundo, 4; no terceiro, 7.

# **Exemplo:** equação de combinação linear em $\mathbb{R}^n$ com coeficientes arbitrários.

# In[393]:


from IPython.display import display as dpl, Math

def comb_lin(*args):
    l = []    
    for i,c in enumerate(list(args)):
        l.append(str(c) + 'x_' + str(i+1))
        
    final = '$v = ' + ' + '.join(l) + '$'
    return final

v2 = comb_lin(1.4,4) 
dpl(Math(v2))

v4 = comb_lin(2,34,12,65.43)
dpl(Math(v4))


# Discussão:
# - A lista de coeficientes é percorrida com agregação dos termos $x_i$, para cada coordenada do espaço n-dimensional.
# - `dpl(Math(v4)` renderiza a equação.

# **Exemplo:** coleta de valores médios de áreas das superfícies radiculares de dentes humanos (em milímetros quadrados) por demanda.

# In[403]:


# dente: (area inf, area sup)
# Ver: https://bit.ly/3iT9tsA, p.37, Quadro 2.1
#dentes = {'Incisivo central':(170,230),
#          'Incisivo lateral':(194,200),
#          'Canino':(270,282),
#          'Primeiro molar':(475,533)}


def med_area_dent(**kwargs):
    for k,v in kwargs.items():
        print(f'Dente: {k} | Área inf: {v[0]} mm2 | Área sup: {v[1]} mm2 ')

        
med_area_dent(incisivo_cent=(160,200),
              incisivo_lat=(194,200))        


# In[397]:


med_area_dent(IC=(160,200),C=(270,882),PM=(475,533))        


# Discussão:
# 
# - `**kwargs` admite a entrada de um dicionário com tamanho variável. Isto é, chaves e valores quaisquer. 
# - Nestes exemplos, imprimimos os valores médidos de áreas dos radiculares.
# 
# > As `keywords` podem ter nomes diferentes!

# ### `any` e `all`
# 
# As funções predefinidas `any` e `all` são chamadas de "redutoras", visto que têm um papel relacionado à filtragem de dados. Elas são aplicáveis a qualquer sequência. Podemos entendê-las como segue: 
# 
# - `all`: retorna `True` se todo elemento do objeto iterável for avaliado com uma condição verdadeira.
# - `any`: retorna `True` se qualquer elemento do objeto iterável for avaliado com uma condição verdadeira.

# **Exemplo:**

# In[410]:


x = [2,-1,3,4]

all(list(map(lambda x: x < 0,x)))


# In[411]:


any(list(map(lambda x: x < 0,x)))


# In[413]:


x = [2,1,3,4]

all(list(map(lambda x: x > 0,x)))

