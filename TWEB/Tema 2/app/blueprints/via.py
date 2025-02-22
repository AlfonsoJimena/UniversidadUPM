from flask import Blueprint # Se importa la clase Blueprint desde el módulo flask

via_bp = Blueprint('via', __name__, template_folder='../../templates/via') # Se define el Blueprint con el nombre 'via' y la carpeta de templates

@via_bp.route('/')
def list():
    return "Listado de vías"
