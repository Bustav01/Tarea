from flask import Blueprint, render_template,request
from app.models import *
from app.methods import *

app_routes = Blueprint('app_routes', __name__)

# RUTAS:
@app_routes.route('/')
def home():
    return render_template('home.html')

@app_routes.route('/ejercicio1',methods=['GET','POST'])
def procesar_notas():
    resultado = None
    formulario = FormularioNotas()
    errores:list[str] = []

    if request.method == 'POST':
        formulario.set_datos(request.form.to_dict())
        datos = formulario.get_datos()

        #Validación campos vacíos y rangos
        campos_vacios = validar_campo_vacio(datos)
        if campos_vacios:
            errores.append(f"Campos vacíos: {', '.join(campos_vacios)}")
        campos_rango = validar_rango({k:datos[k] for k in ['nota1','nota2','nota3']}, 10, 70)
        campos_rango += validar_rango({'asistencia': datos['asistencia']}, 0, 100)
        if campos_rango:
            errores.append(f"Rango inválido: {', '.join(campos_rango)}")

        #Procesar resultado
        if not errores:
            promedio = round((int(datos['nota1']) + int(datos['nota2']) + int(datos['nota3'])) / 3, 1)
            resultado = (promedio, "APROBADO" if promedio >= 40 else "REPROBADO")

    return render_template('ejercicio1.html',
                           resultado=resultado,
                           datos_formulario=formulario.get_datos(),
                           errores="; ".join(errores) if errores else None)

@app_routes.route('/ejercicio2',methods=['GET','POST'])
def ejercicio2():
    resultado = None
    formulario = FormularioNombres()
    errores: list[str] = []

    if request.method == 'POST':
        formulario.set_datos(request.form.to_dict())
        datos = formulario.get_datos()

        #Validación de campos vacíos
        campos_vacios = validar_campo_vacio(datos)
        if campos_vacios:
            errores.append(f"Campos vacíos: {', '.join(campos_vacios)}")
        #Validación de nombres diferentes
        if not campos_vacios:
            #Encontrar máximo de caracteres en nombres
            max_caracteres = max(len(valor) for valor in datos.values())
            #Encontrar nombres que coincidan con valor máximo
            nombres = obtener_valores(datos, max_caracteres)

            if len(nombres) > 1:
                resultado = (f"Los nombres con mayor cantidad de carácteres son: {', '.join(nombres)}",
                    f"Los nombres tienen: {max_caracteres} carácteres")
            else:
                resultado = (f"El nombre con mayor cantidad de carácteres es: {nombres[0]}",
                             f"El nombre tiene: {max_caracteres} caracteres")

    return render_template('ejercicio2.html',
                           resultado=resultado,
                           datos_formulario=formulario.get_datos(),
                           errores="; ".join(errores) if errores else None)
