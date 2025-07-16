from flask import Flask
from markupsafe import escape

app = Flask(__name__)

# rest of your code...


# Sample data for demonstration (usually from a database or file)
portfolio_data = {
    "alice": {
        "profile": {
            "name": "Alice Johnson",
            "title": "Software Developer",
            "bio": "Passionate about building web apps and learning new technologies."
        },
        "skills": ["Python", "Flask", "JavaScript", "HTML", "CSS"],
        "projects": [
            {"name": "Blog Platform", "description": "A blogging platform with user authentication."},
            {"name": "Portfolio Website", "description": "Personal portfolio to showcase my work."}
        ]
    },
    "bob": {
        "profile": {
            "name": "Bob Smith",
            "title": "Data Scientist",
            "bio": "Data enthusiast and machine learning practitioner."
        },
        "skills": ["Python", "Pandas", "NumPy", "Machine Learning", "Deep Learning"],
        "projects": [
            {"name": "Sales Predictor", "description": "Predict sales using regression models."},
            {"name": "Customer Segmentation", "description": "Cluster customers to improve marketing."}
        ]
    }
}

@app.route('/portfolio/<name>')
def profile(name):
    name_lower = name.lower()
    if name_lower not in portfolio_data:
        return f"<h1>No portfolio found for '{escape(name)}'</h1>", 404

    profile = portfolio_data[name_lower]["profile"]
    html = f"""
    <h1>{escape(profile['name'])}</h1>
    <h3>{escape(profile['title'])}</h3>
    <p>{escape(profile['bio'])}</p>
    <p><a href="/portfolio/{escape(name_lower)}/skills">Skills</a> | 
    <a href="/portfolio/{escape(name_lower)}/projects">Projects</a></p>
    """
    return html

@app.route('/portfolio/<name>/skills')
def skills(name):
    name_lower = name.lower()
    if name_lower not in portfolio_data:
        return f"<h1>No portfolio found for '{escape(name)}'</h1>", 404

    skills = portfolio_data[name_lower]["skills"]
    skills_list = "".join(f"<li>{escape(skill)}</li>" for skill in skills)

    html = f"""
    <h1>Skills for {escape(name_lower.title())}</h1>
    <ul>
        {skills_list}
    </ul>
    <p><a href="/portfolio/{escape(name_lower)}">Back to Profile</a></p>
    """
    return html

@app.route('/portfolio/<name>/projects')
def projects(name):
    name_lower = name.lower()
    if name_lower not in portfolio_data:
        return f"<h1>No portfolio found for '{escape(name)}'</h1>", 404

    projects = portfolio_data[name_lower]["projects"]
    rows = "".join(
        f"<tr><td>{escape(p['name'])}</td><td>{escape(p['description'])}</td></tr>" for p in projects
    )

    html = f"""
    <h1>Projects for {escape(name_lower.title())}</h1>
    <table border="1" cellpadding="5" cellspacing="0">
        <thead><tr><th>Project Name</th><th>Description</th></tr></thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    <p><a href="/portfolio/{escape(name_lower)}">Back to Profile</a></p>
    """
    return html

if __name__ == '__main__':
    app.run(debug=True)
