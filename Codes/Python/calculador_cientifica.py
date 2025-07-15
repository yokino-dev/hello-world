import math
import time  # Corrigido: era 'timer'
import os

# Funções matemáticas úteis para calculadora científica:

# math.sqrt(x)       -> Raiz quadrada de x
# math.pow(x, y)     -> x elevado à potência y (x^y)
# math.sin(x)        -> Seno de x (x em radianos)
# math.cos(x)        -> Cosseno de x (x em radianos)
# math.tan(x)        -> Tangente de x (x em radianos)
# math.log(x)        -> Logaritmo natural (base e) de x
# math.log10(x)      -> Logaritmo na base 10 de x
# math.exp(x)        -> Exponencial e^x
# math.degrees(x)    -> Converte x de radianos para graus
# math.radians(x)    -> Converte x de graus para radianos
# math.factorial(x)  -> Fatorial de x (x deve ser inteiro não negativo)
# math.ceil(x)       -> Arredonda x para cima (inteiro)
# math.floor(x)      -> Arredonda x para baixo (inteiro)
# math.fabs(x)       -> Valor absoluto de x (float)
# math.isclose(a,b)  -> Verifica se a e b são aproximadamente iguais

# Exemplo:
# Para calcular o seno de 30 graus, converta para radianos antes:
# math.sin(math.radians(30))  -> 0.5

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


class Calculadora:
    def __init__(self, a=0, b=0, valor=0):
        # O método __init__ é o construtor da classe.
        # Ele é chamado automaticamente quando criamos um objeto da classe,
        # e serve para inicializar os atributos do objeto com os valores passados.

        # O parâmetro 'self' representa o próprio objeto criado,
        # permitindo que a gente defina ou acesse seus atributos e métodos.
        self.valor = 0
        self.a = a
        self.b = b


    def soma(self):
        self.a = int(input("Escolha um número:\n"))
        self.b = int(input("Escolha outro número:\n"))
        resultado = self.a + self.b
        print(f"O resultado da soma é {resultado}")

        while True:
            resposta = input("Você deseja continuar a soma a partir do valor obtido? [S/n] ").strip().lower()
            if resposta in ['', 's']:
                try:
                    novo_valor = int(input("Digite o valor para acrescentar\n"))
                except ValueError:
                    print("Digite um valor válido")
                    continue
                self.a = resultado
                self.b = novo_valor
                resultado = self.a + self.b
                print(f"Novo resultado: {resultado}")
            else:
                print("Saindo do Módulo de soma")
                break


    def sub(self):
        self.a = int(input("Escolha um número:\n"))
        self.b = int(input("Escolha outro número:\n"))
        resultado = self.a - self.b
        print(f"O resultado da subtração é {resultado}")

        while True:
            resposta = input("Você deseja continuar a subtração a partir do valor obtido? [S/n] ").strip().lower()
            if resposta in ['', 's']:
                try:
                    novo_valor = int(input("Digite o valor para subtrair\n"))
                except ValueError:
                    print("Digite um valor válido")
                    continue
                self.a = resultado
                self.b = novo_valor
                resultado = self.a - self.b
                print(f"Novo resultado: {resultado}")
            else:
                print("Saindo do Módulo de subtração")
                break


    def multiplicacao(self):
        self.a = float(input("Escolha um número:\n"))
        self.b = float(input("Escolha outro número:\n"))
        resultado = self.a * self.b
        print(f"O resultado da multiplicação é {resultado}")

        while True:
            resposta = input("Você deseja continuar a multiplicação a partir do valor obtido? [S/n] ").strip().lower()
            if resposta in ['', 's', 'sim']:
                try:
                    novo_valor = float(input("Digite o valor para multiplicar: "))
                except ValueError:
                    print("Digite um valor válido.")
                    continue
                self.a = resultado
                self.b = novo_valor
                resultado = self.a * self.b
                print(f"Novo resultado: {resultado}")
            else:
                print("Saindo do módulo de multiplicação.")
                break


    def divisao(self):
        while True:
            try:
                self.a = int(input("Escolha um número:\n"))
                self.b = int(input("Escolha outro número:\n"))

                if self.b == 0:
                    print("Não é possível dividir por zero.")
                    continue

                resultado = self.a / self.b
                print(f"O valor da sua divisão é {resultado:.2f}")
                time.sleep(2)

                resposta = input("Você gostaria de fazer uma nova divisão? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break

            except ValueError:
                print("Digite um número válido.")


    def raiz_quadrada(self):
        while True:
            try:
                self.a = float(input("Escolha um valor para descobrir a raiz quadrada: "))
                if self.a < 0:
                    print("Erro: Raiz quadrada de número negativo não é definida nos reais.")
                    time.sleep(2)
                    limpar_tela()
                    continue

                resultado = math.sqrt(self.a)
                print(f"A raiz quadrada de {self.a} é {resultado:.2f}")
                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja descobrir outro valor? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Digite um valor numérico válido.")
                time.sleep(2)
                limpar_tela()


    def logaritmo(self, base=10):
        while True:
            try:
                self.a = float(input("Escolha um valor para descobrir o logaritmo: "))
                if self.a <= 0:
                    print("Erro: Logaritmo aceita apenas número positivo.")
                    time.sleep(2)
                    limpar_tela()
                    continue
                resultado = math.log(self.a, base)
                print(f"Logaritmo de {self.a} na base {base} é {resultado:.2f}")
                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja descobrir outro valor? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Por favor, digite um número válido.")
                time.sleep(2)
                limpar_tela()


    def seno(self):
        while True:
            try:
                self.a = float(input("Digite o ângulo em graus para calcular o seno: "))
                rad = math.radians(self.a)
                resultado = math.sin(rad)
                print(f"Seno de {self.a}° é {resultado:.4f}")
                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja calcular outro seno? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Digite um valor numérico válido.")
                time.sleep(2)
                limpar_tela()


    def cosseno(self):
        while True:
            try:
                self.a = float(input("Digite o ângulo em graus para calcular o cosseno: "))
                rad = math.radians(self.a)
                resultado = math.cos(rad)
                print(f"Cosseno de {self.a}° é {resultado:.4f}")
                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja calcular outro cosseno? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Digite um valor numérico válido.")
                time.sleep(2)
                limpar_tela()


    def tangente(self):
        while True:
            try:
                self.a = float(input("Digite o ângulo em graus para calcular a tangente: "))
                rad = math.radians(self.a)

                # Verifica se está próximo de 90°, 270°, etc., onde a tangente tende ao infinito
                if math.isclose(math.cos(rad), 0, abs_tol=1e-9):
                    print("Erro: Tangente indefinida para este ângulo.")
                else:
                    resultado = math.tan(rad)
                    print(f"Tangente de {self.a}° é {resultado:.4f}")

                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja calcular outra tangente? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Digite um valor numérico válido.")
                time.sleep(2)
                limpar_tela()


    def area_circulo(self):
        while True:
            try:
                self.a = float(input("Digite o raio do círculo: "))
                if self.a < 0:
                    print("Erro: O raio não pode ser negativo.")
                    time.sleep(2)
                    limpar_tela()
                    continue

                area = math.pi * (self.a ** 2)
                print(f"A área do círculo de raio {self.a} é {area:.2f}")
                time.sleep(2)
                limpar_tela()
                resposta = input("Deseja calcular outra área? [S/N] ").strip().lower()
                if resposta not in ['s', 'sim', '']:
                    break
                limpar_tela()
            except ValueError:
                print("Digite um valor numérico válido.")
                time.sleep(2)
                limpar_tela()


def menu():
    calc = Calculadora()
    while True:
        limpar_tela()
        print("=== CALCULADORA ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Raiz Quadrada")
        print("6 - Logaritmo")
        print("7 - Seno")
        print("8 - Cosseno")
        print("9 - Tangente")
        print("10 - Área do Círculo")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ").strip()

        match escolha:
            case '1':
                calc.soma()
            case '2':
                calc.sub()
            case '3':
                calc.multiplicacao()
            case '4':
                calc.divisao()
            case '5':
                calc.raiz_quadrada()
            case '6':
                calc.logaritmo()
            case '7':
                calc.seno()
            case '8':
                calc.cosseno()
            case '9':
                calc.tangente()
            case '10':
                calc.area_circulo()
            case '0':
                print("Encerrando...")
                break
            case _:
                print("Opção inválida.")
                time.sleep(2)

menu()
