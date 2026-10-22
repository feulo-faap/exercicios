# EXERCÍCIO 07 — ALERTA DE CONFIANÇA DE UMA PREVISÃO
#
# Enunciado:
# Um sistema faz previsões e informa uma confiança de 0 a 100.
#
# Regras:
# - confiança maior ou igual a 80: aceitar automaticamente;
# - confiança de 50 até 79: enviar para revisão humana;
# - confiança abaixo de 50: solicitar uma nova análise.
#
# Complete o programa para contar as três situações.
#
# Teste manual:
# Entradas: 90, 70, 30, 80, 49
# Resultado esperado:
# - 2 aceitas automaticamente
# - 1 em revisão humana
# - 2 novas análises
#

automaticas = 0
revisoes = 0
novas_analises = 0

for numero in range(1, 6):
    confianca = int(input("Confiança da previsão " + str(numero) + ": "))

    if confianca >= 80:
        print("Aceitar automaticamente")
        automaticas = automaticas + 1
    else:
        # TODO:
        # Complete usando if e else aninhados.
        # Atualize revisoes ou novas_analises.
        print("Classificação ainda não implementada")

print("Aceitas automaticamente:", automaticas)
print("Em revisão humana:", revisoes)
print("Nova análise necessária:", novas_analises)