from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/preview/<site>')
def preview(site):
    # You can simulate different preview texts here
    preview_text = f"This is {site}.com website. It's a dummy preview page."

    # Example: Customize for popular sites
    if site.lower() == "google":
        preview_text = "This is Google.com website. Search anything you like!"
    elif site.lower() == "youtube":
        preview_text = "This is YouTube.com website. Watch and share videos!"
    elif site.lower() == "facebook":
        preview_text = "This is Facebook.com website. Connect with friends!"

    # HTML template with <h1> and <p>
    html_content = f"""
    <!doctype html>
    <html>
    <head>
        <title>Preview of {site}</title>
    </head>
    <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
        <h1>Preview: {site.capitalize()}</h1>
        <p>{preview_text}</p>
    </body>
    </html>
    """

    return render_template_string(html_content)


if __name__ == "__main__":
    app.run(debug=True)
