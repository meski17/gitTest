import printHelloWorld


def fib(n=5):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def f(L=None):
    if L is None:
        L = []
    L.append(42)
    return L


printHelloWorld.func()


if __name__ == "__main__":
    alter = input("Wie alt bist du?: ")
    """
    hier bekommt man einen String daher muss man casten
    """
    alter2 = int(alter) + 5
    print("in 5 Jahren " + str(alter2))
    file_dat = open('text', 'r+')
    """
    es gibt auch in modus nur das w-write .. lesen geht nicht
    a mous - nur anhaengen an der TextDatei
    r+ readAndWrite
    r is also only for read
    mit b ist es in binaryFreom lesen und schreiben
    nur eine Zeile lesen readline() erte Zeile
    mit read(2) bekomme ich die ersten 2 Buchstaben
    """
    print("-----")
    print(file_dat.read())

    file_dat.write("Meski")
    """
    Der w Modus lescht alles weg und screibt erst...
    """
    file_dat.close()
    file_dat = open('text', 'r+')
    file_dat.read()
    file_dat.close()
