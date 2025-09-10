from flask import Flask
from backend import routes

app = Flask(__name__)
app.register_blueprint(routes.routes)

@app.route("/")
def main():
    return "Hello Flask"

if __name__=="__main__":
    app.run()