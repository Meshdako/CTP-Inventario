// Agregar Nuevo Articulo
function agregarArticulo() {
    var container = document.getElementById("articulos-container");
    var nuevoArticulo = document.createElement("div");

    nuevoArticulo.innerHTML = `
        <br>
        <hr>
        <br>
        <div class="from-group">
                <div class="from-group">
                    <label for="categoria_id">Selecciona la Categoría</label>
                    <select class="form-control" name="categoria_id">
                        <option value="1">Mobiliario</option>
                        <option value="2">Aseo</option>
                        <option value="3">Química</option>
                    </select>
                </div>
            </div>

            <br>
            <div class="row">
                <div class="col-md-8">
                    <div class="form-group">
                        <label for="nombre_articulo">Nombre del Articulos</label>
                        <input type="text" class="form-control" name="nombre_articulo"
                            placeholder="Ingresa el articulo">
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="form-group">
                        <label for="cantidad">Cantidad</label>
                        <input type="number" class="form-control" name="cantidad" placeholder="Ingresa la cantidad">
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="precio_unit">Precio Unitario</label>
                        <input type="number" class="form-control" name="precio_unitario"
                            placeholder="Ingresa el precio">
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="total">Total</label>
                        <input type="number" class="form-control" name="total" placeholder="Ingresa el total">
                    </div>
                </div>
            </div>
        `;

    container.appendChild(nuevoArticulo);
}