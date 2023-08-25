# cadastro do cliente 
# código do cliente / nome do cliente 
cadastro = {123: 'Luani', 532: 'Camis', 897: 'Lety'}
cadastro = {123: 'Luani', 
            532: 'Camis', 
            897: 'Lety'}
print(cadastro)
print(cadastro[532])

# alterar item 
cadastro[532] = 'Camis linda'
print(cadastro)

# inserir um item 
cadastro[652] = 'LuCa'
print(cadastro)

# remover um item 
cadastro.pop(652)
print(cadastro)

# busca de uma chave especifica 
codigo = int(input('Código: '))
if codigo in cadastro:
    print(f'Cliente cadastrado: {cadastro[897]}')
else: 
    print('Cliente não cadastrado')
