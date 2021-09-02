#!/usr/bin/env python
# coding: utf-8

# ## Questionário Q22

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

# **Questão 1**. O texto abaixo é uma mensagem encriptada. Cada grupo de 4 caracteres corresponde a um número hexadecimal.
# 
# ```
# 0x45 0x6d 0x20 0x61 0x6c 0x67 0x75 0x6d 0x20 0x6c 0x75 0x67 0x61 0x72 0x2c 0x20 0x61 0x6c 0x67 0x6f 0x20 0x69 0x6e 0x63 0x72 0xed 0x76 0x65 0x6c 0x20 0x65 0x73 0x74 0xe1 0x20 0x65 0x73 0x70 0x65 0x72 0x61 0x6e 0x64 0x6f 0x20 0x70 0x61 0x72 0x61 0x20 0x73 0x65 0x72 0x20 0x64 0x65 0x73 0x63 0x6f 0x62 0x65 0x72 0x74 0x6f 0x2e
# ```
# 
# Use seus conhecimentos de funções _built_in_ para decodificar a mensagem, que é inteligível na Língua Portuguesa. Em seguida, determine quais são os caracteres da mensagem que correspondem, respectivamente, ao maior e menor valor binário entre os elementos da sequência. Assinale a alternativa que melhor descreve a mensagem decodificada, o caracter associado ao maior valor binário e o caracter associado ao menor valor binário, nesta sequência.
# 
# A. `'Em nenhum lugar, todo possível está aguardando para ser manifesto'`, `'ê'` e `' '`.
# 
# B. `'Em algum lugar, tudo incrível está esperando para ser incompleto.'`, `'s` e  `'a'`.
# 
# C. `'Em nenhum lugar, algo possível deve aguardar para ser descoberto'`, `'ê'` e `'í'`.
# 
# D. `'Em algum lugar, algo incrível está esperando para ser descoberto.'`, `'í'` e  `' '`.
# 
# _Obs.:_ Considere que os espaços na mensagem original não devem ser considerados como caracteres na mensagem decodificada e que ali servem apenas para separar os quartetos hexadecimais.

# <hr>
# 
# ### Gabarito
# 

# Alternativa **D**

# In[14]:


frase_code = [0x45, 0x6d, 0x20, 0x61, 0x6c, 0x67, 0x75, 0x6d, 0x20, 0x6c, 0x75, 0x67,0x61, 0x72, 0x2c, 0x20, 0x61,
              0x6c, 0x67, 0x6f, 0x20, 0x69, 0x6e, 0x63,0x72, 0xed, 0x76, 0x65, 0x6c, 0x20, 0x65, 0x73, 0x74, 0xe1,
              0x20, 0x65, 0x73, 0x70, 0x65, 0x72, 0x61, 0x6e, 0x64, 0x6f, 0x20, 0x70, 0x61, 0x72, 0x61, 0x20, 0x73,
              0x65, 0x72, 0x20, 0x64, 0x65, 0x73, 0x63, 0x6f, 0x62, 0x65, 0x72, 0x74, 0x6f, 0x2e]


# In[17]:


maior_int = max(frase_code)
menor_int = min(frase_code)

test  = [(chr(frase_code[_])) for _ in range(len(frase_code))]
a = "".join(test)
maior, menor = max(a),min(a)

print(f"\nResposta esperada: '{a}', '{maior}', '{menor}'\n")


# **Questão 2**. Rindalve é um jovem promissor que conquistou um excelente emprego, mas sofre com a indisciplina financeira. Ele paga o aluguel da casa onde mora sempre com atraso de alguns dias e, extrapola o limite do cartão de crédito com frequência. Neste mês, Jonas pagou seu aluguel de <span> R&#36;</span> 6.500,00 com 12 dias de atraso e hoje faz 6 dias que a fatura de seu cartão, fechada em <span> R&#36;</span> 7.234,77, venceu. 
# 
# A imobiliária que administra a casa de Jonas usa a seguinte regra para calcular o valor adicional devido em caso de atraso no pagamento do aluguel:
# 
# - mora de 6,25% sobre o valor do aluguel + juro simples de 0,025% ao dia
# 
# A administradora de seu cartão de crédito, por outro lado, usa a seguinte regra para calcular o valor adicional devido em caso de atraso no pagamento da fatura do cartão:
# 
# - juro composto de 1,44% ao dia.
# 
# Crie uma função para calcular o valor total atualizado $V_T$ que Jonas deverá desembolsar, em reais, para quitar as despesas citadas. Então, marque a alternativa correta.
# 
# A. <span> R&#36;</span> 19.048,09
# 
# B. <span> R&#36;</span> 19.396,08
# 
# C. <span> R&#36;</span> 14.808.54
# 
# D. <span> R&#36;</span> 16.396,77

# <hr>
# 
# ## Gabarito
# 
# Alternativa C.

# In[3]:


def va_simples(valor,t,taxa,mora):
    if t == 0:
        return valor
    else:
        return valor*(1.0 + (mora + t*taxa)/100) 

def va_composto(valor,t,taxa):
        
    if t == 0:
        return valor
    else:
        return valor*(1.0 + taxa/100)**t

def total(v1,v2):
    return v1 + v2

v1 = va_simples(6500,12,0.025,6.25)
v2 = va_composto(7234.77,6,1.44)
vt = total(v1,v2)
f'Total devido: R$ = {vt:.2f}'


# <hr>
# 
# **Questão 3**. O Ministério da Saúde disponibiliza uma lista de remédios através do programa _Farmácia Popular_. Clicando [aqui](https://antigo.saude.gov.br/images/pdf/2019/janeiro/07/Lista-Medicamentos.pdf), você será redirecionado a uma dessas listas. Crie um _dict_ em Python com as informações relevantes contidas na tabela do arquivo PDF. Em seguida, crie uma função regular que recebe o seu _dict_ como argumento e retorne 3 objetos: um _str_, um _tuple_ e um _int_, os quais nesta, ordem, responderão às seguintes perguntas: 
# 
# - Para que doença a maior quantidade de remédios na gratuidade é indicada? 
# - Qual é a quantidade de remédios nas classes _gratuidade_ e _copopagamento_?
# - Quantos remédios têm a letra C como inicial de seu nome?
# 
# 
# Assinale a alternativa correta:
# 
# A. 'HIPERTENSÃO', (20, 15), 3  
# 
# B. 'ASMA', (20, 15), 7
# 
# C. 'DIABETES', (10, 20), 8
# 
# D. 'ASMA', (18, 17), 6
# 
# 
# _Obs.:_ tente usar funções anônimas sempre que possível.

# <hr>
# 
# ## Gabarito
#     
# Alternativa **B**

# In[5]:


#Criação do dataset
medicamentos = ["ATENOLOL 25MG","CAPTOPRIL 25MG", "CLORIDRATO DE PROPRANOLOL 40MG","HIDROCLOROTIAZIDA 25MG",
               "LOSARTANA POTÁSSICA 50MG","MALEATO DE ENALAPRIL 10MG","GLIBENCLAMIDA 5MG","CLORIDRATO DE METFORMINA 500MG",
               "CLORIDRATO DE METFORMINA 500MG – AÇÃO PROLONGADA", "CLORIDRATO DE METFORMINA 850MG","INSULINA HUMANA 100UI/ML",
               "INSULINA HUMANA REGULAR 100UI/ML","SULFATO DE SALBUTAMOL 5MG","SULFATO DE SALBUTAMOL 100MCG",
               "DIPROPIONATO DE BECLOMETASONA 50MCG","DIPROPIONATO DE BECLOMETASONA 200MCG/DOSE",
               "DIPROPIONATO DE BECLOMETASONA 200MCG/CÁPSULA","DIPROPIONATO DE BECLOMETASONA 250MCG",
               "BROMETO DE IPRATRÓPIO 0,25MG/ML","BROMETO DE IPRATRÓPIO 0,02MG/DOSE","ACETATO DE MEDROXIPROGESTERONA 150MG",
               "ETINILESTRADIOL 0,03MG + LEVONORGESTREL 0,15MG","NORETISTERONA 0,35MG",
                "VALERATO DE ESTRADIOL 5MG + ENANTATO DE NORETISTERONA 50MG","SINVASTATINA 10MG","SINVASTATINA 20MG",
               "SINVASTATINA 40MG", "BUDESONIDA 32MCG", "BUDESONIDA 50MCG","DIPROPINATO DE BELCLOMETASONA 50MCG",
               "CARBIDOPA 25MG + LEVODOPA 250MG", "CLORIDRATO DE BENSERAZIDA 25MG + LEVODOPA 100MG","ALENDRONATO DE SÓDIO 70MG",
               "MALEATO DE TIMOLOL 2,5MG","MALEATO DE TIMOLOL 5MG"]

indicacao = ["HIPERTENSÃO","HIPERTENSÃO","HIPERTENSÃO","HIPERTENSÃO","HIPERTENSÃO","HIPERTENSÃO","DIABETES",
            "DIABETES","DIABETES","DIABETES","DIABETES","DIABETES","ASMA","ASMA","ASMA","ASMA","ASMA","ASMA",
            "ASMA","ASMA","ANTICONCEPÇÃO","ANTICONCEPÇÃO","ANTICONCEPÇÃO","ANTICONCEPÇÃO","DISLIPIDEMIA","DISLIPIDEMIA",
            "DISLIPIDEMIA", "RINITE","RINITE","RINITE","DOENÇA DE PARKINSON","DOENÇA DE PARKINSON","OSTEOPOROSE",
            "GLAUCOMA","GLAUCOMA"]

gratuidade_copagamento = ["GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE",
                         "GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE",
                         "GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","GRATUIDADE","COPAGAMENTO",
                         "COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO",
                         "COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO","COPAGAMENTO",
                          "COPAGAMENTO"]

#verificação se todas estão correspondentes
len(medicamentos),len(indicacao),len(gratuidade_copagamento)


# In[6]:


#juntando indicação + gratuidade_copagamento
ind_grat = [indicacao[_] + " | "+ gratuidade_copagamento[_] for _ in range(len(indicacao))]
#criando o dict
a = dict(zip(medicamentos, ind_grat))
for i in enumerate(a):
    print(f"| {i[0]+1} | {i[1]} | " + ind_grat[i[0]])


# In[11]:


def info_medicamentos(dic):
    import re
    #atribuindo a ind_cop a indicação e o copagamento e names os nomes dos remédios
    ind_cop = [y for x,y in dic.items()]
    names = [x for x,y in dic.items()]
    
    #contando quantos remédios iniciam com a letra "C"
    inicial = list(map(lambda x: x[0][0] == "C",names))
    
    #separando a indicação e a gratuidade para verificar quantidade
    sep = list(map(lambda x: (x.split(' | ')), ind_cop))
    count_grat = 0
    count_copa = 0
    for a,b in sep:
        if b == "GRATUIDADE":
            count_grat += 1
        else:
            count_copa +=1
            
    #indetificando qual indicação contém mais remédios gratuitos      
    junt = " ".join(ind_cop)
    chek = 0
    for indi_list in ["HIPERTENSÃO", "DIABETES", "ASMA"]:
        if len(re.findall(indi_list,junt)) > chek:
            chek, name_ind = len(re.findall(indi_list,junt)) , indi_list   
    
    return print(f"\nResultado esperado: {name_ind} / {count_grat,count_copa} / {inicial.count(True)})")
   


# In[12]:


info_medicamentos(a)

