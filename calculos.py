GREEN = '\033[32m'
RED = '\033[31m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'
YELLOW = '\033[33m'

print("")

print("◈ ━━━━━━━━━━━━━━ ◆ ━━━━━━━━━━━━━━ ◈")

print(MAGENTA+"Author:")
print("╔╗","","","","","","","","","","","╔╗")
print("║╚╗","╔═╗","","╔╗","","║╚╗","╔═╗")
print("║╬║","║╬╚╗","║╚╗","║╔╣","║╬╚╗")
print("╚═╝","╚══╝","╚═╝","╚═╝","╚══╝")

print("")

print(BLUE+"(•ิ_•ิ) Hola mucho gusto")
print(BLUE+"soy un programa que realiza sumas, restas,")
print(BLUE+"multiplicaciones, divisiones,")
print(BLUE+"entregó el residuo de una división")
print(BLUE+"y elevo un número a la potencia.")

print("")

nombre = input(MAGENTA+">> ¿desea utilizarme? ")
print(MAGENTA+"¿",nombre, "?,","muy bien")

if nombre == "no":
    print("(/•ิ_•ิ)/ Entonces vete.")
if nombre == "No":
    print("(/•ิ_•ิ)/ Entonces vete.")
if nombre == "NO":
    print("(/•ิ_•ิ)/ Entonces vete.")
if nombre == "nop":
    print("(/•ิ_•ิ)/ Entonces vete.")
if nombre == "Nop":
    print("(/•ิ_•ิ)/ Entonces vete.")
if nombre == "NOP":
    print("(/•ิ_•ิ)/ Entonces vete.")

print("")

print(WHITE+"..:acontinuación digite los números a utilizar:..")

numero1 = float(input(MAGENTA+">> Digite una Cantidad: "))
numero2 = float(input(MAGENTA+">> Digite una Segunda Cantidad: "))

print(MAGENTA+"")

print("","╔═╗")
print("╔╝ ╚╗","","╔═══╗")
print("╚╗ ╔╝","","╚═══╝")
print("","╚═╝")

print("")
print(WHITE+"..:Operaciones:..")
print(BLUE+"a)suma")
print("b)resta")
print("c)multiplicacion")
print("d)división")
print("e)residuo de división")
print("f)elevar a la potencia")
e = input(MAGENTA+">>¿Qué operación desea realizar? " )
print("")

if e == "a":
    r = numero1 + numero2
    print(BLUE+"( ^-^)/ respuesta es:", r)
elif e == "b":
    r = numero1 - numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
if e == "c":
    r = numero1 * numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
elif e == "d":
    r = numero1 / numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
if e == "e":
    r = numero1 % numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
elif e == "f":
    r = numero1 ** numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
if e == "A":
    r = numero1 + numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
elif e == "B":
    r = numero1 - numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
if e == "C":
    r = numero1 * numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
elif e == "D":
    r = numero1 / numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
if e == "E":
    r = numero1 % numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)
elif e == "F":
    r = numero1 ** numero2
    print(BLUE+"( ^-^)/ La respuesta es:", r)

print("")

print(WHITE+"..:Gracias por utilizarme hasta luego uwu:..")
print("✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏")










