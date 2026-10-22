# EXERCÍCIO 05 — TENTATIVAS DE SENHA
#
# Enunciado:
# O programa deve permitir até três tentativas para acertar a senha.
# Se a senha correta for digitada em qualquer tentativa,
# o acesso deve ser liberado.
#
#
# Testes manuais:
# - acertar na primeira tentativa: acesso liberado
# - acertar na terceira tentativa: acesso liberado
# - errar as três tentativas: acesso bloqueado


senha_correta = "git2026"
acertou = False

for tentativa in range(1, 4):
    senha_digitada = input("Tentativa " + str(tentativa) + ": ")

    if senha_digitada == senha_correta:
        acertou = True
    else:
        print("Senha incorreta")

if acertou:
    print("Acesso liberado")
else:
    print("Acesso bloqueado")