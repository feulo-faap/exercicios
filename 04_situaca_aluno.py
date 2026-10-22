# EXERCÍCIO 04 — SITUAÇÃO DO ALUNO
#
# Enunciado:
# Corrija a regra de aprovação.
#
# Regras:
# - nota maior ou igual a 7: "Aprovado"
# - nota menor que 7: "Recuperação"
#
#
# Testes manuais:
# - nota 6: Recuperação
# - nota 7: Aprovado
# - nota 10: Aprovado


nota = float(input("Digite a nota: "))

if nota > 7:
    print("Aprovado")
else:
    print("Recuperação")