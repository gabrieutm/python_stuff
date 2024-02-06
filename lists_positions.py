listaPessoas = ['Mario','Luigi','Yoshi','Peach']

print(listaPessoas)
listaPessoas.append('Bowser')
print(listaPessoas)
listaPessoas.insert(0,'Toad')
print(listaPessoas)
listaPessoas.sort(reverse=True)
print(listaPessoas)


for pessoa in listaPessoas:
  print(f'Bom dia {pessoa}')

pos = listaPessoas.index('Peach')
print(f'Na posicao {pos} está a pessoa {listaPessoas[pos]}.')
