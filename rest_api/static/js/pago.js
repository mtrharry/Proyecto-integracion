document.addEventListener('DOMContentLoaded', function() {
    const orderID = localStorage.getItem('orderID');
    const sessionID = localStorage.getItem('sessionID');
    const totalAmount = localStorage.getItem('totalAmount');

    document.getElementById('order-id').innerText = orderID;
    document.getElementById('session-id').innerText = sessionID;
    document.getElementById('total-amount').innerText = totalAmount;

    document.getElementById('buy_order').value = orderID;
    document.getElementById('session_id').value = sessionID;
    document.getElementById('amount').value = totalAmount;
});