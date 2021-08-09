#!/usr/bin/env python
# coding: utf-8

# # Problemas propostos

# ## Gematria 
# 
# Converta os caracteres hebraicos de uma string em seus valores numéricos correspondentes e busque por padrões na sequência.

# In[24]:


# integer range from Unicode
a,b = map(lambda x: int(x,16),('0x05d0','0x05eb'))

# hex
hexi = [hex(i) for i in range(a,b)]

# unicode
char = [chr(i) for i in range(a,b)]

# gematry number
numb = list(range(1,10)) + list(range(10,100,10)) + list(range(100,1000,100))

# letter name
name = [
    'Alef',
    'Bet',
    'Gimel',
    'Dalet',
    'He',
    'Vav',
    'Zayin',
    'Het',
    'Tet',
    'Yod',
    'Final Kaf',
    'Kaf',
    'Lamed',
    'Final Mem',
    'Mem',
    'Final Nun',
    'Nun',
    'Samekh',
    'Ayin',
    'Final Pe',
    'Pe',
    'Final Tsadi',
    'Tsadi',
    'Qof',
    'Resh',
    'Shin',
    'Tav',]

cn = list(zip(name,numb,char))

# Hebrew dictionary 
# key as hex
dheb_hex = dict(zip(hexi,cn))

cn = list(zip(hexi,numb,char))

# key as name
dheb = dict(zip(name,cn))


# In[79]:


# "to make many books, there is no limit"
phrase = 'עשות ספרים הרבה אין קץ'

# convert from byte mode to hex
hext = [p.encode().hex() for p in phrase]

# filter to purge whitespace 
hextf = list(filter(lambda x: x != '20',hext))

# não é o mesmo hex!!!
hextf = ['0x' + h for h in hextf]


# ## Imagens oftalmológicas
# 
# Buscando pigmentações predominantes em imagens de ceratometria

# In[87]:


import skimage as ski
import skimage.io as skio

img = skio.imread('../database/eyes/SyntEyeKTC-106_a-net.png')


# In[122]:


import numpy as np

A = np.zeros((np.shape(img)[0]*np.shape(img)[1],3))

for i in [0,1,2]:
    A[:,i] = img[:,:,i].flatten()
    
A = A/255


# In[ ]:




