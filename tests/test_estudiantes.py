from app.estudiantes import registrar_estudiante, calcular_promedio, aprobo


def test_registrar_estudiante_valido():
    resultado = registrar_estudiante("Juan", 20)
    assert resultado == "Estudiante Juan registrado con 20 años"


def test_registrar_estudiante_invalido():
    assert registrar_estudiante("", 20) == "Datos inválidos"
    assert registrar_estudiante("Juan", 0) == "Datos inválidos"


def test_calcular_promedio():
    assert calcular_promedio([8, 9, 7]) == 8.0
    assert calcular_promedio([]) == 0


def test_aprobo():
    assert aprobo(8) == "si aprobó"
    assert aprobo(5) == "no aprobó"
    assert aprobo(7) == "si aprobó"