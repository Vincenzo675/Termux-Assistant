# -*- coding: utf-8 -*-
from gtts  import gTTS
import os
import sys,time
os.system('clear')
def bannar():
  print '''\033[91m
___ ____ ____ _  _ _  _ _  _            
 |  |___ |__/ |\/| |  |  \/             
 |  |___ |  \ |  | |__| _/\_            
                                        
____ ____ ____ _ ____ ___ ____ _  _ ___ 
|__| [__  [__  | [__   |  |__| |\ |  |  
|  | ___] ___] | ___]  |  |  | | \|  |  
                                        
'''
def bannar2 ():
  print ('\033[94m-'*50)

  print ('')

  print (' \033[96m Author   : \033[95m Vince Thongam')
  print ('')
  print (' \033[96m Tool     : \033[95m Vincenzo bot')
  print ('')
  print (' \033[96m Instagram : \033[95m https://www.instagram.com/craftastic_land_?igsh=MWFibHFndGJxZnhyaQ==')
  print ('')
  print (' \033[96m Github   : \033[95m https://www.github.com/Vincenzo675/')
  print ('')
  print (' \033[96m Coded By : \033[95m Vince Thongam')
  print ('')
  print ('\033[94m-'*50)
  print ('')
  print ('             \033[0;37;41m Text To Audio Maker\033[0m ' )
  print ('')
  print ('')
bannar()
bannar2()
love=raw_input("\033[92m [!] Type Your Speech : \033[93m ")
babe=open("speak.txt","w")
biva=babe.write(love)
babe.close()

fh=open("speak.txt","r")
rktText = fh.read().replace("\n","")
language='en'
audio=gTTS(text=rktText,lang=language,slow=False)
audio.save("audio.mp3")
os.system("mv audio.mp3 /sdcard/")
fh.close()
print ''
print ''
print '\033[92m[✓] File Saved In File Manager'
