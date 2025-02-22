from flask import Flask, request, render_template # Importamos la función render_template
import blueprints


app = Flask(__name__, template_folder='templates') # Indicamos la carpeta donde se encuentran los templates
app.register_blueprint(blueprints.via_bp, url_prefix='/vias')
app.register_blueprint(blueprints.bloque_bp, url_prefix='/bloques')
from blueprints.via import via_bp
from blueprints.bloque import bloque_bp

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/about')  
def about():
    return render_template('about.html')

@app.route('/ciudad/<ciudad>')  
def ciudad(ciudad):
    return render_template('city.html', ciudad=ciudad)

@app.route('/disponibilidad')  
def disponibilidad():
    return render_template('availability.html')


