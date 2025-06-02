from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            amount = float(request.form["amount"])
            rate = float(request.form["rate"])
            result = amount * rate
        except ValueError:
            result = "Erro: valores inválidos"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
