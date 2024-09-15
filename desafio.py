CONSTANTE_BONUS = 1000

nome_usuario = input("Digite o seu nome: ")

salaraio_usuario = float(input("Digite o seu salario: "))

bonus_usuario = float(input("Digite o seu bonus: "))     

valor_bonus = CONSTANTE_BONUS + salaraio_usuario * bonus_usuario

print(f"O usuário {nome_usuario} possui o bonus de {valor_bonus}")
