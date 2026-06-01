from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("waste_data.json", "r") as file:
    waste_data = json.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    item = request.form["item"].lower()

    result = waste_data.get(item)

    if result:
        return render_template(
            "result.html",
            item=item.title(),
            data=result
        )
    else:
        return render_template(
            "result.html",
            item=item.title(),
            data=None
        )

if __name__ == "__main__":
    app.run(debug=True)