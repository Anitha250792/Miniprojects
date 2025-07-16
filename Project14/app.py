from flask import Flask

app = Flask(__name__)

@app.route('/wordcount/<text>')
def word_count(text):
    # Split by whitespace to count words
    words = text.split()
    count = len(words)
    
    html = f"""
    <html>
    <head>
        <style>
            h1 {{
                color: #2c3e50;
                font-family: Arial, sans-serif;
            }}
            p {{
                font-size: 18px;
                color: #34495e;
                font-family: Arial, sans-serif;
            }}
        </style>
    </head>
    <body>
        <h1>Word Count Result</h1>
        <p>Input text: "{text}"</p>
        <p>Number of words: {count}</p>
    </body>
    </html>
    """
    return html

@app.route('/wordcount/help')
def help_page():
    html = """
    <html>
    <head>
        <style>
            h1 {
                color: #27ae60;
                font-family: Arial, sans-serif;
            }
            p {
                font-size: 18px;
                color: #2d3436;
                font-family: Arial, sans-serif;
            }
        </style>
    </head>
    <body>
        <h1>Word Counter Help</h1>
        <p>Use the route <strong>/wordcount/&lt;text&gt;</strong> to count words in your text.</p>
        <p>Example: <code>/wordcount/Hello%20world%20from%20Flask</code></p>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
