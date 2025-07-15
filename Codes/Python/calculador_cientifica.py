import math
import timer

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
 

class calculadora:
    def __init__(self,a = 0,b = 0, valor=0):
 # O método __init__ é o construtor da classe.
# Ele é chamado automaticamente quando criamos um objeto da classe,
# e serve para inicializar os atributos do objeto com os valores passados.

# O parâmetro 'self' representa o próprio objeto criado,
# permitindo que a gente defina ou acesse seus atributos e métodos.
        self.valor = 0
        self.a = a
        self.b = b


    def soma (self):
        self.a = int(input("Escolha um número:\n"))
        self.b = int(input("Escolha outro número:\n "))
        resultado = self.a + self.b
        print (f"O resultado da soma é {resultado}")

        while True:
            resposta = input("Você deseja continuar a soma a partir do valor obtido? [S/n]").strip().lower()
            if resposta == '' or resposta in ['s']:
                try:
                    novo_valor = int(input("Digite o valor para acresentar\n"))
                except ValueError:
                    print ("Digite um valor válido")
                    continue
                self.a = resultado
                self.b = novo_valor
                resultado = self.a + self.b

            else:
                print("Saindo do Módulo de soma")
                break


    def sub (self):
        self.a = int(input("Escolha um número:\n"))
        self.b = int(input("Escolha outro número:\n "))
        resultado = self.a - self.b
        print (f"O resultado da soma é {resultado}")

        while True:
            resposta = input("Você deseja continuar a subtração a partir do valor obtido? [S/n]").strip().lower()
            if resposta == '' or resposta in ['s']:
                 try:
                     novo_valor = int(input("Digite o valor para acresentar\n"))
                 except ValueError:
                    print ("Digite um valor válido")
                    continue
                    self.a = resultado
                    self.b = novo_valor
                    resultado = self.a - self.b

            else:
                    print("Saindo do Módulo de subtração")
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
                        timer.sleep(2)

                        resposta = input("Você gostaria de fazer uma nova divisão? [S/N] ").strip().lower()
                        if resposta not in ['s', 'sim', '']:
                            break

                    except ValueError:
                        print("Digite um número válido.")
    def raiz_quadrada(self):
          while True:
                  try:
                      self.a = int(input("Escolha um valor para descobrir a raiz quadrada"))
                      if self.a < 0:
                              return 'Erro: Raiz quadrada de número negativo não definida'
                              continue
                      else:
                          return f'{math.sqrt(self.a):.2f}'
                          timer.sleep(2)
                          limpar_tela()
                          resposta = input("Deseja descobrir outro valor? [S/N]")
                          if resposta not in ['s', 'sim', '']:
                                  break
                  except ValueError:
                      print ("DIgite um valor válido")

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
    
                                               
