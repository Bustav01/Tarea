def validar_campo_vacio(campos: dict[str, str]) -> list[str]:
    '''Valida que los campos no estén vacíos. Retorna lista de claves con campos vacíos
    Parámetros: campos: diccionario con campos y sus valores (string)'''
    return [campo for campo, valor in campos.items() if not valor.strip()]

def validar_rango(campos: dict[str, str], min: int, max: int) -> list[str]:
    '''Valida que los campos estén en el rango correcto. Retorna lista de claves con campos erróneos
    Parámetros: campos: diccionario con campos y sus valores (string -> int).
                min: valor mínimo permitido.
                max: valor máximo permitido.'''
    return [campo for campo, valor in campos.items()
            if valor.strip () and not (min <= int(valor) <= max)]

def obtener_valores(diccionario:dict[str,str], valor) -> list[str]:
    '''Retorna valores del diccionario que sean idénticos al entregado en parámetros.
    Parámetros: diccionario: diccionario con campos y sus valores (string)
                valor: valor a comparar.'''
    resultado = [v for v in diccionario.values() if len(v) == valor]
    return resultado
