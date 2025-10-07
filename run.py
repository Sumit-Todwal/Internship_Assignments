import os
from app import create_app
from flask import render_template
from app.models import database

app = create_app()
database.init_db()

@app.route('/')
def homepage():
    return render_template(("base.html"))

if __name__ == "__main__":
    app.run(debug = True)
