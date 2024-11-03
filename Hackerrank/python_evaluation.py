s='print(2 + 3)'
co = f"{s}"
try:
    print(eval(eval(co)))
except:
    pass
