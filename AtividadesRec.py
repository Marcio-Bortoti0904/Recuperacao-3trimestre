#Exercícios de programação:
print("-------Exercício 1------- ")
print("---Controle do sistema de climatização de uma estufa sensível---")
temp_C = float(input("Digite a temperatura atual da estufa em Celsius(ºC) = "))
if temp_C < 15:
  print("Temperatura Baixa - Ligar Aquecedor")
elif temp_C > 15 and temp_C < 30:
  print("Temperatuura Ideal - Sistema em Espera")
elif temp_C >= 30:
  print("Temperatura Alta - Ligar Exaustores")
else:
  print("Tente Novamente")

print("-------Exercício 2 ------- ")
print("---Monitoramento de Corrente Elétrica---")
correntes = [0.5 , 1.2 , 0.8 , 1.5 , 0.6 , 1.1 , 0.9 , 1.3]
maior_Am = 0
soma = 0
for corrente in correntes:
     soma += corrente
     if corrente > 1.0:
        maior_Am += 1
media = soma / len(correntes)
print(f"A média de todos os elementos: {media}")
print(f"Existem {maior_Am} leituras maiores que 1.0 Ampere.")

print("-------Exercício 3 ------- ")
print("---Gerador de Tabuada---")
num = int(input(" = "))
i = 0
if num < 0:
  print("Tente Novamente")
else:
   print(f"Tabuada de {num}:")
   for i in range(11):
        print(f" {num} x {i} = {num*i}")
        i += 1

print("-------Exercício 4------- ")
print("---Somatório de Elementos da Matriz---")
matriz = [
    [2,5,1],
    [3,4,2],
    [1,6,3]
]
soma_1 = 0
print("Matriz: ")
for linha in matriz:
    print(linha)
    for elemento in linha:
        soma_1 += elemento
print(f"A soma total de todos os elementos: {soma_1}")

print("-------Exercício 5 -------")
print("---Calculadora de Média com Menu---")
notas = []
while True:
  op = int(input("Bem-vindo ao Menu:\n Escolha entre essas opções:\n . 1 = Inserir nova nota (adicione a nota a uma lista).\n . 2 = Ver notas lançadas.\n . 3 = Calcular média final (soma das notas / quantidade).\n . 0 = Sair."))
  if op == 1:
        nota = float(input("Digite sua nota: "))
        notas.append(nota)

  elif op == 2:
        if len(notas) == 0: 
           print("Nenhuma nota Lançada.")
        else:
            print("Notas encontradas:")
            for i in notas: 
              print(f" - {i}")
  elif op == 3:
        if len(notas) == 0:
            print("Nenhuma nota encontrada para média.")
        else:
          soma_2 = 0
          for elemento in notas:
              soma_2 += elemento
          media = soma_2 / len(notas)
          print(f"A média: {media}")
  elif op == 0:
        print("Encerrando o programa...")
        break
  else:
        print("Opção inválida. Tente novamente.")
