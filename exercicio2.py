'''Preencha um dicionário com as informações de 5 produtos.
- Utilize o nome do produto como chave e o preço como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00'''

dados_produtos = {}
for i in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    dados_produtos[nome] = preco
    
for nome in dados_produtos.values():
    if preco > 50:
        print(dados_produtos[preco])
        