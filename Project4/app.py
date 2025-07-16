from flask import Flask

app = Flask(__name__)

# Route for simple hello
@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

# Route for greeting based on time
@app.route('/greet/<name>/<time>')
def greet(name, time):
    time = time.lower()
    if time == 'morning':
        greeting = f"Good Morning {name}!"
    elif time == 'evening':
        greeting = f"Good Evening {name}!"
    else:
        greeting = f"Hello {name}, have a nice day!"
    return greeting

if __name__ == "__main__":
    app.run(debug=True)
