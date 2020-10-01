from flask import Flask, request, render_template, url_for, redirect, jsonify

app = Flask(__name__)
# app.debug = True we can also do it like this


@app.route("/", methods=["GET", "POST"])
def main():
    respuesta = ""
    if request.method == "GET":
        respuesta += "Get metodo! "
        respuesta += request.args.get("key", "")  # path?key=value
        myCookie = request.cookies.get("username")  # also req.cookies['name]
    if request.method == "POST":
        usuario = request.form["username"]
        contrasena = request.form["password"]
        archivo = request.files[
            "file_name"
        ]  # archivo.filename (gets original filename)
        respuesta += "Post metodo!"
    respuesta += " Welcome to whats-with-the-world server app"
    return respuesta


@app.route("/redirect")
def redirectme():
    return redirect(url_for("render"))


@app.route("/api/<username>")
def api(username):
    url_for("static", filename="style.css")
    return "<p>respuesta string para</p> %s" % username


@app.route("/api")
def myJson():
    return jsonify([{"user": "tavo", "age": 31}, {"user": "andy", "age": 34}])


@app.route("/render", methods=["GET"])
def render():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)