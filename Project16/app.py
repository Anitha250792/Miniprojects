from flask import Flask

app = Flask(__name__)

# Route to greet based on hour
@app.route('/greet/<int:hour>')
def greet(hour):
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 18:
        return "Good Afternoon!"
    elif 18 <= hour <= 23 or 0 <= hour < 5:
        return "Good Night!"
    else:
        return "Invalid hour! Please provide an hour between 0 and 23."

# Route to show info about valid hours
@app.route('/greet/info')
def greet_info():
    return """
    <h2>Valid Hours Info</h2>
    <ul>
        <li>0–23 are valid hours.</li>
        <li>Morning: 5–11</li>
        <li>Afternoon: 12–17</li>
        <li>Night: 18–23 and 0–4</li>
    </ul>
    """

if __name__ == '__main__':
    # Enable debug mode so changes reflect automatically
    app.run(debug=True)
