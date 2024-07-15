document.addEventListener('DOMContentLoaded', function() {
    let cart = [];
    let dolar = 0;

    // Fetch the dollar value from the JSON file
    fetch('/static/js/dolar.json')
        .then(response => response.json())
        .then(data => {
            dolar = data.dolar;
            console.log("Valor del dólar cargado: ", dolar);
            // Actualizar los precios a dólares una vez que se obtiene el valor del dólar
            updatePrices('USD');
        })
        .catch(error => console.error('Error fetching dollar value:', error));

    const cartIcon = document.getElementById('cart-icon');
    const cartContainer = document.getElementById('cart-container');
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    const payButton = document.getElementById('pay-button');

    cartIcon.addEventListener('click', function() {
        cartContainer.style.display = cartContainer.style.display === 'none' ? 'flex' : 'none';
    });

    function updateCart() {
        cartItems.innerHTML = '';
        let total = 0;
        cart.forEach(item => {
            const cartItem = `
                <div class="cart-item">
                    <span>${item.descripcionTipoProducto}</span>
                    <span>$${item.precio} x ${item.cantidad}</span>
                    <button class="remove-from-cart" data-id="${item.idProducto}">🗑️</button>
                </div>
            `;
            cartItems.insertAdjacentHTML('beforeend', cartItem);
            total += item.precio * item.cantidad;
        });
        cartTotal.innerHTML = `Total: $${total}`;

        document.querySelectorAll('.remove-from-cart').forEach(button => {
            button.addEventListener('click', function() {
                const id = this.getAttribute('data-id');
                cart = cart.filter(item => item.idProducto !== id);
                updateCart();
            });
        });
    }

    fetch('productos/')
        .then(response => response.json())
        .then(productos => {
            const productosContainer = document.getElementById('productos');
            productos.forEach(producto => {
                const productoCard = `
                    <div class="col-md-4 product" data-price-pesos="${producto.precio}">
                        <div class="card mb-4 shadow-sm">
                            <div class="card-body">
                                <h5 class="card-title">${producto.descripcionTipoProducto}</h5>
                                <p class="card-text">Precio: <span class="price">${producto.precio}</span> CLP</p>
                                <input type="number" class="form-control quantity" min="1" value="1">
                                <button class="btn btn-primary add-to-cart" data-id="${producto.idProducto}" data-name="${producto.descripcionTipoProducto}" data-price="${producto.precio}">Agregar</button>
                            </div>
                        </div>
                    </div>
                `;
                productosContainer.insertAdjacentHTML('beforeend', productoCard);
            });

            document.querySelectorAll('.add-to-cart').forEach(button => {
                button.addEventListener('click', function() {
                    const id = this.getAttribute('data-id');
                    const name = this.getAttribute('data-name');
                    const price = parseFloat(this.getAttribute('data-price'));
                    const quantity = parseInt(this.previousElementSibling.value);

                    const existingItem = cart.find(item => item.idProducto === id);

                    if (existingItem) {
                        existingItem.cantidad += quantity;
                    } else {
                        const producto = { idProducto: id, descripcionTipoProducto: name, precio: price, cantidad: quantity };
                        cart.push(producto);
                    }

                    updateCart();
                });
            });
        })
        .catch(error => console.error('Error fetching productos:', error));

    payButton.addEventListener('click', function() {
        const totalAmount = cart.reduce((sum, item) => sum + item.precio * item.cantidad, 0);
        const orderID = 'ORD' + Math.floor(Math.random() * 1000000);
        const sessionID = 'SES' + Math.floor(Math.random() * 1000000);

        localStorage.setItem('orderID', orderID);
        localStorage.setItem('sessionID', sessionID);
        localStorage.setItem('totalAmount', totalAmount);

        // Redirigir a payment_form después de guardar la información necesaria
        window.location.href = '/payment_form';
    });

    // Function to update prices in either Pesos or Dollars
    function updatePrices(currency) {
        const products = document.querySelectorAll('.product');
        products.forEach(product => {
            const priceElement = product.querySelector('.price');
            const priceInPesos = parseFloat(product.getAttribute('data-price-pesos'));
            if (currency === 'USD') {
                const priceInDollars = priceInPesos / dolar;
                priceElement.textContent = priceInDollars.toFixed(2) + ' USD';
            } else {
                priceElement.textContent = priceInPesos + ' CLP';
            }
        });
    }

    // Event listeners for currency change buttons
    document.getElementById('to-pesos').addEventListener('click', () => updatePrices('CLP'));
    document.getElementById('to-dollars').addEventListener('click', () => {
        if (dolar > 0) {
            updatePrices('USD');
        } else {
            console.error('El valor del dólar no se ha cargado todavía.');
        }
    });
});
