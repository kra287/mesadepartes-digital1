# ---------- VALIDACION ----------
def datos_validos(dni, nombres, tipo_documento, asunto,
                  cantidad_folios):

    if len(dni) != 8 or not dni.isdigit():
        return False

    if nombres == "" or not nombres.replace(" ", "").isalpha():
        return False

    if tipo_documento == "":
        return False

    if asunto == "" or asunto.isdigit():
        return False

    if cantidad_folios <= 0:
        return False

    return True
