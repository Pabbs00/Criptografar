from termcolor import colored
import os
from menu import erro

#listas
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
chave = ["!","@","#","$","%","º","&","*","(",")","=","+","-","_","{","}","/",">","<","[","]","?",".",",",";","^","~"]

#funções

#criptografia e descripitografia
def criptografar(mensagem):
  for letras in mensagem:
    for letras in alfabeto:
      mensagem = mensagem.replace(letras,chave[int(alfabeto.index(letras))])
  else:
    print(f"Mensagem criptografada:",colored(mensagem,"red"))
    return mensagem

def descript(mensagem=str):
  for letra in mensagem:
    if letra in chave:
       mensagem = mensagem.replace(letra,alfabeto[int(chave.index(letra))])
    else:
      print("Mensagem descriptada:",colored(mensagem,"green"))
      return mensagem

#verifcação de sistema para limpar a tela
def limpar():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")