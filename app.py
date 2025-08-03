from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from strength_checker import check_password_strength

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)  # Optional if serving everything from Flask now

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    password = data.get("password", "")
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
