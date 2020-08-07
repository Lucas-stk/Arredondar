import math

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a: {}\n'.format(num, raiz))
p = int(input('Se deu número com vírgula, informe seu número novamente para ser arredondado: '))
print('\n')
print('A raiz arredondada do número {} é igual a: {}\n'.format(num, math.floor(raiz)))
print('##########Feito por Lucas Silva##########')
