from flask import Flask
from markupsafe import Markup

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Enter your banner text</h2>
        <p>Example: <a href="/banner/Hello">/banner/Hello</a></p>
    '''

@app.route('/banner/<text>')
def banner(text):
    return f'<h1>{text}</h1>'

@app.route('/banner/<text>/<size>')
def banner_with_size(text, size):
    if size not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        return f'<p>Invalid size. Please use h1 to h6.</p>', 400
    return Markup(f'<{size}>{text}</{size}>')

if __name__ == '__main__':
    app.run(debug=True)
