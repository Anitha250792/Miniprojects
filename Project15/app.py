from flask import Flask

app = Flask(__name__)

@app.route('/mirror/<text>')
def mirror(text):
    reversed_text = text[::-1]
    text_length = len(text)

    html_content = f"""
    <h2>Text Mirror Tool</h2>
    <pre>
Original Text : {text}
Reversed Text : {reversed_text}
    </pre>
    <h3>Details Table</h3>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr>
            <th>Original</th>
            <th>Reversed</th>
            <th>Length</th>
        </tr>
        <tr>
            <td>{text}</td>
            <td>{reversed_text}</td>
            <td>{text_length}</td>
        </tr>
    </table>
    """

    return html_content

if __name__ == '__main__':
    app.run(debug=True)
