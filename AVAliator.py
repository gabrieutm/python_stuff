def espaço():   #criei uma função para evitar repetições durante o código e deixá-lo mais apresentável.
  print('')

print('Bem-vindo ao AVAliator. Aqui vamos calcular a nota dos seus alunos e retornar seus respectivos resultados.')
espaço()
print('Tenha em mãos as seguintes informações: a quantidade de alunos que serão avaliados e o nome completo de todos estes alunos, bem como suas respectivas notas.')
espaço()

students = {} #criei um dicionário vazio para que posteriormente seja inserido nele a chave (nome) e o valor (notas), de acordo com o exercício.

n = int(input('Qual a quantidade de alunos? ')) #de acordo com o exercício, "n" é a quantidade de alunos, acabei utilizando a mesma variável.


for quantity in range(n): #de acordo com a quantidade de alunos(n), esse código irá se repetir novamente somente ao término loop "for" a seguir, perguntando o nome e criando mais uma lista com seus respectivos dados.
  
  espaço()
  name = input('Digite o nome e o sobrenome do(a) aluno(a): ')
  espaço()

  grades = []   #criei uma lista vazia para que pudesse armazenar as posteriores notas dos alunos, essa lista vai se repetir de acordo com a função "for" de antes.


  for test in range(1,5):   #de acordo com o exercício, são 4 notas, por isso o "range" vai de 1 à 5 (sempre um a menos, ou seja, 4).

    grade = float(input(f'Digite a nota da {test}ª avaliação: ')) #as notas podem ser tanto números inteiros quanto fracionados, por isso decidi deixar como "float". A váriavel "test" (que é a que repete no loop) é o número de 1 à 4, perguntando o número de cada avaliação.
    grades.append(grade)  #a lista vazia de antes será preenchida com as 4 notas.


  students[name] = grades #pego os nomes e notas, agora defini o que é a chave, que nesse caso é nome, e o que é o valor, que nesse caso são as notas, e atualizei o dicionário de antes, automaticamente criando uma lista para cada nome e notas dados, sem misturá-los.


for student, grades in students.items():  #com o dicionário atualizado e possuindo 2 váriaveis (chave e valor), criei um loop que irá se repetir de acordo com a quantidade de itens (valor e chave juntos) dentro do dicionário.


  average = sum(grades)/4   #está função irá somar todos os números dentro do "valor" (que é a variável "grades") e irá dividí-los por 4, que é a quantidade de avaliações. Ao final irá devolver a média.
  

  if average >= 7:  #se na função anterior, a média for maior ou igual a 7, o aluno ficará na categoria de aprovado.
    status = 'Aprovado(a)'

  else: #se na função anterior, a média for menor a 7, o aluno ficará na categoria de reprovado.
    status = 'Reprovado(a)'

  espaço()
  print(f'O(A) aluno(a) {student} recebeu as seguintes notas {grades}. Sua média foi {round(average,1)}.\nResultado: {status}.')  #utilizei a função "round" para arredondar o valor em uma casa decimal de acordo com o exercício.
  #Na mensagem, a variável "student" é o nome, "grades" são as notas, "average" é a média e "status" é o resultado de aprovado ou reprovado. Como foram criados "n" listas por causa do primeiro loop "for" do código, este último loop se repete de acordo com a quantidade de itens destes dicionários, repetindo um após o outro, com seus respectivos dados: nome, notas, média e status, e imprimindo cada um deles.