from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def example():
    return render_template('template.html', current_time = str(datetime.now()))

@app.route("/new/")
def new():
    return "new page"

if __name__ == "__main__":
    app.run()