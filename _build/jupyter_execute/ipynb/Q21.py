#!/usr/bin/env python
# coding: utf-8

# ## Questionário 21 (Q21)
# 
# **Orientações para submissão:** 
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
# A. 1 longitudinal / 4 transversais / 3 diagonais / 4 de ligação. 
# 
# B. 2 longitudinais / 4 transversais / 3 diagonais / 6 de ligação.  
# 
# C. 4 longitudinais / 1 transversal / 1 diagonal / 6 de ligação.  
# 
# D. 5 longitudinais / 1 transversal / 3 diagonais / 6 de ligação.  

# **Questão 2**. Segundo o Balanço Energético Nacional 2019, a matriz elétrica brasileira estava distribuída segundo o gráfico abaixo:
# 
# ```{figure} ../figs/q/ben.png
# ---
# width: 400px
# name: ben
# ---
# Distribuição da matriz elétrica brasileira no final de 2019.
# ```
# 
# Fonte: [[EPE]](https://www.epe.gov.br/pt/abcdenergia/matriz-energetica-e-eletrica).
#         
# 
# Crie um dicionário em que as _keys_ e _values_ correspondam, respectivamente, às fontes de energia legendadas no gráfico e ao percentual que ocupam na matriz energética. Considerando que
# 
# - _i_ é o índice da _key_ "Biomassa" no _dict_ ordenado por valor percentual **crescente** e
# - _j_ é o índice da _key_ "Eólica" no _dict_ ordenado por valor percentual **decrescente**,
# 
# assinale a alternativa correta:
# 
# A. _i_ = 4 e _j_ = 2.
# 
# B. _i_ = 5 e _j_ = 3.
# 
# C. _i_ = 0 e _j_ = 7.
# 
# D. _i_ = 3 e _j_ = 6.

# **Questão 3**: Para que um número de CPF (Cadastro de Pessoa Física) brasileiro seja considerado válido, a soma de todos os seus dígitos deve resultar em um número com dois dígitos iguais. Por exemplo, o número de CPF $003.939.708\text{-}41$ é válido porque 
# 
# $$0 + 0 + 3 + 9 + 3 + 9 + 7 + 8 + 4 + 1 = 44.$$
# 
# Adicionalmente, a sua autenticidade pode ser verificada observando o último dígito imediatamente anterior ao hífen, o qual determina o estado de origem daquele número de CPF. 
# 
# Considerando que um número de CPF possa ser escrito pela máscara
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
# O CPF usado como modelo acima, por exemplo, pertence a São Paulo, já que $i = 8$.
# 
# Fonte: [[ACE Guarulhos]](https://www.aceguarulhos.com.br/blog/como-saber-se-um-cpf-e-verdadeiro/#gsc.tab=0)
# 
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
# Execute esta função para _n_=20. Em seguida, faça um programa para checar se os CPFs gerados são válidos ou inválidos, bem como para determinar o estado brasileiro desses CPFs. Assinale a alternativa correta.
# 
# A. Existem apenas 3 CPFs válidos e 1 deles pertence ao Acre.
# 
# B. Existem apenas 5 CPFs válidos e 2 deles pertencem a São Paulo.
# 
# C. Existe apenas 1 CPF válido, pertencente a Rondônia.
# 
# D. Todos os CPFs são válidos, exceto o último da lista.
# 
# **Dica:** use expressão regular.
