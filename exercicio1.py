'''Preencha um dicionário com as informações de 5 pessoas.
- Utilize o cpf da passoa como chave e o nome como valor.
- Solicite os dados ao usuário'''

dados_do_cliente = {}
for i in range(5):
    cpf = int(input("Insira seu CPF: "))
    nome = input("Digite seu nome: ")
    dados_do_cliente[cpf] = nome 
print(dados_do_cliente)