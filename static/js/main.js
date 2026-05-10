const PRODUCTS = [
  { id: 1, name: 'Pink Velvet Brownie', description: 'Soft strawberry brownie with frosting, pearls, and glitter dust.', price: 8.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 2, name: 'Champagne Fudge Brownie', description: 'Decadent chocolate brownie topped with rose-gold sprinkles.', price: 9.25, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 3, name: 'Caramel Swirl Brownie', description: 'Salted caramel ribbons over lush chocolate brownie.', price: 9.75, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 4, name: 'Berry Bliss Brownie', description: 'Bright berry filling with cream flowers and pastel sugar.', price: 10.00, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 5, name: 'Mint Chocolate Brownie', description: 'Cool mint frosting on rich chocolate brownie with chocolate chips.', price: 9.00, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 6, name: 'Peanut Butter Brownie', description: 'Creamy peanut butter swirls in fudgy chocolate brownie.', price: 9.50, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 7, name: 'White Chocolate Brownie', description: 'Vanilla-infused brownie with white chocolate chunks and macadamia nuts.', price: 10.25, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 8, name: 'Salted Caramel Brownie', description: 'Sea salt caramel sauce drizzled over decadent chocolate brownie.', price: 9.75, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 9, name: 'Raspberry Dream Brownie', description: 'Tangy raspberry ribbons in a velvet chocolate base.', price: 10.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 10, name: 'Hazelnut Truffle Brownie', description: 'Crunchy hazelnut pieces with silky chocolate ganache.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 11, name: 'Mocha Crunch Brownie', description: 'Coffee-infused brownie layered with chocolate crunch.', price: 10.25, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 12, name: 'Coconut Cloud Brownie', description: 'Coconut flakes and white chocolate make every bite dreamy.', price: 9.95, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 13, name: 'Raspberry Cheesecake Brownie', description: 'Creamy cheesecake swirls with fresh raspberry topping.', price: 11.25, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 14, name: 'Cookie Dough Brownie', description: 'Brownie base topped with cookie dough chunks and chocolate chips.', price: 10.50, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 15, name: 'Espresso Delight Brownie', description: 'Bold espresso, chocolate, and a caramel drizzle.', price: 10.75, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 16, name: 'Coconut Almond Brownie', description: 'Toasted almonds and coconut layered on a fudgy base.', price: 10.50, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 17, name: 'Caramel Pecan Brownie', description: 'Sticky caramel, pecans, and brownie goodness.', price: 10.95, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 18, name: 'Strawberry Shortcake Brownie', description: 'Strawberry pieces with creamy frosting and crumbs.', price: 11.25, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 19, name: 'Lemon Zest Brownie', description: 'Bright lemon flavor with a soft, buttery fudge bite.', price: 9.95, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 20, name: 'Cinnamon Spice Brownie', description: 'Warm cinnamon swirls with a gooey chocolate center.', price: 10.00, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 21, name: 'Almond Joy Brownie', description: 'Almonds and coconut in a rich chocolate square.', price: 10.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 22, name: "S'mores Brownie", description: 'Toasted marshmallow with graham cracker crunch.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 23, name: 'Birthday Sprinkle Brownie', description: 'Festive sprinkles over a chocolate party brownie.', price: 9.75, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 24, name: 'Matcha Green Brownie', description: 'Subtle matcha flavor blended with white chocolate.', price: 10.75, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 25, name: 'Dark Ganache Brownie', description: 'Ultra-rich dark chocolate with silky ganache topping.', price: 11.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 26, name: 'Honey Lavender Brownie', description: 'Floral lavender and sweet honey in every bite.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 27, name: 'Rocky Road Brownie', description: 'Marshmallows, nuts, and rich chocolate rocks of joy.', price: 11.25, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 28, name: 'Oreo Crunch Brownie', description: 'Crushed cookies in a fudgy brownie base.', price: 10.75, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 29, name: 'Chocolate Orange Brownie', description: 'Zesty orange paired with deep cocoa flavor.', price: 10.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 30, name: 'Sea Salt Caramel Brownie', description: 'Sweet caramel balanced with a punch of sea salt.', price: 10.95, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 31, name: 'Espresso Walnut Brownie', description: 'Crunchy walnuts and coffee flavors in every bite.', price: 11.00, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 32, name: 'Cherry Blossom Brownie', description: 'Light cherry notes with delicate floral accents.', price: 11.25, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 33, name: 'Pistachio Crunch Brownie', description: 'Toasted pistachios add a crunchy, nutty finish.', price: 11.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 34, name: 'White Raspberry Brownie', description: 'Tart raspberry and creamy white chocolate in harmony.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 35, name: 'Brownie Cheesecake Bar', description: 'Brownie and cheesecake layered into one heavenly bar.', price: 11.75, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 36, name: 'Maple Pecan Brownie', description: 'Warm maple sweetness with crunchy pecans.', price: 11.25, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 37, name: 'Triple Chocolate Brownie', description: 'Milk, dark, and white chocolate layers for chocoholics.', price: 11.50, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 38, name: 'Gingerbread Brownie', description: 'Cozy ginger, cinnamon, and molasses for a seasonal treat.', price: 10.50, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 39, name: 'Nutella Swirl Brownie', description: 'Creamy hazelnut spread swirled into rich brownie batter.', price: 11.00, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 40, name: 'Blueberry Lemon Brownie', description: 'Bright blueberry bursts with zesty lemon glaze.', price: 11.25, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 41, name: 'Peanut Caramel Brownie', description: 'Soft brownie with salted peanut and caramel ribbons.', price: 10.95, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 42, name: 'Vanilla Rose Brownie', description: 'Elegant vanilla and rosewater flavors for a floral bite.', price: 11.50, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 43, name: 'Mocha Almond Brownie', description: 'Coffee and almond crunch meet fudgy chocolate.', price: 11.00, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 44, name: 'Toffee Crunch Brownie', description: 'Crunchy toffee pieces on a soft brownie base.', price: 11.25, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 45, name: 'Walnut Caramel Brownie', description: 'Warm caramel and walnuts over a dark fudge cake.', price: 11.25, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 46, name: 'Berry Vanilla Brownie', description: 'Mixed berries and vanilla cream swirl through brownie layers.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' },
  { id: 47, name: 'Dark Cherry Brownie', description: 'Juicy cherries with a bold dark chocolate base.', price: 11.50, image: '/static/images/pink-brownie-photo-3.png' },
  { id: 48, name: 'Hazelnut Mocha Brownie', description: 'Coffee, chocolate, and hazelnut in perfect balance.', price: 11.50, image: '/static/images/pink-brownie-photo-4.png' },
  { id: 49, name: 'Caramel Apple Brownie', description: 'Apple pieces and caramel ribbons for a cozy twist.', price: 11.25, image: '/static/images/pink-brownie-photo-1.png' },
  { id: 50, name: 'Golden Honey Brownie', description: 'Smooth honey glaze on a soft, buttery brownie.', price: 11.00, image: '/static/images/pink-brownie-photo-2.png' }
];

const REAL_PRODUCT_IMAGES = [
  '/static/images/pink-brownie-photo-1.png',
  '/static/images/pink-brownie-photo-2.png',
  '/static/images/pink-brownie-photo-3.png',
  '/static/images/pink-brownie-photo-4.png',
  '/static/images/cake-mango.png',
  '/static/images/cake-chocolate.png',
  '/static/images/cake-red-velvet.png',
  '/static/images/cake-fruit.png',
  '/static/images/cake-black-forest.png'
];

const INR_CONVERSION_RATE = 85;
const FREE_DELIVERY_THRESHOLD = 2000;
const DELIVERY_FEE = 99;
const formatMoney = (amount) => new Intl.NumberFormat('en-IN', {
  style: 'currency',
  currency: 'INR',
  maximumFractionDigits: 0
}).format(amount);

PRODUCTS.forEach((product, index) => {
  product.image = REAL_PRODUCT_IMAGES[index % REAL_PRODUCT_IMAGES.length];
  product.price = Math.round((product.price * INR_CONVERSION_RATE) / 10) * 10;
});

function getCart() {
  const cart = JSON.parse(localStorage.getItem('brownieCart') || '[]');
  let changed = false;
  const updatedCart = cart.map((item) => {
    const product = PRODUCTS.find((entry) => entry.id === item.id);
    if (product && item.price !== product.price) {
      changed = true;
      return { ...item, price: product.price, image: product.image };
    }
    return item;
  });
  if (changed) localStorage.setItem('brownieCart', JSON.stringify(updatedCart));
  return updatedCart;
}

function setCart(cart) {
  localStorage.setItem('brownieCart', JSON.stringify(cart));
  renderCartCount();
}

function addToCart(productId) {
  const product = PRODUCTS.find((item) => item.id === productId);
  if (!product) return;
  const cart = getCart();
  const existing = cart.find((item) => item.id === productId);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }
  setCart(cart);
  toast(`${product.name} added to cart!`);
}

function removeFromCart(productId) {
  const cart = getCart().filter((item) => item.id !== productId);
  setCart(cart);
  renderCart();
}

function renderCartCount() {
  const count = getCart().reduce((sum, item) => sum + item.quantity, 0);
  const countNode = document.getElementById('cart-count');
  if (countNode) countNode.textContent = count;
}

function renderCart() {
  const cartItems = document.getElementById('cart-items');
  const cartTotal = document.getElementById('cart-total');
  const cartSubtotal = document.getElementById('cart-subtotal');
  const cart = getCart();
  if (!cartItems || !cartTotal) return;
  cartItems.innerHTML = '';
  if (!cart.length) {
    cartItems.innerHTML = '<p class="empty-cart">Your cart is empty. Add a few brownies to begin.</p>';
  } else {
    cart.forEach((item) => {
      const row = document.createElement('div');
      row.className = 'order-item';
      row.innerHTML = `
        <div class="item-details">
          <strong>${item.name}</strong>
          <span>${item.quantity} x ${formatMoney(item.price)}</span>
        </div>
        <button class="remove-btn" onclick="removeFromCart(${item.id})" aria-label="Remove ${item.name}">x</button>
      `;
      cartItems.appendChild(row);
    });
  }
  const subtotal = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
  const deliveryFee = subtotal >= FREE_DELIVERY_THRESHOLD ? 0 : DELIVERY_FEE;
  const total = subtotal + deliveryFee;
  if (cartSubtotal) cartSubtotal.textContent = formatMoney(subtotal);
  cartTotal.textContent = formatMoney(total);
  const cartData = document.getElementById('cart-data');
  if (cartData) cartData.value = JSON.stringify(cart);

  const deliveryLine = document.getElementById('delivery-fee');
  if (deliveryLine) {
    deliveryLine.textContent = deliveryFee === 0 ? 'Free' : formatMoney(deliveryFee);
  }
}

function submitCheckoutForm(event) {
  event.preventDefault();
  const cart = getCart();
  if (!cart.length) {
    toast('Cart is empty. Add at least one brownie.');
    return;
  }
  const form = event.target;
  const formData = new FormData(form);
  const payload = {
    customerName: formData.get('customerName'),
    email: formData.get('email'),
    phone: formData.get('phone'),
    address: formData.get('address'),
    city: formData.get('city'),
    postalCode: formData.get('postalCode'),
    deliveryInstructions: formData.get('deliveryInstructions'),
    paymentMethod: formData.get('paymentMethod'),
    cardNumber: formData.get('cardNumber'),
    expiry: formData.get('expiry'),
    cvc: formData.get('cvc'),
    cart: JSON.stringify(cart)
  };

  fetch('/create-order', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.success) {
        localStorage.removeItem('brownieCart');
        window.location.href = `/order-success/${data.orderId}`;
      } else {
        toast(data.message || 'Unable to place order.');
      }
    })
    .catch(() => {
      toast('Could not connect to server.');
    });
}

function toast(message) {
  let toastBox = document.getElementById('toast-box');
  if (!toastBox) {
    toastBox = document.createElement('div');
    toastBox.id = 'toast-box';
    toastBox.style.position = 'fixed';
    toastBox.style.bottom = '22px';
    toastBox.style.right = '22px';
    toastBox.style.zIndex = '9999';
    document.body.appendChild(toastBox);
  }
  const toastItem = document.createElement('div');
  toastItem.textContent = message;
  toastItem.style.background = 'rgba(58, 23, 17, 0.96)';
  toastItem.style.color = '#fff';
  toastItem.style.padding = '14px 18px';
  toastItem.style.borderRadius = '8px';
  toastItem.style.marginTop = '10px';
  toastItem.style.boxShadow = '0 20px 40px rgba(58, 23, 17, 0.24)';
  toastItem.style.opacity = '0';
  toastItem.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
  toastBox.appendChild(toastItem);
  requestAnimationFrame(() => {
    toastItem.style.opacity = '1';
    toastItem.style.transform = 'translateY(-4px)';
  });
  setTimeout(() => {
    toastItem.style.opacity = '0';
    toastItem.style.transform = 'translateY(0)';
    setTimeout(() => toastItem.remove(), 300);
  }, 2600);
}

function initPage() {
  renderCartCount();
  renderCart();
  const checkoutForm = document.getElementById('checkout-form');
  if (checkoutForm) {
    checkoutForm.addEventListener('submit', submitCheckoutForm);
    // Payment method toggle
    const paymentMethod = checkoutForm.querySelector('[name="paymentMethod"]');
    if (paymentMethod) {
      paymentMethod.addEventListener('change', toggleCardFields);
      toggleCardFields(); // Initial state
    }
  }
  const sendOtpBtn = document.getElementById('sendOtpBtn');
  if (sendOtpBtn) {
    sendOtpBtn.addEventListener('click', sendOtp);
  }
  const signupBtn = document.getElementById('signupBtn');
  if (signupBtn) {
    signupBtn.addEventListener('click', signup);
  }
  const sliderPrev = document.getElementById('sliderPrev');
  const sliderNext = document.getElementById('sliderNext');
  if (sliderPrev) {
    sliderPrev.addEventListener('click', () => scrollMenuSlider(-1));
  }
  if (sliderNext) {
    sliderNext.addEventListener('click', () => scrollMenuSlider(1));
  }
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const navLinks = document.getElementById('nav-links');
  if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
  }
  initHeroImageSlider();
}

function initHeroImageSlider() {
  const track = document.getElementById('heroImageTrack');
  if (!track) return;

  const slides = Array.from(track.querySelectorAll('.hero-image-slide'));
  if (!slides.length) return;

  let current = 0;
  let timer = null;

  function goToHeroImage(index) {
    current = (index + slides.length) % slides.length;
    track.style.transform = `translateX(-${current * 100}%)`;
    slides.forEach((slide, slideIndex) => {
      slide.classList.toggle('is-active', slideIndex === current);
    });
  }

  goToHeroImage(0);
  timer = setInterval(() => goToHeroImage(current + 1), 3200);
}

function toggleCardFields() {
  const paymentMethod = document.querySelector('[name="paymentMethod"]').value;
  const cardFields = document.getElementById('card-fields');
  if (cardFields) {
    cardFields.style.display = paymentMethod === 'Card' ? 'block' : 'none';
    const inputs = cardFields.querySelectorAll('input');
    inputs.forEach(input => {
      input.required = paymentMethod === 'Card';
    });
  }
}

function scrollMenuSlider(direction) {
  const slider = document.getElementById('productSlider');
  if (!slider) return;
  const cardWidth = slider.querySelector('.slider-card')?.offsetWidth || 280;
  slider.scrollBy({ left: direction * (cardWidth + 22), behavior: 'smooth' });
}

function sendOtp() {
  const email = document.getElementById('login-email').value;
  if (!email) {
    toast('Please enter your email.');
    return;
  }
  fetch('/send-otp', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  })
    .then(res => res.json())
    .then(data => {
      toast(data.message);
    })
    .catch(() => {
      toast('Could not send OTP.');
    });
}

function showTab(tabName) {
  document.querySelectorAll('.auth-tab').forEach(tab => tab.classList.remove('active'));
  document.querySelectorAll('.auth-tab-content').forEach(content => content.classList.remove('active'));
  document.querySelector(`[onclick="showTab('${tabName}')"]`).classList.add('active');
  document.getElementById(`${tabName}-tab`).classList.add('active');
}

function signup() {
  const name = document.getElementById('signup-name').value;
  const email = document.getElementById('signup-email').value;
  const phone = document.getElementById('signup-phone').value;
  const address = document.getElementById('signup-address').value;
  const city = document.getElementById('signup-city').value;
  const state = document.getElementById('signup-state').value;
  const postal_code = document.getElementById('signup-postal').value;
  
  if (!name || !email || !phone || !address || !city || !state || !postal_code) {
    showSignupMessage('Please fill all fields.', 'error');
    return;
  }
  fetch('/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams({ name, email, phone, address, city, state, postal_code })
  })
    .then(res => res.json())
    .then(data => {
      showSignupMessage(data.message, data.success ? 'success' : 'error');
      if (data.success) {
        document.getElementById('login-email').value = email;
        setTimeout(() => showTab('login'), 2000);
      }
    })
    .catch(() => {
      showSignupMessage('Could not create account.', 'error');
    });
}

function showSignupMessage(message, type) {
  const msgDiv = document.getElementById('signup-message');
  msgDiv.innerHTML = `<div class="form-message ${type}">${message}</div>`;
}

window.addEventListener('DOMContentLoaded', initPage);
