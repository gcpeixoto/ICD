#!/usr/bin/env python
# coding: utf-8

# ## Questionário Q24

# Orientações: 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-a à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# <hr>

# **Questão 1.** A ESPN forneceu o censo completo dos jogadores da copa de 2018. O arquivo <a href="data/copa2018.npy" download="data/copa2018.npy">copa2018.npy</a> contém uma tabela de peso, altura e idade de cada um desses atletas.  Com base nesses dados, crie os _arrays_ `altura`, `idade` e `peso`. Por fim, defina um _dict_ que associe esses dados aos respectivos jogadores.
# 
# O _Índice de Massa Corpórea_ (IMC) é usado para saber se um indivíduo está no peso ideal. Ele é definido pela fórmula:
# 
# $$IMC = \frac{M}{A^2},$$
# 
# onde $M$ é a massa (considere quilogramas) do indivíduo e $A$ é a sua altura (considere metros).
# 
# Determine quantos jogadores possuem $IMC$ menor do que 21.7 e quantos possuem $IMC$ maior do que 21.9. Em seguida, assinale a alternativa que, nesta ordem, é a correta.
# 
# A. 7 e 16
# 
# B. 7 e 12
# 
# C. 6 e 17
# 
# D. 5 e 14
# 
# **Dica:** Use a função do *numpy* `load('...')`, com a opção `allow_pickle=True` e manipule o _array_ bidimensional.

# <hr>
# 
# ## Gabarito
# Alternativa **B**
# 
# **_Obs_**: Os alunos provalmente vão fazer tudo na mão, o senhor tem a opção de disponibilizar o dataset ou fazer com que eles corram atrás, fiz usando ferramentas mais avançadas para facilitar pra mim, tenho ciência que eles não vão fazer dessa forma.

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ws = pd.read_html("https://www.espn.com.br/artigo/_/id/4310177/selecao-brasileira-veja-o-censo-completo-dos-jogadores-que-vao-a-copa")


# In[3]:


#As tabelas no site estão em ordem crescente de acordo com os atributos, vamos alterar e deixar de acordo com os nomes
ws0 = ws[0].sort_values(by=['Jogador'], ignore_index=True)
ws1 = ws[1].sort_values(by=['Jogador'], ignore_index=True)
ws2 = ws[2].sort_values(by=['Jogador'], ignore_index=True)


# In[45]:


#criando dataframe único com atributos
db = ws0
db["Peso"] = ws1["Peso"]
db['Idade'] = ws2["Idade"]
db


# In[13]:


altura = np.array(db["Altura"])
peso = np.array(db["Peso"])
idade = np.array(db["Idade"])

IMC = np.array(list(map(lambda x,y: x/y**2, peso,altura)))

grupo1 = [IMC < 21.7]
grupo2 = [IMC > 21.9]

count_true = len([_ for _ in grupo1[0] if _ == True in grupo1[0]])
count_false = len([_ for _ in grupo2[0] if _ == True in grupo1[0]])
f'{count_true} // {count_false}'


# **Questão 2.** A _Taxa Metabólica Basal_ (TMB) é a quantidade mínima de energia que o ser humano, em repouso, precisa para sobreviver. A _Equação de Mifflin - St. Jeor_ para calcular a TMB em kcal/dia (quilocalorias por dia) de pessoas do sexo masculino é dada por:
# 
# $$TMB = 10M + 6.25A-5I+5,$$
# 
# onde $M$ é a massa do indivíduo, $A$ sua altura e $I$ sua idade.
# 
# [[Fonte: Wiikipedia]](https://en.wikipedia.org/wiki/Basal_metabolic_rate)
# 
# Calcule a energia necessária total para a manutenção vital de todos os jogadores da seleção de 2018 durante um ano inteiro, isto é, a TMB anual. Considere 1 ano = 365 dias.
# 
# Calcule a TMB anual necessária para a manutenção vital de todos os jogadores da seleção de 2018 durante o quinquênio 2020 - 2024. Assuma que: 
# 
# - 1 ano = 365 dias;
# - o período inicia-se em 1 de janeiro de 2020 e 
# - a escalação do time permaneça inalterada no período.
# 
# Marque a alternativa que, corretamente, reporta a TMB total da equipe para os anos de 2022 e 2024. 
# 
# A. 2022: 4922219.625, 2024: 4838039.625
# 
# B. 2022: 4992720.9375, 2024: 4992720.9375
# 
# C. 2022: 4824820.9375, 2024: 4782845.9375
# 
# D. 2022: 4824820.9375, 2024: 4740870.9375

# <hr>
# 
# ## Gabarito
# Alternativa **D**
# 

# In[6]:


#E um ano
year = 365
TMB_eq = np.sum(list(map(lambda m,a,i: (10*m) + (6.25*a) - (5*i)+5, peso,altura,idade)))*365
TMB_eq


# In[7]:


#Durante 5 anos
TMB = {}
for i in range(5):
    TMB[2020+i] = np.sum(365*np.sum(list(map(lambda m,a,i: (10*m) + (6.25*a) - (5*i)+5, peso,altura,idade+i)))) # kcal necessárias por ano para o time
TMB


# **Questão 3:** O movimento executado por uma bola de futebol ao ser chutada a partir do campo por um jogador é similar ao movimento parabólico de um projétil. A velocidade da bola $V_b$ pode ser calculada pela expressão:
# 
# $$V_b = V_p\left( \dfrac{M_p}{M_p + M_b} \right)(1 + e),$$
# 
# onde $V_p$ é a velocidade da perna do chutador, $M_p$ é a massa da perna do chutador, $M_b$ é a massa da bola e $e$ é o *coeficiente de restituição* da bola. 
# 
# O alcance $a$ é a medida horizontal máxima que a bola atinge a partir do ponto de lançamento de acordo com um certo ângulo em que é lançada. Como conhecemos da Física Básica, a fórmula para o alcance é dada por: 
# 
# $$a = \dfrac{V_b^2\textrm{sen}(2\alpha)}{g}$$
# 
# Diante disso, considere os seguintes dados: 
# 
# - A massa da bola de futebol profissional é de 400 gramas e seu coeficiente de restituição é 0.7.
# - A massa da perna de um jogador equivale a 10% de sua massa.
# - A velocidade da perna de um jogador é de 20 m/s.
# - A constante gravitacional equivale a 9.8 m/s<sup>2</sup>.
# 
# Assuma que um campo de futebol profissional "padrão FIFA" possui área de 100 x 68 m<sup>2</sup>. Além disso, defina um *Whole-Field Kicker* (WFK) o jogador que, chutando uma bola a um ângulo de 45 graus, consegue transportá-la de gol a gol, ou seja de uma linha de fundo a outra, e como *Not Whole-Field Kicker* (not WFK) aquele que não consegue realizar esta proeza.
# 
# Usando os dados disponíveis na tabela dos jogadores da seleção de 2018, assinale a alternativa que contém o nome: do  melhor WFK do time (quem chuta mais longe) e do pior Not WFK.
# 
# [[Fonte: Physics of Kicking a Soccer Ball]](http://www.mathematicshed.com/uploads/1/2/5/7/12572836/physicsofkickingsoccerball.pdf)
# 
# 
# A. Alisson / William
# 
# B. Ederson / Neymar
# 
# C. Cássio / Fred
# 
# D. Ederson / Fagner

# <hr>
# 
# ## Gabarito
# 
# Alternativa **C**

# In[48]:


# vp: velocidade da perna do jogador (fixa: 20 m/s)
# mp: massa da perna do jogador (10% da massa do jogador)
# e: coeficiente de restituição da bola (média da bola oficial: 0.7)
# mb: massa da bola de futebol oficial (mb = 0.4 kg)
# alpha: angulo de lançamento da bola (chute)
# g: constante gravitacional (9.8 m/s2)

# velocidade da bola em m/s
vb = lambda vp,mp,mb,e: vp*(mp/(mp + mb))*(1 + e)

# formula do alcance: movimento projetil
alcance = lambda vb, alpha, g: vb**2*np.sin(2*alpha)/g

# Considere o campo FIFA: 100 m x 68 m

e = 0.7
vp = 20.0
mb = 0.4
g = 9.8
alpha = 45

MP = 0.2*db["Peso"] # massas perna
VB = vb(vp,MP,mb,e) # vels bola
ALC = alcance(VB,alpha,g)

# quais jogadores conseguem um 'chute de campo inteiro'
kicker = ALC >= 100

db["Alcance"] = ALC


# In[51]:


WFK = db[db["Alcance"] >= 100].sort_values(by="Alcance", ascending=False)
not_WFK = db[db["Alcance"] < 100].sort_values(by="Alcance", ascending=True)
WFK[:1]


# In[52]:


not_WFK[:1]


# In[ ]:




