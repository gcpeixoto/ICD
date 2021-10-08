#!/usr/bin/env python
# coding: utf-8

# ## Questionário 32 (Q32)

# Orientações: 
# 
# - Registre suas respostas no questionário de mesmo nome no SIGAA.
# - O tempo de registro das respostas no questionário será de 10 minutos. Portanto, resolva primeiro as questões e depois registre-as.
# - Haverá apenas 1 (uma) tentativa de resposta.
# - Submeta seu arquivo-fonte (utilizado para resolver as questões) em formato _.ipynb_ pelo SIGAA anexando-o à Tarefa denominada "Envio de arquivo" correspondente ao questionário.
# 
# *Nota:* o arquivo-fonte será utilizado apenas como prova de execução da tarefa. Nenhuma avaliação será feita quanto ao estilo de programação.
# 
# <hr>

# **Questão 1.** Marque a alternativa cujas funções são as utilizadas para imprimir as 4 primeiras e as 6 últimas linhas, respectivamente, de um _DataFrame_ `d`, tal que  `len(d) = 20`.
# 
# A. `df.head(6)`, `df.tail(4)`
# 
# B. `df.head(-6)`, `df.tail(4)`
# 
# C. `df.head(-16)`, `df.tail(6)`
# 
# D. `df.tail(-6)`, `df.tail(4)`

# <hr>
# 
# **Questão 2** No dia 01/08/2021, três veículos saíram de João Pessoa - PB (JPA) com destino a três cidades de outros estados com distâncias (em quilômetros) e durações de viagem (em horas) em relação à origem dadas pelo quadro abaixo. 
# 
# | Veículo | Estado    |Distância de JPA (km) | Duração (h) |
# |--------:|:----------|-----------------:|:-------------|
# |  VW Gol | Bahia     |              848 | 7,5          |
# |  BMW Z4 | Ceará     |              728 | 10           |
# |Chery QQ | Sergipe   |              640 | 9,5          |
# 
# Tendo chegado ao destino, verificou-se por meio de um sistema de monitoramento que às 13:45h desse mesmo dia, todos os veículos haviam registrado no velocímetro uma velocidade igual à velocidade média calculada para o percurso. Entretanto, a partir desse instante, o sistema mostrou que os veículos haviam acelerado de tal forma que, às 13:47h, a velocidade média havia aumentado em 12% de seu valor. 
# 
# Construa um _DataFrame_ `df` que calcule as velocidades e acelerações dos veículos – em unidades de metro e segundo – nos instantes de interesse e defina as variáveis a seguir:
# 
# - `a = df.loc['VW Gol']['Vel. inicial (m/s)']`
# 
# - `b = df.loc['BMW Z4']['Vel. final (m/s)']`
# 
# - `c = df.loc['Chery QQ']['Aceleração (m/s2)']`
# 
# Então, assinale a alternativa que corresponde à tupla `(a,b,c)`, com aproximação de duas casas decimais. 
# 
# A. (10.12, 20.20, 0.01)
# 
# B. (18.71, 20.96, 0.03)
# 
# C. (20.22, 22.65, 0.02)
# 
# D. (31.41, 22.65, 0.02)

# <hr>
# 
# **Questão 3.** O _dataset_ encontrado no arquivo [flights.csv](https://github.com/gcpeixoto/ICD/blob/main/database/flights.csv?raw=true) (_Box & Jenkins arline data_) registra a quantidade de passageiros transportados por uma companhia aérea entre 1949 e 1960.
# 
# Utilizando agrupamentos, determine: 
# 
# - `y`: o ano em que o maior número de passageiros foi transportado;
# - `p`: o total de passageiros transportados no ano `y`;
# - `m1, m2, m3`: os 3 meses que, na média, transportaram os maiores números de passageiros ao longo desses anos (TOP 3);
# 
# Assinale a alternativa que corresponde aos valores corretos dessas variáveis na seguinte ordem: `y`, `p`, `(m1,m2,m3)`.

# A. 1957, 4421, (Jul, Ago, Set)
# 
# B. 1960, 5714, (Jul, Ago, Jun)
# 
# C. 1960, 5714, (Nov, Fev, Jan)
# 
# D. 1951, 2042, (Ago, Set, Out)
