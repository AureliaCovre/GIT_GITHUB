""" 
- BIBLIOTECA WEBBROWSER: Fornece uma interface de alto nível para permitir a exibição de documentos Web aos usuários.

- BIBLIOTECA TKINTER: Fornece interface pafrão do Python para o kit de ferramentas gráficas Tk.
"""

import webbrowser
from tkinter import *

root = Tk( ) #O root representa o tkinter, e não tem nome no sistema

root.title("Abrir Browser") # Definindo o titulo do root "Abrir browser"
root.geometry("300x200") #Definindo o tamanho 300 pixel x 200 pixel

# Função para abrir o browser no google.com
def google():
    webbrowser.open("www.google.com")
 
  
mygoogle = Button(root, text="Abrir o Google", command= google).pack(pady=20)
root.mainloop()    