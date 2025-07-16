from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Hardcoded product data
products = {
    "1": {"name": "Laptop", "price": 75000, "stock": "In Stock"},
    "2": {"name": "Smartphone", "price": 35000, "stock": "Out of Stock"},
    "3": {"name": "Headphones", "price": 1500, "stock": "In Stock"}
}

@app.route("/product/<id>")
def product_info(id):
    print(f"Accessed /product/{id} route")  # Print to terminal

    product = products.get(id)
    if not product:
        abort(404, description="Product not found")

    # Return details as HTML
    return render_template_string("""
        <h1>Product Info</h1>
        <p><strong>Name:</strong> {{ product.name }}</p>
        <p><strong>Price:</strong> ₹{{ product.price }}</p>
        <p><strong>Stock Status:</strong> {{ product.stock }}</p>
        <a href="/products">Back to all products</a>
    """, product=product)


@app.route("/products")
def list_products():
    print("Accessed /products route")  # Print to terminal

    # Return product list as HTML table
    return render_template_string("""
        <h1>All Products</h1>
        <table border="1" cellpadding="5" cellspacing="0">
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Link</th>
            </tr>
            {% for id, product in products.items() %}
            <tr>
                <td>{{ id }}</td>
                <td>{{ product.name }}</td>
                <td><a href="/product/{{ id }}">View</a></td>
            </tr>
            {% endfor %}
        </table>
    """, products=products)


if __name__ == "__main__":
    app.run(debug=True)
