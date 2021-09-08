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
# C. 2022: 4908770.9375, 2024: 4824820.9375
# 
# D. 2022: 4908770.9375, 2024: 4824820.9375

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
