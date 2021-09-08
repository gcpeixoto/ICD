#!/usr/bin/env python
# coding: utf-8

# # Computação vetorizada

# ## Objetivos
# 
# - Compreender as capacidades da computação vetorizada;
# - Associar conceitos abstratos de Matemática a estruturas computacionais; 
# - Saber estruturar dados em arrays multidimensionais;

# ## Introdução
# 
# - Computação científica, problemas de alta complexidade e recursos computacionais. 
# - Resolução eficiente de problemas na ciência de dados
# - Computação vetorizada (arrays x listas)

# ## O pacote *numpy* 
# 
# - Biblioteca padrão em Python para trabalhar com *arrays* multidimensionais e computação vetorizada. 
# - Superpoderes às listas
# > A grande regra: _vetorize seus cálculos numéricos o máximo possível!_

# In[1]:


import numpy as np


# ## Motivação
# 
# Este exemplo compara a eficiência de operações feitas com listas comuns e com *numpy*.

# In[2]:


# 1 µs = 1/1e6 segundo
# 1 ns = 1/1e9 segundo

L = range(500)
get_ipython().run_line_magic('timeit', '-n 10 [i**2 for i in L] # executa o laço 10 vezes')

a = np.arange(500)
get_ipython().run_line_magic('timeit', '-n 10 a**2 # eleva ao quadrado diretamente 10 vezes')


# ## Criação de arrays unidimensionais (1D)

# In[3]:


a = [1,2,3]
np.array(a) # a partir de lista


# In[4]:


np.array([1,2,3]) # diretamente


# In[5]:


np.array([2]*5)


# ## Criação de arrays bidimensionais (2D)

# In[6]:


A = [ [1,2], [0,2] ] # lista de listas
np.array(A) # matrix 2 x 2


# In[7]:


np.array([ [1,2], [0,2] ]) # diretamente


# In[8]:


A2 = [[1,2,3],[4,3,2]] # cada lista é uma linha da matriz
np.array(A2) # matriz 2 x 3 


# In[9]:


np.array([1,1],[0,1]) # parênteses externos são obrigatórios! 


# ### Dimensão, formato e comprimento

# In[11]:


x = np.array(a)
np.ndim(x) # aplica a função ndim


# In[12]:


x.ndim # como método


# In[13]:


np.shape(x) # formato


# In[14]:


x.shape # sem parênteses


# In[15]:


len(x) # comprimento


# In[16]:


X = np.array(A)
np.ndim(X) # array bidimensional


# In[17]:


np.shape(X) 


# In[18]:


len(X) # apenas um comprimento. Qual?


# In[19]:


X2 = np.array(A2)
len(X2) # apenas da primeira dimensão. LINHAS


# In[20]:


X2.shape


# ## Funções para criação de arrays

# ### `arange`
# 
# **Exemplo:** crie um array de números ímpares positivos menores do que 36.

# In[21]:


np.arange(1,36,2) # start,stop,step


# **Exemplo:** crie um array de números pares positivos menores ou iguais a 62.

# In[22]:


np.arange(0,63,2)


# **Exemplo:** calcule o valor de $f(x) = x^3 + 2x$ para $x$ elementos dos arrays anteriores.

# In[23]:


imp, par = np.arange(1,36,2), np.arange(0,63,2)
f = lambda x: x**3 + 2
fi, fp = f(imp), f(par)
print(fi)
print(fp)


# ### `linspace`
# 
# **Exemplo:** crie um array igualmente espaçado de elementos em [0,1] com 11 elementos.

# In[24]:


np.linspace(0,1,num=11)


# In[25]:


np.linspace(0,1,11) # 'num' pode ser omitido


# In[26]:


x = np.linspace(0,1,10,endpoint=False) # exclui último
x


# In[27]:


y = np.arange(0,1,0.1) # equivalente
y


# In[28]:


x == y # comparação é elemento a elemento


# In[29]:


x == -y # apenas 0 é True


# In[30]:


x[1:] == y[1:]


# ### `all` e `any`

# In[31]:


np.all( x == y ) # verifica se todos são 'True'


# In[32]:


np.any( x == -y ) # verifica se pelo menos um é 'True'


# ### `random`
# 
# **Exemplo**: crie um *array* 1D com 5 números aleatórios entre [0,1].

# In[33]:


r = np.random.rand(5)
r


# **Exemplo**: crie um *array* 1D com 50 números inteiros aleatórios entre [0,7].

# In[34]:


r2 = np.random.randint(0,7+1,50) # menor, maior é 8 (exclusive), tamanho
r2


# **Exemplo**: crie uma matriz m x n com números inteiros aleatórios entre inteiros [l,h].

# In[35]:


def gera_matriz(m,n,l,h):
    return np.random.randint(l,h,(m,n)) # tupla (m,n)


# In[36]:


gera_matriz(2,2,0,4)


# In[37]:


gera_matriz(3,2,0,4)


# In[38]:


gera_matriz(4,4,-2,7)


# ### `ones`
# 
# Criando arrays unitários.

# In[39]:


np.ones(4) 


# In[40]:


np.ones((3,2)) # tupla necessária para linhas e colunas


# ### `eye`
# 
# Criando arrays 2D identidade. 1 na diagonal e 0 nas demais.

# In[41]:


np.eye(3) # matriz identidade 3 x 3 


# ### `zeros`
# 
# Arrays nulos.

# In[42]:


np.zeros(3)


# In[43]:


np.zeros((2,4)) # 2 x 4


# ### `full`
# 
# Arrays de valor constante.

# In[44]:


np.full(3,0) # 1 x 3 com constante 0


# In[45]:


np.full(shape=(3,),fill_value=0)


# In[46]:


F1 = np.full(shape=(2,2),fill_value=1) # 2 x 2 com 1
F1


# In[47]:


F1 == np.ones(2) # mesmo resultado que ones


# Outras maneiras:

# In[48]:


F2 = 3*np.ones((4,4))
F2


# ## Especificando tipos de dados 
# 
# Observe o seguinte exemplo:

# In[49]:


F2


# In[50]:


F3 = np.full((4,4),3)
F3


# In[51]:


F2 == F3 # valores iguais


# In[52]:


F2.dtype == F3.dtype # tipos diferentes


# In[53]:


F2.dtype


# In[54]:


F3.dtype


# Especificamos o tipo de dados com `dtype`.

# In[55]:


np.ones((4,2),dtype=bool) # matriz de booleanos


# In[56]:


np.ones((4,2),dtype=str) # matriz de strings; 'U1' diz que há no máximo 1 caracter


# In[57]:


S = np.array(['dias','mes','ano'])
S.dtype # 4 é o no. máximo de caracteres nas strings


# ## Indexação e fatiamento
# 
# Funcionam de maneira similar ao uso com listas.

# In[58]:


I = np.linspace(0,20,11)
I


# In[59]:


I[3],I[2:4],I[5:8],I[-4:-1]


# In[60]:


I[::-1] # invertendo o array


# In[61]:


I2 = np.array([I,2*I,3*I,4*I])
I2


# Em arrays bidimensionais, a indexação é feita por meio de uma tupla. Porém, a explicitação dos parênteses é desnecessária.

# In[62]:


I2[(2,3)] # 3a. linha; 4a. coluna


# In[63]:


I2[2,3]


# In[64]:


I2[0,:] # 1a. linha


# In[65]:


I2[1,:] # 2a. linha


# In[66]:


I2[-1,:] # última linha


# In[67]:


I2[:,0] # 1a. coluna


# In[68]:


I2[:,1] # 2a. coluna


# In[69]:


I2[:,8] # 9a. coluna


# In[70]:


I2[:,2:4] # 3a. - 4a. coluna


# In[71]:


I2[1:3,6:10] # submatriz: linhas 2 - 3; 7-10


# ### Alteração de valores
# 
# Os arrays são mutáveis por indexação.

# In[72]:


A3 = np.random.rand(4,4)
A3


# In[73]:


A3[0:4,0] = -1
A3


# In[74]:


A3[:,-1] = -1
A3


# In[75]:


A3[1:3,1:3] = 0
A3


# Podemos alterar valores com arrays.

# In[76]:


A3[1,:] = -2*np.ones(4)
A3


# A indexação pode usar um comprimento de passo (*step*).

# In[77]:


A3[0:4:3,1:3] = np.full((1,2),8) # na indexação esquerda, 1a. linha : 4a. linha : step de 3
A3


# ### `newaxis`
# 
# `newaxis` é uma instância do `numpy` que permite aumentar de 1 a dimensão de um array existente. 

# **Exemplo:** como inserir a diagonal de uma matriz em uma segunda matriz como uma coluna adicional?

# Criamos duas matrizes aleatórias.

# In[78]:


# matriz 4 x 4 de inteiros aleatórios entre 0 e 9
B1 = np.random.randint(0,10,(4,4)) 
B1


# In[79]:


# matriz 4 x 4 de inteiros aleatórios entre -10 e 9
B2 = np.random.randint(-10,10,(4,4)) 
B2


# Extraímos a diagonal da primeira.

# In[80]:


# diagonal de B1
db1 = np.diag(B1)
db1


# Notemos agora que as dimensões são diferentes.

# In[81]:


print(B2.ndim)
print(db1.ndim)


# Para podermos aglutinar a diagonal como uma nova coluna na primeira matriz, primeiro temos que transformar o array unidimensional para uma matriz.  

# In[82]:


db1 = db1[:,np.newaxis]
print(db1.ndim) # agora o array é bidimensional
db1 


# `newaxis` é um "eixo imaginário" incluído *inplace*, mas que altera dinamicamente o array. No caso acima, o array tornou-se em uma coluna.

# Agora, podemos "colar" um array 2D com outro por uma concatenação. 

# ### `concatenate`
# 
# `concatenate` é usado para concatenar *arrays*. A concatenação requer uma tupla contendo os *arrays* a concatenar e o eixo de referência.

# In[83]:


B3 = np.concatenate((B2,db1), axis=1) 
B3


# No caso acima, `axis=1` indica que a concatenação é ao longo da coluna. Dessa forma, inserimos a segunda diagonal como uma coluna adicional na segunda matriz. Claramente, isto só é possível porque ambas as matrizes eram de mesmo formato.

# #### `axis`
# 
# Nos arrays multidimensionais do Python, `axis` é usado para indicar a "direção" dos dados. Em arrays bidimensionais, `axis=0` refere-se à direção de cima para baixo (ao longo das linhas), ao passo que `axis=1` refere-se à direção da esquerda para a direita (ao longo das colunas). 
# 
# **Obs.:** note que a palavra `axis` ("eixo") deve ser usada, e não "axes" ("eixos").

# Para aglutinar uma linha na matriz anterior, fazemos uma concatenação em linha.

# In[84]:


# array de zeros com mesmo número de colunas de B3
db2 = np.zeros(np.shape(B3)[1]) 
db2


# In[85]:


db2 = db2[np.newaxis,:] # cria o "eixo imaginário" na direção 0


# In[86]:


B4 = np.concatenate((B3,db2),axis=0) # concatena ao longo das linhas
B4


# ## Indexação avançada
# 
# Podemos usar máscaras como artifícios para indexação avançada.

# In[87]:


IA1 = np.arange(-10,11)
IA1


# Vamos criar um *array* aleatório de True e False no mesmo formato que o *array* anterior.

# In[88]:


mask1 = np.random.randint(0,2,np.shape(IA1),dtype=bool) 
mask1 


# Esta *máscara booleana* pode ser aplicada no array para extrair apenas os elementos cujos índices são marcados como `True` pela máscara.

# In[89]:


IA1[mask1]


# Há maneiras mais diretas aplicáveis a filtragens. Para extrair os valores negativos do array:

# In[90]:


IA1 < 0 # máscara booleana


# In[91]:


IA1[IA1 < 0] 


# Para extrair os valores positivos do array:

# In[92]:


IA1[IA1 > 0] # máscara booleana para positivos


# Para extrair os valores no intervalo $]-2,5[$, fazemos:

# In[93]:


IA1[(IA1 > -2) & (IA1 < 5)] # & é o operador booleano 'elemento a elemento'


# Para extrair pares e ímpares, poderíamos fazer:

# In[94]:


pares, impares = IA1[IA1 % 2 == 0] , IA1[IA1 % 2 == 1] 
pares,impares 


# Podemos usar listas como máscaras:

# In[95]:


alguns = pares[[0,2,3,5]] # acessa 1o., 3o. 4o. e 6o. elemento de 'pares'


# In[96]:


impares[alguns] # estude este caso


# No caso acima, por exemplo, -10 é uma indexação reversa que excede o compriemento do array à esquerda. Portanto, ele retorna o primeiro elemento do array, que é -9. O índice -6 acessa o sexto elemento a partir da direita, que é -1. O índice -4 acessa o quarto elemento a partir da direita. Por fim, o índice 0 acessa o primeiro elemento que é -9. 

# ## Operações elemento a elemento
# 
# As operações aritméticas e de cálculo são feitas elemento a elemento nos *arrays*. Já mostramos alguns exemplos acima, mas vamos tornar isto mais claro aqui.

# In[97]:


a = np.array([1,2,3]) 
b = np.array([4,5,6])


# In[98]:


# operações elemento a elemento
print(a + b) 
print(a - b) 
print(a * b) 
print(a / b)
print(a ** b)


# In[99]:


2*a + 4*b - 6*b**2 + 1.1/2*a


# ## Funções matemáticas
# 
# O `numpy` possui a maioria dass funções disponíveis no módulo `math` e outras mais. As funções são diretamente aplicáveis aos *arrays*. Lembre-se que para fazer o mesmo usando em listas, tínhamos de construir meios de iterar sobre elas e aplicar a função a cada elemento por vez. Isto não é mais necessário com o `numpy`. Eis a beleza da computação vetorizada!
# 
# Vejamos uma série de exemplos.

# In[100]:


x = np.arange(10)
x


# In[101]:


np.sqrt(x)


# In[102]:


np.cos(x) + 2*np.sqrt(x)


# In[103]:


y = np.sin(2*x)
z = np.exp(x + y)
y - z


# ## *Broadcasting*
# 
# *Broadcasting* é a capacidade que o *numpy* oferece para realizarmos operações em arrays com diferentes dimensões.

# ### Regras do *broadcasting* 
# 
# 1. Se dois *arrays* tiverem dimensões diferentes, o formato do array com menor dimensão é preenchido por 1 do lado esquerdo.
# 2. Se o formato dos *arrays* não for igual em dimensão alguma, o array com tamanho igual a 1 é esticado nesta direção para ficar no mesmo tamanho correspondente do outro array.
# 3. Se em qualquer direção os tamanhos dos *arrays* forem diferentes e nenhum deles for igual a 1, então um erro é retornado.

# #### Exemplo da Regra 1

# In[104]:


A = np.array([[1, 2, 3],[4, 5, 6]]) # array 2D
b = np.array([10, 20, 30]) # array 1D
print(A.shape)
print(b.shape)


# In[105]:


A + b


# A soma pode ser realizada mesmo assim. O que ocorreu? Cada linha de `A` foi somada à única linha de `b`. O *broadcasting* amplia o array de menor dimensão automaticamente da seguinte forma:
# 
# Pela regra 1, o *array* `b` tem dimensão menor. Então, ele é preenchido de modo que:
# 
# ```python
# A.shape -> (2, 3)
# b.shape -> (1, 3)
# ```
# 
# Pela regra 2, a primeira dimensão de `A` é 2 e a de `b` é 1. Então, a dimensão de `b` é "esticada", de modo que:
# 
# ```python
# A.shape -> (2, 3)
# b.shape -> (2, 3)
# ```

# A mesma operação poderia ter sido feita com:

# In[106]:


A + np.array([b,b])


# #### Exemplo da Regra 2

# In[107]:


A = np.arange(3).reshape((3, 1))
b = np.arange(3) 
print(A.shape)
print(b.shape)


# In[108]:


A + b


# Neste caso, ambos os arrays sofrem *broadcasting*. Ele ocorre da seguinte forma.
# 
# Como 
# 
# ```python 
# A.shape = (3, 1)
# b.shape = (3,)
# ```
# a regra 1 diz que `b` deve ser preenchido de modo que
# 
# ```python
# A.shape -> (3, 1)
# b.shape -> (1, 3)
# ```
# e, pela regra 2, cada uma das dimensões 1 deve ser alterada de modo que:
# 
# ```python
# A.shape -> (3, 3)
# b.shape -> (3, 3)
# ```
# 
# Assim, o *broadcasting* é permitido.

# #### Exemplo da Regra 3

# In[109]:


A = np.ones((3, 2))
b = np.arange(3)
print(A.shape)
print(b.shape)


# In[110]:


A + b


# Neste exemplo, o *broadcasting* não é permitido. O caso é levemente diferente do primeiro exemplo em que `A` é transposta.
# 
# Temos que 
# 
# ```python 
# M.shape = (3, 2)
# a.shape = (3,)
# ```
# 
# Pela regra 1, devemos ter
# 
# ```python
# M.shape -> (3, 2)
# a.shape -> (1, 3)
# ```
# 
# e, pela regra 2, a primeira dimensão deve ser esticada para combinar-se com a de `A` enquanto a segunda não é alterada por não ser 1.
# 
# ```python
# M.shape -> (3, 2)
# a.shape -> (3, 3)
# ```
# Porém, o formato final de ambos não se combina. Sendo incompatíveis, o *broadcasting* falha.
