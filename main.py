# Exercícios Extras de Python
# 1. Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda
# estrangeira.
# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21

carteira = float (input ("Digite quanto de dinheiro tem em sua carteira em R$ e descubra o quanto poderia comprar em 7 moedas diferentes:" + '\n'))

# Dólar Americano
# Peso Argentino
# 
# A = 4.91
# B = 0.02
# C = 3.18
# D = 3.64
# E = 0.42
# F = 5.36
# G = 6.21

# def cambio ():
#   print ("R$", A * carteira, "é o valor em Dólar Americano")
#   print ("R$", B * carteira , "é o valor em Peso Argentino")
#   print ("R$", C * carteira , "é o valor em Dólar Australiano")
#   print ("R$", D * carteira , "é o valor em Dólar Canadense")
#   print ("R$", E * carteira , "é o valor em Franco Suiço")
#   print ("R$", F * carteira , "é o valor em Euro")
#   print ("R$", G * carteira , "é o valor em Libra esterlina")
# cambio ()
valor_em_real =1
valor_moeda = [4.91, 
         0.02, 
         3.18,
         3.64,
         0.42,
         5.36,
         6.21
        ]
nome_moeda = ["Dólar Americano", 
         "Peso Argentino", 
         "Dólar Australiano",
         "Dólar Canadense",
         "Franco Suiço",
         "Euro",
         "Libra esterlina"
          ]

for i in range (len(valor_moeda)): #carteira menor que valor
 print ("{value:.2f}".format(value=(valor_em_real / valor_moeda [i]) * carteira) , nome_moeda [i], valor_moeda [i]) #formatacao 
 print (f'{(valor_em_real / valor_moeda [i]) * carteira: .2f}' , nome_moeda [i], valor_moeda [i]) #formatacao abreviada value: e o .2f dois é a quantidade de casas decimais que quero que meu numeral tenha 

# print ("O valor informado em sua carteira pode comprar:" + '\n' , cambio )


# 2. Escreva um programa que pergunte a quantidade de km
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$ 80,00 por dia e R$ 0,20 por km rodado.

# 3. Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário.
# Se o salário for até R$ 1000,00 o funcionário terá 20% de
# aumento.
# Entre R$ 1001,00 até R$ 2800,00 o funcionário terá 10% de
# aumento.
# Acima de R$ 2801,00 o funcionário terá 5% de aumento.

# 4. Crie um programa que tenha a função leiaInt(), que vai funcionar
# de forma semelhante à função input() do Python, só que fazendo a
# validação para aceitar apenas um valor númerico.
# Ex:
# n = leiaInt(‘Digite um n’)