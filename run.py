import os
import json
from datetime import datetime
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
   data = []
   with open("data/company.json", "r") as json_data:
      data = json.load(json_data)
   return render_template('about.html', page_title="About", company=data)


@app.route("/contact")
def contact():
   """
   Displays the contact page
   """
   return render_template('contact.html', page_title="Contact")


@app.route("/careers")
def careers():
  """
  Displays careers page
  """
  return render_template('careers.html', page_title="Careers")


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

if __name__ == "__main__":
    app.run(
      host=os.environ.get("IO", "0.0.0.0"),
      port=int(os.environ.get("PORT", "5001")),
      debug=True
    )

