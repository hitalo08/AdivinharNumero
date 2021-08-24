import random
import emoji
print(emoji.emojize(':beating_heart:'*27))
print('\033[35mJogo de adivinhação\033[m'.center(50))
print("""\033[32mVocê poderá escolher o nivel de dificuldade     
e começará com 1000 pontos. Os seus pontos 
serão subtraído pelo valor correspondente 
a diferença entre o chute e o numero secreto\033[m""")
print(emoji.emojize(':beating_heart:'*27))
n = random.randint(1,40)
n1 = 20
n2 = 10
n3 = 5
print('         Nivel 1 - 20 Tentativas\n         Nivel 2 - 10 Tentativas\n         Nivel 3 - 5 Tentativas')
print(emoji.emojize(':beating_heart:'*27))
nivel = int(input('\033[36mQual nivel deseja?\033[m '.rjust(38)))
print(emoji.emojize(':beating_heart:'*27))
if nivel == 1:
    print('  Você escolheu o nivel 1. Restantes {}'.format(n1))
    while n1 > 0:
        print(emoji.emojize(':beating_heart:' * 27))
        v = int(input('Valor: '))
        print(emoji.emojize(':beating_heart:' * 27))
        if v == n:
            print('\033[36mVocê acertou o número secreto!!!')
            break
        elif v > n:
            print(emoji.emojize('\033[35mO número digitado é maior que o número secreto.\033[m :up_arrow:'))
        elif v < n:
            print(emoji.emojize('\033[36mO número digitado é menor que o número secreto.\033[m :down_arrow:'))
        else:
            print('Valor inválido')
        print('Você possui {} tentativas'.format(n1))
        n1 = n1 - 1
    print('Número secreto: {}'.format(n))
if nivel == 2:
    print('  Você escolheu o nivel 2. Restantes {}'.format(n2))
    print(emoji.emojize(':beating_heart:' * 27))
    while n2 > 0:
        print(emoji.emojize(':beating_heart:' * 27))
        v = int(input('Valor: '))
        print(emoji.emojize(':beating_heart:' * 27))
        if v == n:
            print('\033[36mVocê acertou o número secreto!!!')
            break
        elif v > n:
            print(emoji.emojize('\033[35mO número digitado é maior que o número secreto.\033[m :up_arrow:'))
        elif v < n:
            print(emoji.emojize('\033[36mO número digitado é menor que o número secreto.\033[m :down_arrow:'))
        else:
            print('Valor inválido')
        print('Você possui {} tentativas'.format(n2))
        n2 = n2 - 1
    print('Número secreto: {}'.format(n))
if nivel == 3:
    print('  Você escolheu o nivel 3. Restantes {}'.format(n3))
    print(emoji.emojize(':beating_heart:' * 27))
    while n3 > 0:
        print(emoji.emojize(':beating_heart:' * 27))
        v = int(input('Valor: '))
        print(emoji.emojize(':beating_heart:' * 27))
        if v == n:
            print('\033[36mVocê acertou o número secreto!!!')
            break
        elif v > n:
            print(emoji.emojize('\033[35mO número digitado é maior que o número secreto.\033[m :up_arrow:'))
        elif v < n:
            print(emoji.emojize('\033[36mO número digitado é menor que o número secreto.\033[m :down_arrow:'))
        else:
            print('Valor inválido')
        print('Você possui {} tentativas'.format(n3))
        n3 = n3 - 1
    print('Número secreto: {}'.format(n))

