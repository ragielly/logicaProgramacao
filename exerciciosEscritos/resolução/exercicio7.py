numero_secreto = 7
tentativas = 0

while True:
    chute = int(input("Adivinhe o número (entre 1 e 10): "))
    tentativas += 1
    if chute == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Tente novamente!")