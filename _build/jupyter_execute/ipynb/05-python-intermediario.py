#!/usr/bin/env python
# coding: utf-8

# # Python intermediário - I

# ## Visão geral sobre sequencias
# 
# A linguagem Python oferece diversas estruturas de dados caracterizadas como sequencias. As sequencias são implementadas com eficiência nos moldes da linguagem C. 
# 
# Sequencias podem ser classificadas como: 
# 
# - _Sequências contêinerizadas_ (_container sequences_): guardam referências aos objetos que elas contêm, que podem ser de qualquer tipo. Exemplos são: `list`, `tuple` e `collections.deque`.
# 
# - _Sequências rasas_ (_flat sequences_): armazenam fisicamente o valor de cada item dentro de seu próprio espaço na memória, e não como objetos distintos. Exemplos são: `str`,`bytes` e `array.array`.
# 
# Sequências rasas são mais compactas do que as contêinerizadas, mas são limitadas para armazenar valores primitivos como caracteres, bytes e números. 
# 
# Outra forma de agrupar tipos de sequências é por mutabilidade: 
# 
# - _Sequências mutáveis_: podem ter seus elementos alterados. Exemplos: `list`,`bytearray`,`memoryview`.
# 
# - _Sequências imutáveis_: seus elementos são inalteráveis. Exemplos: `tuple`,`str`,`bytes`.

# ## Tuplas 
# 
# Tuplas são sequências imutáveis de comprimento fixo.

# **Exemplo:** Crie uma tupla com 4 elementos e desempacote-a em 4 variáveis.

# In[1]:


tup1 = -1,'a',12.23,'$'
a,b,c,d = tup1

tup2 = (-1,'a',12.23,'$')
e,f,g,h = tup2

print(tup1)
print(tup2)


# Discussão: 
# 
# - `tup1` é uma tupla criada pelo sequenciamento de elementos, sem parênteses.
# - `tup2` é uma tupla idêntica criada pelo sequenciamento de elementos, com parênteses.
# - Em `a`,`b`,`c`,`d` há um processo de desempacotamento (_unpacking_).
# - Em `e`,`f`,`g`,`h` temos um desempacotamento equivalente.
# - Ambas as tuplas são equivalentes.

# **Exemplo:** Crie uma tupla a partir de objetos existentes.

# In[2]:


tuple(tup1)


# Discussão: 
# 
# - Este processo é também conhecido como _type casting_.

# **Exemplo:** Construa tuplas aninhadas.

# In[3]:


nums = (0,2,4,6,8),(1,3,5,7,9)
nums


# **Exemplo:** Altere elementos de uma tupla _in-place_.

# In[4]:


t = tuple(['a',[1,2,3],False])

# imutabilidade!
t[2] = True


# In[5]:


# alteração in-place
t[1].append(4)
t


# Discussão: 
# 
# - A operação `t[2] = True` retorna um erro porque a tupla não pode ser alterada.
# - Por outro lado, a lista armazenada na segunda posição pode ser modificada _in-place_.

# **Exemplo:** Crie tuplas por concatenação.

# In[6]:


('a',1) + ('b',2) + ('c',3)


# In[7]:


('+','-')*3


# **Exemplo:** Imprima tabela de valores usando desempacotamento e iteração.

# In[8]:


s = [(1,2,3),(4,5,6),(7,8,9)]
s

for (m,n,p) in s:
    print('a={0}, b={1}, c={2}'.format(m,n,p))


# **Exemplo:** Desempacote elementos em iteráveis de comprimento arbitrário.

# O desempacotamento de uma tupla (ou sequência) em objetos iteráveis que tenham comprimento arbitrário pode ser feito por meio de uma _expressão estrela_ (_star expression_).

# In[9]:


# desempacota por star expression e ignora primeiro item
_,*restante = tup1
restante


# Discussão:
# 
# - Usamos 2 variáveis para desempacotar uma tupla de 4 elementos.
# - A variável `p` é uma lista contendo os últimos elementos de `tup1`.
# - A variável `_` possui valor, mas é ignorada.

# ```{hint}
# Use um _underscore_ (`_`) para representar uma variável que, devido ao desempacotamento, você considere "indesejada".
# ```

# Comentário: 
# 
# - Outros casos em que _star expressions_ são úteis envolvem dados que possuem mais de um valor atribuível a um mesmo registro (p.ex.: 1 pessoa com 2 números de telefone), ou quando se quer quebrar iteráveis em comprimentos arbitrários. 
# 
# - _Star expressions_ produzem listas.
# 
# Por exemplo:   

# In[10]:


_,*m4,_ = (3,4,8,12,16,10)
m4 # múltiplos de 4


# In[11]:


_,_,_,*m5 = (4,8,12,5,10)
m5 # múltiplos de 5


# In[12]:


*m6,_,_ = (6,12,5,10)
m6 # múltiplos de 6


# In[13]:


# 2 star expressions não são permitidas
*m6,*m5 = (6,12,5,10)


# ```{note}
# Ao usar uma _star expression_, certifique-se que o número de variáveis usadas no desempacotamento é consistente com os seus objetivos.
# ```

# ### Métodos de tupla
# 
# Métodos são funções atribuídas a alguns objetos. Embora tuplas sejam imutáveis, elas possuem métodos bastante úteis. Aqui, consideraremos dois:
# 
# - `count`: conta quantas vezes um dado valor aparece na tupla.
# - `index`: localiza o índice de um valor dado.

# **Exemplo:** Contando valores em tupla.

# In[15]:


tupla = (4,3,2,1,1,2,3,4,2,2,2,3,3,3,1,3,1,2,3,4,2,1,3,4,2,2)

print(tupla.count(0))
print(tupla.count(3))
print(tupla.count(4))


# **Exemplo:** Localizando posição.

# In[16]:


tupla.index(3)


# Comentário: 
# 
# - Caso haja valores repetidos na tupla, o método `index` retornará o índice da relativo à primeira aparição. Como o número 3 aparece 8 vezes na tupla e seu primeiro registro ocorre na segunda posição, o valor de retorno de `index` é 1.

# ### _Swap_ de variáveis
# 
# O modo Pythônico de realizar uma troca de variáveis (_swap_) é o seguinte:

# In[17]:


x,y = 1,2
y,x = x,y
x,y


# ### Tuplas como registros
# 
# Tuplas servem para armazenar registros: cada item na tupla é o dado de um campo e a posição do item dá o significado. 

# **Exemplo:** Tuplas como registros. 

# In[18]:


# latitute e longitude da Torre Eiffel
eiffel_ll = (48.85844772530444, 2.2948031631859886)

# capitais do mundo
caps = [('Afeganistão','Cabul','Ásia'),
        ('Barbados','Bridgetown','América'),
        ('Chade','Jamena','África')]

# população indígena no Brasil por decênio
popind = [(1991,294131),(2000,734127),(2010,817963)]

for a,p in popind:
    print(f'Em {a}, o Brasil possuía {p} habitantes indígenas.')


# Comentários: 
# 
# - Imprimimos os valores dos registros por desempacotamento.

# In[19]:


print('{:14} | {:14} | {:14}'.format('PAÍS','CAPITAL','CONTINENTE'))
print('-'*(14*3+2))
fmt = '{:14} | {:14} | {:14}'
for pais, cap, cont in caps:
    print(fmt.format(pais,cap,cont))


# Comentários: 
# 
# - Neste exemplo, simulamos uma tabela usando um formato-base e criamos uma linha de cabeçalho por concatenação de string.

# ## Dicionários 
# 
# Um dicionário (_dict_) é uma estrutura conhecida como _tabela hash_ ou _array associativo_. É uma coleção de tamanho flexível composta de pares do tipo _chave:valor_. Criamos um `dict` por diversas formas. A mais simples é usar chaves e pares explícitos.

# In[20]:


d = {} # dict vazio
d


# Os pares chave-valor incorporam quaisquer tipos de dados.

# In[21]:


d = {'par': [0,2,4,6,8], 'ímpar': [1,3,5,7,9], 'nome':'Meu dict', 'teste': True}
d


# ### Acesso a conteúdo

# Para acessar o conteúdo de uma chave, indexamos pelo seu nome.

# In[22]:


d['par'] 


# In[23]:


d['nome']


# **Exemplo:** construindo soma e multiplicação especial.

# In[24]:


# dict
op = {'X' :[1,2,3], 'delta' : 0.1}

# função
def sp(op):
    s = [x + op['delta'] for x in op['X']]
    p = [x * op['delta'] for x in op['X']]
    
    return (s,p) # retorna tupla

soma, prod = sp(op) # desempacota

for i,s in enumerate(soma):
    print(f'pos({i}) | Soma = {s} | Prod = {prod[i]}')


# ### Inserção de conteúdo

# In[25]:


# apensa variáveis
op[1] = 3 
op['novo'] = (3,4,1) 
op


# ### Alteração de conteúdo

# In[26]:


op['novo'] = [2,1,4] # sobrescreve
op


# ### Deleção de conteúdo com `del` e `pop`

# In[27]:


del op[1] # deleta chave 
op


# In[28]:


novo = op.pop('novo') # retorna e simultaneamente deleta
novo


# In[29]:


op


# ### Listagem de chaves e valores
# 
# Usamos os métodos `keys()` e `values()` para listar chaves e valores.

# In[30]:


arit = {'soma': '+', 'subtr': '-', 'mult': '*', 'div': '/'} # dict

k = list(arit.keys())
print(k)
val = list(arit.values())
print(val)
for v in range(len(arit)):
    print(f'A operação \'{k[v]}\' de "arit" usa o símbolo \'{val[v]}\'.')


# ### Combinando dicionários
# 
# Usamos `update` para combinar dicionários. Este método possui um resultado similar a `extend`, usado em listas.

# In[31]:


pot = {'pot': '**'}
arit.update(pot)
arit


# ### Dicionários a partir de sequencias
# 
# Podemos criar dicionários a partir de sequencias existentes usando `zip`.

# In[32]:


arit = {'soma', 'subtr', 'mult', 'div', 'pot'} 
ops = {'+', '-', '*', '/', '**'}

dict_novo = {}

for chave,valor in zip(arit,ops):
    dict_novo[chave] = valor
    
dict_novo


# Visto que um `dict` é composto de várias tuplas de 2, podemos criar um  de maneira ainda mais simples.

# In[33]:


dict_novo = dict(zip(arit,ops)) # visto que dicts
dict_novo


# ## Conjuntos
# 
# Um conjunto (_set_) é uma coleção não ordenada de elementos únicos. Eles podem ser criados através da função `set` ou de uma expressão literal com um par de chaves `{}`. Eles são parecidos com _dicts_, porém não possuem chaves (_keys_).
# 

# **Exemplo:** Crie o conjunto dos números pares positivos e menores do que 15.

# In[34]:


pq1 = set(range(0,15,2))
pq2 = {0,2,4,6,8,10,12,14}


# Discussão: 
# 
# - Em `pq1`, criamos o conjunto por função, usando `range` para gerar os números.
# - Em `pq2`, criamos o conjunto literalmente, por extensão.

# In[35]:


{1,2,2,3,3,4,4,4} # 'set' possui unicidade de elementos


# ### Operações com conjuntos 
# 
# A seguir mostraremos uma série de operações com conjuntos. Considere os seguintes conjuntos.

# In[36]:


A = {1,2,3}
B = {3,4,5}
C = {6}


# #### União de conjuntos

# In[37]:


A.union(B) # união


# In[38]:


A | B # união com operador alternativo ('ou')


# #### Atualização de conjuntos (união)
# 
# A união *in-place* de dois conjuntos pode ser feita com `update`.

# In[39]:


C


# In[40]:


C.update(B) # C é atualizado com elementos de B
C


# In[41]:


C.union(A) # conjunto união com A


# In[42]:


C # os elementos de A não foram atualizados em C


# A atualização da união possui a seguinte forma alternativa com `|=`.

# In[43]:


C |= A # elementos de A atualizados em C
C


# #### Interseção de conjuntos

# In[44]:


A.intersection(B) # interseção


# In[45]:


A & B # interseção com operador alternativo ('e')


# #### Atualização de conjuntos (interseção)
# 
# A interseção *in-place* de dois conjuntos pode ser feita com `intersection_update`.

# In[46]:


D = {1, 2, 3, 4}
E = {2, 3, 4, 5}


# In[47]:


D.intersection(E) # interseção com E


# In[48]:


D # D inalterado


# In[49]:


D.intersection_update(E) 
D # D alterado


# A atualização da interseção possui a seguinte forma alternativa com `&=`.

# In[50]:


D &= E
D


# #### Diferença entre conjuntos

# In[51]:


A


# In[52]:


D


# In[53]:


A.difference(D) # apenas elementos de A


# In[54]:


D.difference(A) # apenas elementos de D


# In[55]:


A - D # operador alternativo 


# In[56]:


D - A 


# #### Atualização de conjuntos (diferença)
# 
# A interseção *in-place* de dois conjuntos pode ser feita com `difference_update`.

# In[57]:


D = {1, 2, 3, 4}
E = {1, 2, 3, 5}


# In[58]:


D


# In[59]:


D.difference(E)
D


# In[60]:


D.difference_update(E)
D


# A atualização da diferença possui a seguinte forma alternativa com `-=`.

# In[61]:


D -= E
D


# #### Adição ou remoção de elementos

# In[62]:


A


# In[63]:


A.add(4) # adiciona 4 a A
A


# In[64]:


B


# In[65]:


B.remove(3) # remove 3 de B
B


# #### Reinicialização de um conjunto (vazio)
# 
# Podemos remover todos os elementos de um conjunto com `clear`, deixando-o em um estado vazio.

# In[66]:


A


# In[67]:


A.clear()
A # A é vazio


# In[68]:


len(A) # 0 elementos


# #### Continência
# 
# Podemos verificar se um conjunto $A$ é subconjunto de (está contido em) outro conjunto $B$ ($A \subseteq B$) ou se $B$ é um superconjunto para (contém) $A$ ($B \supseteq A$) com `issubset` e  `issuperset`. 

# In[69]:


B


# In[70]:


C


# In[71]:


B.issubset(C) # B está contido em C


# In[72]:


C.issuperset(B) # C contém B


# #### Subconjuntos e subconjuntos próprios

# Podemos usar operadores de comparação entre conjuntos para verificar continência.
# 
# - $A \subseteq B$: $A$ é subconjunto de $B$
# - $A \subset B$: $A$ é subconjunto próprio de $B$ ($A$ possui elementos que não estão em $B$)

# In[73]:


{1,2,3} <= {1,2,3} # subconjunto


# In[74]:


{1,2} < {1,2,3} # subconjunto próprio


# In[75]:


{1,2,3} > {1,2}


# In[76]:


{1,2} >= {1,2,3}


# #### Disjunção
# 
# Dois conjuntos são disjuntos se sua interseção é vazia. Podemos verificar a disjunção com `isdisjoint`

# In[77]:


E


# In[78]:


G = {1,2,3,4}
G


# In[79]:


E.isdisjoint(G) # 1,2,3 são comuns


# #### Igualdade entre conjuntos
# 
# Dois conjuntos são iguais se contém os mesmos elementos.

# In[80]:


H = {3,'a', 2}
I = {'a',2, 3}
J = {1,'a'}


# In[81]:


H == I


# In[82]:


H == J


# In[83]:


{1,2,2,3} == {3,3,3,2,1} # lembre-se da unicidade


# ## Compreensões de lista
# 
# As listas são as sequências mais comuns em Python. Listas são objetos mutáveis de comprimento variável. Dominar este tipo de dado é fundamental para compreender o preenchimento de sequências de praticamente qualquer outro tipo. Começaremos aprendendo sobre compreensões de lista, ou, no jargão do Python, _listcomps_.

# **Exemplo:** Construa uma lista dos códigos _Unicode_ correspondentes dos caracteres de uma _string_.

# In[84]:


palavra = '!@#$%'
cods = []
for c in palavra:
    cods.append(ord(c))
cods    


# Discussão:
# 
# - `ord` produz o número ordinal correspondente de um caracter segundo o padrão Unicode. Para saber o código hexadecimal correspondente, pode-se fazer `hex(ord(c))`.
# 
# 
# ```{hint}
# Caracteres, emojis e símbolos são números codificados! Para saber mais sobre o padrão Unicode, veja este [site](https://home.unicode.org).
# ```

# **Exemplo:** Construa uma _listcomp_ correspondente.

# In[85]:


palavra = '!@#$%'
cods = [ord(c) for c in palavra]
cods


# Comentário: 
# 
# - Uma _listcomp_ é mais legível e sua intenção é explícita. Todavia, é preciso ser cauteloso para não criarmos códigos ilegíveis abusando de _listcomps_.
# - Como quebras de linha são ignoradas dentro de pares `[]`,`()` ou `{}`, é possível quebrar uma instrução de _listcomp_ sem usar o caracter de escape para quebra de linha `\`.

# In[86]:


# listcomp com quebra de linha sem `\`
[ord(c) 
 for c 
 in palavra]


# **Exemplo:** Construa um produto cartesiano de pares $(a,b)$, onde $a$ é um tipo de sangue de acordo com o sistema ABO e $b$ é o Fator Rh.

# In[87]:


A = ['A','B','O','AB']
Rh = ['+','-']
sangue = [(a,b) for a in A for b in Rh]
sangue


# Discussão: 
# 
# - A _listcomp_ anterior usa dois `for` que iteram sobre as sequências `A` e `Rh` e constroi uma lista de tuplas do tipo _(a,b)_.

# **Exemplo:** Construa um produto cartesiano de pares $(a,b)$, onde $a$ é o FatorRh e $b$ é um tipo de sangue de acordo com o sistema ABO.

# In[88]:


[(b,a) for a in A for b in Rh]


# Comentário: 
# 
# - Note que, neste caso, basta alterarmos a ordem dos elementos da tupla.

# **Exemplo:** Use _listcomps_ com condicionais para criar filtros.

# In[89]:


# equipes da fórmula 1
f1 = ['Red Bull Racing','Mercedes',
 'McLaren','Ferrari','AlphaTauri',
 'Aston Martin','Alpine','Alfa Romeo Racing',
 'Williams','Haas F1 Team']

# equipes que começam com A, em maiúsculas
[team.upper() for team in f1 if team[0] == 'A']


# In[90]:


# equipes cujo nome não inicia com A e tem menos do que 10 caracteres
[team for team in f1 
 if team[0] != 'A' and len(team) < 10]


# ## Compreensões de conjuntos
# 
# Semelhantemente a _listcomps_, podemos realizar "_setcomps_".

# In[91]:


# comprimentos de nomes de equipes (únicos)
{len(team) for team in f1}


# In[92]:


[len(team) for team in f1]


# Comentários: 
# 
# - Note que a _listcomp_ para este caso possuiria elementos repetidos.

# In[93]:


# comprimento de nomes de equipes que terminam com "ing"
{len(team) for team in f1 if team.endswith('ing')}


# ## Compreensões de dicionários
# 
# Compreensões de dicionários, ou "_dictcomps_", possuem resultados similares às anteriores e são convenientes para criar _dicts_.

# In[94]:


{k:v for k,v in enumerate(f1)}


# Comentário:
# 
# - `enumerate` é um objeto que constroi uma enumeração para um iterável.

# In[95]:


# enumera a partir do índice 7, mas percorre toda a lista
{k:v for k,v in enumerate(f1,7)}


# ## _Sorted_ 

# Listas em Python possuem um método chamado `sort` com o qual podemos realizar uma ordenação _in-place_ de uma lista. Por outro lado, a função `sorted` permite que façamos o mesmo criando uma nova lista e, dessa maneira, não alterando a lista original.

# In[96]:


# copia lista f1
f1c = f1.copy()
f1c


# In[97]:


# lista ordenada
f1c.sort()
f1c


# In[98]:


# lista f1 ordenada
f1c2 = sorted(f1)
f1c2


# In[99]:


# lista original intacta
f1


# Para realizar a ordenação reversa, usamos `reverse=True` na função `sorted`.

# In[100]:


# ordenação re
sorted(f1,reverse=True)


# ## Aleatoriedade
# 
# Números aleatórios, ou também chamados de randômicos, são úteis para fabricar experimentos estatísticos, realizar amostragem e desenvolver uma série de estudos envolvendo probabilidade.  
# 
# Em Python, podemos usar o módulo `random` para atingir uma diversidade de propósitos em ciência de dados. Vamos explorar algumas funções para geração aleatória: `choice`, `random`, `randint`, `shuffle` e `sample`.

# In[101]:


import random


# **Exemplo:** Crie um experimento de lançamento de dados e realize uma escolha aleatória em $n$ lançamentos.

# In[102]:


dado = list(range(1,7))

n = 4
for _ in range(n):
    print(random.choice(dado))


# Comentários:
# 
# - O _loop_ será repetido $n$ vezes.
# - O método `choice` escolhe um valor ao acaso entre os disponíveis na lista. 

# **Exemplo:** Crie um experimento de probabilidade aleatório que determine a salinidade presente em 1 litro de água marinha (3 - 5%). 

# In[103]:


na = 5
saly = []
for _ in range(na):
    saly.append(0.03 + (0.05-0.03)*random.random())
saly    


# Comentários: 
# 
# - Este experimento equivale a coletar 5 amostras de água marinha com salinidade variável entre 3 e 5%.
# - O método `random` determina um número aleatório no intervalo [0,1).

# **Exemplo:** Crie um experimento que ordena 15 arremessadores para cestas de 3 pontos durante um treinamento do time do Los Angeles Lakers (0 a 99) excluindo a lista de números reservados. Considere que se o número sorteado não estiver atribuído a nenhum jogador atual ou se já tiver sido sorteado, o técnico escolherá o próximo da lista.
# 
# Lista de números reservados: 8,13,17,19,22,24,25,32,33,34,42,44,52,99.

# In[104]:


reservados = [8,13,17,19,22,24,25,32,33,34,42,44,52,99]

shooter = []
while len(shooter) != 15:
    x = random.randint(0,99)
    if x not in reservados and x not in shooter:
        shooter.append(x)    

print('Los Angeles Lakers :: 3-point shooters (Training Schedule):')
for s in shooter:
    print(s)
        


# Comentários: 
# 
# - O _loop_ _while_ encerrará quando uma lista com 15 arremessadores estiver completa.
# - A estrutura condicional previne que números já sorteados entrem na lista.
# - O método `randint` escolhe um número inteiro aleatório entre 0 e 99.

# **Exemplo:** Crie uma alteração no schedule de treinamento anterior a partir da última lista disponível.

# In[105]:


print(random.shuffle(shooter))
shooter


# Comentário: 
# 
# - O método `shuffle` reordena a lista `shooter` randomicamente e produz um valor `None` como saída. Dessa forma, geramos uma nova lista com os mesmos arremessadores pré-selecionados, mas em ordem distinta.

# **Exemplo:** Construa uma tabela aleatória de 3 jogos de beisebol entre times da MLB.

# In[106]:


# lê arquivo com nome de times da MLB
with open('../database/mlb-teams.csv') as f:
    mlb = f.read().splitlines()
    
for _ in range(3):
    a,b = random.sample(mlb,2)
    print(f'Game {_+1}: {a} x {b}')        


# Comentários: 
# 
# - O método `sample` realiza uma amostragem de $k$ valores disponíveis na lista. Aqui, escolhemos $k=2$, de modo que 2 times são escolhidos ao acaso para comporem 3 jogos.

# ## Expressões regulares
# 
# Expressões regulares (_regular expressions_), também conhecidas como _RE_, _regexes_, ou _regex pattern_ são regras estabelecidas para localizar padrões desejados em strings. REs, na verdade, formam uma pequena linguagem de programação dentro de uma linguagem maior. 
# 
# Em Python, REs funcionam com base em códigos escritos na linguagem C. Nossa intenção aqui é fazer uma introdução sobre a utilidade e aplicabilidade de expressões regulares. Para entender este tema com profundidade, é necessário estudar aspectos internos de compiladores. 
# 
# ### Para que usamos _regex_? 
# 
# Expressões regulares são implicitamente usadas por nós quase que diariamente quando utilizamos comandos do tipo _Localizar_ para buscar uma palavra em uma página da internet ou dentro de um arquivo PDF. Porém, elas nos permitem fazer muito mais do que uma simples busca por palavras. 
# 
# O texto a seguir é um trecho do livro _Memórias Póstumas de Brás Cubas_, de Machado de Assis, que pode ser recuperado pelo arquivo <a href="database/bras-cubas.txt" download="database/bras-cubas.txt">bras-cubas.txt</a>:

# > Não durou muito a evocação; a realidade dominou logo; o presente expeliu o passado. Talvez eu exponha ao leitor, em algum canto deste livro, a minha teoria das edições humanas. O que por agora importa saber é que Virgília — chamava-se Virgília — entrou na alcova, firme, com a gravidade que lhe davam as roupas e os anos, e veio até o meu leito. O estranho levantou-se e saiu. Era um sujeito, que me visitava todos os dias para falar do câmbio, da colonização e da necessidade de desenvolver a viação férrea; nada mais interessante para um moribundo. Saiu; Virgília deixou-se estar de pé; durante algum tempo ficamos a olhar um para o outro, sem articular palavra. Quem diria? De dois grandes namorados, de duas paixões sem freio, nada mais havia ali, vinte anos depois; havia apenas dois corações murchos, devastados pela vida e saciados dela, não sei se em igual dose, mas enfim saciados. Virgília tinha agora a beleza da velhice, um ar austero e maternal; estava menos magra do que quando a vi, pela última vez, numa festa de São João, na Tijuca; e porque era das que resistem muito, só agora começavam os cabelos escuros a intercalar-se com alguns fios de prata.

# Suponha que você quisesse localizar quantas vezes a palavra "Vírgilia" aparece neste trecho do livro. Com a ajuda de um editor de textos munido de um comando de busca, facilmente encontraríamos a resposta. São 4 vezes.
# 
# Agora, suponha que você quisesse localizar se, neste mesmo texto, há alguma ocorrência do seguinte padrão: _palavra que se inicia com a letra "p", maiúscula ou minúscula, possui pelo menos uma letra "i" e a letra "i" deve ser, no máximo, o quarto caracter_. Claramente, não conseguiríamos cumprir esta exigência tão facilmente como encontrar "Virgília". Com algum esforço visual, conseguimos verificar no texto que "paixões" atende este critério. Como faríamos isto usando Python? Ou melhor, como faríamos isto usando Python em um arquivo com 550.000 palavras para serem analisadas?
# 
# O padrão que acabamos de descrever pode ser procurado por meio de uma _regex_. Ou seja, _regex_ são úteis quando desejamos buscar um determinado padrão em _strings_. A seguir, vamos usar o pequeno texto de Machado de Assis como base para aprender um pouco sobre _regex_.

# ### Padrões simples, caracterese ordinários e metacaracteres
# 
# A tarefa mais simples que podemos executar com REs é combinar caracteres. Por exemplo, sabemos que a string `'murchos'` equivale à string `'murchos'`, mas não equivale à string `'moribundos'`. No primeiro caso, todos os caracteres se combinam e estão posicionados nos mesmos lugares; no segundo caso, embora alguns caracteres se combinem, a exemplo de `'m'`, `'r'`, `'o'` e `'s'`, e estejam posicionados aparentemente em mesmos lugares (no início, terceira posição e final da string), obviamente uma string não combina **exatamente** com a outra. 
# 
# Há muitos caracteres que podem ser usados para combinações simples. Por exemplo, quando em _case insensitive_, `'mur'` é um padrão encontrado tanto em `'Murcho'`, quanto em `'muralha'` ou em `'HAMURABI'`. Entretanto, há caracteres que não podem ser combinados da forma como o lemos. Por exemplo, para buscarmos o padrão `'\textsuperscript'` em uma string, o caracter `'\'` não pode ser usado de forma _literal_. Ele é um _metacaracter_. 
# 
# _Caracteres ordinários_ são basicamente todos os caracteres ASCII alfanuméricos, tais como `'b'`,  `'B'` e `'1'`.
# 
# ```{note}
# ASCII, de _American Standard Code for Information Interchange_, é um padrão de codificação de caracteres que foi predominantemente usado desde a década de 1960 e tornou-se um padrão da internet em 2015 contendo apenas 128 caracteres. Em 2007, ele foi suplantado pelo padrão UTF-8 (_Unicode Transformation Format - 8 bit_), gerido pela iniciativa Unicode (_Universal Coded Character Set_). O UTF-8 é um padrão mais novo que comporta 1.112.064 caracteres e também é o usual no Python 3. Os 128 primeiros caracteres do padrão UTF-8 são os 128 primeiros da lista do UTF-8, dos quais alguns tornaram-se obsoletos.
# ```
# 
# _Caracteres especiais_ são todos os metacaracteres. A lista dos metacaracteres é a seguinte: 
# 
# ```
# . ^ $ * + ? { } [ ] \ | ( )
# ``` 
# 
# Todos eles exercem papéis especiais na linguagem das REs como veremos a seguir. 
# 
# Para efeito de curiosidade, o seguinte código imprime os caracteres ASCII mais comuns. A partir do fatiamento da lista, podemos gerar as sublistas que contêm apenas números e letras. Deixaremos isto como exercício. Cabe enfatizar, entretanto, que em Python 3, o padrão de caracter 

# In[107]:


# imprime caracteres ASCII mais comuns 
# end = ' ' altera a terminação padrão '\n'
for i in range(33,127):
    print(chr(i), end = ' ')


# ### O módulo `re`
# 
# Em Python, temos à disposição o módulo `re` para trabalhar com REs. Vejamos o que ele pode nos proporcionar. Antes de prosseguir, vamos ler o arquivo e salvar o texto em uma _string_.

# In[108]:


with open('../database/bras-cubas.txt', 'r') as f:
    cubas = f.read()
cubas    


# In[109]:


# importa o módulo
import re


# As principais funções do módulo `re` podem ser resumidas ao seguinte modelo:
# 
# ```python
# re.f(pattern,string)
# ```
# onde _f_ é o nome da função, _pattern_ é o padrão, isto é, a _regex_, e _string_ é a string na qual o padrão é procurado. Exploraremos algumas delas a seguir compreendendo, simultaneamente, o papel desempenhado pelos metacaracteres. 

# **Exemplo:** Procure pelo padrão "que" no texto-base e conte quantas vezes ele aparece.

# In[110]:


# busca todas as combinações
que = re.findall('que',cubas)
print(que)
print(len(que))


# Discussão:
# - O método `findall` procura em `cubas` todas as combinações do padrão "que"
# - `len` permite que contemos o número de elementos da lista e, consequentemente, o número de vezes que o padrão aparece. Entretanto, observemos que o padrão poderia ser algo que não formasse uma palavra inteligível. Vejamos o próximo exemplo:

# In[111]:


# padrão presente, mas não é palavra inteligível
re.findall('xou',cubas)


# Buscas por caracteres ordinários são sempre exatas, no sentido de que o caracter é combinado como ele é. Vejamos um exemplo que conta as vogais que aparecem no texto.

# In[112]:


for vogal in ['a','e','i','o','u']:    
    print(f'A vogal \'{vogal}\' foi localizada {len(re.findall(vogal,cubas))} vezes no texto.')


# **Exemplo:** Busque pelo padrão "Tijuca" no texto e determine suas posições de início e término.

# In[113]:


# busca por combinação retornado posição
p = re.search('Tijuca',cubas)
p.start(), p.end(), p.group()


# Discussão: 
# 
# - O método `search` procura pelo padrão `'Tijuca'` em `cubas` e retorna três informações:
#     - `start`: a posição inicial do padrão
#     - `end`: a posição final do padrão
#     - `group`: o padrão localizado
# - O padrão aparece apenas uma vez no texto na fatia `cubas[1042:1048]`.

# Comentários: 
# 
# - Caso houvesse repetição do padrão, apenas os índices da primeira aparição seriam retornados. Vejamos: 

# In[114]:


p2 = re.search('que',cubas)
p2.start(), p2.end(), p2.group()


# Vimos anteriormente que há 7 aparições do padrão "que" no texto-base. Porém, apenas a primeira é retornada por `search`. Vejamos:

# In[115]:


# uma maneira de mostrar que há apenas
# um 'que' até o caracter 182 de 'cubas'
# por meio de split e interseção de conjuntos
set(cubas[0:182].split(' ')).intersection({'que'})


# Como este conjunto é unitário, há apenas um padrão 'que' até a posição 182 de `cubas`.

# **Exemplo:** Busque pelo padrão "Não" no texto e verifique se ele aparece no início da string.

# In[116]:


p3 = re.match('Não',cubas)
p3.start()


# Discussão:
# 
# - O método `match` busca por um determinado padrão que aparece **somente** no início de uma string. Quando tal combinação de caracteres é encontrada o método retorna um objeto. Caso contrário, retorna `NoneType`.
# - No exemplo anterior, o método `start` mostra que o primeiro caracter do padrão `'Não'`, qual seja, `'N'` , ocupa a primeira posição da string, isto é, a posição 0. 

# Comentários: 
# 
# - Enquanto `re.search` realiza a busca por um padrão em qualquer posição da string, `re.match` busca se esse mesmo padrão ocorre, exclusivamente, no início da string. 
# 
# - Há muitas situações em que `match` será a escolha a fazer em seu programa. Em uma string de várias linhas, por exemplo, `match` procurará pelo padrão apenas na primeira linha e ignorará a ocorrência dele nas demais. Opostamente, `search` procurará por ele em todas as linhas. Se forem detectadas mais de uma ocorrência, retornará a posição da primeira ocorrência.
# 
# - Em ambos os métodos, quando o padrão não existe na string, o objeto retornado é um `NoneType`.

# **Exemplo:** Substitua o padrão "Virgília" por "Ofélia" em toda a string do texto.

# In[117]:


cubas_novo = re.sub('Virgília','Ofélia',cubas)
cubas_novo


# Discussão: 
# 
# - O método `sub` realiza a substituição de um padrão por outro na string passada e sua sintaxe mais genérica é do tipo `re.sub(p,r,s)`, onde `p` é o padrão que se deseja substituir por `r` na string `s`. 
# 
# - No exemplo dado, a operação com `sub` simplesmente substituirá todas as entradas da palavra "Vírgília" por "Ofélia" em `cubas`, resultando em uma string nova chamada `cubas_novo`.

# **Exemplo:** Substitua o padrão "Virgília" por "Ofélia" apenas nas duas primeiras aparições

# In[118]:


cubas_novo2 = re.sub('Virgília','Ofélia',cubas,count=2)
cubas_novo2


# Discussão: 
# 
# - É possível usar a keyword `count` e especificar quantas vezes, em ordem, o padrão deverá ser substituído. 
# 
# - Como `count=2`, o método `sub` fará a substituição de "Virgília" por "Ofélia" apenas nas duas primeiras ocorrências do padrão, das quatro existentes no texto.

# Comentários:

# - Note que se usássemos `re.findall` para fazer uma breve verificação nas strings `cubas`, `cubas_novo` e `cubas_novo2`, o número de ocorrências de "Virgília" diferiria em cada caso.

# In[119]:


# original
print(len(re.findall('Virgília',cubas)))

# "Virgília" -> "Ofélia" integralmente
print(len(re.findall('Virgília',cubas_novo)))

# "Virgília" -> "Ofélia" em 2 ocorrências apenas
print(len(re.findall('Virgília',cubas_novo2)))


# **Exemplo:** Seccione o texto em várias substrings usando a vírgula (",") como ponto de quebra:

# In[120]:


cubas_sep = re.split(',',cubas)
cubas_sep


# Na próxima sessão, vamos incorporar sintaxes especiais nos métodos que aprendemos para realizar propósitos bem mais avançados. 

# Discussão: 
# 
# - O método `split` quebra a string em partes (_substrings_) substituindo usando o padrão passado ao método como ponto de quebra. Neste exemplo, as vírgulas são removidas e uma lista de strings é retornada.
# 
# - Ao utilizar `re.split(a,b)`, lembre-se que `a` é  um padrão a ser encontrado na string `b`. Ele não é necessariamente um caracter único, mas uma expressão regular.

# **Exemplo:** Separe a string do texto em no máximo 3 substrings usando o padrão "ão" como ponto de quebra. 

# In[121]:


# maxsplit = n; logo, n + 1 substrings
cubas_sep3 = re.split("ão",cubas,maxsplit=2)
cubas_sep3


# Discussão: 
# 
# - A _keyword_ `maxsplit` permite que limitemos o número de quebras. Neste exemplo, como `maxsplit=2`, há dois pontos de quebra e, portanto, 3 substrings. 
# 
# - Note que, neste exemplo, a substring 1 é formada por apenas um caracter, ao passo que a substring 3 comporta todos os caracteres além da segunda ocorrência do padrão "ão".
# 
# - Perceba, adicionalmente, que o padrão não é preservado durante o _split_.

# ### Sintaxes especiais
# 
# Os metacaracteres podem ser usados para criar REs das formas mais variadas (e criativas) possíveis. Vejamos exemplos.

# #### Metacaracter `.`
# 
# Serve para combinar qualquer caracter, exceto o _newline_ (`\n`), se usado no modo padrão. Em uso não padrão, pode também combinar-se com `\n`.

# **Exemplo:** Localize padrões com 5 caracteres contendo "lh" na 3a. e 4a. posições.

# In[122]:


re.findall('..lh.',cubas)


# Comentário: 
# 
# - Espaço também é um caracter. Por isso, na lista, temos também o padrão possível `'e lhe'`.
# 

# **Exemplo:** Localize padrões iniciando com a letra T maiúscula e contendo, ao todo, 3 caracteres.

# In[123]:


re.findall('T...',cubas)


# #### Metacaracter `\`
# 
# Serve para criar escapes de caracteres especiais ou sinalizar uma sequência especial.

# **Exemplo:** Quebre a string usando o ponto final (".") como ponto de quebra.

# In[124]:


# escape do metacaracter '.'
mt1 = re.split('\.',cubas)
mt1


# Comentário:
# 
# - Note que, todas as substrings intermediárias passaram a iniciar-se com um caracter de espaço. Como isto é pouco útil para nós, poderíamos ter utilizado o padrão `. ` (com espaço) para realizar a quebra.

# In[125]:


# considera um espaço no padrão
mt2 = re.split('\. ',cubas)
mt2


# #### Metacaracter `^`
# 
# Também chamado _caret_, serve para buscar padrões no início de uma string. 

# **Exemplo:** Use as substrings do exemplo anterior para buscar quais delas iniciam-se por `'T'`.

# In[126]:


for k,s in enumerate(mt2):
    aux = re.match('^T',s)
    if aux: # se lista não for vazia
        print(f'---> Padrão detectado na substring {k}:\n\"{s}\"')


# Comentário:
# 
# - Poderíamos ter usado `re.search` ou `re.match` também para atingir o mesmo propósito, visto que a expressão regular `'^T'` força o início com "T".

# #### Metacaracter `$`
# 
# Visto em sentido oposto a `^`, `$` serve para buscar padrões no final de uma string, ou logo antes de um caracter _newline_.

# **Exemplo:** Use as substrings do exemplo anterior para buscar quais delas terminam por `'o'`.

# In[127]:


for k,s in enumerate(mt2):
    aux = re.findall('o$',s)
    if aux: # se lista não for vazia
        print(f'---> Padrão detectado na substring {k}:\n\"{s}\"')


# Discussão: 
# 
# - Neste exemplo, identificamos todas as substrings que terminam com o caracter 'o'.
# 
# - Com expressões regulares mais exatas, restringimos as possibilidades. Vejamos o exemplo a seguir.

# In[128]:


# busca substring terminando com 'undo'
for k,s in enumerate(mt2):
    aux = re.findall('undo$',s)
    if aux: # se lista não for vazia
        print(f'---> Padrão detectado na substring {k}:\n\"{s}\"')


# Comentário:
# 
# - Note que para buscar o caracter literal '$' em uma string devemos usar o caracter de escape. Vejamos o próximo exemplo.

# In[129]:


real = 'João me pagou R$ 150,00.'
v = re.search('\$',real)
print(f'Caracter $ identificado na posição {v.start()}.')


# #### Metacaracter `*`
# 
# Serve para buscar 0 ou mais repetições de um caracter precedente. Este caracter especial é de _repetição_.

# **Exemplo:**

# In[130]:


re.findall('hav*.',cubas)


# Discussão: 
# 
# - A RE `'hav*.'` procura por padrões que atendem às seguintes restrições: 
#     - o caracter 'v' aparece 0 ou mais vezes após 'ha'.
#     - quando não houver 'v', o terceiro caracter passa a ser qualquer um que vier na sequência por causa do metacaracter '.'. 
#     - quando houver um 'v', o quarto caracter é qualquer um
#     - quando houver n repetições de 'v' após 'a', todos os n são considerados, e o n+1-ésimo caracter é qualquer um.

# Comentários: 
# 
# - Descrever em palavras o que a expressão regular faz exatamente não é sempre muito fácil. Vejamos mais um exemplo.
#     

# In[131]:


c = 'ha hahaa hav havv havva-havvva; haiiaa havia'

re.findall('hav*.',c)


# #### Metacaracter `+`
# 
# Serve para buscar 1 ou mais repetições de um caracter precedente. Assim como `*`, `+` também é um caracter especial de _repetição_.

# **Exemplo:**

# In[132]:


re.findall('hav+.',cubas)


# Discussão: 
# 
# - A RE `'hav+.'` é similar à anterior. Porém, pelo fato de ser obrigatória a ocorrência de pelo menos 1 caracter 'v' após 'a', os padrões 'ha ', 'ham' e 'har' são excluídos.
# - Se encontradas n ocorrências de 'v', o padrão será encerrado pelo n+1-ésimo caracter arbitrário
# - Como no texto existe tal padrão com apenas uma ocorrência de 'v', o quarto caracter, sendo arbitrário, é encontrado como 'i'.
# - O padrão 'havia', que forma uma palavra compreensível em Português, é ignorado por conter 5 caracteres.

# #### Metacaracter `?`
# 
# Serve para buscar 0 ou 1 repetição de um caracter precedente. Assim como `*`, `+` também é um caracter especial de _repetição_.

# **Exemplo:**

# In[133]:


re.findall('s?an.',cubas)


# Comentários: 
# 
# - Esta RE procurará por 0 ou 1 repetição de 's' seguida por 'an' e qualquer outro caracter. 
# 
# - Neste caso, a substring 'ssan', por exemplo, existente na palavra 'interessante' não seria coberta por `?`.

# #### Metacaracteres `[]`
# 
# Os colchetes devem ser usados, juntos, em par, para indicar um conjunto de caracteres sobre os quais a expressão regular deve operar. Em geral, usa-se o par `[]` para os seguintes propósitos: 

# - Listar caracteres individualmente
# 
# A RE `[vnd]` combinará os caracteres `'v'`, `'n'` ou `'d'`.

# **Exemplo:**

# In[134]:


# localiza todas as ocorrências 
# de 'v', 'n', ou 'd'
print(re.findall('[vnd]',cubas))


# - Localizar um intervalo de caracteres
# 
# Uma RE do tipo `[a-d]` combinará os caracteres de `'a'` a `'d'`, ao passo que `[a-z]` combinará todas as letras minúsculas da tabela ASCII (e não Unicode!), ou seja, de `'a'` a `'z'`.
# 
# Do mesmo modo, `[0-4]` combinará os dígitos de 0 a 4, e `[0-9]` todos os dígitos decimais. Por outro lado, a expressão `[0-3][3-8]` combinará todos os números de dois dígitos de 03 a 38.
# 
# Se o símbolo `-` for escapado (p.ex. `[a\-d]`), ou se for colocado como primeiro ou último caracter (p.ex. `[-b]` ou `[b-]`), ele significará o hífen literal ('-').

# **Exemplo:**

# In[135]:


re.findall('[a-z]um',cubas)


# Discussão: 
# 
# - Esta RE procurará todos os padrões que iniciam por qualquer letra minúscula (de 'a' a 'z') seguidas por 'um'.

# **Exemplo:**

# In[136]:


re.findall('[v-z][a-].',cubas)


# Discussão: 
# 
# - Esta RE procurará todos os padrões que iniciam por uma letra minúscula entre 'v' e 'z' seguidas por 'a', '-', ou 'a-' e um caracter qualquer adicional.

# **Exemplo:**

# In[137]:


# mesmo efeito que anterior
re.findall('[v-z][-a].',cubas)


# - Localizar caracteres especiais como literais
# 
# Os caracteres especiais perdem seu status quando aparecem entre colchetes. Por exemplo, a RE `[(+*)]` procurará por qualquer um dos literais `(`, `+`, `*` ou `)`.

# In[138]:


ex = 'Quanto é (22 + 3)*1 - 6*1?'
re.findall('[0-9][)*]',ex)


# Discussão:
# 
# - Esta RE busca padrões em que um dígito de 0 a 9 precede um ')' ou '*' literalmente.

# In[139]:


re.findall('[0-9][?]',ex)


# Discussão:
# 
# - Esta RE busca padrões em que um dígito de 0 a 9 precede um '?' literal.

# #### Metacaracteres `{}`
# 
# As chaves, assim como os colchetes, devem ser usadas juntas, em par, para localizar cópias ou repetições de uma expressão regular. Em geral, ela é usada para os seguintes objetivos:

# - Localizar exatamente _m_ cópias de uma RE anterior

# **Exemplo:**

# In[140]:


# busca pelo padrão 'rr'
re.search('r{2}',cubas).group()


# **Exemplo:**

# In[141]:


ex2 = '0110011000110011001010110100110111111000'
re.findall('0{2}',ex2)


# In[142]:


re.findall('1{3}',ex2)


# In[143]:


# busca 000000 - 111111
# com variações de 0,1 intermediárias
re.findall('[0-1]{6}',ex2)


# - Localizar entre _m_ e _n_ repetições de uma RE anterior

# **Exemplos:**

# In[144]:


set(re.findall('10{2,3}',ex2))


# In[145]:


set(re.findall('01{2,3}',ex2))


# In[146]:


set(re.findall('[0-1]{2,3}',ex2))


# #### Metacaracter `|`
# 
# Usamos o _pipe_ para significar "ou" com o objetivo de localizar mais de uma RE. Por exemplo, `A|B` buscará padrões determinados pela RE `A` **ou** por `B`. _Pipes_ adicionais constroem sintaxes conjuntivas. Ou seja, `A|B|C|D...|Z` significaria "A ou B ou C ou ... D".

# **Exemplos:**

# In[147]:


# busca por 'rre' ou 'ssa'
re.findall('r{2}e|s{2}a',cubas)


# In[148]:


# busca por 'cha', 'cho' ou
# 'lha', 'lhi' ou 
# 'pra', 'pre', 'pri', 'pro', 'pru'
re.findall('ch[ao]|lh[ai]|pr[aeiou]',cubas)


# #### Metacaracteres `()`
# 
# Servem para criar _grupos de captura_. Um grupo de captura é formado por uma RE confinada entre parênteses. Grupos de captura podem ser aplicados para extrair padrões que possuam uma certa estrutura. 

# **Exemplo**:

# In[149]:


table = ['alfa00-LAX','beta22-PET', 'zeta92-XIR']

for t in table:
    pat = re.match("([a-z][a-z][a-z][a-z][0-9][0-9])-([A-Z]{3})", t)
    if pat:
        print(pat.groups())


# Discussão: 
# 
# - A RE acima é composta de dois grupos de captura que são separados pelo `-` literal. 
# 
# - O primeiro grupo de captura é `([a-z][a-z][a-z][a-z][0-9][0-9])`
# 
# - O segundo grupo de captura é `([A-Z]{3})`
# 
# - Tuplas com dois elementos são impressas com `groups()`.

# Comentários: 
# 
# - Como se vê, os grupos de captura permitiram que identificássemos padrões separados em uma lista de strings que continha uma estrutura predefinida. 
# 
# - Entretanto, as REs anteriores criadas como grupos de captura poderiam ser definidas de uma forma muito mais concisa através de _identificadores_.

# #### Identificadores e _tokens_ gerais
# 
# Ao trabalhar com REs, podemos utilizar identificadores e _tokens_ diversos para significar padrões de maneira concisa. 
# 
# O exemplo anterior sobre grupos de captura, por exemplo, poderia ser escrito de outra forma:

# In[150]:


for t in table:
    pat = re.match("(\w+)\W(\w+)", t)
    if pat:
        print(pat.groups())


# Neste caso, `\w` e  `\W` são chamados _identificadores_.

# A tabela a seguir resume os principais identificadores e seu significado.
# 
# |Identificador|Significado|
# |---|---|
# |`\d`|qualquer caracter que é um dígito decimal. Equivalente a `[0-9]`|
# |`\D`|qualquer caracter exceto dígido (não-dígito). Equivalente a `[^0-9]`|
# |`\w`|qualquer caracter Unicode. Se a flag `ASCII` for utilizada, equivale ao conjunto `[a-zA-Z0-9_]`|
# |`\W`|o oposto de `\w`. Se a flag `ASCII` for utilizada, equivale ao conjunto `[^a-zA-Z0-9_]`|
# |`\s`|qualquer caracter que é um espaço.|
# |`\S`|qualquer caracter que não seja espaço.|
# 
# A tabela a seguir resume _tokens_ gerais e seu significado.
# 
# |_Token_|Significado|
# |---|---|
# |`\n`|quebra de linha. _Newline_.|
# |`\r`|_carriage return_|
# |`\t`|TAB|
# |`\0`|caracter nulo|

# **Exemplo:** Identificando padrões de data e hora. 

# In[151]:


dt = ['2021-04-06 10:32:00', '2020-12-03 01:12:58'] 
for m in dt:
    pat = re.match('(\d+)-(\d+)-(\d+)\s(\d+):(\d+):(\d+)',m)
    if pat:
        print(pat.groups())


# **Exemplo:** Identificando cores em padrão hexadecimal.

# In[152]:


cores = ['(1,23,43)','#3ed4f4', '#ffcc00','(C,M,Y,K)','#9999ff'] 

for c in cores:
    ok = re.match('#[a-fA-F0-9]{6}',c)
    if ok:
        print(ok.group())


# **Exemplo:** Identificando URLs no domínio Wikipedia Português.

# In[262]:


urls = ['http://pt.wikipedia.org/wiki/Bras',
       'http://wikipedia.org/wiki/Bras',
       'https://pt.wikipedia.org/wiki/Bras',
       'http://pt.wikipedia.org/wik/Bras',
       'https://pt.wikipedia.org/wiki/Cubas']

for u in urls:
    ok = re.match('((http|https)://)?(pt.wikipedia.org/wiki/).+',u)
    if ok:
        print(ok.group())


# #### Compilação e literais
# 
# Até agora abordamos REs de uma maneira direta, mostrando como podemos localizar padrões pela utilização de alguns métodos. Vale comentar que REs podem ser compiladas como objetos mais abstratos. 
# 
# Para compilar expressões, podemos utilizar o método `compile`, no qual REs são manipuladas como strings. 

# **Exemplo:**

# In[199]:


rex = re.compile('[p-t]a[b-d]a?')
rex.findall(cubas)


# Aqui, `rex` é um objeto abstrato.

# In[174]:


print(type(rex))


# Se imprimirmos `rex`, veremos o seguinte:

# In[200]:


rex


# O prefixo `r` torna a string literal e serve para tratar problemas com escape. Todavia, deixaremos esta discussão para um momento posterior. Para saber mais, leia sobre a [Praga do Backspace](https://docs.python.org/3/howto/regex.html#the-backslash-plague).

# #### Recursos de aprendizagem
# 
# Para aprofundar seu entendimento sobre expressões regulares, recomendamos os seguintes sites: 
# 
# - [regex101.com](https://regex101.com)
# - [regexr.com](https://regexr.com)
# - [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
# - [Documentação do módulo `re`](https://docs.python.org/3/library/re.html)

# <!-- ## Exercícios
# 
# Encontrar padrões em uma permutação
# ___
# 
# Encontrar padrões em um filamento de DNA. Ciência forense.
# 
# https://www.sciencelearn.org.nz/resources/1980-dna-profiling
# 
# https://github.com/tvdaal/dna-patterns
# ___
# 
# dna_seq = 'CGTACTGACGTAGCTAGCTTGATTTCGAATCGCCCGCGTAGCTAGAGTCGATATAG'
# re.findall('[GAT]{2,3}',dna_seq)
#  -->
