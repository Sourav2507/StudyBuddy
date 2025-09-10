from flask import Blueprint

routes = Blueprint("route",__name__,template_folder='frontend/templates',url_prefix='/route')

@routes.route("/hi")
def hi():
    return "Hi from routes"