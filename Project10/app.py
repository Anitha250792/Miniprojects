from flask import Flask, render_template_string
import random

app = Flask(__name__)

# List of motivational messages
messages = [
    "Believe in yourself and all that you are!",
    "You are stronger than you think!",
    "Every day is a fresh start.",
    "Dream it. Wish it. Do it.",
    "Push yourself, because no one else is going to do it for you.",
    "Don't watch the clock; do what it does. Keep going.",
    "Stay positive, work hard, make it happen.",
    "Great things never come from comfort zones.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Success doesn’t just find you. You have to go out and get it."
]

@app.route('/message')
def random_message():
    message = random.choice(messages)
    return render_template_string(html_template, message=message)

@app.route('/message/<int:index>')
def message_by_index(index):
    if 0 <= index < len(messages):
        message = messages[index]
    else:
        message = "Invalid index! Please choose a value between 0 and {}.".format(len(messages)-1)
    return render_template_string(html_template, message=message)

# Inline HTML template with colorful CSS
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Motivational Message</title>
    <style>
        body {
            background: linear-gradient(135deg, #f6d365, #fda085);
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 100px;
            color: #ffffff;
        }
        .message-box {
            background: rgba(0,0,0,0.3);
            padding: 40px;
            border-radius: 15px;
            display: inline-block;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 {
            font-size: 28px;
        }
    </style>
</head>
<body>
    <div class="message-box">
        <h1>{{ message }}</h1>
    </div>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
