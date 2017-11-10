def f():
    def local():
        var = "local text"

    def do_nonlocal():
        nonlocal var
        var = "non local text"

    def do_global():
        global var
        var = "global text"

    var = "text"
    local()
    do_nonlocal()
    do_global()
    print("after init: ", var)


f()
print("global", var)
