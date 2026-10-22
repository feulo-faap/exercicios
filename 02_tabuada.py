# EXERCÍCIO 02 — TABUADA
#
# Enunciado:
# Corrija o programa para mostrar a tabuada completa de um número,
# de 1 até 10.
#
#
# Teste manual:
# Para o número 7, a última linha deve ser:
# 7 x 10 = 70


numero = int(input("Digite um número: "))

for multiplicador in range(1, 10):
    resultado = numero * multiplicador
    print(numero, "x", multiplicador, "=", resultado)