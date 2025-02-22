from flask import Flask, render_template
from blueprints.coche import coches_bp
from errors.handlers import init_error_handlers  

app = Flask(__name__)

# Registrar el blueprint de coches
app.register_blueprint(coches_bp, url_prefix="/coches")

# Registrar manejadores de errores
init_error_handlers(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
