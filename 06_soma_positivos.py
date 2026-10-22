# EXERCÍCIO 06 — SOMA DE NÚMEROS POSITIVOS
#
# Enunciado:
# O programa deve ler cinco números e somar somente os positivos.
#
#
# Teste manual:
# Entradas: 5, -2, 3, -1, 4
# Resultado esperado: 12


soma = 0

for contador in range(1, 6):
    numero = int(input("Digite o número " + str(contador) + ": "))

    if numero < 0:
        soma = soma + numero

print("Soma dos positivos:", soma)