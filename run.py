import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  """
  Displays "Hello, World" on the index page
  """
  return render_template('index.html')


@app.route("/about")
def about():
   """
   Displays about page
   """
   return render_template('about.html')


@app.route("/contact")
def contact():
   """
   Displays the contact page
   """
   return render_template('contact.html')


@app.route("/careers")
def careers():
  """
  Displays careers page
  """
  return render_template('careers.html')

if __name__ == "__main__":
    app.run(
      host=os.environ.get("IO", "0.0.0.0"),
      port=int(os.environ.get("PORT", "5001")),
      debug=True
    )

