from flask import Blueprint, render_template, request, redirect, url_for

coches_bp = Blueprint("coches", __name__)

# Datos de ejemplo (Seeder)
coches = [
    {"id": 1, "marca": "Mazda", "modelo": "MX-5 Miata", "cv": 100, "manual": True, "anio": 1990, "precio": 3000, "descapotable": True},
    {"id": 2, "marca": "Mazda", "modelo": "MX-5 ND RF", "cv": 184, "manual": True, "anio": 2025, "precio": 44000, "descapotable": True},
    {"id": 3, "marca": "Mazda", "modelo": "MX-5 ND NC", "cv": 131, "manual": True, "anio": 2025, "precio": 41000, "descapotable": True},
    {"id": 4, "marca": "Porsche", "modelo": "987 Cayman S", "cv": 295, "manual": True, "anio": 2008, "precio": 35000, "descapotable": False},
    {"id": 5, "marca": "Porsche", "modelo": "911 Carrera", "cv": 385, "manual": True, "anio": 2012, "precio": 60000, "descapotable": False},
    {"id": 6, "marca": "BMW", "modelo": "Z4", "cv": 197, "manual": False, "anio": 2020, "precio": 55000, "descapotable": True},
    {"id": 7, "marca": "Toyota", "modelo": "GR86", "cv": 234, "manual": True, "anio": 2023, "precio": 38000, "descapotable": False},
    {"id": 8, "marca": "Toyota", "modelo": "Supra A90", "cv": 340, "manual": False, "anio": 2022, "precio": 67000, "descapotable": False},
    {"id": 9, "marca": "Ford", "modelo": "Mustang GT", "cv": 450, "manual": True, "anio": 2024, "precio": 58000, "descapotable": True},
    {"id": 10, "marca": "Chevrolet", "modelo": "Corvette C8", "cv": 495, "manual": False, "anio": 2023, "precio": 75000, "descapotable": True},
    {"id": 11, "marca": "Honda", "modelo": "S2000", "cv": 240, "manual": True, "anio": 2006, "precio": 30000, "descapotable": True},
    {"id": 12, "marca": "Nissan", "modelo": "370Z", "cv": 328, "manual": True, "anio": 2018, "precio": 35000, "descapotable": False}
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