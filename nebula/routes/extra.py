# Copyright 2022 iiPython

# Modules
from nebula import app, rpath
from flask import render_template, send_from_directory

# Routes
@app.route("/s/<path:path>", methods = ["GET"])
def route_static_file(path: str) -> None:
    return send_from_directory(rpath("src/static"), path)

# Error handlers
@app.errorhandler(400)
def errorhandle_400(e: Exception) -> None:
    return render_template("errors/400.html"), 400

@app.errorhandler(404)
def errorhandle_404(e: Exception) -> None:
    return render_template("errors/404.html"), 404

@app.errorhandler(500)
def errorhandle_500(e: Exception) -> None:
    return render_template("errors/500.html"), 500
