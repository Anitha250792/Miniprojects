from flask import Flask

app = Flask(__name__)

# Home page: returns name, profession, and contact info in HTML
@app.route("/")
def home():
    return """
    <h1>John Doe</h1>
    <h2>Software Engineer</h2>
    <p>Email: john.doe@example.com</p>
    <p>Phone: +1-234-567-890</p>
    """

# About page: explains your background
@app.route("/about")
def about():
    return """
    <h1>About Me</h1>
    <p>I am a passionate software engineer with 5+ years of experience building web and mobile applications.
    I love working with Python, Flask, and modern web technologies.</p>
    """

# Skills page: show skills for given name
@app.route("/skills/<name>")
def skills(name):
    # Example hardcoded skills for demonstration
    skills_dict = {
        "john": ["Python", "Flask", "JavaScript", "SQL"],
        "jane": ["Java", "Spring Boot", "Angular", "Docker"],
        "alex": ["C++", "Embedded Systems", "Robotics"]
    }

    # Convert to lowercase for case-insensitive matching
    person = name.lower()
    if person in skills_dict:
        skills_list = skills_dict[person]
        skills_html = "<ul>" + "".join(f"<li>{skill}</li>" for skill in skills_list) + "</ul>"
        return f"<h1>Skills of {name.title()}</h1>{skills_html}"
    else:
        return f"<h1>No skills found for {name.title()}</h1>"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
