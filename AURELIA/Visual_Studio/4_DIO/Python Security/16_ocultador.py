"""  
BIBLIOTECA CTYPES: fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas
compartilhadas.
"""

import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("16_ocultar.txt") 

if retorno:
    print("arquivo foi ocultado!")
else:
    print("O arquivo não foi ocultado!")    
    
    
# Aqui tambem é possivel ocultar pasta 
pasta = input("Digite o caminho da pasta a ser ocultada ex: (C:\pasta): ")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW("#CAMINHO DA PASTA#") 

if retorno:
    print("arquivo foi ocultado!")
else:
    print("O arquivo não foi ocultado!")    
    

   
    