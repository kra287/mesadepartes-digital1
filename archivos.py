# ---------- GENERAR EXPEDIENTE ----------
def generar_expediente(dni):
    return "EXP-2026-" + dni


# ---------- GUARDAR EXPEDIENTE ----------
ARCHIVO = "expedientes.txt"


def guardar_expediente(registro):
    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.write(";".join(registro) + "\n")
    archivo.close()


# ---------- CARGAR EXPEDIENTES ----------
def cargar_expedientes():
    lista = []

    archivo = open(ARCHIVO, "a", encoding="utf-8")
    archivo.close()

    archivo = open(ARCHIVO, "r", encoding="utf-8")

    for linea in archivo:
        linea = linea.strip()

        if linea != "":
            lista.append(linea.split(";"))

    archivo.close()
    return lista


# ---------- BUSCAR EXPEDIENTE ----------
def buscar_expediente(lista, buscado):
    for registro in lista:
        if registro[0] == buscado:
            return registro

    return None
