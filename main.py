from func import criptografar, descript, limpar
from menu import tela, linha, encerrar, tela2, tela3, erro

#execução
def iniciar():
  limpar()
  var = True
  while var == True:
    tela()
    resposta = input("DIGITE A OPÇÃO ESCOLHIDA: ")
    if resposta == "3":
      limpar()
      encerrar()
      exit()
    elif resposta == "2":
      limpar()
      linha()
      msgm = input("DIGITE A MENSAGEM A SER DESCRIPTOGRAFADA: ")
      if msgm == "":
        limpar()
        erro()
        input("")
        limpar()
        var = True
      else:
        descript(msgm)
        linha()
        tela3()
        resposta4 = input("DIGITE AQUI A OPÇÃO DESEJADA: ")
        if resposta4 == "2":
          limpar()
          encerrar()
          exit()
        elif resposta4 == "1":
          limpar()
          var = True
        else:
          limpar()
          erro()
          input("")
          var = True
          limpar()
    elif resposta == "1":
      limpar()
      linha()
      msg = input("DIGITE A MENSAGEM A SER CRIPTOGRAFADA: ")
      if msg == "":
        limpar()
        erro()
        input("")
        limpar()
        var = True
      else:
        criptografar(msg)
        linha()
        tela2()
        resposta2 = input("DIGITE AQUI A OPÇÃO DESEJADA: ")
        if resposta2 == "3":
          limpar()
          encerrar()
          exit()
        elif resposta2 == "2":
          limpar()
          var = True
        elif resposta2 == "1":
          limpar()
          linha()
          descript(msg)
          linha()
          tela3()
          resposta3 = input("DIGITE AQUI A OPÇÃO DESEJADA: ")
          if resposta3 == "2":
            limpar()
            encerrar()
            exit()
          elif resposta3 == "1":
            limpar()
            var = True
          else:
            limpar()
            erro()
            input("")
            var = True
            limpar()
        else:
          limpar()
          erro()
          input("")
          limpar()
          var = True
    else:
      limpar()
      erro()
      input("")
      limpar()
      var = True

iniciar()