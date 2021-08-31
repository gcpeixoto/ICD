#!/usr/bin/env python
# coding: utf-8

# # Tone generator
# 
# Required: `pip install tones`
# https://pypi.org/project/tones/

# In[53]:


from tones.mixer import Mixer

notes = ['c','d','e','f','g','a','b']
octave = 3

for note in notes:
    mixer = Mixer(44100,0.5)
    mixer.create_track(0)
    mixer.add_note(0,note=note,octave=octave,duration=1.0)
    mixer.write_wav(f'../database/musical-tones/{note}-{octave}.wav')
    del mixer


# In[106]:


# multiple outputs
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from IPython.display import Audio
import os

bdir = '../database/musical-tones/'
files = [name for name in os.listdir('../database/musical-tones/') if name.endswith('3.wav')]

# natural order 
files = (sorted(files) + sorted(files)[0:2] )[2:]

for f in files: 
    Audio(os.path.join(bdir,f))        

