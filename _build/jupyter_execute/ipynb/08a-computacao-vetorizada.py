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
# A computação científica é uma ciência interdisciplinar que procura resolver problemas de alta complexidade utilizando recursos computacionais. Ao longo das décadas, a capacidade de processamento computacional aumentou dramaticamente. Em junho de 2020, o site [[Top500]](https://www.top500.org/news/japan-captures-top500-crown-arm-powered-supercomputer/), que atualiza semestralmente a lista dos computadores mais potentes do mundo, divulgou que o primeiro da lista agora é o Fugaku, um computador de alto desempenho japonês capaz de realizar 415,5 petaflops no teste de referência Linpack para medição de desempenho. Se um petaflop já equivale à impressionante marca de um quadrilhão ($10^{15}$) de operações numéricas executadas por segundo, o que dizer de 415,5 vezes isto?! É realmente um número inimaginável. Para saber mais sobre medidas utilizadas na computação de alto desempenho, veja esta página da [[Universidade de Indiana]](https://kb.iu.edu/d/apeq).
# 
# Todo este potencial serve para resolver problemas de engenharia, das ciências da saúde, das ciências atmosféricas, de energia, entre tantas outras áreas. Por outro lado, a computação científica depende de algoritmos e projetos de software otimizados e bem construídos para atingir cada vez mais eficência, portabilidade e facilidade de execução. Em ciência de dados, embora o foco não seja resolver problemas utilizando os mesmos moldes da computação científica, devemos ter em mente que grande parte das ferramentas computacionais que permitem que um problema da ciência de dados seja resolvido deve-se a um trabalho muito minucioso de cientistas da computação e engenheiros que trabalham em nível de hardware. E é aí que entra a *computação vetorizada*.
# 
# O conceito de *computação vetorizada*, ou *computação baseada em arrays* está relacionado à execução de operações que podem ser feitas de uma só vez a um conjunto amplo de valores. Até agora, vimos no curso, por exemplo, que podemos percorrer uma lista de números inteiros e calcular o quadrado desses números um de cada vez utilizando um laço, ou mesmo realizando um mapeamento. A computação vetorizada, por outro lado, evita que tais operações dependam de laços e iterações. Com ela, podemos simplesmente aplicar uma função ao *array* (uma coleção de dados) inteiro de uma só vez e produzir um *array* com o resultado desejado diretamente. Ou seja, a ideia principal da computação vetorizada é evitar laços e cálculos com repetições a fim de acelerar operações matemáticas. O nome *vetorizada* está relacionado a *vetor*. Como veremos aqui, estruturas multidimensionais e, mais geralmente, *arrays*, identificam-se com a nossa compreensão de vetores, matrizes e tensores. 
# 
# Vetores são arrays unidimensionais. Matrizes são arrays bidimensionais. Tensores são arrays de três ou mais dimensões. Todavia, é importante salientar que o conceito de "dimensão" em *computação vetorizada* deve ser distinguido da ideia mais abstrata de dimensão como você estudadará em Cálculo Vetorial, Geometria Analítica ou Álgebra Linear. *Arrays* possuem alguns atributos, tais como "comprimento", "formato" e "dimensão, os quais dizem respeito, de certa forma, à quantidade de seus elementos e ao modo como ocupam a memória. Esses nomes variam de linguagem para linguagem. Em Python, existem funções e métodos específicos para verificar comprimento, formato e dimensão, tais como `len`, `shape` e `ndim`. As duas últimas serão apresentadas a seguir. Em outras linguagens, usa-se também `size` para desempenhar o mesmo papel que `shape`. A palavra "dimension", em Python, é encontrada de maneira explicativa em documentações. Para não confundir "comprimento", "formato" e "dimensão", redobre seu entendimento. 
# 
# ## Comprimento, tamanho e dimensão
# 
# Para exemplificar o que queremos dizer com "comprimento", "tamanho" e "dimensão", vejamos uma ilustração. Se $x_1$ e $x_2$ são dois números inteiros, a lista `[x1,x2]` seria um array unidimensional, mas de comprimento dois (você verifica isto com `len`). Agora, imagine que $(x_1,x_2)$ seja a notação matemática para representar as coordenadas de um ponto do plano cartesiano. Sabemos da geometria que o plano cartesiano tem duas dimensões. Porém, poderíamos, computacionalmente, usar a mesma lista anterior para armazenar no computador essas duas coordenadas. A lista continuaria sendo unidimensional, porém de tamanho dois. Logo, embora a entidade matemática seja bidimensional, não necessariamente a sua representação computacional deve ser bidimensional.
# 
# Vejamos outra ilustração. Uma esfera é um sólido geométrico. Cada ponto da esfera está no espaço tridimensional. Isto significa que precisamos de 3 coordenadas para localizar este ponto. Embora você talvez tenha estudado pouco ou nada sobre a geometria analítica em três dimensões, o exemplo que daremos aqui será simples. Do mesmo modo que o caso anterior, suponha você tenha não apenas $x_1$ e $x_2$ como dois números inteiros, mas também um terceiro, $x_3$, para montar as coordenadas do seu ponto espacial. Você poderia representá-lo, matematicamente, por uma tripleta $(x_1,x_2,x_3)$ sem problema algum. Por outro lado, no computador, a lista `[x1,x2,x3]` seria um *array* adequado para armazenar os valores das suas coordendas. Entretanto, esta lista continuaria sendo um array unidimensional, mas com tamanho 3. Portanto, *arrays* unidimensionais podem representar dados em dimensões maiores do que um.
# 
# Vejamos outra ilustração. Uma matriz 2 x 2 pode ser escrita, em matemática, utilizando 4 números da seguinte forma:
# 
# $$\begin{bmatrix}
# a_{11} & a_{12}\\
# a_{21} & a_{22}
# \end{bmatrix}$$
# 
# Uma matriz é um *array* formado por outros *arrays*. Usando listas, a construção anterior poderia ser representada, no computador, por exemplo, com a lista de listas `[[a11,a12],[a21,a22]]`. Porém, teríamos que ter total controle sobre isto para poder dizer que `[a11,a12]` é a primeira linha da matriz e que `[a21,a22]` é a segunda linha. Neste exemplo, a matriz é uma entidade matemática caracterizada como bidimensional por ser um "retângulo (ou quadrado) cheio de números" , mas para a Python, ela deve ser um *array bidimensional* basicamente porque existem "duas direções" nos dados: linhas e colunas. Agora, você consegue imaginar o que seria uma matriz de matrizes? 
# 
# Imagine duas folhas de papel A4 postas uma sobre a outra em uma mesa. Agora, pense como se cada folha de papel fosse uma matriz. No final das contas, você tem uma "caixa com matrizes dentro". Isto é o que seria um tensor, uma "caixa de números", embora, física e matematicemente, não seja esta a definição. Uma matriz de matrizes é um *array tridimensional*. Se as suas duas matrizes fossem idênticas e iguais à do exemplo acima, você teria duas listas de listas `[[a11,a12],[a21,a22]]`, quatro listas (2 iguais a `[a11,a12]` e 2 iguais a `[a21,a22]`) e uma superlista com duas listas de listas dentro! 
# 
# Como veremos adiante, o *numpy* é a ferramenta ideal para lidar com tudo isso. 
# 
# 
# ## O pacote *numpy* 
# 
# O *numpy* é a biblioteca padrão em Python para trabalhar com *arrays* multidimensionais e computação vetorizada. Ela praticamente dá "superpoderes" às listas e permite que trabalhemos com cálculos numéricos de maneira ágil, simples e eficiente. Com *numpy*, também podemos ler e escrever arquivos, trabalhar com sistemas lineares e realizar muito mais. Para importar o numpy use a instrução abaixo, onde `np` é um alias padrão:
# 
# ```python
# import numpy as np
# ```
# 
# Nesta aula, daremos uma introdução aos aspectos elementos do *numpy* para criar e manipular *arrays* multdimensionais. A grande regra é: vetorize seus cálculos numéricos o máximo possível!

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


gera_matriz(2,2,0,1)


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


# ### Problema resolvido (Laboratório Computacional 1C)

# Observe a tabela a seguir, onde **DS (UA)** é a distância do referido planeta do até o Sol em unidades astronômicas (UA), **Tm (F)** sua temperatura superficial mínima em graus Farenheit e **TM (F)** sua temperatura superficial máxima em graus Farenheit.
# 
# | | DS (UA) | Tm (F) | TM (F) | DS (km) | TmM (C) |
# |--|--|--|--|--|--|
# Mercúrio | 0.39 | -275 | 840 | ? | ? |
# Vênus | 0.723 | 870 | 870 | ? | ? |
# Terra | 1.0 | -129 | 136 | ? | ? |
# Marte | 1.524 | -195 | 70 | ? | ? |
# 
# 
# 
# - Escreva um código para converter a temperatura dos planetas de graus Farenheit (**F**) para Celsius (**C**).
# 
# - Escreva um código para converter unidades astronômicas em quilômetros.
# 
# - Imprima os valores que deveriam ser inseridos na coluna **DS (km)** horizontalmente usando `print`.
# 
# - Repita o item anterior para a coluna **TmM (C)**, que é a média aritmética entre **Tm** e **TM**.
#     
#     
# *Observação:* use notação científica (exemplo: $4.2 \times 10^8$ pode ser escrito como `4.2e8` em Python).

# #### Resolução
# 
# Há várias maneiras de resolver. Aqui apresentamos uma estratégia com `lambdas`.
# 
# - Montar os arrays dos dados numéricos.

# In[104]:


DS = np.array([0.39,0.723,1.0,1.524])
Tm = np.array([-275,870,-129,-195])
TM = np.array([840,870,136,70])


# - Fórmula e cálculo da conversão Farenheit para Celsius:

# In[105]:


C = lambda F: 5/9*(F-32)
CTm = C(Tm)
CTM = C(TM)
print(CTm) # minimas em C
print(CTM) # maximas em C


# - Fórmula e cálculo da conversão UA para km:

# In[106]:


UA = lambda km: 1.496e+8*km 
UADS = UA(DS) 
print(UADS) # valores a inserir


# - Cálculo da média

# In[107]:


TmM = 0.5*(CTm + CTM)
print(TmM)


# ### `reshape` e `hstack`
# 
# A montagem do array bidimensional com os cálculos resultantes não foi requisitada no problema. Porém, vamos mostrar uma maneira de fazer isto usando `reshape`, que é uma função utilizada para reformatar os dados e `hstack`, que é usada para "empilhar" arrays horizontalmente.
# 
# Note que todos os nossos *arrays* são unidimensionais. Vamos torná-los bidimensionais com formato 4 x 1 e empilhá-los horizontalmente, isto é, na direção do eixo 1 (esquerda para direita). 
# 
# **Obs:** consulte também `vstack`.

# In[108]:


todos = [DS,CTm,CTM,UADS,TmM] # lista com todos os arrays

for i,ar in enumerate(todos):
    todos[i] = np.reshape(ar, (4,1)) # reformata

final = np.hstack(todos) # empilha


# Explicando o que fizemos: 
# 
# - Colocamos todos os arrays em uma lista: neste ponto, nada novo.
# - Iteramos sobre a lista, reformatamos um por um e reatribuímos na mesma lista como arrays bidimensionais
# 
# Para o segundo ponto, observe:

# In[109]:


DS.shape # formato é 1 x 4 (unidimensional)


# In[110]:


np.reshape(DS,(4,1)) # reformata 


# In[111]:


np.reshape(DS,(4,1)).shape # novo formato é 4 x 1


# In[112]:


np.reshape(DS,(4,1)).ndim # o array agora é bidimensional


# Procedendo assim para todos, conseguimos reformatá-los e adicioná-los em uma lista. Se desejarmos, podemos sobrescrever essa lista ou não. Na resolução anterior, escolhemos sobrescrever. Assim, suponha que a lista dos arrays reformatados seja:

# In[113]:


L = [np.reshape(DS,(4,1)),np.reshape(TmM,(4,1))] # apenas DS e TmM
L


# - Criamos o array final por empilhamento.

# Note que a lista `L` possui 2 arrays de formato 4 x 1. Para criar o array 4 x 2, faremos um empilhamento horizontal similar à uma concatenação na direção 1. 

# In[114]:


Lh = np.hstack(L)
Lh


# Agora podemos verificar que, de fato, o array está na forma como queremos. 

# In[115]:


Lh[:,0] # 1a. coluna idêntica à DS


# In[116]:


Lh[:,0] == DS # teste


# In[117]:


np.all( Lh[:,0] == DS ) # teste completo


# In[118]:


Lh[:,1] # 2a. coluna idêntica a TmM


# In[119]:


Lh[:,1] == TmM # teste


# In[120]:


np.all( Lh[:,1] == TmM ) # teste completo


# ## *Broadcasting*
# 
# *Broadcasting* é a capacidade que o *numpy* oferece para realizarmos operações em arrays com diferentes dimensões.

# ### Regras do *broadcasting* 
# 
# 1. Se dois *arrays* tiverem dimensões diferentes, o formato do array com menor dimensão é preenchido por 1 do lado esquerdo.
# 2. Se o formato dos *arrays* não for igual em dimensão alguma, o array com tamanho igual a 1 é esticado nesta direção para ficar no mesmo tamanho correspondente do outro array.
# 3. Se em qualquer direção os tamanhos dos *arrays* forem diferentes e nenhum deles for igual a 1, então um erro é retornado.

# #### Exemplo da Regra 1

# In[121]:


A = np.array([[1, 2, 3],[4, 5, 6]]) # array 2D
b = np.array([10, 20, 30]) # array 1D
print(A.shape)
print(b.shape)


# In[122]:


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

# In[123]:


A + np.array([b,b])


# #### Exemplo da Regra 2

# In[124]:


A = np.arange(3).reshape((3, 1))
b = np.arange(3)
print(A.shape)
print(b.shape)


# In[125]:


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

# In[126]:


A = np.ones((3, 2))
b = np.arange(3)
print(A.shape)
print(b.shape)


# In[127]:


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
