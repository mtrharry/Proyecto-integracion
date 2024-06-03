document.addEventListener('DOMContentLoaded', function() {
    const productList = document.getElementById('product-list');
    const editProductForm = document.getElementById('edit-product-form');
    const editProductTitle = document.getElementById('edit-product-title');

    function fetchProductTypes() {
        fetch('/tipoproducto/')
            .then(response => response.json())
            .then(types => {
                const productTypeSelect = document.getElementById('product-type');
                productTypeSelect.innerHTML = '';
                types.forEach(type => {
                    const option = document.createElement('option');
                    option.value = type.idTipoProducto;
                    option.textContent = type.descripcionTipoProducto;
                    productTypeSelect.appendChild(option);
                });

                const editProductTypeSelect = document.getElementById('edit-product-type');
                editProductTypeSelect.innerHTML = '';
                types.forEach(type => {
                    const option = document.createElement('option');
                    option.value = type.idTipoProducto;
                    option.textContent = type.descripcionTipoProducto;
                    editProductTypeSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching product types:', error));
    }

    function fetchProducts() {
        fetch('/productos/')
            .then(response => response.json())
            .then(products => {
                productList.innerHTML = '';
                products.forEach(product => {
                    const productItem = `
                        <div class="card mb-3" data-id="${product.idProducto}">
                            <div class="card-body">
                                <h5 class="card-title">${product.descripcionTipoProducto}</h5>
                                <p class="card-text">Precio: $${product.precio}</p>
                                <p class="card-text">Stock: ${product.cantidadstock ?? 'No especificado'}</p>
                                <button class="btn btn-warning btn-sm edit-product" data-id="${product.idProducto}">Editar</button>
                                <button class="btn btn-danger btn-sm delete-product" data-id="${product.idProducto}" data-type-id="${product.idTipoProducto}">Eliminar</button>
                            </div>
                        </div>
                    `;
                    productList.insertAdjacentHTML('beforeend', productItem);
                });

                document.querySelectorAll('.edit-product').forEach(button => {
                    button.addEventListener('click', function() {
                        const id = this.getAttribute('data-id');
                        editProduct(id);
                    });
                });

                document.querySelectorAll('.delete-product').forEach(button => {
                    button.addEventListener('click', function() {
                        const id = this.getAttribute('data-id');
                        const typeId = this.getAttribute('data-type-id');
                        deleteProduct(id, typeId);
                    });
                });
            })
            .catch(error => console.error('Error fetching products:', error));
    }

    function editProduct(id) {
        fetch(`/productos/${id}/`)
            .then(response => response.json())
            .then(product => {
                document.getElementById('edit-product-id').value = product.idProducto;
                document.getElementById('edit-product-price').value = product.precio;
                document.getElementById('edit-product-type').value = product.idTipoProducto;
                document.getElementById('edit-product-stock').value = product.cantidadstock || '';
                
                editProductTitle.classList.remove('d-none');
                editProductForm.classList.remove('d-none');
            })
            .catch(error => console.error('Error fetching product:', error));
    }

    function updateProduct(event) {
        event.preventDefault();
        const id = document.getElementById('edit-product-id').value;
        const price = document.getElementById('edit-product-price').value;
        const type = document.getElementById('edit-product-type').value;
        const stock = document.getElementById('edit-product-stock').value;

        const productData = {
            precio: price,
            idTipoProducto: type,
            cantidadstock: stock
        };

        fetch(`/put/productos/${id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.idProducto) {
                fetchProducts();
                editProductForm.reset();
                editProductTitle.classList.add('d-none');
                editProductForm.classList.add('d-none');
            } else {
                console.error('Error updating product:', data);
            }
        })
        .catch(error => console.error('Error updating product:', error));
    }

    function addProduct(event) {
        event.preventDefault();
        const price = document.getElementById('product-price').value;
        const type = document.getElementById('product-type').value;
        const stock = document.getElementById('product-stock').value;

        const productData = {
            precio: price,
            idTipoProducto: type
        };

        fetch('/post/productos/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(productData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.idProducto) {
                if (stock) {
                    const stockData = {
                        idProducto: data.idProducto,
                        cantidad: stock
                    };
                    fetch('/post/creastock/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(stockData),
                    })
                    .then(stockResponse => stockResponse.json())
                    .then(stockData => {
                        console.log('Stock created:', stockData);
                        fetchProducts();
                        document.getElementById('add-product-form').reset();
                    })
                    .catch(error => console.error('Error creating stock:', error));
                } else {
                    fetchProducts();
                    document.getElementById('add-product-form').reset();
                }
            } else {
                console.error('Error creating product:', data);
            }
        })
        .catch(error => console.error('Error creating product:', error));
    }

    function addProductType(event) {
        event.preventDefault();
        const name = document.getElementById('type-name').value;
        const description = document.getElementById('type-description').value;

        const typeData = {
            nombreTipoProducto: name,
            descripcionTipoProducto: description
        };

        fetch('/post/creartipo/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(typeData),
        })
        .then(response => response.json())
        .then(data => {
            if (data.idTipoProducto) {
                fetchProductTypes();
                document.getElementById('add-type-form').reset();
            } else {
                console.error('Error creating product type:', data);
            }
        })
        .catch(error => console.error('Error creating product type:', error));
    }

    function deleteProduct(id, typeId) {
        fetch(`/delete/productos/${id}/`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                checkAndDeleteProductType(typeId);
                fetchProducts(); // Actualizar la lista de productos después de la eliminación
            } else {
                response.json().then(data => {
                    console.error('Error deleting product:', data);
                });
            }
        })
        .catch(error => console.error('Error deleting product:', error));
    }

    function checkAndDeleteProductType(tipoProductoId) {
        fetch(`/delete/tipoproducto/${tipoProductoId}/`)
            .then(response => response.json())
            .then(products => {
                if (products.length === 0) {
                    deleteProductType(tipoProductoId);
                }
            })
            .catch(error => console.error('Error checking product type usage:', error));
    }
    
    function deleteProductType(id) {
        fetch(`/delete/tipoproducto/${id}/`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                console.log('Tipo de Producto eliminado');
                fetchProductTypes();
            } else {
                response.json().then(data => {
                    console.error('Error deleting product type:', data);
                });
            }
        })
        .catch(error => console.error('Error deleting product type:', error));
    }

    document.getElementById('add-product-form').addEventListener('submit', addProduct);
    document.getElementById('add-type-form').addEventListener('submit', addProductType);
    document.getElementById('edit-product-form').addEventListener('submit', updateProduct);

    fetchProductTypes();
    fetchProducts();
});
