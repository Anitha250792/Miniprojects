from flask import Flask

app = Flask(__name__)

@app.route('/zodiac/<date>')
def zodiac(date):
    try:
        # Split the string "YYYY-MM-DD"
        parts = date.split('-')
        if len(parts) != 3:
            return f"<strong>Error:</strong> Invalid date format.<br>Use <i>YYYY-MM-DD</i>."

        year, month, day = map(int, parts)

        # Dummy logic for zodiac sign (you can improve it later)
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            sign = "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            sign = "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            sign = "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            sign = "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            sign = "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            sign = "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            sign = "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            sign = "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            sign = "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            sign = "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            sign = "Aquarius"
        elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
            sign = "Pisces"
        else:
            sign = "Unknown"

        return f"""
            <h2>Zodiac Sign Result</h2>
            <hr>
            <p>Your birth date: <strong>{date}</strong></p>
            <p>Your Zodiac sign is: <strong>{sign}</strong></p>
            <p><i>Thank you for using our Zodiac Generator!</i></p>
        """
    except Exception as e:
        return f"<strong>Error:</strong> {str(e)}"

@app.route('/zodiac/help')
def help_page():
    return """
        <h2>Zodiac Sign Generator Help</h2>
        <hr>
        <p>Please enter your birth date in the URL like this:</p>
        <p><strong>/zodiac/YYYY-MM-DD</strong></p>
        <p><i>For example:</i> /zodiac/2000-12-25</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
