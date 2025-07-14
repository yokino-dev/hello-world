import math

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

class Op_basicas:
    def soma(*args): # *args pode receber qualquer quantidade
        total = 0 # variavel para armanezar o resultado da soma
        for num in args # vai somar todos os numeros que a função(*args) recebeu
            total += num # vai ser equivalente a total = total + num
        return total # vai retornar o valor total já com o números somados

    def sub(*args):
        if len(args)<= 2:# len()retorna a quantidade de itens dentro de algo
            raise ValueError("Precisa ser dois números ou mais") # raise serve para lançar um error
