GREEN = '\033[32m'
RED = '\033[31m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
WHITE = '\033[37m'

print("Author:",MAGENTA+"")
print("╔╗","","","","","","","","","","","╔╗")
print("║╚╗","╔═╗","","╔╗","","║╚╗","╔═╗")
print("║╬║","║╬╚╗","║╚╗","║╔╣","║╬╚╗")
print("╚═╝","╚══╝","╚═╝","╚═╝","╚══╝")

print("")

print(GREEN+"Hola mucho gusto")
print(GREEN+"soy un programa que realiza sumas, restas,")
print(GREEN+"multiplicaciones, divisiones,")
print(GREEN+"entregó el residuo de una división")
print(GREEN+"y elevo un número a la potencia.")

print("")

nombre = input(RED+">> ¿desea utilizarme?: ")
print(GREEN+"¿",nombre, "?,","muy bien")

if nombre == "no":
    print("Entonces vete")
if nombre == "No":
    print("Entonces vete")
if nombre == "NO":
    print("Entonces vete")
if nombre == "nop":
    print("Entonces vete")
if nombre == "Nop":
    print("Entonces vete")
if nombre == "NOP":
    print("Entonces vete")

print("")

print(BLUE+"..:acontinuación digite los números a utilizar:..")

numero1 = float(input(RED+">> Digite un número: "))
numero2 = float(input(RED+">> Digite un segundo número: "))

print(MAGENTA+"")

print("","╔═╗")
print("╔╝ ╚╗","","╔═══╗")
print("╚╗ ╔╝","","╚═══╝")
print("","╚═╝")

print(RED+"")

print("a)suma")
print("b)resta")
print("c)multiplicacion")
print("d)división")
print("e)residuo de división")
print("f)elevar a la potencia")
e = input(RED+">> ¿Qué operación desea realizar? " )
print("")

if e == "a":
    r = numero1 + numero2
    print(GREEN+"La respuesta es:", r)
elif e == "b":
    r = numero1 - numero2
    print(GREEN+"La respuesta es:", r)
if e == "c":
    r = numero1 * numero2
    print(GREEN+"La respuesta es:", r)
elif e == "d":
    r = numero1 / numero2
    print(GREEN+"La respuesta es:", r)
if e == "e":
    r = numero1 % numero2
    print(GREEN+"La respuesta es:", r)
elif e == "f":
    r = numero1 ** numero2
    print(GREEN+"La respuesta es:", r)
if e == "A":
    r = numero1 + numero2
    print(GREEN+"La respuesta es:", r)
elif e == "B":
    r = numero1 - numero2
    print(GREEN+"La respuesta es:", r)
if e == "C":
    r = numero1 * numero2
    print(GREEN+"La respuesta es:", r)
elif e == "D":
    r = numero1 / numero2
    print(GREEN+"La respuesta es:", r)
if e == "E":
    r = numero1 % numero2
    print(GREEN+"La respuesta es:", r)
elif e == "F":
    r = numero1 ** numero2
    print(GREEN+"La respuesta es:", r)

print("")

print(BLUE+"Gracias por utilizarme hasta luego uwu.")









