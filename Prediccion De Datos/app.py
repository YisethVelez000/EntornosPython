from flask import Flask, render_template, request

from predicciones import predecir

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('Name')
        matematicas = request.form.get('nmats')
        lecto = request.form.get('lecto')
        apoyo = request.form.get('apoyo')
        
        pred= predecir(float(matematicas),float(lecto), bool(apoyo))
        return render_template("index.html", pred=pred)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    