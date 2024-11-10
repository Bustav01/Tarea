class BaseFormulario:
    def __init__(self, campos:dict[str, int|str]):
        self.campos = campos
    def get_datos(self):
        return self.campos
    def set_datos(self, datos:dict[str, str]):
        self.campos = {campo: datos[campo] if campo in datos else valor
                       for campo, valor in self.campos.items()}
class FormularioNotas(BaseFormulario):
    def __init__(self):
        super().__init__({
            'nota1':'',
            'nota2': '',
            'nota3': '',
            'asistencia': ''
        })

class FormularioNombres(BaseFormulario):
    def __init__(self):
        super().__init__({
            'nombre1':'',
            'nombre2': '',
            'nombre3': ''
        })