from flask import Blueprint

bloque_bp = Blueprint('bloque', __name__, template_folder='../templates/bloque')

@bloque_bp.route('/')
def list():
    return "Listado de bloques"