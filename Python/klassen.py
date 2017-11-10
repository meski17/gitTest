class MyClass:
    zahl = 15
    string = "zeichenkette"

    def my_func(self, m):
        self.zahl = m


instanz = MyClass()
instanz.my_func(4)
print(instanz.zahl)
