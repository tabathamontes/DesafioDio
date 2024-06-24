while True:
        nome = input("Qual é o nome do super-heroi? ")
        nivel = int(input("Qual é o xp do super-heroi? "))

        if nivel  <= 1000 :
                elemento = "ferro"
        elif nivel >= 1001 and nivel <= 2000:
                elemento =" bronze"
        elif nivel >= 2001 and nivel <= 5000: 
                elemento = "prata"
        elif nivel >= 5001 and nivel <= 7000: 
                elemento = "ouro"
        elif nivel >= 7001 and nivel <= 8000:
                elemento = "platina"
        elif nivel >= 8001 and nivel <= 9000: 
                elemento = "ascendente"
        elif nivel >= 9001 and nivel <= 10000: 
                elemento = "imortal"
        else:
                elemento = "radiante" 

        print ( f"O Herói {nome} está no nível de {nivel} xp,o elemento dele é {elemento}.")

        while True:
                continuar = input(f"Você deseja saber o elemento de outro super-heroi? ") .upper() .strip()
                if continuar in 'SN':
                        break
        if continuar  == "N":
                break
print("Até mais!!!")



