import os
import time

# Esse pequeno código em Python irá fazer as 4 operações básica da matemática:
# Somar, Subtrair, Multiplicação, Divisão
# O intuito principal desse conceito código são para utilizar as funções (def)
# e como são aplicadas dentro do código.
# pretendo melhorar futuramente pra torna-lo uma calculadora cientifica de facil uso
# no momento apenas diretamente pelo terminal, depois aplicando interface grafica, começando pela
# mais simples, Tkinter, nativa do Python.

# Editor de Código: helix - Konsole

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Mac

class Calculadora:
    def soma (self,a,b):
        c = a+b
        return c

    def subtrair (self,a,b):
        c = a-b
        return c

    def multiplicaçao (self,a,b):
        c = a*b 
        return c

    def dividir(self, a,b):
        if b != 0:
            return a / b

        else:
            return "Valor invalido"


print ("Bem vindo a calculadora simples \n feita em Python!")
time.sleep(4)
limpar_tela()

while True:
     try:
        a = int(input("Escolha um valor para a:"))
        b = int(input("Escolha um valor para b:"))

        calc = Calculadora()
        print (calc.soma(a,b))
        print (calc.subtrair(a,b))
        print (calc.multiplicaçao(a,b))
        print (calc.dividir(a,b))

        continua = input("deseja escolher outro valor?:S/n[ ]").lower() .strip()

        if continua == "" or continua in ["s","y"]:
          print ("Reiniciando a calculadora simples")
          time.sleep (2)
          limpar_tela()

        else:
            print ("até a próxima!")
            break
     except ValueError:
        print("Insira um número inteiro valido!")
        
