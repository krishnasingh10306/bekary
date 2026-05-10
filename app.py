import os
import json
import sqlite3
from datetime import datetime, timedelta, UTC
from flask import Flask, render_template, request, redirect, url_for, session, g, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
from email.mime.text import MIMEText
import random
import string


def utc_now():
    return datetime.now(UTC).replace(tzinfo=None)


app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'krishna-ki-bekary-secret-2026')

DATABASE = os.getenv('DATABASE_PATH', os.path.join(app.root_path, 'bakery.db'))
INR_CONVERSION_RATE = 85
FREE_DELIVERY_THRESHOLD = 2000
DELIVERY_FEE = 99


def format_inr(amount):
    return f"₹{float(amount):,.0f}"


app.jinja_env.filters['inr'] = format_inr


# -------------------------------------------------
# Email OTP
# -------------------------------------------------

def send_otp_email(email, otp):
    sender_email = os.getenv('GMAIL_SENDER_EMAIL')
    sender_password = os.getenv('GMAIL_APP_PASSWORD')

    if not sender_email or not sender_password:
        print("Email credentials missing. Set GMAIL_SENDER_EMAIL and GMAIL_APP_PASSWORD.")
        print(f"DEV OTP for {email}: {otp}")
        return True

    message = MIMEText(
        f"Your OTP for Krishna Ki Bekary login is: {otp}. "
        f"It expires in 10 minutes."
    )
    message['Subject'] = 'Your OTP Code'
    message['From'] = sender_email
    message['To'] = email

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())

        return True

    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def password_matches(stored_password, password):
    if not stored_password:
        return False

    try:
        return check_password_hash(stored_password, password)
    except ValueError:
        return stored_password == password


# -------------------------------------------------
# Products
# -------------------------------------------------

PRODUCTS = [
    {'id': 1, 'name': 'Pink Velvet Brownie', 'description': 'Soft strawberry brownie with frosting, pearls, and glitter dust.', 'price': 8.50, 'image': 'https://images.unsplash.com/photo-1607478900766-efe13248b125?w=640&h=640&fit=crop'},
    {'id': 2, 'name': 'Champagne Fudge Brownie', 'description': 'Decadent chocolate brownie topped with rose-gold sprinkles.', 'price': 9.25, 'image': 'https://images.unsplash.com/photo-1587668178277-295251f900ce?w=640&h=640&fit=crop'},
    {'id': 3, 'name': 'Caramel Swirl Brownie', 'description': 'Salted caramel ribbons over lush chocolate brownie.', 'price': 9.75, 'image': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=640&h=640&fit=crop'},
    {'id': 4, 'name': 'Berry Bliss Brownie', 'description': 'Bright berry filling with cream flowers and pastel sugar.', 'price': 10.00, 'image': 'https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=640&h=640&fit=crop'},
    {'id': 5, 'name': 'Mint Chocolate Brownie', 'description': 'Cool mint frosting on rich chocolate brownie with chocolate chips.', 'price': 9.00, 'image': 'https://images.unsplash.com/photo-1606312619070-d48b4c652a52?w=640&h=640&fit=crop'},
    {'id': 6, 'name': 'Peanut Butter Brownie', 'description': 'Creamy peanut butter swirls in fudgy chocolate brownie.', 'price': 9.50, 'image': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=640&h=640&fit=crop'},
    {'id': 7, 'name': 'White Chocolate Brownie', 'description': 'Vanilla-infused brownie with white chocolate chunks and macadamia nuts.', 'price': 10.25, 'image': 'https://images.unsplash.com/photo-1607478900766-efe13248b125?w=640&h=640&fit=crop'},
    {'id': 8, 'name': 'Salted Caramel Brownie', 'description': 'Sea salt caramel sauce drizzled over decadent chocolate brownie.', 'price': 9.75, 'image': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=640&h=640&fit=crop'},
    {'id': 9, 'name': 'Raspberry Dream Brownie', 'description': 'Tangy raspberry ribbons in a velvet chocolate base.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1505253212946-8ec396e41e33?w=640&h=640&fit=crop'},
    {'id': 10, 'name': 'Hazelnut Truffle Brownie', 'description': 'Crunchy hazelnut pieces with silky chocolate ganache.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1542444459-db2313c95823?w=640&h=640&fit=crop'},
    {'id': 11, 'name': 'Mocha Crunch Brownie', 'description': 'Coffee-infused brownie layered with chocolate crunch.', 'price': 10.25, 'image': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=640&h=640&fit=crop'},
    {'id': 12, 'name': 'Coconut Cloud Brownie', 'description': 'Coconut flakes and white chocolate make every bite dreamy.', 'price': 9.95, 'image': 'https://images.unsplash.com/photo-1505253212946-8ec396e41e33?w=640&h=640&fit=crop'},
    {'id': 13, 'name': 'Raspberry Cheesecake Brownie', 'description': 'Creamy cheesecake swirls with fresh raspberry topping.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1542444459-db2313c95823?w=640&h=640&fit=crop'},
    {'id': 14, 'name': 'Cookie Dough Brownie', 'description': 'Brownie base topped with cookie dough chunks and chocolate chips.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=640&h=640&fit=crop'},
    {'id': 15, 'name': 'Espresso Delight Brownie', 'description': 'Bold espresso, chocolate, and a caramel drizzle.', 'price': 10.75, 'image': 'https://images.unsplash.com/photo-1505253212946-8ec396e41e33?w=640&h=640&fit=crop'},
    {'id': 16, 'name': 'Coconut Almond Brownie', 'description': 'Toasted almonds and coconut layered on a fudgy base.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1542444459-db2313c95823?w=640&h=640&fit=crop'},
    {'id': 17, 'name': 'Caramel Pecan Brownie', 'description': 'Sticky caramel, pecans, and brownie goodness.', 'price': 10.95, 'image': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=640&h=640&fit=crop'},
    {'id': 18, 'name': 'Strawberry Shortcake Brownie', 'description': 'Strawberry pieces with creamy frosting and crumbs.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1505253212946-8ec396e41e33?w=640&h=640&fit=crop'},
    {'id': 19, 'name': 'Lemon Zest Brownie', 'description': 'Bright lemon flavor with a soft, buttery fudge bite.', 'price': 9.95, 'image': 'https://images.unsplash.com/photo-1542444459-db2313c95823?w=640&h=640&fit=crop'},
    {'id': 20, 'name': 'Cinnamon Spice Brownie', 'description': 'Warm cinnamon swirls with a gooey chocolate center.', 'price': 10.00, 'image': 'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=640&h=640&fit=crop'},
    {'id': 21, 'name': 'Almond Joy Brownie', 'description': 'Almonds and coconut in a rich chocolate square.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 22, 'name': "S'mores Brownie", 'description': 'Toasted marshmallow with graham cracker crunch.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 23, 'name': 'Birthday Sprinkle Brownie', 'description': 'Festive sprinkles over a chocolate party brownie.', 'price': 9.75, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 24, 'name': 'Matcha Green Brownie', 'description': 'Subtle matcha flavor blended with white chocolate.', 'price': 10.75, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 25, 'name': 'Dark Ganache Brownie', 'description': 'Ultra-rich dark chocolate with silky ganache topping.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 26, 'name': 'Honey Lavender Brownie', 'description': 'Floral lavender and sweet honey in every bite.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 27, 'name': 'Rocky Road Brownie', 'description': 'Marshmallows, nuts, and rich chocolate rocks of joy.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 28, 'name': 'Oreo Crunch Brownie', 'description': 'Crushed cookies in a fudgy brownie base.', 'price': 10.75, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 29, 'name': 'Chocolate Orange Brownie', 'description': 'Zesty orange paired with deep cocoa flavor.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 30, 'name': 'Sea Salt Caramel Brownie', 'description': 'Sweet caramel balanced with a punch of sea salt.', 'price': 10.95, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 31, 'name': 'Espresso Walnut Brownie', 'description': 'Crunchy walnuts and coffee flavors in every bite.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 32, 'name': 'Cherry Blossom Brownie', 'description': 'Light cherry notes with delicate floral accents.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 33, 'name': 'Pistachio Crunch Brownie', 'description': 'Toasted pistachios add a crunchy, nutty finish.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 34, 'name': 'White Raspberry Brownie', 'description': 'Tart raspberry and creamy white chocolate in harmony.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 35, 'name': 'Brownie Cheesecake Bar', 'description': 'Brownie and cheesecake layered into one heavenly bar.', 'price': 11.75, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 36, 'name': 'Maple Pecan Brownie', 'description': 'Warm maple sweetness with crunchy pecans.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 37, 'name': 'Triple Chocolate Brownie', 'description': 'Milk, dark, and white chocolate layers for chocoholics.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 38, 'name': 'Gingerbread Brownie', 'description': 'Cozy ginger, cinnamon, and molasses for a seasonal treat.', 'price': 10.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 39, 'name': 'Nutella Swirl Brownie', 'description': 'Creamy hazelnut spread swirled into rich brownie batter.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 40, 'name': 'Blueberry Lemon Brownie', 'description': 'Bright blueberry bursts with zesty lemon glaze.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 41, 'name': 'Peanut Caramel Brownie', 'description': 'Soft brownie with salted peanut and caramel ribbons.', 'price': 10.95, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 42, 'name': 'Vanilla Rose Brownie', 'description': 'Elegant vanilla and rosewater flavors for a floral bite.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 43, 'name': 'Mocha Almond Brownie', 'description': 'Coffee and almond crunch meet fudgy chocolate.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 44, 'name': 'Toffee Crunch Brownie', 'description': 'Crunchy toffee pieces on a soft brownie base.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 45, 'name': 'Walnut Caramel Brownie', 'description': 'Warm caramel and walnuts over a dark fudge cake.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 46, 'name': 'Berry Vanilla Brownie', 'description': 'Mixed berries and vanilla cream swirl through brownie layers.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 47, 'name': 'Dark Cherry Brownie', 'description': 'Juicy cherries with a bold dark chocolate base.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 48, 'name': 'Hazelnut Mocha Brownie', 'description': 'Coffee, chocolate, and hazelnut in perfect balance.', 'price': 11.50, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 49, 'name': 'Caramel Apple Brownie', 'description': 'Apple pieces and caramel ribbons for a cozy twist.', 'price': 11.25, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'},
    {'id': 50, 'name': 'Golden Honey Brownie', 'description': 'Smooth honey glaze on a soft, buttery brownie.', 'price': 11.00, 'image': 'https://images.unsplash.com/photo-1491897554428-130a60dd4757?w=640&h=640&fit=crop'}
]

REAL_PRODUCT_IMAGES = [
    '/static/images/pink-brownie-photo-1.png',
    '/static/images/pink-brownie-photo-2.png',
    '/static/images/pink-brownie-photo-3.png',
    '/static/images/pink-brownie-photo-4.png',
    '/static/images/cake-mango.png',
    '/static/images/cake-chocolate.png',
    '/static/images/cake-red-velvet.png',
    '/static/images/cake-fruit.png',
    '/static/images/cake-black-forest.png'
]

for index, product in enumerate(PRODUCTS):
    product['image'] = REAL_PRODUCT_IMAGES[index % len(REAL_PRODUCT_IMAGES)]
    product['price'] = round(product['price'] * INR_CONVERSION_RATE / 10) * 10


# -------------------------------------------------
# Database
# -------------------------------------------------

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row

    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def migrate_users_table(db):
    existing_columns = [row['name'] for row in db.execute("PRAGMA table_info(users)").fetchall()]
    required_columns = {
        'phone': 'TEXT',
        'address': 'TEXT',
        'city': 'TEXT',
        'state': 'TEXT',
        'postal_code': 'TEXT',
        'password': 'TEXT',
        'role': 'TEXT',
        'created_at': 'TEXT'
    }

    for column, column_type in required_columns.items():
        if column not in existing_columns:
            db.execute(f"ALTER TABLE users ADD COLUMN {column} {column_type}")


def init_db():
    db = get_db()

    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            postal_code TEXT,
            password TEXT,
            role TEXT,
            created_at TEXT
        )
    ''')

    migrate_users_table(db)

    db.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            customer_name TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            city TEXT,
            postal_code TEXT,
            delivery_instructions TEXT,
            total REAL,
            status TEXT,
            created_at TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    db.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            price REAL,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        )
    ''')

    db.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            method TEXT,
            amount REAL,
            card_last4 TEXT,
            status TEXT,
            created_at TEXT,
            FOREIGN KEY(order_id) REFERENCES orders(id)
        )
    ''')

    db.execute('''
        CREATE TABLE IF NOT EXISTS otps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            otp TEXT,
            created_at TEXT,
            expires_at TEXT
        )
    ''')

    db.commit()

    user_count = db.execute('SELECT COUNT(*) AS count FROM users').fetchone()

    if user_count and user_count['count'] == 0:
        now = utc_now().isoformat()

        db.execute(
            '''
            INSERT INTO users 
            (name, email, phone, address, city, state, postal_code, password, role, created_at) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                'Krishna Ki Bekary Fan',
                'user@example.com',
                '+91 98765 43210',
                '12 Brigade Road',
                'Bengaluru',
                'Karnataka',
                '560001',
                generate_password_hash('user123'),
                'user',
                now
            )
        )

        db.commit()

    admin_user = db.execute(
        'SELECT id, password FROM users WHERE email = ?',
        ('admin@example.com',)
    ).fetchone()

    now = utc_now().isoformat()

    if not admin_user:
        db.execute(
            '''
            INSERT INTO users
            (name, email, phone, address, city, state, postal_code, password, role, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                'Krishna Ki Bekary Admin',
                'admin@example.com',
                '',
                '',
                '',
                '',
                '',
                generate_password_hash('admin123'),
                'admin',
                now
            )
        )

        db.commit()

    elif not password_matches(admin_user['password'], 'admin123'):
        db.execute(
            'UPDATE users SET password = ?, role = ? WHERE id = ?',
            (generate_password_hash('admin123'), 'admin', admin_user['id'])
        )

        db.commit()


with app.app_context():
    init_db()


@app.before_request
def load_current_user():
    user = session.get('user')
    g.current_user = user if user else None


# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)


@app.route('/menu')
def menu():
    return render_template('menu.html', products=PRODUCTS)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', user=g.current_user)


@app.route('/create-order', methods=['POST'])
def create_order():
    payload = request.get_json(silent=True) or request.form.to_dict(flat=True)

    cart_json = payload.get('cart')

    try:
        cart = json.loads(cart_json or '[]')
    except json.JSONDecodeError:
        cart = []

    if not cart:
        return jsonify({'success': False, 'message': 'Cart is empty.'}), 400

    customer_name = payload.get('customerName', '').strip()
    email = payload.get('email', '').strip().lower()
    phone = payload.get('phone', '').strip()
    address = payload.get('address', '').strip()
    city = payload.get('city', '').strip()
    postal_code = payload.get('postalCode', '').strip()
    delivery_instructions = payload.get('deliveryInstructions', '').strip()
    payment_method = payload.get('paymentMethod', 'Card')
    card_number = payload.get('cardNumber', '').strip()

    if not customer_name or not email or not phone or not address or not city or not postal_code:
        return jsonify({'success': False, 'message': 'Please fill all required fields.'}), 400

    now = utc_now().isoformat()

    try:
        subtotal = sum(float(item['price']) * int(item['quantity']) for item in cart)
    except (KeyError, ValueError, TypeError):
        return jsonify({'success': False, 'message': 'Invalid cart data.'}), 400

    delivery_fee = 0 if subtotal >= FREE_DELIVERY_THRESHOLD else DELIVERY_FEE
    total = round(subtotal + delivery_fee, 2)

    user_id = g.current_user['id'] if g.current_user else None

    db = get_db()

    cursor = db.execute(
        '''
        INSERT INTO orders 
        (user_id, customer_name, email, phone, address, city, postal_code, delivery_instructions, total, status, created_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            user_id,
            customer_name,
            email,
            phone,
            address,
            city,
            postal_code,
            delivery_instructions,
            total,
            'Preparing',
            now
        )
    )

    order_id = cursor.lastrowid

    payment_status = 'Paid' if card_number else 'Pending'
    card_last4 = card_number[-4:] if card_number else 'N/A'

    db.execute(
        '''
        INSERT INTO payments 
        (order_id, method, amount, card_last4, status, created_at) 
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (
            order_id,
            payment_method,
            total,
            card_last4,
            payment_status,
            now
        )
    )

    for item in cart:
        db.execute(
            '''
            INSERT INTO order_items 
            (order_id, product_name, quantity, price) 
            VALUES (?, ?, ?, ?)
            ''',
            (
                order_id,
                item['name'],
                int(item['quantity']),
                float(item['price'])
            )
        )

    db.commit()

    return jsonify({'success': True, 'orderId': order_id})


@app.route('/order-success/<int:order_id>')
def order_success(order_id):
    db = get_db()

    order = db.execute(
        'SELECT * FROM orders WHERE id = ?',
        (order_id,)
    ).fetchone()

    if not order:
        return 'Order not found', 404

    items = db.execute(
        'SELECT * FROM order_items WHERE order_id = ?',
        (order_id,)
    ).fetchall()

    return render_template('order_success.html', order=order, items=items)


@app.route('/track')
def track():
    order_id = request.args.get('orderId')
    order = None
    message = None

    if order_id:
        db = get_db()

        order = db.execute(
            'SELECT * FROM orders WHERE id = ?',
            (order_id,)
        ).fetchone()

        if not order:
            message = 'Order not found. Please verify your number.'

    return render_template('track.html', order=order, message=message)


# -------------------------------------------------
# OTP Login
# -------------------------------------------------

@app.route('/send-otp', methods=['POST'])
def send_otp():
    data = request.get_json(silent=True) or request.form

    email = data.get('email', '').strip().lower()

    if not email:
        return jsonify({'success': False, 'message': 'Email is required.'}), 400

    db = get_db()

    user = db.execute(
        'SELECT * FROM users WHERE email = ?',
        (email,)
    ).fetchone()

    if not user or user['role'] != 'user':
        return jsonify({'success': False, 'message': 'Email not registered.'}), 404

    otp = ''.join(random.choices(string.digits, k=6))
    now = utc_now()
    expires_at = now + timedelta(minutes=10)

    db.execute(
        '''
        INSERT INTO otps 
        (email, otp, created_at, expires_at) 
        VALUES (?, ?, ?, ?)
        ''',
        (
            email,
            otp,
            now.isoformat(),
            expires_at.isoformat()
        )
    )

    db.commit()

    if send_otp_email(email, otp):
        return jsonify({'success': True, 'message': 'OTP sent to your email.'})

    return jsonify({'success': False, 'message': 'Failed to send OTP.'}), 500


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        otp = request.form.get('otp', '').strip()

        if not email or not otp:
            message = 'Email and OTP are required.'
            return render_template('login.html', message=message)

        db = get_db()

        otp_record = db.execute(
            '''
            SELECT * FROM otps 
            WHERE email = ? 
            AND otp = ? 
            AND expires_at > ? 
            ORDER BY created_at DESC 
            LIMIT 1
            ''',
            (
                email,
                otp,
                utc_now().isoformat()
            )
        ).fetchone()

        if otp_record:
            user = db.execute(
                'SELECT * FROM users WHERE email = ?',
                (email,)
            ).fetchone()

            if user and user['role'] == 'user':
                session['user'] = {
                    'id': user['id'],
                    'name': user['name'],
                    'email': user['email'],
                    'role': user['role']
                }

                db.execute(
                    'DELETE FROM otps WHERE id = ?',
                    (otp_record['id'],)
                )

                db.commit()

                return redirect(url_for('account'))

            message = 'User not found.'

        else:
            message = 'Invalid or expired OTP.'

    return render_template('login.html', message=message)


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip().lower()
    phone = request.form.get('phone', '').strip()
    address = request.form.get('address', '').strip()
    city = request.form.get('city', '').strip()
    state = request.form.get('state', '').strip()
    postal_code = request.form.get('postal_code', '').strip()

    if not name or not email or not phone or not address or not city or not state or not postal_code:
        return jsonify({'success': False, 'message': 'All fields are required.'}), 400

    db = get_db()

    existing_user = db.execute(
        'SELECT id FROM users WHERE email = ?',
        (email,)
    ).fetchone()

    if existing_user:
        return jsonify({'success': False, 'message': 'Email already registered.'}), 409

    now = utc_now().isoformat()

    db.execute(
        '''
        INSERT INTO users 
        (name, email, phone, address, city, state, postal_code, password, role, created_at) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            name,
            email,
            phone,
            address,
            city,
            state,
            postal_code,
            '',
            'user',
            now
        )
    )

    db.commit()

    return jsonify({'success': True, 'message': 'Account created. Please login with OTP.'})


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('menu'))


@app.route('/account')
def account():
    if not g.current_user:
        return redirect(url_for('login'))

    db = get_db()

    orders = db.execute(
        'SELECT * FROM orders WHERE email = ? ORDER BY created_at DESC',
        (g.current_user['email'],)
    ).fetchall()

    return render_template('account.html', orders=orders)


@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    message = None

    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        db = get_db()

        user = db.execute(
            'SELECT * FROM users WHERE email = ? AND role = ?',
            (email, 'admin')
        ).fetchone()

        if user and password_matches(user['password'], password):
            session['user'] = {
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
                'role': user['role']
            }

            return redirect(url_for('admin_dashboard'))

        message = 'Invalid admin email or password.'

    return render_template('admin_login.html', message=message)


@app.route('/admin-dashboard')
def admin_dashboard():
    if not g.current_user or g.current_user.get('role') != 'admin':
        return redirect(url_for('admin_login'))

    db = get_db()

    orders = db.execute(
        'SELECT * FROM orders ORDER BY created_at DESC'
    ).fetchall()

    return render_template('admin_dashboard.html', orders=orders)


@app.route('/admin-update-status', methods=['POST'])
def admin_update_status():
    if not g.current_user or g.current_user.get('role') != 'admin':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 403

    data = request.get_json(silent=True) or {}
    order_id = data.get('orderId')
    status = data.get('status')

    valid_statuses = {'Preparing', 'Out for delivery', 'Delivered'}

    if not order_id or status not in valid_statuses:
        return jsonify({'success': False, 'message': 'Invalid order update.'}), 400

    db = get_db()
    cursor = db.execute(
        'UPDATE orders SET status = ? WHERE id = ?',
        (status, order_id)
    )
    db.commit()

    if cursor.rowcount == 0:
        return jsonify({'success': False, 'message': 'Order not found.'}), 404

    return jsonify({'success': True})


@app.route('/api/products')
def api_products():
    return jsonify(PRODUCTS)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=os.getenv('FLASK_DEBUG') == '1', host='0.0.0.0', port=port)
