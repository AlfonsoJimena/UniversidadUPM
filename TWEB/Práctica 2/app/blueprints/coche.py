from flask import Blueprint, render_template, request, redirect, url_for

coches_bp = Blueprint("coches", __name__)

# Datos de ejemplo (Seeder)
coches = [
    {"id": 1, "marca": "Porsche", "modelo": "Cayman 987", "cv": 295, "manual": True, "año": 2010},
    {"id": 2, "marca": "Mazda", "modelo": "MX-5 ND RF", "cv": 184, "manual": True, "año": 2022},
    {"id": 3, "marca": "BMW", "modelo": "M3 E46", "cv": 343, "manual": True, "año": 2003}
]

# Listar coches
@coches_bp.route("/")
def listar_coches():
    return render_template("coches/list.html", coches=coches)

# Mostrar detalle de un coche
@coches_bp.route("/<int:coche_id>")
def mostrar_coche(coche_id):
    coche = next((c for c in coches if c["id"] == coche_id), None)
    return render_template("coches/show.html", coche=coche) if coche else ("Coche no encontrado", 404)

# Formulario para nuevo coche
@coches_bp.route("/new")
def formulario_nuevo():
    return render_template("coches/new.html")

# Crear coche
@coches_bp.route("/", methods=["POST"])
def crear_coche():
    nuevo_coche = {
        "id": len(coches) + 1,
        "marca": request.form["marca"],
        "modelo": request.form["modelo"],
        "anio": int(request.form["anio"]),
        "precio": float(request.form["precio"]),
        "descapotable": request.form.get("descapotable") == "on"
    }
    coches.append(nuevo_coche)
    return redirect(url_for("coches.listar_coches"))

# Formulario para editar coche
@coches_bp.route("/<int:coche_id>/edit")
def formulario_editar(coche_id):
    coche = next((c for c in coches if c["id"] == coche_id), None)
    return render_template("coches/edit.html", coche=coche) if coche else ("Coche no encontrado", 404)

# Editar coche
@coches_bp.route("/<int:coche_id>", methods=["POST"])
def editar_coche(coche_id):
    coche = next((c for c in coches if c["id"] == coche_id), None)
    if coche:
        coche.update({
            "marca": request.form["marca"],
            "modelo": request.form["modelo"],
            "anio": int(request.form["anio"]),
            "precio": float(request.form["precio"]),
            "descapotable": request.form.get("descapotable") == "on"
        })
        return redirect(url_for("coches.listar_coches"))
    return ("Coche no encontrado", 404)

# Eliminar coche
@coches_bp.route("/<int:coche_id>/delete", methods=["POST"])
def eliminar_coche(coche_id):
    global coches
    coches = [c for c in coches if c["id"] != coche_id]
    return redirect(url_for("coches.listar_coches"))