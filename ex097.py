# Exercício Python 097: Faça um programa que tenha uma função chamada
# escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.
#
# Ex:
# escreva('Olá, Mundo!')
# Saída:
# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(texto):
    tamanho = len(texto) + 4
    print('~'*tamanho)
    print(f'  {texto}')
    print('~'*tamanho)


escreva('david martins leite')
escreva('casa')
