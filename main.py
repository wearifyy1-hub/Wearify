from flask import Flask, render_template, redirect, url_for, request, session, jsonify

app = Flask(__name__)

# Sample data placeholders
PRODUCTS = [
    {'id': 1, 'title': 'T-Shirt'},
    {'id': 2, 'title': 'Hoodie'}
]

Tshirt_Photos = [
    {'filename': 'tshirt1.jpg', 'title': 'Classic White T-Shirt'},
    {'filename': 'tshirt2.png', 'title': 'Black Printed Tee'},
    {'filename': 'tshirt3.png', 'title': 'Blue Sports Tee'}
]

Hoodie_Photos = [
    {'filename': 'hoodie1.png', 'title': 'Grey Zip Hoodie'},
    {'filename': 'hoodie2.png', 'title': 'Black Pullover Hoodie'},
    {'filename': 'hoodie3.png', 'title': 'Red Oversized Hoodie'}
]



@app.route('/')
def home():
    return render_template('home.html', products=PRODUCTS)


@app.route('/api/products')
def list_products():
    return jsonify(PRODUCTS)


@app.route('/tshirt_photos')
def tshirt_photos():
    return render_template('tshirt_photos_page.html', photos=Tshirt_Photos)


@app.route('/hoodie_photos')
def hoodie_photos():
    return render_template('hoodie_photos_page.html', photos=Hoodie_Photos)


@app.route('/tshirt_photos_page.html')
def tshirt_photos_redirect():
    return redirect(url_for('tshirt_photos'), code=301)


@app.route('/hoodie_photos_page.html')
def hoodie_photos_redirect():
    return redirect(url_for('hoodie_photos'), code=301)


@app.route('/tshirt/<int:tshirt_id>')
def tshirt_detail(tshirt_id):
    if 1 <= tshirt_id <= len(Tshirt_Photos):
        tshirt = Tshirt_Photos[tshirt_id - 1]
        return render_template('tshirt_detail.html', tshirt=tshirt)
    else:
        return "T-Shirt not found", 404


if __name__ == '__main__':
    app.run(debug=True)
