from flask import Blueprint, render_template

admin_bp = Blueprint(
    "admin_bp", 
    __name__, 
    template_folder='templates'
    )

@admin_bp.route("/")
def admin():
    source={'appname','Hermes'}
    return render_template("admin.html", source=source)