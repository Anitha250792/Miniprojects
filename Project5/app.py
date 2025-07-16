from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Hardcoded quotes for each day
quotes = {
    'monday': "Believe you can and you're halfway there.",
    'tuesday': "Your limitation—it's only your imagination.",
    'wednesday': "Push yourself, because no one else is going to do it for you.",
    'thursday': "Great things never come from comfort zones.",
    'friday': "Dream it. Wish it. Do it.",
    'saturday': "Success doesn’t just find you. You have to go out and get it.",
    'sunday': "The harder you work for something, the greater you’ll feel when you achieve it."
}

# Home route: show today's quote
@app.route('/')
def home():
    today = datetime.now().strftime("%A").lower()
    quote = quotes.get(today, "No quote for today.")
    return f'''
        <div style="font-family: Arial; margin: 50px; text-align: center;">
            <h1 style="color: #2c3e50;">Today's Quote ({today.capitalize()})</h1>
            <p style="font-size: 24px; color: #16a085;">"{quote}"</p>
        </div>
    '''

# Route for specific day
@app.route('/quote/<day>')
def quote_for_day(day):
    day_lower = day.lower()
    quote = quotes.get(day_lower)
    if quote:
        return f'''
            <div style="font-family: Arial; margin: 50px; text-align: center;">
                <h1 style="color: #2c3e50;">Quote for {day.capitalize()}</h1>
                <p style="font-size: 24px; color: #16a085;">"{quote}"</p>
            </div>
        '''
    else:
        return f'''
            <div style="font-family: Arial; margin: 50px; text-align: center;">
                <h1 style="color: red;">Invalid day: {day.capitalize()}</h1>
                <p style="font-size: 18px;">Please use monday, tuesday, etc.</p>
            </div>
        '''

if __name__ == '__main__':
    app.run(debug=True)
