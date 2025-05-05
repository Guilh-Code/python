pessoas = {
    'nome' : 'Guilherme',
    'sexo' : 'M',
    'idade' : 19
}

pessoas['peso'] = 70.6
pessoas['nome'] = 'Leandro'
del pessoas['sexo']

print(pessoas)
print(pessoas['nome'])

print('-' * 30)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('-' * 30)

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('-' * 20)

for k in pessoas.keys():
    print(k)

print('-' * 20)

for k in pessoas.values():
    print(k)

print('-' * 20)

for k, v in pessoas.items():
    print(f'{k} = {v}')
