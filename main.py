# ==========================================
# MESA DE PARTES DIGITAL - UPN
# Fundamentos de Programacion
# ==========================================

from validaciones import datos_validos
from archivos import (generar_expediente, guardar_expediente,
                      cargar_expedientes, buscar_expediente)


# ---------- ELEGIR TIPO DE DOCUMENTO ----------
def elegir_tipo_documento():
    print("\nTIPO DE DOCUMENTO")
    print("1. Solicitud")
    print("2. Carta")
    print("3. Oficio")
    print("4. Reclamo")
    print("5. Otro")

    while True:
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            return "Solicitud"
        elif opcion == "2":
            return "Carta"
        elif opcion == "3":
            return "Oficio"
        elif opcion == "4":
            return "Reclamo"
        elif opcion == "5":
            otro = input("Escriba el tipo de documento: ").strip()

            if otro != "" and not otro.isdigit():
                return otro

            print("ERROR: escriba un tipo de documento valido.")
        else:
            print("ERROR: seleccione una opcion del 1 al 5.")


# ---------- BIENVENIDA ----------
def bienvenida():
    print("=" * 45)
    print(" BIENVENIDO A LA MESA DE PARTES DIGITAL")
    print(" Municipalidad de San Martin de Porres")
    print("=" * 45)


# ---------- REGISTRAR EXPEDIENTE ----------
def registrar():
    print("\n--- REGISTRO DE EXPEDIENTE ---")

    while True:
        dni = input("Ingrese DNI (8 digitos): ").strip()

        if len(dni) == 8 and dni.isdigit():
            break
        else:
            print("ERROR: DNI incorrecto. Debe tener 8 digitos numericos.")

    while True:
        nombres = input("Ingrese nombres completos: ").strip()

        if nombres != "" and nombres.replace(" ", "").isalpha():
            break
        else:
            print("ERROR: ingrese nombres validos, no deje vacio.")

    tipo_documento = elegir_tipo_documento()

    while True:
        asunto = input("Ingrese el asunto: ").strip()

        if asunto != "" and not asunto.isdigit():
            break
        else:
            print("ERROR: el asunto no puede estar vacio ni ser solo numeros.")

    while True:
        texto_folios = input("Ingrese cantidad de folios: ").strip()

        if texto_folios.isdigit() and int(texto_folios) > 0:
            cantidad_folios = int(texto_folios)
            break
        else:
            print("ERROR: ingrese un numero entero mayor que cero.")

    numero = generar_expediente(dni)

    nombres = nombres.replace(";", ",")
    tipo_documento = tipo_documento.replace(";", ",")
    asunto = asunto.replace(";", ",")

    registro = [
        numero,
        dni,
        nombres,
        tipo_documento,
        asunto,
        str(cantidad_folios)
    ]

    guardar_expediente(registro)

    print("\nREGISTRO EXITOSO")
    print("Numero de expediente:", numero)


# ---------- BUSCAR EXPEDIENTE ----------
def buscar():
    print("\n--- BUSQUEDA DE EXPEDIENTE ---")

    buscado = input("Ingrese numero de expediente: ").strip()

    if buscado == "":
        print("ERROR: debe ingresar un numero de expediente.")
        return

    lista = cargar_expedientes()
    registro = buscar_expediente(lista, buscado)

    if registro != None:
        print("\nEXPEDIENTE ENCONTRADO")
        print("Numero:", registro[0])
        print("DNI:", registro[1])
        print("Nombres:", registro[2])
        print("Tipo de documento:", registro[3])
        print("Asunto:", registro[4])
        print("Folios:", registro[5])
    else:
        print("ERROR: expediente no encontrado.")


# ---------- PROGRAMA PRINCIPAL ----------
def principal():
    bienvenida()

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Registrar expediente")
        print("2. Buscar expediente")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar()
        elif opcion == "2":
            buscar()
        elif opcion == "3":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("ERROR: seleccione 1, 2 o 3.")


principal()
