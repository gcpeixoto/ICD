#!/usr/bin/env python
# coding: utf-8

# # Python intermediário - III

# ## Entrada e saída de dados 
# 
# - Fluxos de informações são geralmente realizados por meio de _objetos-tipo arquivo_ (_file objects_). 
# 
# - A esses objetos dá-se também o nome de _input/output stream_, de onde segue o termo _I/O stream_. 
# 
# - Para entendimento prático, _streams_ são os tradicionais "arquivos" que transitam em nossas máquinas. 

# ### Tipos de arquivo
# 
# - _Texto formatado_ (_Text file_). Recebem e produzem objetos _str_. Ocorre codificação/decodificação dos dados durante o fluxo. 
# - _Binário_ (_Binary file_). Lidam com objetos na forma de _bytes_. Nenhum processo de codificação/decodificação dos dados ocorre durante o fluxo. O texto é _não formatado_.

# ## Operações com arquivos
# 
# - Aprenderemos a manipular o fluxo de entrada e saída de diversos tipos de arquivo. 
# 
# - A forma mais fácil de criar uma _stream_ é usando a função predefinida `open`.

# **Exemplo:** ler arquivo de texto.

# In[1]:


f = open('../etc/icd.yml')
f 


# Comentários:
# - Por padrão, `open` abre um arquivo em modo de leitura.
# - O arquivo é especificado pelo seu caminho no disco.
# - `f` é um objeto abstrato como se vê, que mostra o esquema de codificação usado para decodificar arquivo. Quando não especificado, o `encoding` padrão do sistema é utilizado.
# - Percebe-se que o encoding padrão do sistema é `UTF-8`.

# **Exemplo:** ler arquivo de texto com especificação de modo.

# In[2]:


# o arquivo aqui é uma imagem PNG
o = open('../database/eyes/SyntEyeKTC-106_a-net.png',mode='r')
o


# Comentários:
# 
# - O segundo argumento de `open` é `mode`, no qual especificamos o modo com que o arquivo será tratado.
# - Para modo de leitura, usamos `'r'`; para modo de escrita, usamos `'w'`; para modo de apensamento, usamos `'a'`, e para modo binário, usamos `'b'`. A seguir, veremos mais exemplos.
# - É importante notar que tanto `f` quanto `o` estão "abertos" e devem ser fechadas imediatamente após o uso para evitar consumo de memória e outros problemas.

# In[3]:


# as streams 'f' e 'o' estão abertas 
f.closed,o.closed 


# In[4]:


# fechando streams
f.close(), o.close()

# verifica novamente que foram fechadas
f.closed,o.closed


# **Exemplo:** Ler arquivo e armazenar conteúdo.

# In[5]:


with open('../etc/icd.yml') as f:
    content = f.read()

# imprime conteúdo do arquivo 
print(content)


# In[6]:


# não é necessário fechar!
f.closed


# Comentários:
# 
# - A _keyword_ `with` possibilita que o fluxo de arquivos seja facilitado.
# - Com a _keyword_ `with`, o arquivo é automaticamente fechado.
# - É possível gerir a abertura de mais de um arquivo com apenas uma chamada de `with` com 
# 
# ```python
# with A() as a, B() as b:
# ```
# 
# ```{note}
# Para saber mais acerca de `with`, consulte o [PEP 343](https://www.python.org/dev/peps/pep-0343/#motivation-and-summary).
# ```

# In[6]:


with open('../etc/icd.yml','r') as f, open('../database/bras-cubas.txt') as g :
    content_f = f.read()
    content_g = g.read()

# opera sobre conteúdos
len(content_f),type(content_g)    


# #### Modos de arquivos 
# 
# Antes de prosseguirmos, vamos resumir os principais modos com os quais um arquivo é operado em Python. 
# 
# |Caracter|Significado|
# |---|---|
# |`'r'`| abre para leitura (padrão)|
# |`'w'`| abre para escrita, truncando o arquivo|
# |`'x'`| cria um novo arquivo e o abre para escrita|
# |`'a'`| abre para escrita apensando conteúdo no fim do arquivo|
# |`'b'`| abre em modo binário|
# |`'t'`| abre em modo texto (padrão)|
# 
# Para uma discussão mais ampla sobre todas as possabilidades, consulte este [post](https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/) e [este](https://riptutorial.com/python/example/978/file-modes).
# 

# **Exemplo:** Ler arquivo linha por linha.

# In[8]:


with open('../database/bras-cubas.txt','rt',encoding='utf-8') as f:
    for linha in f:
        print(linha.lower())


# Discussão:
# - Note que especifica o modo `'rt'` é totalmente decorativo, já que são as opções padrão.
# - O parâmetro `encoding` indica a codificação na qual o texto deve ser lido. `UTF-8` é o padrão. Entretanto, veremos adiante algumas especifidades com relação a _encoding_ de caracteres.

# ### Escrita de arquivos de texto
# 
# Para escrever conteúdo em um arquivo, devemos assumir ou que ele é inexistente e precisa ser criado, ou que ele existe e queremos adicionar informações nele.
# 
# **Exemplo:** escrever um simulacro de "jogo da velha" com caracteres em um arquivo `.txt`.

# In[9]:


def velha(n):
    '''Simula um jogo da velha fictício.'''
    
    from random import sample
    
    c = ['o','x']            
    l = f'  -   -   -  \n'
    ll = l
    
    for _ in range(3):
        l += f'| {sample(c,1)[0]} | {sample(c,1)[0]} | {sample(c,1)[0]} |\n'
    l += ll # sobrecarga de +
    
    l = f'Game: #{n}\n' + l + '\n' 
    
    return l


# cria log de n partidas
def n_games_log(n):
    
    with open('../etc/velha-log.txt','w') as v:
        for i in range(1,n+1):
            v.write(velha(i)) # escreve em arquivo
            
# executa função para 4 partidas            
n_games_log(4)            


# Para visualizarmos o conteúdo do arquivo podemos usar a função `cat` via terminal ou abrir uma nova _stream_ de leitura (exercício): 

# In[10]:


get_ipython().system("cat '../etc/velha-log.txt'")


# **Exemplo:** escrever arquivo e apensar dados.

# In[65]:


# escreve
with open('../etc/lista.txt','w') as f:
    f.write( str(list(range(5))).strip('[,]')) # escreve str e purga '[' e ']'

get_ipython().system('cat ../etc/lista.txt ')


# In[66]:


# abre para apensar
with open('../etc/lista.txt','a') as f:
    f.write(', ') # o que temos sem isto?
    f.write(str(list(range(5,11))).strip('[]'))

get_ipython().system('cat ../etc/lista.txt     ')


# Comentários:
# 
# - No modo de apensamento, o arquivo original não é sobrescrito, mas alterado em seu final.
# - No exemplo anterior, incluímos a complementaridade da sequência de inteiros de 5 a 10 que não estava no arquivo anterior.

# **Exemplo:** apensar em arquivo redirecionando a saída de `print`.

# In[67]:


with open('../etc/lista.txt','a') as f:
    print('!!!',file=f) # mesmo objeto f

get_ipython().system('cat ../etc/lista.txt  ')


# Comentário:
# - Neste exemplo, a string `'!!!'`, que seria impressa na tela por `print` é apensada no arquivo `lista.txt` via _redirecionamento_. 
# 
# 
# Em ambiente UNIX, o redirecionamento pode ser feito via Terminal com o operador `>`, e o apensamento com `>>`. Por exemplo, o comando `cat > lista.txt` cria um arquivo vazio e redireciona as linhas digitáveis em tela para o arquivo. O comando `cat >> lista.txt`, por outro lado, permite que mais linhas digitáveis  em tela sejam adicionadas ao arquivo. Veja um exemplo [aqui](https://www.gotothings.com/unix/unix-redirection-and-pipes.htm).
# 

# **Exemplo:** escrever para arquivo com redirecionamento, _star expression_ e sem `with`.

# In[78]:


dado = ('graus C',16,22.5) # tupla com diferentes dados

f = open('../etc/lista-2.txt','w')
print(*dado,sep='',file=f)  
f.close() # sem 'with', é necessário fechar a stream 

get_ipython().system('cat ../etc/lista-2.txt')


# Discussão:
# - Neste exemplo, `*dado` desempacota a tupla – que tem tipos de dado diferentes –, separa os elementos por `,`, imprime na tela e redireciona para o arquivo de texto `lista-2.txt`.
# - Observe que arquivo é aberto em modo de escrita.

# ### Escrita de arquivos binários

# **Exemplo:** pré-visualizar um arquivo PDF no _Jupyter Notebook_.

# In[80]:


from IPython.display import IFrame
IFrame('../etc/logo-icd.pdf',width=500,height=500) 


# Comentários:
# - Arquivos _PDF_, assim como áudios, imagens e executáveis, possuem conteúdo em formato binário. O que visualizamos acima é compreensível por humanos. 
# - O exemplo a seguir mostra o real conteúdo do arquivo _PDF_ em termos de bytes.
# 
# 
# Tente reproduzir este exemplo com o Jupyter Notebook executando localmente em sua máquina. Em alguns navegadores, o livro online pode não reproduzir esta pré-visualização.
# 

# **Exemplo:** ler arquivo binário e imprimir seu conteúdo.

# In[82]:


# modo 'rb'
with open('../etc/logo-icd.pdf','rb') as f:
    pdf = f.read()

# 200 primeiros caracteres
pdf[:200]


# In[83]:


# verifica tipo da variável
type(pdf) 


# Comentários:
# - A variável `pdf` guarda dados em formato **binário**.
# - O prefixo `'b'` sugere que o tipo de dado é binário e está "codificado" em linguagem de "bytes".
# - Perceba que nós humanos enxergamos caracteres, mas **o computador enxerga apenas _bytes_**.

# **Exemplo:** escrever arquivo binário.

# In[84]:


# modo 'wb'
with open('../etc/logo-icd-part.pdf','wb') as f:
    f.write(pdf[:200])     


# In[86]:


from IPython.display import IFrame
IFrame('../etc/logo-icd-part.pdf',width=500,height=500)  


# Discussão:
# - O conteúdo parcial tomado da string de _bytes_ `'pdf'` é escrito em um segundo arquivo.
# - Ao ler o conteúdo e tentar visualizá-lo, um erro será lançado. Isto é naturalmente esperado, visto que a sequência de bytes está danificada.
# 
# 
# Tente reproduzir este exemplo com o Jupyter Notebook executando localmente em sua máquina. Em alguns navegadores, o livro online pode não reproduzir esta pré-visualização.

# ### Como evitar sobrescrição acidental 
# 
# Podemos usar o modo `'x'`, que garante a "exclusividade" do arquivo existente.

# **Exemplo:** escrever arquivo em modo de "exclusividade".

# In[87]:


with open('../etc/lista.txt','x') as f:
    print('???',file=f) # mesmo objeto f


# Discussão:
# - Tentamos escrever outro conteúdo para o arquivo `lista.txt`, o que geraria uma sobrescrição de seu conteúdo original. 
# - Utilizando o modo `'x'`, o interpretador se encarrega de verificar se o arquivo existe e só permite que a operação seja concluída em caso negativo.
# - Como o arquivo existe no disco, um erro de `FileExistsError` é lançado.
# - O próximo exemplo é bem-sucedido, visto que `lista-3.txt` não existe ainda no disco.

# In[92]:


with open('../etc/lista-3.txt','x') as f:
    print('OK!',file=f) # mesmo objeto f
    
get_ipython().system('cat ../etc/lista-3.txt    ')


# In[93]:


# remove o arquivo para reproduzir teste
get_ipython().system('rm ../etc/lista-3.txt')


# In[94]:


# verifica remoção
get_ipython().system('cat ../etc/lista-3.txt   ')


# #### Testando a existência de arquivos
# 
# Uma forma de verificar a existência de arquivos no disco é valer-se do módulo `os` – discutiremos um pouco sobre este módulo à frente –. O exemplo a seguir praticamente alcança o mesmo objetivo que o modo `'x'` ao checar a pré-existência de arquivos.

# In[95]:


from os.path import exists

if exists('../etc/lista-3.txt'):
    print('O arquivo existe... Pé no freio... :( ')
else:
    print('O arquivo não existe! Pé na tábua! 8) ')


# O módulo [`os`](https://docs.python.org/3/library/os.html?highlight=os%20module#module-os) fornece meios poderosos para navegar pelo sistema operacional e é bastante útil na leitura e escrita de arquivos.

# ### Leitura e escrita de arquivos comprimidos
# 
# A [compressão de dados](https://en.wikipedia.org/wiki/Data_compression) baseia-se em reduzir a quantidade de _bits_ utilizadas para armazenar os dados, mas assegurar a sua integridade genuína. 
# 
# Em Python, temos à disposição, por exemplo, os módulos [`bz2`](https://docs.python.org/3/library/bz2.html) e [`gzip`](https://docs.python.org/3/library/gzip.html) para operar com arquivos comprimidos. Ambos são baseados na biblioteca [zlib](https://www.zlib.net). A seguir, veremos exemplos de como podemos manipular arquivos comprimidos.

# **Exemplo:** escrever arquivos comprimidos.

# In[98]:


# sem compressão
with open('../etc/texto.txt','w') as f:
    f.write('[]'*500000)

# compressão com bz2
import bz2
with bz2.open('../etc/texto.bz2','w') as f:
    f.write(b'[]'*500000) # deve ser string de bytes
    
# compressão com gzip
import gzip
with gzip.open('../etc/texto.gz','w') as f:
    f.write(b'[]'*500000) # deve ser string de bytes      


# In[99]:


get_ipython().system(' ls -l ../etc/texto.*')


# Comentários:
# - Note a diferença no tamanho dos arquivos. A taxa de compressão é gigantesca! Os arquivos comprimidos possuem 73 _bytes_ de tamanho, ao passo que o não comprimido possui 1.000.000 de _bytes_ (1 MB) de tamanho.
# - Para realizarmos a leitura dos arquivos, basta alterar o modo de `'w'` para `'r'`.

# ## O módulo `os`
# 
# Com o módulo [`os`](https://docs.python.org/3/library/os.html?highlight=os%20module#module-os), podemos realizar uma série de operações para manipular caminhos de arquivos.

# **Exemplo:** manipular caminhos para coletar informações de diretórios.

# In[107]:


import os

arq = '../database/bras-cubas.txt'


# In[109]:


# última parte do caminho
os.path.basename(arq)


# In[110]:


# diretório
os.path.dirname(arq)


# In[112]:


# cria caminho unindo partes
os.path.join('pasta','subpasta',os.path.basename(arq))


# In[113]:


# separa basename e extensão
os.path.splitext(arq)


# In[114]:


# separa pasta e nome
os.path.split(arq)


# **Exemplo:** realizar testes para verificar tipos de arquivo.

# In[115]:


# testa se é arquivo
os.path.isfile('../etc/velha-log.txt')


# In[117]:


# testa se é diretório
os.path.isdir('../etc/icd.yml')


# Comentários:
# - Com o submódulo `os.path`, podemos acessar praticamente toda a hierarquia de arquivos e diretórios no sistema operacional.

# #### Coletando metadados de arquivos
# 
# Metadados dos arquivos, tais como tamanho e data de modificação, podem ser obtidos por meio do módulo `os` também.

# **Exemplo:** obtendo tamanho do arquivo.

# In[118]:


# no. de bytes
os.path.getsize('../etc/logo-icd.pdf') 


# In[120]:


import time
time.ctime(os.path.getmtime('../etc/logo-icd.pdf'))


# Discussão:
# - A função `getmtime` retorna a informação temporal da última modificação do arquivo especificado. 
# - O módulo `time` fornece funções para manipular quantidades em unidade de tempo.
# - A função `ctime` converte uma medida de tempo em segundos para uma _string_ de data/hora de acordo com as configurações locais da máquina. 

# **Exemplo:** listar diretórios.

# In[121]:


os.listdir('../etc/') 


# **Exemplo:** buscar por todos os arquivos comuns em um diretório.

# In[122]:


pasta = '../etc/'
arqs = [a for a in os.listdir(pasta)
       if os.path.isfile(os.path.join(pasta,a))]
arqs


# **Exemplo:** buscar por todos os diretórios.

# In[123]:


pasta = '../'
dirs = [a for a in os.listdir(pasta)
       if os.path.isdir(os.path.join(pasta,a))]
dirs  


# **Exemplo:** buscar por todos os arquivos de uma dada extensão.

# In[124]:


# lista apenas .txt
txts = [a for a in os.listdir('../etc/')
       if a.endswith('.txt')]
txts 


# ## Codificação e decodificação de caracteres

# - Caracteres impressos em tela são apenas símbolos renderizados
# - São processados em "camadas abstratas": armazenamento + textual
# - Existem vários sistemas de codificação de caracteres. (ASCII, ISO-8859, CP-1252) 
# - Mais comum: UTF-8. 

# - O [[Unicode]](https://home.unicode.org) foi proposto para definir um único número para cada caracter independentemente de plataforma, programa ou linguagem. 
# - Melhor definição de caracter que existe hoje: _caracter Unicode_.
# - Identidade do caracter Unicode: _code point_ (número de 0 a 1.114.111 em base 10).
# - Padrão Unicode: 4 a 6 dígitos hexadecimais seguidos do prefixo "U+". 

# - Exemplos de caracteres, ponto de código e nome no padrão Unicode.
# 
# |Caracter|Ponto de código|Nome Unicode|
# |---|---|---|
# |â|U+00E2|LATIN SMALL LETTER A WITH CIRCUMFLEX|
# |ݔ|U+0754|ARABIC LETTER BEH WITH TWO DOTS BELOW AND DOT ABOVE|
# |😛|U+1F61B|FACE WITH STUCK-OUT TONGUE|
# |ぎ|U+304E|HIRAGANA LETTER GI|
# 
# > Todos os caracteres Unicode são encontrados em tabelas, as chamadas [[_Code Charts_]](https://www.unicode.org/charts/).

# - Impressão usando uma _string Unicode_ hexadecimal de 32-bits:
# 
# ```python
# '\U000000E2','\U00000754','\U0001f61b','\U0000304e'
# ```
# 
# - Impressão usando o nome Unicode do caracter:
# 
# ```python
# '\N{LATIN SMALL LETTER A WITH CIRCUMFLEX}',
# '\N{ARABIC LETTER BEH WITH TWO DOTS BELOW AND DOT ABOVE}',
# '\N{FACE WITH STUCK-OUT TONGUE}',
# '\N{HIRAGANA LETTER GI}'
# ```

# ### _bytes_ x texto
# 
# - _Encoding_: conversão de _code points_ => _bytes_.
# - _Decoding_: conversão de _bytes_ => _code points_. 

# **Exemplo:** codificação e decodificação.

# In[178]:


s = 'balé'
len(s)


# In[179]:


b = s.encode('utf8')
b


# In[180]:


# caracter 'é' representado por dois bytes
# \xc3 e \xa9
len(b)


# In[181]:


b.decode('utf8')


# Discussão:
# 
# - `encode` leva o texto para _bytes_.
# - `b'` é uma string literal de _bytes_.
# - `bal` está no intervalo ASCII imprimível, enquanto que `\xc3` e `\xa9` não.
# - `decode` leva de _bytes_ para texto.

# Comentários:
# 
# - O próprio caracter ASCII é usado para _bytes_ no intevalo imprimível.
# - Para _bytes_ correspndendo ao TAB, _newline_, _carriage return_ e '\\', as sequências de escape `\t`, `\n`, `\r` e `\\` são usadas.
# - Para qualquer outro _byte_, usa-se uma sequência de escape hexadecimal.

# **Exemplo**: decodificação para outros sistemas.

# In[182]:


# erro! 
# 'é' não é ASCII
s.encode().decode('ascii')  


# In[183]:


s.encode().decode('iso8859')


# In[184]:


s.encode().decode('cp1252')


# ## Referências complementares
# 
# - [Módulo `os`](https://docs.python.org/3/library/os.html?highlight=os%20module#module-os)
# - [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html)
# - [Nam & Fischer, Character Encoding & Unicode - How to (╯°□°）╯︵ ┻━┻ with dignity](https://www.slideshare.net/fischertrav/character-encoding-unicode-how-to-with-dignity-33352863)
