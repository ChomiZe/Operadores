print("Introduce dos numero a comparar: \n")

nu_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))

print("\n Los numeros a comparar son: ", nu_uno, "y", num_dos, "\n")

if nu_uno == num_dos:
    print("Son Iguales")
if nu_uno != num_dos:
    print("Son Diferentes")
if nu_uno < num_dos:
    print("Es menor")
if nu_uno > num_dos:
    print("Es mayor")
if nu_uno <= num_dos:
    print("Es menor o igual")
if nu_uno >= num_dos:
    print("Es mayor o igual")
