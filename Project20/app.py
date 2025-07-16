from flask import Flask, jsonify

app = Flask(__name__)

# Simple dictionary mapping hour ranges to advice
def get_health_advice(hour):
    hour = int(hour)
    if 5 <= hour < 8:
        return "Good morning! Start your day with some stretching or a light walk."
    elif 8 <= hour < 11:
        return "Stay hydrated! Have a glass of water or a healthy breakfast."
    elif 11 <= hour < 14:
        return "Time to take a break! Do some deep breathing or quick stretches."
    elif 14 <= hour < 17:
        return "Refocus! Take a short walk or enjoy some fruit for an energy boost."
    elif 17 <= hour < 20:
        return "Great time for some exercise or a relaxing hobby."
    elif 20 <= hour < 22:
        return "Wind down! Avoid screens and prepare for a good night's sleep."
    else:
        return "It might be late. Make sure to rest well and stay hydrated!"

@app.route('/reminder/<int:hour>')
def reminder(hour):
    if 0 <= hour <= 23:
        advice = get_health_advice(hour)
        return jsonify({"hour": hour, "advice": advice})
    else:
        return jsonify({"error": "Hour must be between 0 and 23"}), 400

@app.route('/reminder/help')
def help():
    help_text = """
    Usage:
    - /reminder/<hour>: Get health advice for a specific hour (hour should be 0 to 23).
    - /reminder/help: Show this help message.
    Example:
    Visit /reminder/10 to get advice for 10 AM.
    """
    return help_text, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(debug=True)
