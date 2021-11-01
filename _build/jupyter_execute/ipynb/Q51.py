#!/usr/bin/env python
# coding: utf-8

# ## Questionário 51 (Q51)

# 
# 
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

# **Questão 1.** Considere a descrição dos quatro problemas a seguir.
# 
# *Problema I:* 
# 
# > Sistemas de recomendação oferecem serviços a usuários com base na análise de seus perfis e preferências. Considere que você recebeu a atribuição de desenvolver um sistema de recomendação para clientes a partir da atividade deles na plataforma _Twitter_. Sabe-se que os usuários do _Twitter_ podem se comunicar de maneira aberta e livre, desde que respeitem as diretrizes da empresa. Você então coletou 1000 _tweets_ provenientes de 100 usuários escolhidos aleatoriamente e observou três comportamentos: pessoas que se comunicavam de maneira rude (uso desenfreado de xingamentos e impropérios); pessoas que se comunicavam de maneira moderada (uso de vocabulário informal, porém isento de palavras de baixo calão) e pessoas que se comunicavam de maneira formal (uso zero de palavras ofensivas). A partir disso, você começou a perceber através de uma pesquisa exploratória que a maioria das pessoas que se comunicavam de maneira rude acompanhavam páginas que abordavam assuntos relacionados a futebol e política. Já as pessoas que se comunicavam de maneira moderada acompanhavam páginas sobre jogos de entretenimento e música. Por fim, as pessoas que se comunicavam de maneira formal se interessavam mais por ciência e portais de notícia.
# 
# *Problema II:* 
# 
# > O consumo crescente das famílias eleva a taxa de produção de resíduos e,  consequentemente alerta os órgãos de gestão ambiental e do lixo. Suponha que a companhia responsável pela coleta de lixo em um munícipio brasileiro seja capaz de monitorar o volume de lixo orgânico e inorgânico produzido em cada bairro do município e de registrar tais informações em um grande banco de dados. Então, a companhia, em parceria com o governo estadual, começa a realizar estudos para implantar biodigestores de grande escala nos locais mais críticos do município para acelerar a decomposição da matéria orgânica e reduzir a sobrecarga de lixões. Os gestores decidem contratar você para ajudar a empresa a identificar os bairros ou microrregiões que produzem a maior quantidade de lixo semanalmente e assim ter uma ideia sobre onde seriam os lugares mais propícios para a instalação dos biodigestores. 
# 
# *Problema III:*
# 
# > Um hospital especializado em traumatologia possui um setor que pode atender casos gerais de emergência e dispõe de uma lista dos pacientes atendidos. Suponha que um número considerável de pessoas com sintomas de acidente vascular cerebral - AVC procurem o hospital mensalmente e que, para cada paciente com esse quadro, sejam feitas as seguintes perguntas: 
# > - Qual é a sua idade? 
# > - Você é fumante? 
# > - Você é casado? 
# > - De um a quatro, qual seu nível de estresse no trabalho? 
# > - Você mora em área rural ou urbana? 
# > - Você tem hipertensão? 
# > - Já teve algum ataque cardíaco? 
# >
# > As respostas são registradas em um prontuário e simultaneamente enviadas para o banco de dados do hospital. Tempos depois, desejando aperfeiçoar sua capacidade de atendimento emergencial e imediato, a administração central do hospital contrata você como cientista de dados para desenvolver um sistema capaz de predizer se um potencial paciente que adentrou no setor de emergência com sintomas similares a AVC esteja, de fato, sofrendo um AVC.
# 
# *Problema IV:* 
# 
# > A imobiliária CondoSmart está programando um evento para estimular a venda de casas em condomínio. Seus imóveis estão registrados em uma planilha de _x_ linhas e _p_ colunas. Atualmente, _x = 200_ é o número de casas disponíveis e _p = 5_ é o número de características de cada uma. As características levadas em conta por unidade são: área em $m^2$; número de quartos, número de banheiros, bairro e valor. Nos últimos anos, a imobiliária detectou um aumento vertiginoso na taxa de procura por casas de alto padrão e chegou à conclusão de que precisava de um sistema inteligente para encontrar a casa com o melhor custo benefício para seus clientes. Então, a imobiliária contrata você como cientista de dados para desenvolver um modelo que seja capaz de varrer o banco de dados de casas e localizar aquela que satisfaça as preferências impostas e informe, finalmente, o valor da "casa pretendida" com baixa margem de erro.
# 
# 
# Tome as duas maiores classes de problema de aprendizado de máquina e a numeração proposta abaixo.
# 
# 1. Aprendizagem supervisionada: Regressão logística
# 
# 2. Aprendizagem não-supervisionada: Estimativa de densidade
# 
# 3. Aprendizagem não-supervisionada: Clusterização
# 
# 4. Aprendizagem supervisionada: Classificação
# 
# Assinale a opção cuja ordem é a que melhor faz o paralelo entre os problemas a serem solucionados e as classes listadas.
# 
# A. I:1, II:2, III:4, IV:3
# 
# B. I:2, II:1, III:3, IV:4
# 
# C. I:3, II:2, III:4, IV:1
# 
# D. I:4, II:2, III:3, IV:1
# 

# **Questão 2.** No *Problema IV* da *Questão 1*, assuma que a planilha seja carregada na variável `B`. Se `B` equivale à entidade matemática descrita por $B = [B_{ij}]$, tal que $i = 1,2,\ldots, 200$ e $j = 1,2,3,4$, então
# 
# A. `B` é o vetor alvo (_target_).
# 
# B. `B` é a matriz de atributos (_features_).
# 
# C. `B` é a matriz de _labels_.
# 
# D. `B` é o vetor de _pesos_.
# 

# **Questão 3.** Sejam os vetores:
#             
# ```python            
# y = array([
# 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1,
# 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0,
# 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1,
# 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1,
# 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
# 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0,
# 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0,
# 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0,
# 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1,
# 1, 1])
# ```   
# e 
# 
# ```python
# Y = array([
# 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1,
# 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1,
# 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1,
# 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0,
# 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1,
# 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1,
# 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1,
# 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1,
# 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
# 1, 1])
# ```
#        
# Construa a matriz de confusão correspondente a `y` e `Y` e assinale corretamente a opção que, nesta ordem, fornece os valores aproximados com duas casas decimais para: _acurácia_, _recall_, _especificidade, _precisão_  e _valor previsto negativo (VPN)_,
# 
# A. 0.53, 0.50, 0.54, 0.50, 0.56
# 
# B. 0.54, 0.50, 0.51, 0.50, 0.55
# 
# C. 0.53, 0.51, 0.54, 0.50, 0.57
# 
# D. 0.54, 0.51, 0.54, 0.52, 0.56
