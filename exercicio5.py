'''Crie uma lista de tuplas, onde cada tupla contém informações sobre um aluno:
(Nome do aluno, Idade, Nota média)
Escreva uma função chamada "alunos_aprovados" que recebe a lista de alunos e retorna
uma nova lista apenas com os alunos que têm uma nota média maior ou igual a 7.
Escreva uma função chamada "idade_media" que calcula a idade média de todos os alunos
na lista.
'''

def alunos_aprovados(alunos):
    aprovados = []
    for tupla in alunos:
        if tupla[2] >= 7:
            aprovados.append(tupla)
    return aprovados

alunos = []

while True:
    nome = input("Nome do aluno (digite 0 para finalizr): ")
    if nome == "0":
        break
    idade = int(input("Informe a idade: "))
    media = float(input("Informe a média: "))
    tupla = (nome, idade, media)
    alunos.append(tupla)
print(alunos)
print(alunos_aprovados())











