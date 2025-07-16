from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! This is the homepage."

@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    bmi_value = weight / (height ** 2)
    return f"BMI: {bmi_value:.2f}"

if __name__ == '__main__':
    app.run(debug=True)
