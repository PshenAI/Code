from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.BLACK)
print(Back.GREEN)

first = input( 'Шо делаем? (+,-):')

print(Back.RED)

a = float( input('1ое число:') )
b = float( input('2ое число:') )

print(Back.YELLOW)

if first == "+":
    c = a + b
    print('Маэмо шо маэмо\n' + str(c))
elif first == "-":
    c = a - b
    print('Маэмо шо маэмо\n' + str(c))
else:
    print( "Fuck you!" )

input()

