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

// Función para agregar un nuevo artículo
function agregarArticulo() {
    var container = document.getElementById("articulos-container");
    var nuevoArticulo = document.createElement("div");
    var articuloId = "articulo_" + campoIndex;

    nuevoArticulo.innerHTML = `
        <br>
        <hr>
        <br>
        <div id="articulo_${campoIndex}">
            {% csrf_token %}
            <div class="form-group">
                <label for="{{ articulo_form.categoria_${campoIndex}.id_for_label }}">Selecciona la categoría</label>
                <select class="form-control" id="{{ articulo_form.categoria_${campoIndex}.id_for_label }}" name="{{ articulo_form.categoria_${campoIndex}.html_name }}">
                    <option value="1">Mobiliario</option>
                    <option value="2">Aseo</option>
                    <option value="3">Química</option>
                    <option value="4">Accesorios de Computadora</option>
                </select>
            </div>

            <br>
            <div class="row">
                <div class="col-md-8">
                    <div class="form-group">
                        <label for="{{ articulo_form.nombre_articulo_${campoIndex}.id_for_label }}">Nombre del Articulo</label>
                        <input type="text" class="form-control" id="{{ articulo_form.nombre_articulo_${campoIndex}.id_for_label }}" name="{{ articulo_form.nombre_articulo_${campoIndex}.html_name }}" placeholder="Ingresa el artículo">
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-group">
                        <label for="{{ articulo_form.cantidad_${campoIndex}.id_for_label }}">Cantidad</label>
                        <input type="text" class="form-control" id="{{ articulo_form.cantidad_${campoIndex}.id_for_label }}" name="{{ articulo_form.cantidad_${campoIndex}.html_name }}" oninput="formatInput(this)" placeholder="Ingresa la cantidad">
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="{{ articulo_form.precio_unitario_${campoIndex}.id_for_label }}">Precio Unitario</label>
                        <input type="text" class="form-control" id="{{ articulo_form.precio_unitario_${campoIndex}.id_for_label }}" name="{{ articulo_form.precio_unitario_${campoIndex}.html_name }}" oninput="formatInput(this)" placeholder="Ingresa el precio">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="{{ articulo_form.total_${campoIndex}.id_for_label }}">Total</label>
                        <input type="text" class="form-control" id="{{ articulo_form.total_${campoIndex}.id_for_label }}" name="{{ articulo_form.total_${campoIndex}.html_name }}" oninput="formatInput(this)" placeholder="Ingresa el total">
                    </div>
                </div>
            </div>

            <!-- Botón para eliminar el artículo -->
            <br>
            <button type="button" onclick="eliminarArticulo('${articuloId}')" class="btn btn-danger mt-2">Eliminar Articulo</button>
        </div>
    `;

    container.appendChild(nuevoArticulo);

    // Incrementar el índice de campo para el próximo artículo
    campoIndex++;
}
