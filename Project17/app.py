from flask import Flask

app = Flask(__name__)

# List of valid operations
valid_ops = ['add', 'sub', 'mul', 'div']

@app.route('/ops')
def list_ops():
    ops_html = "<h2>Valid operations:</h2>"
    ops_html += "<ul>"
    for op in valid_ops:
        ops_html += f"<li>{op}</li>"
    ops_html += "</ul>"
    return ops_html

@app.route('/calc/<op>/<num1>/<num2>')
def calculate(op, num1, num2):
    # Validate numeric inputs
    try:
        n1 = float(num1)
        n2 = float(num2)
    except ValueError:
        return "<h2>Invalid numbers provided!</h2>"

    # Perform operations
    if op == 'add':
        result = n1 + n2
    elif op == 'sub':
        result = n1 - n2
    elif op == 'mul':
        result = n1 * n2
    elif op == 'div':
        if n2 == 0:
            return "<h2>Error: Division by zero is not allowed!</h2>"
        result = n1 / n2
    else:
        return f"<h2>Invalid operation! Visit /ops to see valid operations.</h2>"

    return f"<h2>Result of {op} between {n1} and {n2} is: {result}</h2>"

if __name__ == '__main__':
    app.run(debug=True)
