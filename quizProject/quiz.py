nombre = input("Ingrese su nombre: ")
dias = int(input("Ingrese los números de días trabajados: "))
salario = int(input("Ingrese su salario: "))

cesantias = (salario * dias)/360

print(f'''Señor {nombre} para los {dias} laborados y salario {salario}, su liquidacion se componen asi:
    prima: {(salario * dias)/360:.2f}
    cesantias: {cesantias:.2f}
    intereses cesantías: {(cesantias * 0.12)/dias:.2f}
    vacaciones: {(salario*dias)/720:.2f}''')