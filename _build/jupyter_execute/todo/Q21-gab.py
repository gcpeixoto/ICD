#!/usr/bin/env python
# coding: utf-8

# ## Questionário 21
# 
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

# **Questão 1**. As rodovias federais brasileiras interligam cidades, estados e regiões. De acordo com o Departamento Nacional de Infraestrutura de Transportes (DNIT), há 5 categorias de rodovias: radiais, longitudinais, transversais, diagonais e de ligação.
# 
# Fonte: [DNIT](https://www.gov.br/dnit/pt-br/rodovias/rodovias-federais/nomeclatura-das-rodovias-federais).
# 
# Usando _listcomps_, desenvolva um programa que organiza os códigos das rodovias que passam pelo estado da Paraíba separando os algarismos da sigla "BR" e assinale a alternativa correta quanto ao número de rodovias por categoria:
# 
# A. 1 longitudinais / 4 transversal / 3 diagonal / 4 de ligação  
# 
# B. 2 longitudinais / 4 transversal / 3 diagonal / 6 de ligação  
# 
# C. 4 longitudinais / 1 transversal / 1 diagonal / 6 de ligação  
# 
# D. 5 longitudinais / 1 transversal / 3 diagonal / 6 de ligação  

# ### Gabarito
# 
# - BR-101, BR-104, BR-110, BR-116;
# - BR-230; 
# - BR-361;
# - BR-405, BR-408, BR-412, BR-426, BR-427, BR-434.
# 
# Alternativa C.

# In[1]:


rodovias = ["BR-101","BR-230","BR-104","BR-408","BR-412","BR-110","BR-361","BR-426","BR-427","BR-116","BR-405","BR-434"]


# In[3]:


#GABARITO Q1
#Criando listas de categoria
categorias = ["Radial","Longitudinal","Transversais","Diagonais","Ligação"]
#separador
algarismos = [x[3:] for x in rodovias] #Ou pode ser usado o x.split("-")

#identificando o numero chave do algarimo
identify = [int(i[0][0]) for i in algarismos]

#relacionando o valor chave e sua categoria
categorias_relacionadas = [categorias[identify[k]] for k in range(len(identify))]

#concatenando o codigo de br com sua categoria
resultado = [rodovias[a] + " " + categorias_relacionadas[a] for a in range(len(rodovias))]; resultado


#   

#  

# **Questão 2**. Segundo o Balanço Energético Nacional 2019, a matriz elétrica brasileira estava distribuída segundo o gráfico abaixo:
# 
# ```{figure} ../figs/q/ben.png
# ---
# width: 400px
# name: ben
# ---
# Fonte: Matriz elétrica brasileira em 2019
# ```
# 
# Fonte: [[EPE]](https://www.epe.gov.br/pt/abcdenergia/matriz-energetica-e-eletrica).
#         
# 
# Crie um dicionário em que as _keys_ e _values_ correspondam, respectivamente, às fontes de energia e ao percentual na matriz. Considere que:
# 
# - _i_ é o índice da _key_ "Biomassa" no _dict_ ordenado por valor percentual **crescente**;
# - _j_ é o índice da _key_ "Eólica" no _dict_ ordenado por valor percentual **decrescente**.
# 
# Assinale a alternativa correta:
# 
# A. _i_ = 4, _j_ = 2
# 
# B. _i_ = 5, _j_ = 3
# 
# C. _i_ = 0, _j_ = 7
# 
# D. _i_ = 3, _j_ = 6

# ### Gabarito
# 
# Alternativa A.

# In[2]:


M_el = {'Carvão e derivados': 3.3, 'Hidráulica': 64.9, 'Nuclear': 2.5, 'Gás natural': 9.3, 
        'Solar': 1, 'Eólica' : 8.6, 'Biomassa': 8.4, 'Derivados de petróleo': 2 }


# a) Crie uma função para exibir de forma crescente as porcentagens do dicionário acima e suas respectivas fontes de energia:

# In[5]:


# COLOQUE SEU CÓDIGO AQUI


# b) Agora faça o mesmo sendo que de forma decrescente.

# In[6]:


# COLOQUE SEU CÓDIGO AQUI


# c) Crie uma função para indicar a fontes que é mais utilizada e a que é menos utilizada na Matriz Elétrica.

#  

# In[34]:


#Célula para mostrar a resolução, remover célula na hora de mandar para os alunos

#Resolução a)

def crescente(x):
    y = []

    for i in sorted(x, key = x.get):
        y.append([i, x[i]])

    for i in range(len(y)):
        print("{} : {}%" .format(y[i][0], y[i][1]))
        
#Resolução b)

def decrescente(x):
    y = []

    for i in sorted(x, key = x.get, reverse = True):
        y.append([i, x[i]])

    for i in range(len(y)):
        print("{} : {}%" .format(y[i][0], y[i][1]))

#Resolução c)
def MaioreMenor(x):
    y = []

    for i in sorted(x, key = x.get, reverse = True):
        y.append([i, x[i]])

    print("A maior é a {} com {}%" .format(y[0][0], y[0][1]))
    print("A menor é a {} com {}%" .format(y[len(y) - 1][0], y[len(y) - 1][1]))
    
crescente(M_el)    
print('\n')
decrescente(M_el)


#  

# **Questão 3**: Para que um número de CPF (Cadastro de Pessoa Física) brasileiro seja considerado válido, a soma de todos os seus números deve resultar em um número com dois dígitos iguais. Por exemplo, o número de CPF $003.939.708-41$ é válido porque 
# 
# $$0 + 0 + 3 + 9 + 3 + 9 + 7 + 8 + 4 + 1 = 44.$$
# 
# Adicionalmente, a sua autenticidade pode ser verificada observando o último número antes do hífen, o qual determina o estado de origem daquele número de CPF. Considerando que um número de CPF possa ser escrito pela máscara
# 
# $$abc.def.ghi\text{-}jk,$$
# 
# o estado ao qual o número de CPF pertence será determinado a partir da correspondência abaixo.
# 
# - $i=0$: Rio Grande do Sul    
# - $i=1$: Distrito Federal – Goiás – Mato Grosso – Mato Grosso do Sul – Tocantins    
# - $i=2$: Pará – Amazonas – Acre – Amapá – Rondônia – Roraima    
# - $i=3$: Ceará – Maranhão – Piauí    
# - $i=4$: Pernambuco – Rio Grande do Norte – Paraíba – Alagoas    
# - $i=5$: Bahia – Sergipe    
# - $i=6$: Minas Gerais    
# - $i=7$: Rio de Janeiro – Espírito Santo
# - $i=8$: São Paulo
# - $i=9$: Paraná – Santa Catarina
# 
# Fonte: [[ACE Guarulhos]](https://www.aceguarulhos.com.br/blog/como-saber-se-um-cpf-e-verdadeiro/#gsc.tab=0)
# A função a seguir cria _n_ CPFs fictícios de modo aleatório:
# 
# ```python
# import random 
# def random_cpf(n):
#     random.seed(38)
#     cpf = []    
#     for _ in range(n):              
#         n = random.randrange(10000000000,99999999999)
#         cpf.append(n)
#     return cpf 
# ```    
# 
# Execute esta função para _n_=2. Em seguida, faça um programa para checar se os CPFs gerados são válidos ou inválidos, bem como para determinar o estado brasileiro desses CPFs. Assinale a alternativa correta.
# 
# A. Existem apenas 3 CPFs válidos e 1 deles pertence ao Acre.
# B. Existem apenas 5 CPFs válidos e 2 deles pertencem a São Paulo.
# C. Existe apenas 1 CPF válido, pertencente a Rondônia.
# D. Todos os CPFs são válidos, exceto o último da lista.
# 
# **Dica:** use expressão regular.

# ### Gabarito 
# 
# Alternatva B.
# 
# ##### Função de gerar os cpfs, limpar a parte do gabarito

# ##### Atenção professor, retirar toda a parte comentada, corresponde a resolução

# In[33]:


#toda a parte comentada corresponde a resolução da questão, RETIRAR DO NOTEBOOK
import random 
def random_cpf(n):
    random.seed(38)
    cpf = []
    #cpf_valido = []
    #valido = 0
    for _ in range(n):              
        n = random.randrange(10000000000,99999999999)
        cpf.append(n)
        #x = str(n)
        #s = str(sum([int(digit) for digit in x]))
        #if s[0] == s[1]:
            #valido+=1
            #cpf_valido.append(n)
        #s = 0   
    return cpf #valido, cpf_valido


# In[37]:


cpfs = random_cpf(20);cpfs
#COLOQUE SEU CÓDIGO AQUI (crie mais células abaixo se necessário)


# Assinale e marque a resposta correta:
# - a) São válidos apenas 3 CPFs, e são de, respectivamente: 
#         'Minas Gerais', 'São Paulo', 'Pernambuco – Rio Grande do Norte – Paraíba – Alagoas', 'São Paulo'.
# 
# 
# - b) É válido apenas 1 CPF, e é de:
#          'São Paulo'.
# 
# 
# 
# - c) São válidos apenas 2 CPFs,e são de  respectivamente:
#          'São Paulo', 'Pernambuco – Rio Grande do Norte – Paraíba – Alagoas'.
#   
#   
# 
# - d) São válidos apenas 5 CPFs, e são de, respectivamente:
#          'Minas Gerais', 'Pará – Amazonas – Acre – Amapá – Rondônia – Roraima', 'São Paulo',
#          'Pernambuco – Rio Grande do Norte – Paraíba – Alagoas', 'São Paulo'.
#          
#          
#          
# - e) Nenhum CPF é válido, visto que são numeros gerados aleatóriamente tornando quase impossível conter tal coincidência!        

# ### GABARITO

# In[28]:


#Para rodar daqui em diante é necessário descomentar as funções anteriores
#verificando qual o melhor seed para a criação da função, utilizar seed=38, VAI CONTER 5 CPFS VÁLIDOS
s = 1
maior = 0
while s < 50:
    cpf = random_cpf(20,s)
    if cpf[1] > maior:
        seed,maior,cpf_valido = s, cpf[1],cpf[2]
    s += 1
print(f"O seed: {seed}, obteve {maior} CPFs válidos: {cpf_valido}")


# In[29]:


#Após obter os cpfs válidos, sempre vai corresponder a estes locais
#importando biblioteca necessária
import re
#criando lista de possíveis lugares
lugares = ["Rio Grande do Sul","Distrito Federal – Goiás – Mato Grosso – Mato Grosso do Sul – Tocantins",
          "Pará – Amazonas – Acre – Amapá – Rondônia – Roraima","Ceará – Maranhão – Piauí",
          "Pernambuco – Rio Grande do Norte – Paraíba – Alagoas","Bahia – Sergipe", "Minas Gerais",
          "Rio de Janeiro – Espírito Santo", "São Paulo","Paraná – Santa Catarina"] #Pode ser usado dict
#função para localizar
def localyze(s):
    lista= []
    lugar = []
    a = [str(s[_]) for _ in range(len(s))]
    #usando a função espressões regulares para pegar apenas o digito que nos interessa
    x = [re.findall('[0-9]', a[_][8]) for _ in range(len(a))]
    #criando lista com os index correspondente a lista de lugares
    lista.extend([int(x[i][0]) for i in range(len(x))])
    #criando lista com lugares correspondentes a lista criada
    lugar.extend(lugares[lista[i]] for i in range(len(x)))
    return lugar


# In[30]:


localyze(cpf_valido)

