from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"items": []}
    return render_template('items.html', items=data.get("items", []))

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products_list = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products_list.append(row)
    return products_list

def read_sql():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template('product_display.html', error="Wrong source")

    try:
        if source == 'json':
            products_list = read_json()
        elif source == 'csv':
            products_list = read_csv()
        elif source == 'sql':
            products_list = read_sql()
    except Exception as e:
        return render_template('product_display.html', error=str(e))

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Product not found")
        products_list = [p for p in products_list if p['id'] == product_id]
        if not products_list:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
