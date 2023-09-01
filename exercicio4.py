'''Conte a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é
a vogal e o valor é a quantidade de vezes que essa vogal aparece no texto.'''

quantidade = {}

texto = input("Digite uma frase: ")

for letra in texto.lower():
    if letra in 'aeiou':
        if letra in quantidade:
            quantidade[letra] += 1      # incrementa
        else:
            quantidade[letra] = 1       # insere
    print(quantidade)