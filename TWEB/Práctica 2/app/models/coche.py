from flask import Flask, render_template, request, redirect, url_for, Blueprint

app = Flask(__name__)

# Datos simulados (Seeder)
coches = [
    {"id": 1, "marca": "Porsche", "modelo": "Cayman 987", "cv": 295, "manual": True, "año": 2010},
    {"id": 2, "marca": "Mazda", "modelo": "MX-5 ND RF", "cv": 184, "manual": True, "año": 2022},
    {"id": 3, "marca": "BMW", "modelo": "M3 E46", "cv": 343, "manual": True, "año": 2003}
]

# Rutas principales
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Blueprint para coches
coches_bp = Blueprint('coches', __name__, template_folder='templates')

@coches_bp.route('/coches')
def lista_coches():
    return render_template('coches/list.html', coches=coches)

@coches_bp.route('/coches/new', methods=['GET', 'POST'])
def nuevo_coche():
    if request.method == 'POST':
        nuevo_id = max([c['id'] for c in coches]) + 1
        coche = {
            "id": nuevo_id,
            "marca": request.form['marca'],
            "modelo": request.form['modelo'],
            "cv": int(request.form['cv']),
            "manual": request.form.get('manual') == 'on',
            "año": int(request.form['año'])
        }
        coches.append(coche)
        return redirect(url_for('coches.lista_coches'))
    return render_template('coches/new.html')

@coches_bp.route('/coches/<int:coche_id>')
def mostrar_coche(coche_id):
    coche = next((c for c in coches if c['id'] == coche_id), None)
    if coche:
        return render_template('coches/show.html', coche=coche)
    return render_template('errors/error404.html'), 404

@coches_bp.route('/coches/<int:coche_id>/edit', methods=['GET', 'POST'])
def editar_coche(coche_id):
    coche = next((c for c in coches if c['id'] == coche_id), None)
    if not coche:
        return render_template('errors/error404.html'), 404
    
    if request.method == 'POST':
        coche['marca'] = request.form['marca']
        coche['modelo'] = request.form['modelo']
        coche['cv'] = int(request.form['cv'])
        coche['manual'] = request.form.get('manual') == 'on'
        coche['año'] = int(request.form['año'])
        return redirect(url_for('coches.lista_coches'))
    
    return render_template('coches/edit.html', coche=coche)

@coches_bp.route('/coches/<int:coche_id>/delete', methods=['POST'])
def eliminar_coche(coche_id):
    global coches
    coches = [c for c in coches if c['id'] != coche_id]
    return redirect(url_for('coches.lista_coches'))

# Registro del blueprint
app.register_blueprint(coches_bp)

# Manejo de errores
@app.errorhandler(404)
def error_404(error):
    return render_template('errors/error404.html'), 404

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/error500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
