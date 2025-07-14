# Primeiro uso de import dataclass nesse código


# # Importa o decorator dataclass para simplificar a criação de classes
from dataclasses import dataclass
import os
# Decorador que transforma a classe para criar automaticamente o __init__, __repr__, etc
@dataclass

# vou utilizar a mesma ideia da calculadora_cientifica.py

class Calculadora:
    a: float = 0
    b: float = 0

    def soma(self) -> float: # -> Infomra que essa função deverá retornar o valor da frente.
        return self.a + self.b

    def sub(self) -> float:
        return self.a - self.b

    def limpar_tela():
    # Comando 'cls' para Windows, 'clear' para Linux/macOS
        os.system('cls' if os.name == 'nt' else 'clear')

print ("soma = 1")
print ("subtração = 2")
escolha = int(input("escolha uma opção a cima:"))
a = float(input("Digite o valor de a: "))
b = float(input("DIgite o valor de b: "))

calc = Calculadora(a,b)

if escolha == 1:
         print (calc.soma())
elif escolha == 2:
    print (calc.sub())


# O próposito desse arquivo é para experimentar o uso do import dataclass e como seria a substituição
# do mesmo no construtor __init__
# no arquivo calculadora_cientifica.py tem a utilização do construtor de modo claro
