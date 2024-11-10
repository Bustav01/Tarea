document.addEventListener('DOMContentLoaded', () =>
{
    const msgError = document.getElementById('msgError')

    const formNota = document.getElementById('formNota');
    const formNombres = document.getElementById('formNombres');

    if (formNota)
    {
        formNota.addEventListener('input', () => validarCamposNotas(formNota));
        formNota.addEventListener('submit', (event) =>
        {
            if (!validarCamposNotas(formNota))
            {
                event.preventDefault();
            }
        });
    }

    if (formNombres)
    {
        formNombres.addEventListener('input', () => validarCamposNombres(formNombres));
        formNombres.addEventListener('submit', (event) =>
        {
            if (!validarCamposNombres(formNombres))
            {
                event.preventDefault();
            }
        });
    }

    function validarCamposNotas(form)
    {
        const  inputsNotas = form.querySelectorAll('input[name^="nota"]');
        const inputAsistencia = form.querySelector('#asistencia');
        let errores = [];

        inputsNotas.forEach(input =>
        {
            const valor = parseInt(input.value, 10);
            if (isNaN(valor) || valor < 10 || valor > 70)
            {
                errores.push(`${input.name} debe estar entre 10 y 70`)
            }
        });

        const asistenciaValor = parseInt(inputAsistencia.value, 10);
        if (isNaN(asistenciaValor) || asistenciaValor < 0 || asistenciaValor > 100)
        {
            errores.push('Asistencia debe estar entre 0 y 100')
        }

        return mostrarErrores(errores);
    }

    function  validarCamposNombres(form)
    {
        const inputsNombres = form.querySelectorAll('input[name^="nombre"]');
        let errores = []

        inputsNombres.forEach(input =>
        {
            if (input.value.trim() === '')
            {
                errores.pusj(`${input.name} no puede estar vacío`);
            }
        });

        return mostrarErrores(errores);
    }

    function  mostrarErrores(errores)
    {
        if (errores.length > 0)
        {
            msgError.innerText = errores.join('; ');
            msgError.style.display = 'block';
            return false;
        } else
        {
            msgError.innerText = '';
            msgError.style.display = 'none';
            return true;
        }
    }

})