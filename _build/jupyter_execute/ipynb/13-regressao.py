#!/usr/bin/env python
# coding: utf-8

# # Análise de regressão

# Como vimos no capítulo anterior, a correlação investiga se existe ou não interferência entre duas variáveis. Em particular, ela procura se ambas possuem algum grau de dependência linear. 
# 
# Um pouco além, a _análise de regressão_, ou simplesmente _regressão_, busca saber de que maneira uma variável pode predizer o comportamento da outra. Assim, no mundo real, algumas perguntas que procuramos responder são: 
# 
# - Como o volume de vendas de canetas esferográficas muda se o preço da unidade subir? 
# 
# - De que maneira a taxa de inflação deste ano prediz o aumento do aluguel para os próximos dois meses?
# 
# - A que horas seria melhor sair da universidade para evitar ficar preso pelo tráfego intenso na via?
# 
# ```{hint}
# O termo "regressão" deve-se ao estatístico inglês do século XIX Sir Francis Galton. Galton usou o termo para interpretar resultados de um experimento sobre hereditariedade, para o qual coletou alturas de pais e filhos para realizar predições sobre alturas das próximas gerações. Percebendo que a altura de um filho "regredia" (era menor do que) em relação à altura de seus pais por um fator de 2/3, publicou um artigo intitulado _Regression towards Mediocrity in Hereditary Stature_ que, ironicamente, deu surgimento ao nome que usamos para o método estatístico que estamos aprendendo. Galton não aplicou o _método dos mínimos quadrados_ (que é a base teórica para a regressão linear), já conhecido há 80 anos antes de sua época por Gauss e Legendre. Ele simplesmente "traçou uma reta". Para Galton, a "regressão" representava apenas uma tendência de os dados "reverterem" a tendência média. Isto é, a origem do método _regressão_ é uma "ironia do destino". Para saber a história completa, veja este [post](https://blog.minitab.com/en/statistics-and-quality-data-analysis/so-why-is-it-called-regression-anyway).
# ```
# 
# A estrutura comum de perguntas como essas é a seguinte: elas exigem uma _resposta_ que pode ser expressa como uma combinação de uma ou mais _variáveis independentes_ chamadas de _preditores_ ou _covariantes_. Dessa maneira, o objetivo da análise de regressão é _construir modelos preditivos a partir dos dados_.

# ## Regressão linear
# 
# O modelo mais básico de regressão é o linear. A _regressão linear_ procura ajustar um modelo matemático aos dados cuja resposta ${\bf y}$ depende linearmente de $d$ preditores. Em termos vetoriais, o modelo pode ser descrito como: 
# 
# $${\bf y} = a_1{\bf x}_1 + a_2{\bf x}_2 + \ldots + a_d{\bf x}_d,$$
# 
# em que os $a_i \in \mathbb{R}, \, i = 1,\ldots d$, são os _parâmetros_ ou _coeficientes_ do modelo e os ${\bf x}_i$ as variáveis. 
# 
# Se levarmos em conta $n$ observações de cada variável, cada um dos ${\bf x}_i$ e ${\bf y}$ são identificados como vetores do espaço $\mathbb{R}^n$, de maneira que a equação anterior pode ser reescrita como um _sistema matricial_ da forma ${\bf y} = {\bf X}{\bf a}$, onde: 
# 
# $${\bf y} = 
# \begin{bmatrix}
# y_1 \\
# y_2 \\
# \vdots \\
# y_n \\
# \end{bmatrix},
# \quad
# {\bf X} =
# \begin{bmatrix}
# x_{11} & x_{12} & \ldots & x_{1d} \\
# x_{21} & x_{22} & \ldots & x_{2d} \\
# \vdots & \vdots & \ddots & \vdots \\
# x_{n1} & x_{n2} & \ldots & x_{nd}
# \end{bmatrix},
# \quad
# {\bf a} = 
# \begin{bmatrix}
# a_1 \\
# a_2 \\
# \vdots \\
# a_n \\
# \end{bmatrix}
# $$
# 

# ### Regressão linear simples
# 
# A regressão linear simples assume um modelo "tipo reta", contendo apenas um regressor dado por
# 
# $${\bf y} = a_0 + a_1{\bf x},$$
# 
# onde $a_0$ é o _termo constante_, também chamado de _offset_ ou _intercept_, e $a_1$ é a _inclinação_.
# 
# Dessa forma, dados $n$ pares de valores $(x_i, y_i)$, para preditor e resposta, podemos encontrar $a_0$ e $a_1$ e, enfim, explicar como ambos se relacionam.
# 
# Entretanto, uma pergunta a se fazer é a seguinte: quais seriam os valores de $a_0$ e $a_1$ que produziriam a melhor reta para os dados? Em outras palavras, que reta melhor explicaria como ${\bf y}$ depende linearmente de ${\bf x}$?
# 
# A resposta é: a reta que produz os menores erros no sentido do método conhecido como _mínimos quadrados_ (_least squares_). 

# #### Mínimos quadrados
# 
# O _método dos mínimos quadrados_ sugere que a distância Euclidiana entre os valores preditos (modelados) e os valores dados deve ser _minimizada_. Na linguagem matemática, devemos encontrar $a_0$ e $a_1$ de maneira que o _resíduo_ (ou erro) ${\bf r}$
# seja o menor possível, isto é, que a norma
# 
# $$\|\bf{r}\|^2 =  \|\bf{y} - (a_0 + a_1\bf{x})\|^2 = \sum_{j=1}^{n}(y_j - a_0 - a_1x_j)^2,$$
# 
# seja minimizada.

# ## Estudo de caso: o gelo marinho e as mudanças climáticas
# 
# Vamos entender a _análise de regressão_ por meio de um estudo de caso. A pergunta que queremos responder é:
# 
# > A queda na área coberta por gelo no mar pode nos levar a crer que o clima está mudando? 
# 
# Vamos trabalhar com o _dataset_ G02135 - Sea Ice Index, Version 3, 
# do [NSIDC](https://nsidc.org/data/G02135/versions/3).

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sb
import scipy.stats as sts
import matplotlib.pyplot as plt


# In[2]:


#
sii = pd.read_csv('../database/Sea_Ice_Index_Monthly_Baffin-Area-km^2.csv')
month = 'jan'
s = sb.lmplot(x='year',y=month,data=sii,fit_reg=True);
s.set(title='Ice coverage area in Baffin Area [km2]');


# Comentários:
# 
# - A função `lmplot()` realiza a análise de regressão simples com o modelo linear (reta) a partir dos dados passados.
# - O _dataset_ em questão mostra que a área de cobertura do gelo está sob uma tendência de declínio desde 1980.
# - A reta da regressão pode ser retirada do gráfico usando `fit_reg=False`.

# A seguir, "desdobramos" o _DataFrame_ original para realizar uma análise de regressão durante os anos de 1997 a 2017 levando em conta valores mensais.

# In[3]:


# intervalo de 20 anos
siif = sii.set_index('year').loc[1997:2017]

# desdobra o DataFrame
siif2 = pd.DataFrame(columns=['year','month','area'])
for i in siif.index:
    # astype('float') necessário aqui, pois como 'Int64' temos erro de SVD em lmplot
    c1 = pd.Series(np.full(12,i)).astype('float')        
    c2 = pd.Series(range(1,13)).astype('float') 
    c3 = siif.loc[i]      
    d = pd.DataFrame({'year':c1,'month':c2,'area':c3.values})
    siif2 = pd.concat([siif2,d],axis=0)    


# In[4]:


sb.lmplot(x='month',y='area',data=siif2).set(title='Ice coverage in Baffin Area: 1997-2017 [km2]');    


# Comentários: 
# - Pode se ver que ao longo do ano, a cobertura de gelo segue um padrão periódico. Todavia, a análise de regressão mostra que há uma tendência de declínio da cobertura. 
# - A flutuação periódica é coerente com as estações do ano.
# - O declínio se verifica pela queda da amplitude do ciclo periódico.

# ### Normalização dos dados
# 
# Para evitar a flutuação, normalizaremos a área usando desvios em relação às médias mensais e o percentual relativo à média para o período de anos estudado. A expressão matemática é dada por:
# 
# $$\tilde{\bf a}_i = 100\frac{({\bf a}_i - \mu_i)}{\mu}, = 1,\ldots, 12$$
# 
# onde $\tilde{\bf a}_i$ é a série contendo valores das áreas normalizadas, ${\bf a}_i$ a série contendo valores das áreas originais, $\mu_i$ as médias, todas para o $i$-ésimo mês, e $\mu$ é a média das áreas para todo o período de 20 anos (todos os meses).

# In[5]:


import warnings; warnings.simplefilter('ignore') 

siif2['arean'] = siif2['area']

for i in np.linspace(1,12,12):
    siif2.arean[siif2.month == i] = 100*(siif2.arean[siif2.month == i] -                                          siif2.arean[siif2.month == i].mean())                                          /siif2.area.mean()


# Plotando os dados normalizados, vemos o seguinte gráfico.

# In[6]:


sb.lmplot(x='month',y='arean',data=siif2).set(title='Normalized data');    


# ### Regressão sobre dados normalizados
# 
# Realizando uma nova análise de regressão para todo o período de 20 anos, com 95% de índice de confiança, visualizamos uma permanente tendência negativa. 

# In[7]:


# eixo x como 'float' devido 
# à incompatibilidade de lmplot com type 'Int64'
sb.lmplot(x='year',y='arean',data=siif2).set(title='Ice coverage decay: 1997-2017 [km2]');


# A conclusão do estudo é: embora haja variações de ano a ano, nota-se uma tendência de queda na corbertura da área de gelo na área estudada. Esta diminuição da área de cobertura do gelo leva-nos a crer que o aquecimento global é a causa direta deste fenômeno.

# ### Análise quantitativa 
# 
# No caso anterior, fizemos uma análise qualitativa (visual) de como a área de cobertura de gelo (resposta) diminuiu ao longo do ano (preditor). Entretanto, não temos ideia da "cara" deste modelo ainda. Para saber a equação da análise de regressão, podemos utilizar alguns métodos. 

# #### `scipy.stats.linregress`
# 
# A primeira forma que temos de encontrar a equação do modelo linear é usando `scipy.stats.linregress`.

# In[8]:


res = sts.linregress(siif2['year'],siif2['arean'])

# inclinação, intercept, coef. de correlação
m,b,rho = res.slope,res.intercept,res.rvalue
(m,b,rho)


# In[9]:


plt.scatter(x=siif2['year'],y=siif2['arean'])

# eq. da reta
xx = np.unique(siif2['year'])
yy = m*xx + b

plt.plot(xx,yy,'r-',label=f'y={round(m,2)}x + {round(b,2)}')
plt.legend(loc=3);


# #### `sklearn.linear_model.LinearRegression`
# 
# A primeira forma que temos de encontrar a equação do modelo linear é usando `sklearn.linear_model.LinearRegression`.

# In[10]:


from sklearn.linear_model import LinearRegression

# modelo de ajuste
lr = LinearRegression(fit_intercept=True)

# resolvendo (input deve ser array 2D)
res2 = lr.fit(siif2[['year']],siif2[['arean']])

# slope, intercept
m2,b2 = res2.coef_[0][0], res2.intercept_[0]
m2,b2


# Comentários:
# 
# - Verificamos que os valores de slope e intercept obtidos pelo `sklearn.linear_model.LinearRegression` equivalem àqueles obtidos com `scipy.stats.linregress`.

# ### Preditores e estimadores
# 
# Estimadores geram predições a partir da análise de regressão. Usando o módulo `sklearn`, podemos avaliar quão bem o modelo construído se ajusta aos dados conhecidos atra'ves de duas métricas bastante populares: 
# 
# - _erro quadrático médio_ (ou _MSE_, do inglês _mean squared error_), que fornece uma "média" do quadrado dos $n$ erros existentes pontualmente entre as séries de dados conhecidos $\{y_i\}$ e de dados estimados $\{\hat{y}_i\}$. Ele pode ser definido em termos de um _preditor_ ou de um _estimador_. Ambos os conceitos são levemente distintos. Para nossos propósitos, vamos utilizar a definição do primeiro caso, que é:
# 
# $$\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i -\hat{y}_i)^2$$
# 
# Notemos que, em notação vetorial, $\text{MSE} = \frac{1}{n}({\bf e} \cdot {\bf e})$, com
# ${\bf e} = {\bf y} - \hat{\bf y}$.
# 
# - _coeficiente de determinação_, que mede a "qualidade" do ajuste. Este coeficiente é simplesmente o quadrado do coeficiente de correlação. Comumente, ele é denotado por $R^2$ e $ 0 \leq R^2 \leq 1$. Todavia, dependendo de como ele for definido, valores negativos são possíveis. Se $R^2 = 0$, o ajuste é o pior possível; se $R^2 = 1$, o melhor possível.
# 
# Vamos calcular essas métricas para um conjunto de dados do `sklearn` sobre diabetes.

# In[34]:


from sklearn import metrics, datasets


# In[55]:


# dataset "diabetes"
diabetes_x, diabetes_y = datasets.load_diabetes(return_X_y=True)

# usa apenas uma feature
diabetes_x = diabetes_x[:,np.newaxis,2]

# separação dos dados entre "treinamento" e "teste"
# a predição ocorrerá para o conjunto de "teste"

# preditor
diabetes_x_treino = diabetes_x[:-20] # 422 valores
diabetes_x_teste = diabetes_x[-20:] # 20 valores

# resposta
diabetes_y_treino = diabetes_y[:-20] # 422 valores
diabetes_y_teste = diabetes_y[-20:] # 20 valores

# modelo de RL
linregr = LinearRegression(fit_intercept=True)

# treinamento do modelo
linregr.fit(diabetes_x_treino,diabetes_y_treino)

# predição
diabetes_y_predicao = linregr.predict(diabetes_x_teste)


# Agora, verificamos a qualidade do ajuste dos dados pela regressão linear.

# In[52]:


metrics.mean_squared_error(diabetes_y_teste,diabetes_y_predicao)


# In[53]:


metrics.r2_score(diabetes_y_teste, diabetes_y_predicao)


# Uma plotagem gráfica simples nos dá a melhor reta de ajuste para os dados segundo o método de mínimos quadrados.

# In[79]:


plt.scatter(diabetes_x_teste,diabetes_y_teste,color='#ad1c12')
plt.plot(diabetes_x_teste,diabetes_y_predicao,'-k');


# Uma vez que temos à disposição os coeficientes de ajuste, podemos predizer valores em locais desconhecidos.

# In[100]:


m3,b3 = linregr.coef_[0],linregr.intercept_
print((m3,b3))

# plot
plt.scatter(diabetes_x_teste,diabetes_y_teste,color='#ad1c12')
plt.plot(diabetes_x_teste,diabetes_y_predicao,'-k');

# estimativas
x_est1, x_est2, x_est3 = 0.03, 0.10, 0.3
p = lambda x: m3*x + b3
plt.plot(x_est1,p(x_est1),'sg',ms=10)
plt.plot(x_est2,p(x_est2),'*b',ms=10)
plt.plot(x_est3,p(x_est3),'vm',ms=10);


# ## Regressão múltipla
# 
# Estenderemos a discussão sobre regressão apresentando um exemplo simples de regressão mútlipla. Como vimos anteriormente, na regressão múltipla haverá mais do que um preditor. Neste caso, em vez de uma reta, o modelo matemático é um _hiperplano_. Hiperplano é um termo que generaliza o conceito de plano em um espaço vetorial de $d$ dimensões.
# 
# O _dataset_ [Advertising.csv](https://github.com/gcpeixoto/ICD/blob/main/database/Advertising.csv) contém informação sobre orçamentos destinados para anúncios em TV, rádio e jornal, bem como do número de vendas. O objetivo é saber como esses orçamentos influenciam a venda de produtos.

# In[112]:


# importa statsmodels
import statsmodels.api as sm


# In[114]:


# carrega dataset
ad = pd.read_csv('../database/Advertising.csv',index_col=0)
ad.head()


# Realizamos a análise de regressão linear para verificar se poderíamos usar a variável `TV` para predizer as vendas.

# In[117]:


y_ad = ad['Sales']
X_ad = ad['TV']
X_ad = sm.add_constant(X_ad)

lr = sm.OLS(y_ad,X_ad).fit()

lr.summary()


# In[119]:


# R^2
lr.rsquared


# Comentário:
# 
# - $R^2 \approx 0.61$ indica que cerca de 61% da variância na relação TV-vendas pode ser explicada pelo modelo `lr`.

# In[124]:


plt.scatter(ad['TV'],ad['Sales']);
plt.xlabel('TV')
plt.ylabel('Vendas');


# Embora o valor de $R^2$ seja razoável, vamos repetir a análise, mas agora com a variávell `Radio`.

# In[127]:


y_ad2 = ad['Sales']
X_ad2 = ad['Radio']
X_ad2 = sm.add_constant(X_ad2)

lr2 = sm.OLS(y_ad2,X_ad2).fit()

lr2.summary()


# In[126]:


lr2.rsquared


# Neste caso, o modelo retorna um valor de $R^2$ pior que o anterior. Mas, e se ambos os preditores forem postos juntos no modelo?

# In[128]:


y_ad3 = ad['Sales']
X_ad3 = ad[['TV','Radio']]
X_ad3 = sm.add_constant(X_ad3)

lr3 = sm.OLS(y_ad3,X_ad3).fit()

lr3.summary()


# In[130]:


lr3.rsquared


# Com ambos os preditores, o valor de $R^2$ saltou para quase 90%, o que é um número melhor. Assim se forma a regressão múltipla.
# 
# Para ver o plano da regressão múltipla, devemos fazer um plot 3D. 

# In[144]:


from mpl_toolkits.mplot3d import Axes3D

# X e Y usando tamanhos deTV and Radio
X_axis, Y_axis = np.meshgrid(np.linspace(ad['TV'].min(), ad['TV']. max(), 100), 
                             np.linspace(ad['Radio'].min(), ad['Radio'].max(), 100))


# equação do hiperplano calculano o eixo Z correspondente (Sales)
# z = a0 + a1x + a2y
Z_axis = lr3.params[0] + lr3.params[1] * X_axis + lr3.params[2] * Y_axis

# Cria matplotlib 3D axes
fig = plt.figure(figsize=(12, 8)) # figsize refers to width and height of the figure
ax = Axes3D(fig, azim=-100)

 # Plota o hiperplane
ax.plot_surface(X_axis, Y_axis, Z_axis, cmap=plt.cm.coolwarm, alpha=0.5, linewidth=0)

# Plota pontos 
ax.scatter(ad['TV'], ad['Radio'],ad['Sales'])

# labels
ax.set_xlabel('TV'); ax.set_ylabel('Radio'); ax.set_zlabel('Sales');

