from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    print(f"Route /user/{name} accessed")
    return f"Welcome, {name}!"

@app.route('/user/<name>/location/<city>')
def user_location(name, city):
    print(f"Route /user/{name}/location/{city} accessed")
    return f"Hi {name}, how is {city}?"

if __name__ == '__main__':
    app.run(debug=True)
