from flask import Blueprint, render_template

print("initiate home-route.py")

home_bp = Blueprint(
    "home_bp", 
    __name__,
    template_folder='templates'
    )

@home_bp.route("/")
def admin():
    source={'appname','Hermes'}
    return render_template("home.html", source=source)