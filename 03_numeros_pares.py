# EXERCÍCIO 03 — CONTADOR DE NÚMEROS PARES
#
# Enunciado:
# Corrija o programa para contar quantos números pares existem
# entre 1 e o limite informado.
#
#
# Testes manuais:
# - limite 5: resultado esperado = 2
# - limite 10: resultado esperado = 5
#

limite = int(input("Digite um limite: "))
quantidade_pares = 0

for numero in range(1, limite + 1):
    if numero % 2 == 1:
        quantidade_pares = quantidade_pares + 1

print("Quantidade de números pares:", quantidade_pares)