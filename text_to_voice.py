# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:48:19 2020

@author: pc owinoh
"""

import os
from gtts import gTTS

Text = "I love Django  and Python programming Language.I am a python Developer"

print("please wait....processing")
TTS = gTTS(text=Text, lang='en-uk')

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
os.system("start voice.mp3")