#!/usr/bin/env python
# coding: utf-8

# ## Questionário Q23

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

# **Questão 1.** Está transcrito abaixo o poema _Se_, datado de 1895 e de autoria do escritor anglo-indiano Rudyard Kipling (Prêmio Nobel de Literatura – 1907). O poema foi publicado pela primeira vez apenas em 1910 em uma coletânea de contos e poemas intitulada _Rewards and Fairies_.
# 
# > _Se és capaz de manter a tua calma quando
# Todo o mundo ao teu redor já a perdeu e te culpa;
# De crer em ti quando estão todos duvidando?
# E para esses no entanto achar uma desculpa;
# Se és capaz de esperar sem te desesperares?
# Ou? enganado? não mentir ao mentiroso?
# Ou? sendo odiado? sempre ao ódio te esquivares?
# E não parecer bom demais? nem pretensioso;
# Se és capaz de pensar –sem que a isso só te atires?
# De sonhar –sem fazer dos sonhos teus senhores.
# Se encontrando a desgraça e o triunfo conseguires
# Tratar da mesma forma a esses dois impostores;
# Se és capaz de sofrer a dor de ver mudadas
# Em armadilhas as verdades que disseste?
# E as coisas? por que deste a vida? estraçalhadas?
# E refazê-las com o bem pouco que te reste;
# Se és capaz de arriscar numa única parada
# Tudo quanto ganhaste em toda a tua vida?
# E perder e? ao perder? sem nunca dizer nada?
# Resignado? tornar ao ponto de partida;
# De forçar coração? nervos? músculos? tudo
# A dar seja o que for que neles ainda existe,
# E a persistir assim quando? exaustos? contudo
# Resta a vontade em ti que ainda ordena: “Persiste!”;
# Se és capaz de? entre a plebe? não te corromperes
# E? entre reis? não perder a naturalidade?
# E de amigos? quer bons? quer maus? te defenderes?
# Se a todos podes ser de alguma utilidade?
# E se és capaz de dar? segundo por segundo?
# Ao minuto fatal todo o valor e brilho?
# Tua é a terra com tudo o que existe no mundo
# E o que mais – tu serás um homem? ó meu filho!_
# 
# Fonte: [Revista Prosa Verso e Arte](https://www.revistaprosaversoearte.com/conheca-se-um-dos-mais-belos-poemas-de-todos-os-tempos-de-rudyard-kipling/).
# 
# Entretanto, diferentemente da versão original, esta transcrição contém pontos de interrogação onde deveria haver vírgulas. Use seus conhecimentos de operações com arquivos para criar um arquivo chamado `"Se_RK.txt"`no qual a versão corrigida deve ser salva. Em seguide, quebre duas linhas e apense o nome do autor, _Rudyard Kipling_ ao arquivo. 
# 
# Assinale a alternativa cuja tupla corresponda, respectivamente, ao número de vírgulas substituídas e ao número total de caracteres no arquivo após a inclusão do nome do autor.
# 
# A. (38, 1452)  
# 
# B. (39, 1437)
# 
# C. (38, 1454)
# 
# D. n.d.a.

# <hr>
# 
# ## GABARITO
# 
# Alternativa **A**

# In[8]:


#texto da questão acima
with open('textt.txt','r+') as t:
    textt = t.read()
#Já vou realizar a contagem das vírgulas já que vou substituir ? por ,   
count = 0
Se_RS = ""
for _ in textt:
    if _ == "?":
        count+=1
        Se_RS+=","
    else:    
        Se_RS+= _
print(Se_RS)


# In[9]:


with open("Se_RS.txt",'w') as f:
    f.write(Se_RS)

    
with open('Se_RS.txt','a') as f:
    f.write("\n\nRudyard Kipling")
    
with open('Se_RS.txt','r+') as f:
    content = f.read()
    
print(f"Resposta esperada: {count,len(content)}")


# **Questão 2.** Em Python, o módulo `os` fornece funções específicas para manipular caminhos e transitar arquivos. Marque a alternativa cujas funções do submódulo `path` listadas são utilizadas para retornar o tamanho de um arquivo e realizar teste de sua existência no disco.
# 
# A.`getfn()` / `isdir()`
# 
# B.`join()` / `isfile()`
# 
# C.`isfile()` / `getsize()`
# 
# D.`getamount()` / `isfile()`

# <hr>
# 
# ## Gabarito
# Alternativa **C**

# <hr>
# 
# **Questão 3**. Em criptografia, diversos métodos são utilizados para proteger o conteúdo de mensagens. A tabela abaixo representa um sistema hipotético de criptografia que associa caracteres Unicode por "transliteração". Ou seja, mensagens escritas com caracteres em um sistema original são reveladas por caracteres equivalentes da Língua Portuguesa.
# 
# |  Escape  |Original |Equivalente|
# |----------|---------|-----------|
# |  \u0061  |    ʠ    |     a     |
# |  \u0062  |    ʡ    |     b     |
# |  \u0063  |    ʢ    |     c     |
# |  \u0064  |    ʣ    |     d     |
# |  \u0065  |    ʤ    |     e     |
# |  \u0066  |    ʥ    |     f     |
# |  \u0067  |    ʦ    |     g     |
# |  \u0068  |    ʧ    |     h     |
# |  \u0069  |    ʨ    |     i     |
# |  \u006A  |    ʩ    |     j     |
# |  \u006B  |    ʪ    |     k     |
# |  \u006C  |    ʫ    |     l     |
# |  \u006D  |    ʬ    |     m     |
# |  \u006E  |    ʭ    |     n     |
# |  \u006F  |    ʮ    |     o     |
# |  \u0070  |    ʯ    |     p     |
# |  \u0071  |    ΰ    |     q     |
# |  \u0072  |    α    |     r     |
# |  \u0073  |    β    |     s     |
# |  \u0074  |    γ    |     t     |
# |  \u0075  |    δ    |     u     |
# |  \u0076  |    ε    |     v     |
# |  \u0077  |    ζ    |     w     |
# |  \u0078  |    η    |     x     |
# |  \u0079  |    θ    |     y     |
# |  \u007A  |    ι    |     z     |
# 
# 
# Crie uma função que "decodifica" palavras escondidas no sistema original em palavras equivalentes em nossa língua (p.ex: `ʢʠʬʠ` => `cama`) e assinale a alternativa que contém a palavra equivalente ao anagrama `ʨʭʣδʡʨγʠεʤʫʬʤʭγʤ`:
# 
# A. 'inevitavelmente'
# 
# B. 'indiscutivelmente'
# 
# C. 'indubitavelmente'
# 
# D. 'indiscretamente'
# 
# _Dica:_ para sequências de escape, vide [[aqui]](https://www.rapidtables.com/code/text/unicode-characters.html).

# <hr>
# 
# ## GABARITO 
# Alternativa **C**

# Criação da tabela code

# In[3]:


bas = [str(i) for i in range(0,10)] + ['A','B','C','D','E','F']
letras = [r"\u00" + str(i) for i in range(61,70)] + [r"\u006" + bas[10+i] for i in range(6)] + [r"\u00" + str(i) for i in range(70,80)] + [r"\u007A"]
codes = [r'\u02A' + i for i in bas] + [r'\u03B' + i for i in bas[:10]]

d = dict(zip(letras,codes))
print(21*'-')
print('|  Escape  | Unicode |\n' + '|' + 10*'-' + '|' + 9*'-' + '|')
for k,v in d.items():
    aux = v.encode('utf-8').decode('unicode-escape')
    print('| ',k,' |   ', aux,'   |')
print(21*'-')


# Função para decodificar a mensagem

# In[4]:


def my_decode(a):
    name_reverse = []
    sep = [a[_] for _ in range(len(a))]
    for x in range(len(sep)):
        for a,b in d.items():
            if sep[x] == b.encode('utf-8').decode('unicode-escape'):
                name_reverse += a.encode('utf-8').decode('unicode-escape')
    
    return "".join(name_reverse)   


# In[5]:


my_decode('ʨʭʣδʡʨγʠεʤʫʬʤʭγʤ')


# In[ ]:




