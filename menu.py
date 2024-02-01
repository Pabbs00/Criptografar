from termcolor import colored

img = """ _____      _       _                  ______     _     _     
/  __ \    (_)     | |                 | ___ \   | |   | |    
| /  \/_ __ _ _ __ | |_ ___    ______  | |_/ /_ _| |__ | |__  
| |   | '__| | '_ \| __/ _ \  |______| |  __/ _` | '_ \| '_ \ 
| \__/\ |  | | |_) | || (_) |          | | | (_| | |_) | |_) |
 \____/_|  |_| .__/ \__\___/           \_|  \__,_|_.__/|_.__/ 
             | |                                              
             |_| """

def linha():
  print(colored("=" * 65 ,"blue"))

def tela():
  linha()
  print(colored(img,"red"))
  linha()
  print('''\n[1] CRIPTOGRAFAR MENSAGEM\n[2] DESCRIPTOGRAFAR MENSAGEM\n[3] FECHAR PROGRAMA
  ''')
  linha()

def tela2():
  print(("OPÇÕES POSSIVEIS\n").center(62," "))
  print("[1] DESCRIPTOGRAFAR ESSA MENSAGEM\n[2] VOLTAR A MENU INICIAL\n[3] ENCERRAR PROGRAMA")
  linha()

def tela3():
  print(("OPÇÕES POSSIVEIS\n").center(62," "))
  print("[1] VOLTAR A MENU INICIAL\n[2] ENCERRAR PROGRAMA")
  linha()
  
def encerrar():
  linha()
  print(("PROGRAMA ENCERRADO COM SUCESSO !!\n").center(62," "))
  print(colored('''                            ─▒▒▒▒▒─
                            ▒─▄▒─▄▒
                            ▒▒▒▒▒▒▒
                            ▒▒▒▒▒▒▒
                            ▒─▒─▒─▒''',"red"))
  linha()

def erro():
  linha()
  print("EITA BIXO !! OCORREU UM ERRO... APERTE ENTER PARA RETORNAR AO INICIO")
  linha()