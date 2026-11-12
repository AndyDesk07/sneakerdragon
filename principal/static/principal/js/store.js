(function () {
    const countElements = document.querySelectorAll('[data-cart-count]');
    const addButtons = document.querySelectorAll('[data-add-cart]');
    const openButton = document.querySelector('[data-cart-open]');
    const cartOverlay = document.querySelector('[data-cart-overlay]');
    const cartItems = document.querySelector('[data-cart-items]');
    const emptyMessage = document.querySelector('[data-cart-empty]');
    const totalElement = document.querySelector('[data-cart-total]');
    const clearButton = document.querySelector('[data-cart-clear]');
    const checkoutButton = document.querySelector('[data-cart-checkout]');
    const cartNote = document.querySelector('[data-cart-note]');
    const toast = document.querySelector('[data-toast]');
    const newsletter = document.querySelector('[data-newsletter]');
    const storageKey = 'sneakerdragon_cart_items';
    const countStorageKey = 'sneakerdragon_cart';
    const currencyFormatter = new Intl.NumberFormat('es-CL');
    let cart = loadCart();
    let lastFocusedElement = null;

    function loadCart() {
        const savedCart = localStorage.getItem(storageKey);
        if (!savedCart) return [];

        try {
            const parsedCart = JSON.parse(savedCart);
            if (!Array.isArray(parsedCart)) {
                throw new TypeError('El formato guardado del carrito no es válido.');
            }
            return parsedCart.filter((item) =>
                item &&
                typeof item.id === 'string' &&
                typeof item.name === 'string' &&
                typeof item.image === 'string' &&
                Number.isFinite(item.price) &&
                Number.isInteger(item.quantity) &&
                item.quantity > 0 &&
                Number.isInteger(item.stock) &&
                item.stock >= item.quantity
            );
        } catch (error) {
            console.error('No se pudo cargar el carrito guardado:', error);
            return [];
        }
    }

    function saveCart() {
        localStorage.setItem(storageKey, JSON.stringify(cart));
        localStorage.setItem(countStorageKey, String(getItemCount()));
    }

    function getItemCount() {
        return cart.reduce((total, item) => total + item.quantity, 0);
    }

    function formatPrice(price) {
        return `$${currencyFormatter.format(price)}`;
    }

    function showToast(message) {
        if (!toast) return;
        toast.textContent = message;
        toast.classList.add('show');
        window.clearTimeout(window.sneakerToastTimer);
        window.sneakerToastTimer = window.setTimeout(() => {
            toast.classList.remove('show');
        }, 2200);
    }

    function createCartItem(item) {
        const row = document.createElement('article');
        row.className = 'cart-item';

        const image = document.createElement('img');
        image.className = 'cart-item__image';
        image.src = item.image;
        image.alt = item.name;

        const info = document.createElement('div');
        info.className = 'cart-item__info';

        const name = document.createElement('h3');
        name.textContent = item.name;
        const price = document.createElement('p');
        price.className = 'cart-item__price';
        price.textContent = formatPrice(item.price);

        const controls = document.createElement('div');
        controls.className = 'cart-item__controls';

        const decrease = document.createElement('button');
        decrease.type = 'button';
        decrease.textContent = '−';
        decrease.setAttribute('aria-label', `Quitar una unidad de ${item.name}`);
        decrease.dataset.cartAction = 'decrease';
        decrease.dataset.productId = item.id;

        const quantity = document.createElement('span');
        quantity.textContent = item.quantity;
        quantity.setAttribute('aria-label', `Cantidad: ${item.quantity}`);

        const increase = document.createElement('button');
        increase.type = 'button';
        increase.textContent = '+';
        increase.setAttribute('aria-label', `Agregar una unidad de ${item.name}`);
        increase.dataset.cartAction = 'increase';
        increase.dataset.productId = item.id;
        increase.disabled = item.quantity >= item.stock;

        const remove = document.createElement('button');
        remove.type = 'button';
        remove.className = 'cart-item__remove';
        remove.textContent = 'Quitar';
        remove.dataset.cartAction = 'remove';
        remove.dataset.productId = item.id;

        controls.append(decrease, quantity, increase);
        info.append(name, price, controls);
        row.append(image, info, remove);
        return row;
    }

    function renderCart() {
        if (!cartItems) return;

        const isEmpty = cart.length === 0;
        const count = getItemCount();
        countElements.forEach((element) => {
            element.textContent = count;
        });
        cartItems.replaceChildren(...cart.map(createCartItem));
        emptyMessage.hidden = !isEmpty;
        clearButton.hidden = isEmpty;
        checkoutButton.hidden = isEmpty;
        if (cartNote) cartNote.hidden = isEmpty;
        totalElement.parentElement.hidden = isEmpty;
        totalElement.textContent = formatPrice(
            cart.reduce((total, item) => total + item.price * item.quantity, 0)
        );
    }

    function addProduct(button) {
        const id = button.dataset.productId;
        const name = button.dataset.productName;
        const price = Number(button.dataset.productPrice);
        const image = button.dataset.productImage;
        const stock = Number(button.dataset.productStock);

        if (!id || !name || !image || !Number.isInteger(price) || !Number.isInteger(stock)) {
            showToast('No se pudo agregar este producto al carrito');
            return;
        }
        if (stock < 1) {
            showToast('Este producto no tiene stock disponible');
            return;
        }

        const item = cart.find((cartItem) => cartItem.id === id);
        if (item) {
            if (item.quantity >= stock) {
                showToast('Alcanzaste el stock disponible de este producto');
                return;
            }
            item.quantity += 1;
            item.stock = stock;
        } else {
            cart.push({ id, name, price, image, stock, quantity: 1 });
        }

        saveCart();
        renderCart();
        showToast('Producto añadido al carrito');
    }

    function openCart() {
        if (!cartOverlay) return;
        lastFocusedElement = document.activeElement;
        cartOverlay.hidden = false;
        document.body.classList.add('cart-open');
        openButton.setAttribute('aria-expanded', 'true');
        cartOverlay.querySelector('[data-cart-close]:not(.cart-backdrop)').focus();
    }

    function closeCart() {
        if (!cartOverlay || cartOverlay.hidden) return;
        cartOverlay.hidden = true;
        document.body.classList.remove('cart-open');
        openButton.setAttribute('aria-expanded', 'false');
        if (lastFocusedElement) lastFocusedElement.focus();
    }

    addButtons.forEach((button) => {
        button.addEventListener('click', () => addProduct(button));
    });

    if (openButton) openButton.addEventListener('click', openCart);

    if (cartOverlay) {
        cartOverlay.querySelectorAll('[data-cart-close]').forEach((button) => {
            button.addEventListener('click', closeCart);
        });

        cartOverlay.addEventListener('click', (event) => {
            const actionButton = event.target.closest('[data-cart-action]');
            if (!actionButton) return;

            const item = cart.find((cartItem) => cartItem.id === actionButton.dataset.productId);
            if (!item) return;

            if (actionButton.dataset.cartAction === 'increase') {
                if (item.quantity >= item.stock) {
                    showToast('Alcanzaste el stock disponible de este producto');
                    return;
                }
                item.quantity += 1;
            } else if (actionButton.dataset.cartAction === 'decrease') {
                item.quantity -= 1;
                if (item.quantity === 0) {
                    cart = cart.filter((cartItem) => cartItem.id !== item.id);
                }
            } else if (actionButton.dataset.cartAction === 'remove') {
                cart = cart.filter((cartItem) => cartItem.id !== item.id);
            }

            saveCart();
            renderCart();
        });

        cartOverlay.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') closeCart();
        });
    }

    if (clearButton) {
        clearButton.addEventListener('click', () => {
            cart = [];
            saveCart();
            renderCart();
        });
    }

    if (checkoutButton) {
        checkoutButton.addEventListener('click', () => {
            showToast('La compra estará disponible próximamente');
        });
    }

    if (newsletter) {
        newsletter.addEventListener('submit', (event) => {
            event.preventDefault();
            newsletter.reset();
            showToast('¡Gracias por unirte a SneakerDRAGON!');
        });
    }

    renderCart();
})();
