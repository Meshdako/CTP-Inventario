// Separar números en miles
function formatInput(input) {
    // Obtener el valor ingresado
    let value = input.value;

    // Eliminar cualquier separador de miles existente
    value = value.replace(/\./g, '');

    // Convertir a número y formatear con separadores de miles
    let formattedValue = addThousandsSeparator(value);

    // Actualizar el valor en la casilla de entrada
    input.value = formattedValue;
}

function addThousandsSeparator(number) {
    // Convertir a número
    let parsedNumber = parseFloat(number);

    // Verificar si el número es válido
    if (isNaN(parsedNumber)) {
        return number; // Devolver el valor original si no es un número válido
    }

    // Formatear con separadores de miles y punto decimal
    return parsedNumber.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 });
}

// Agregar Nuevo Articulo
// Variable para realizar un seguimiento del índice de campo
var campoIndex = 0;

function eliminarArticulo(id) {
    var articulo = document.getElementById(id);
    articulo.remove();
}

// Agregar evento al cargar el documento
document.addEventListener("DOMContentLoaded", function () {
    var valorNetoInput = document.getElementById("id_valor_neto");
    var ivaInput = document.getElementById("id_iva");
    var totalInput = document.getElementById("id_total");

    valorNetoInput.addEventListener("input", function () {
        var valorNeto = parseInt(valorNetoInput.value);
        var iva = Math.round(valorNeto * 0.19);  // Calcula el 19% del valor neto
        var total = valorNeto + iva;

        ivaInput.value = iva;
        totalInput.value = total;
    });
});
