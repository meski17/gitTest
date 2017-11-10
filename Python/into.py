import printHelloWorld
counter = 0

if counter < 50:
    print("counter ist kleiner als 50")
    counter -= 1
elif counter == 50:
    print("counter ist 50")
else:
    print("counter groesser als 50")


while counter > 0:
    print("Counter: ",  counter)
    counter -= 1


x = 0
while x < 50:
    print("X: ", x)
    x += 1
print("------------------------")


meski = ["42", "Java", "Haskell"]
for x in meski:
    for y in meski:
        print(x, y)

print("-----------------------")

for i in range(5, 12, 2):
    print(i)

print("-----------------------")

for i in range(0, len(meski), 2):
    print(i)

print("-----------------------Break And Countinue")

for i in range(5, 21):
    if i % 2 == 0:
        break  # Bricht die ganze Schleife ab, also verschwindet alles
    print(i)

print("_____ und hier continue")
for i in range(0, 21):
    if i % 2 == 1:
        continue

print("Funktionen ---------------")


def allNumbersFromTo(a, b, steps):
    for i in range(a, b, steps):
        print(i)
    print("finisch")


allNumbersFromTo(4, 10, 2)


print("-----------------------------------")
m = """ meskidfgdfgdfgdfgfdgfgdfg g dfg dfgdgdf g dfg gdfg
dfgdfgdfgdfffgd gdfgdf gdfgdfgdfgfdgdfg
gdgdfgdfgdfgdfgdfgdffgdffgdfgdfgdfgdf "gdfgsfdgd" dgsdfgsfdg
dfgsdg'tsdfgsfdg"""

print(type(m))

test = 5 + 2j

print(type(test))
print(test.imag)
print(test.real)

print("-----------------Defaultwerte")


def fib(n=5):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def f1(L=[]):
    L.append(42)
    return L


def f(L=None):
    if L is None:
        L = []
    L.append(2)
    L.append(6)
    L.append(4)

    return L


print(f1())
print(f1())
print(f())
print(f())

print()
printHelloWorld.func()
