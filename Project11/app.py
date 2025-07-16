from flask import Flask, abort
from datetime import datetime

app = Flask(__name__)

@app.route('/age/<name>/<int:year>')
def age_checker(name, year):
    current_year = datetime.now().year
    if year >= current_year:
        return f"""
        <h2>Error</h2>
        <p>Invalid birth year: {year}. It must be less than the current year ({current_year}).</p>
        """
    age = current_year - year
    return f"""
    <html>
        <head>
            <title>Age Checker</title>
        </head>
        <body>
            <h1>Hi {name}, you are {age} years old.</h1>
        </body>
    </html>
    """

if __name__ == '__main__':
    # This allows running with: python app.py
    app.run(host='0.0.0.0', port=5050, debug=True)
