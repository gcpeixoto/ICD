#!/usr/bin/env python
# coding: utf-8

# ## Algoritmo de avaliação personalizado (ICD)
# 
# Lucas Miranda de Aguiar

# In[1]:


import pandas as pd
import numpy as np
import random


# ##### Alunos Ativos no SIGAA (em ordem alfabética)

# In[2]:


alunos = pd.read_excel("notas_GDCOC0089_T01_20211.xls")


# In[3]:


matriculas_alun = ["20180042677 - ANA PAULA CARDOSO DE CASTRO KENDALL", "20200111286 - ÂNGELA THAÍS ALVES DA SILVA",
                   "20200026560 - CLELIO SANDOVAL DA FONSECA", "20190035175 - FRANCELINO TEOTONIO JUNIOR",
                   "20200112309 - GABRIEL BARBOSA FERRAZ JARDIM", "20200026247 - GUILHERME HERCULANO FERNANDES",
                   "20200161250 - GUILHERME IRAM SILVA ARAUJO", "20200114706 - GUILHERME PUJONI MENEZES",
                   "20190133775 - IKARO HENRIQUE MONTEIRO ANDRADE", "20200154050 - INGRID DAYANE DA SILVA FERREIRA",
                   "20200024162 - ISMAEL ALVES LIMA", "20200139170 - JANSEN CRUZ DE SOUZA",
                   "20200088188 - JOSUE CALEB AVELINO DOS SANTOS","20190033519 - KENYO MAILTON DA SILVA OLIVEIRA",
                   "20180116153 - LEANDRO QUEIROZ CIRINO ARAUJO", "20190036379 - LUIS HENRIQUE AUGUSTO DE LIMA",
                   "11510431 - MANOEL CLEONALDO MENDES PEREIRA SOBRINHO", "20200133309  - MARCOS DANTAS GUIMARAES FILHO",
                   "20200026200 - MARIA IARA DE ARAUJO", "20200025900 - MARIA RAQUEL SOUZA MARTINEZ",
                   "20170052034 - MARIANA FRANZ MARROQUIM","20200025508 - MATHEUS VICTOR ALVES BRAGA MACIEL",
                   "11507225 - RAMON AZEVEDO DOS SANTOS CAVALCANTI", "20200026327 - RENAN CAVALCANTI FLORENTINO",
                   "20180044519 - RHUAN GABRIEL DO NASCIMENTO GALDINO", "20180034639 - SAULO DE ALMEIDA ATAIDE NETO",
                   "20200025983 - TALES NOBRE LEITE DIAS DE OLIVEIRA", "20190145696 - VIVIANNY KHATLY MEDEIROS PEREIRA",
                   "20200116827 - WEDSON CHAVES DE SOUSA", "20200024583 - WILSON FILLIPE DO NASCIMENTO LIMA"]


# ##### Criação do DataFrame, todos os valores precisam começar com 0 e posteriormente vai modificando de acordo com a nota do aluno

# In[5]:


#Ta com notas random apenas para testes.

notas = pd.DataFrame({"A2": [random.randint(0,10)], "Q21":[random.randint(0,10)],"Q22":[random.randint(0,10)],"Q23":[random.randint(0,10)],"Q24":[random.randint(0,10)],"Q25":[random.randint(0,10)]},index = matriculas_alun)


# In[6]:


notas["A3"]  = 0
notas["Q31"] = 0
notas["Q32"] = 0

notas["A4"]  = 0
notas["Q41"] = 0
notas["Q42"] = 0
notas["Q43"] = 0
notas["Q44"] = 0

notas["A5"]  = 0
notas["Q51"] = 0
notas["Q52"] = 0

notas["A6"]  = 0
notas["Q61"] = 0
notas["Q62"] = 0

notas["A7"]  = 0
notas["Q71"] = 0
notas["Q72"] = 0
notas["Q73"] = 0
notas["Q74"] = 0


# #### Função para inserção de notas

# In[7]:


def insere(df):
    ## dados do aluno para modificação das notas
    aluno = input("Insira a matrícula: ")
    aluno = aluno + " - " + input("Insira o nome completo: ").upper()
    alvo = input("Qual atividade será atribuida nota? (Ex: Q32) ")
    nota = float(input("Insira a nota do aluno para essa atividade: "))
    
    #contador para alterar valores em lista
    count = 0
    #criando nova lista pra modificar o dataset
    lista = np.ones(len(df[alvo]))
    
    #modificando nota específica
    for x,y in df[alvo].items():
        if x == aluno:
            lista[count] = lista[count]*nota
        else:
            lista[count] = lista[count]*y
        
        count+=1
           
    df[alvo] = lista
    return df


# Inserindo a nota do A2 em Francelino

# In[8]:


insere(notas);notas


# ## Nota das partes
# 
# $$
# \begin{array}{rcl}
# N_p&=&0,5(A_p)+\sum_{i} x_i(Qpi)\\
#     \\
# \end{array}
# $$
# - p: parte
# - Qpi: questionário i da parte p
# - xi: peso do questionário Qpi (igual para todos os Qpi, obedecendo a soma 0,5)

# In[10]:


#É preciso ir colocando as notas gradativamente, primeiro a parte 2, dps a parte 3...

def nota_partes(df):
    #Inserindo a parte
    parte = int(input("Inisira a parte: ")) 
    
    #Selecionando os questionários correspondentes a parte
    if parte == 2:
        Q = df.loc[:,["Q21","Q22","Q23","Q24","Q25"]]
    elif parte == 3:
        Q = df.loc[:,["Q31","Q32"]]
    elif parte == 4:
        Q = df.loc[:,["Q41","Q42","Q43","Q44"]]
    elif parte == 5:
        Q = df.loc[:,["Q51","Q52"]]
    elif parte == 6:
        Q = df.loc[:,["Q61","Q62"]]        
    elif parte == 7:
        Q = df.loc[:,["Q71","Q72","Q73","Q74"]]
    else:
        print("Parte inválida.")
        return 0
    
    #Formula da nota das partes 
    df["Parte "+str(parte)] = (0.5*df["A"+str(parte)])+(np.array([sum((0.5/len(Q.columns)) * Q.values[_]) for _ in range(len(Q))]))
    
    #retorna a matrícula, o nome e a nota da parte.
    return Q.join(df.loc[:,["A"+str(parte),"Parte "+str(parte)]])


# Observe a nota de Francelino

# In[11]:


nota_partes(notas)


# ## Nota das unidades
# 
# $$
# \begin{array}{rcl}
# N_u&=&\frac{1}{P}*\sum_{p=1}^p N_p\\
#     \\
# \end{array}
# $$
# - u: unidade
# - Np: nota da parte
# - P: numero de partes

# In[12]:


def nota_unidade(df):
    #Inserindo a unidade
    unidade = int(input("Inisira a unidade: ")) 
    
    #Selecionando a parte correspondente
    if unidade == 1:
        P = notas.loc[:,["Parte 2"]]
    elif unidade == 2:
        P = notas.loc[:,["Parte 3", "Parte 4"]]
    elif unidade == 3:
        P = df.loc[:,["Parte 5","Parte 6"]]
    elif unidade == 4:
        P = df.loc[:,["Parte 7"]]        
    else:
        print("Unidade inválida.")
        return 0
    
    #Formula da nota das partes            
    df["Und. "+str(unidade)] = (1/(len(P.columns)))*(np.array([sum(P.values[_]) for _ in range(len(P))]))
    
    return P.join(df.loc[:,["Und. "+str(unidade)]])


# In[13]:


nota_unidade(notas)


# ## Nota das FINAL
# 
# $$
# \begin{array}{rcl}
# N_f&=&\sum_{u=1}^4 0,1N_u + 0,6 NPF\\
#     \\
# \end{array}
# $$
# - u: unidade
# - Nf: nota final
# - NPF: Nota do projeto final

# In[16]:


notas["NPF"] = 0
#basta chamar a função insere(notas) e atribuir os valores do projeto final


# In[18]:


def nota_final(df):
    n_u = df.loc[:,["Unid. 1","Unid. 1","Unid. 1","Unid. 1","Unid. 1"]]
    df['NotaFinal'] = 0.1*n_u.values + 0.6*df['NPF']
    return n_u.join(df.loc[:,['NotaFinal']])

