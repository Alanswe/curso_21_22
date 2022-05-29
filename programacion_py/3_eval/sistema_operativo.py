import platform
import os

my_os = platform.system()

if my_os == 'Windows':
    limpiar_pantalla = os.system('cls')
else:
    limpiar_pantalla = os.system('clear')

# 'Darwin'  for macOS 
# 'Linux' for Linux
print("OS in my system : ",my_os)


import sys
my_os=sys.platform
print("OS in my system : ",my_os)
"""
`win32`   for Windows(Win32)
'cygwin'  for Windows(cygwin)
'darwin'  for macOS
'aix'     for AIX
"""