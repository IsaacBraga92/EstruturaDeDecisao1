#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o seu sexo. (M para masculino, F para feminino: ").upper()

if sexo == 'M':
    print("Sexo Masculino")
elif sexo == 'F':
    print("Sexo Feminino")
else:
    print("Invalido")
