from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Route for business hours status
@app.route('/')
def home():
    # Check current server time
    now = datetime.now()
    # Let's assume business hours are 9 AM to 6 PM
    if 9 <= now.hour < 18:
        status = "<b>We are open!</b>"
    else:
        status = "<b>Closed</b>"

    return f"""
    <h1>Business Status</h1>
    <p>{status}</p>
    <hr>
    <p>Welcome to our digital visiting card website.</p>
    """

# Route for contact info
@app.route('/contact')
def contact():
    return """
    <h1>Contact Us</h1>
    <p>Email: <b>contact@example.com</b></p>
    <p>Phone: <b>+1-234-567-890</b></p>
    <hr>
    <p>We look forward to hearing from you!</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
