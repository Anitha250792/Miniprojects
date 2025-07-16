from flask import Flask

app = Flask(__name__)

# Dictionary of fun facts
animal_facts = {
    "cat": "Cats can jump up to six times their length.",
    "dog": "Dogs have a sense of smell that's 40 times better than humans.",
    "elephant": "Elephants are the only animals that can't jump.",
    "dolphin": "Dolphins have names for each other.",
    "kangaroo": "Kangaroos can't walk backwards."
}

@app.route('/fact/<animal>')
def get_fact(animal):
    fact = animal_facts.get(animal.lower())
    if fact:
        return f"""
        <html>
            <body style='background-color: #f0f8ff; color: #333; font-family: Arial; padding: 20px;'>
                <h2>Fun Fact about {animal.title()}:</h2>
                <ul>
                    <li style='color: #ff4500;'>{fact}</li>
                </ul>
                <a href="/fact/list">Back to Animal List</a>
            </body>
        </html>
        """
    else:
        return f"""
        <html>
            <body style='background-color: #ffe4e1; color: #333; font-family: Arial; padding: 20px;'>
                <h2>No fun fact found for '{animal}'</h2>
                <a href="/fact/list">See Available Animals</a>
            </body>
        </html>
        """

@app.route('/fact/list')
def list_animals():
    animals = list(animal_facts.keys())
    list_items = ''.join([f"<li style='color: #008b8b;'>{a.title()}</li>" for a in animals])
    return f"""
    <html>
        <body style='background-color: #fafad2; color: #333; font-family: Arial; padding: 20px;'>
            <h2>Available Animals</h2>
            <ul>
                {list_items}
            </ul>
            <p>Use <code>/fact/&lt;animal&gt;</code> to see a fun fact!</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
