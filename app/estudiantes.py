def registrar_estudiante(nombre, edad):
    if nombre == "" or edad <= 0:
        return "Datos inválidos"
    return f"Estudiante {nombre} registrado con {edad} años"


def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def aprobo(promedio):
    if promedio >= 7:
        return "Estudiante aprobado"
    return "Estudiante reprobado"