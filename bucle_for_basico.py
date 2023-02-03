# Básico: imprime todos los números enteros del 0 al 150.
for x in range(0, 151):
    print(x)

print('*' * 20)

# Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for x in range(5, 1000, 5):
    print(x)

print('*' * 20)

# Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for x in range(1, 20):
    if x % 5:
        print(x, 'Coding')
    elif x % 10:
        print(x, 'Coding Dojo')

# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
print('*' * 20)
sum = 0

for x in range(0, 500000):
    if x % 2 != 0:
        sum = (sum + x)
        print(sum)

# Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
print('*' * 20)

for x in range(2018, 0, -4):
    print(x)

# Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas).
print('*' * 20)

lowNum = 2
highNum = 9
multi = 3
i = lowNum

while lowNum <= highNum:
    if lowNum % multi == 0:
        print(lowNum)
    lowNum = lowNum + 1
