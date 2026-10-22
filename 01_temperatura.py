# EXERCÍCIO 01 — CLASSIFICADOR DE TEMPERATURA
#
# Enunciado:
# Corrija a classificação de temperatura.
#
# Regras:
# - abaixo de 15 graus: "Frio"
# - de 15 até 30 graus: "Ameno"
# - acima de 30 graus: "Quente"
#
#
# Testes manuais:
# - 14 deve resultar em "Frio"
# - 15 deve resultar em "Ameno"
# - 30 deve resultar em "Ameno"
# - 31 deve resultar em "Quente"

temperatura = int(input("Digite a temperatura: "))

if temperatura <= 15:
    print("Frio")
else:
    if temperatura <= 30:
        print("Ameno")
    else:
        print("Quente")