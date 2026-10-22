# Prática de Git e Python

Este repositório contém exercícios curtos de Python para praticar colaboração com Git e GitHub.

Cada estudante deverá corrigir ou completar **apenas um** arquivo dentro da pasta `exercicios/`.

## Objetivos

Ao concluir a atividade, você deverá conseguir:

- clonar um repositório remoto;
- criar e usar uma branch;
- alterar um arquivo;
- executar e testar seu programa;
- revisar alterações com `git status` e `git diff`;
- criar um commit;
- enviar sua branch com `git push`;
- abrir um Pull Request.

## Exercícios

| Arquivo | Tema |
|---|---|
| `01_classificar_temperatura.py` | Classificação de temperatura |
| `02_tabuada.py` | Tabuada com `for` |
| `03_contar_pares.py` | Contagem de números pares |
| `04_situacao_aluno.py` | Aprovação e recuperação |
| `05_senha_tentativas.py` | Tentativas de senha |
| `06_somar_positivos.py` | Soma de números positivos |
| `07_alerta_confianca.py` | Classificação de confiança de previsões |
| `08_planejador_estudos.py` | Plano de estudos com revisão |

## Passo a passo

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
cd pratica-git-python
```

Confirme que está no repositório correto:

```bash
git status
git remote -v
```

### 2. Crie sua branch

Escolha o exercício combinado e crie uma branch com um nome descritivo.

Exemplo:

```bash
git switch -c feature/07-alerta-confianca-seu-nome
```

Não trabalhe diretamente na branch `main`.

### 3. Resolva o exercício

- Altere somente o arquivo que ficou sob sua responsabilidade.
- Leia cuidadosamente os comentários no início do arquivo.
- Execute o programa com:

```bash
python3 exercicios/NOME_DO_ARQUIVO.py
```

- Teste os casos indicados no comentário do exercício.

### 4. Revise sua alteração

```bash
git status
git diff
```

Confirme que apenas o arquivo correto foi alterado.

### 5. Crie o commit

```bash
git add exercicios/NOME_DO_ARQUIVO.py
git commit -m "Corrige NOME_DO_EXERCICIO"
```

Exemplo:

```bash
git commit -m "Corrige contagem de numeros pares"
```

### 6. Envie sua branch

```bash
git push -u origin NOME_DA_BRANCH
```

Exemplo:

```bash
git push -u origin feature/07-alerta-confianca-seu-nome
```

### 7. Abra um Pull Request

No GitHub:

1. abra o repositório;
2. selecione sua branch;
3. clique em **Compare & pull request**;
4. confira se o destino é `main`;
5. descreva brevemente:
   - o que foi corrigido;
   - quais testes foram feitos;
   - o resultado obtido;
6. crie o Pull Request.

## Regras

- Não altere arquivos de outros colegas.
- Não faça `push` diretamente para `main`.
- Não use `git push --force`.
- Não publique senhas, tokens, e-mails pessoais, matrícula ou outros dados pessoais.
- Faça um commit com uma mensagem que descreva a alteração.
- Antes de enviar, sempre use `git status` e `git diff`.

## Critério de conclusão

A atividade estará concluída quando:

- o programa funcionar de acordo com o enunciado;
- os testes manuais indicados forem realizados;
- o commit estiver na sua branch remota;
- existir um Pull Request aberto para `main`.