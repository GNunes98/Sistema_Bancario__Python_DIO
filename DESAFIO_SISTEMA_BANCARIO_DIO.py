import time
saldo = 1000
extrato = ""
saque = 0
deposito = 0
inicial ="""
    ######  Bem Vindo Usuário  ######
    Escolha um dos serviço abaixo:

    S - Saque
    D - Deposito
    E - Extrato

    Q - Sair



"""

LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
contagem_diaria = 0


menu = ""



while True:

    print(inicial)

    menu = input("digite sua escolha:")

   
    if menu == "e":
      print("***************************************************\n") 
      print("    ### EXTRATO ###")    
      print( f"    Seu Saldo:{saldo:.2f}")  
      print("***************************************************\n")  
      print(extrato)
      print("***************************************************\n") 
      time.sleep(3)

    elif menu == "s":

      print("***************************************************\n")  
      saque = float(input("Digite o valor: "))
  
      
      if saldo >= saque : 
        if contagem_diaria < LIMITE_DIARIO :
          contagem_diaria += 1
          if saque <= LIMITE_SAQUE:
             
            saldo = saldo - saque
            extrato += f"    Saque: R${saque:.2f}\n"
            print("################################################\n")  
            print("A operacao esta sendo processada ...")
            time.sleep(2)
            print(f"Saque de R${saque:.2f} realizado com sucesso")
            time.sleep(3)
            print("\n################################################")  
          else:
            print("O valor excede o valor limite de saque")
        else:
          print("Voce atingiu seu limite diarios de movimentações")
      else:
        print("você não possui saldo para completar a operação")
  
    elif menu == "d":
      print("-----------------------------------------------------\n")  
      deposito = float(input("Digite o valor a ser depositado:"))
      print("\n-----------------------------------------------------")  
      if deposito > 0 : 
                               
        saldo += deposito
        extrato += f"    Deposito: R${deposito:.2f}\n"
        print("-----------------------------------------------------\n")  
        print("A operacao esta sendo processada ...")
        time.sleep(2)
        print(f"Deposito de R${deposito:.2f} realizado com sucesso")
        time.sleep(3)
        print("\n-----------------------------------------------------")  

      else:
        print("-----------------------------------------------------\n")   
        print("Valores negativos ou zero não são aceitos")
        print("\n-----------------------------------------------------")  
    elif menu == "q":

        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("saindo do sistema!")
        time.sleep(2)
        print("volte sempre!")
        print("n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        time.sleep(1)
        break 
    else:
      print("\n***************************************************")    
      print("Digite um comando válido")
      print("***************************************************\n")    
    

