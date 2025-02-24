from flask import Flask, render_template, request
from blueprints.coche import coches_bp
from errors.handlers import init_error_handlers  

app = Flask(__name__)

# Middleware antes de procesar cada request
@app.before_request
def registrar_peticiones():
    print(f"Petición: {request.method} {request.path}")  

# Middleware después de procesar cada request
@app.after_request
def modificar_respuesta(response):
    response.headers["X-Developer"] = "TuNombre"  
    return response

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

