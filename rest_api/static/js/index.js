document.addEventListener('DOMContentLoaded', function() {
    let cart = [];
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
                    <div class="col-md-4">
                        <div class="card mb-4 shadow-sm">
                            
                            <div class="card-body">
                                <h5 class="card-title">${producto.descripcionTipoProducto}</h5>
                                <p class="card-text">$${producto.precio}</p>
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

        window.location.href = 'payment_form';
    });
});