# Copyright 2022 iiPython

# Modules
from itertools import islice
from nebula import app, rpath
from flask import render_template, send_from_directory

# Initialization
def chunks(data: dict):
    it = iter(data)
    for i in range(0, len(data), 4):
        yield {k: data[k] for k in islice(it, 4)}

# Routes
@app.route("/", methods = ["GET"])
def route_index() -> None:
    return render_template(
        "index.html",
        data = chunks(app.reader.get_current())
    ), 200

@app.route("/api/docs", methods = ["GET"])
def route_api_docs() -> None:
    return render_template("api.html"), 200

@app.route("/s/<path:path>", methods = ["GET"])
def route_static_file(path: str) -> None:
    return send_from_directory(rpath("src/static"), path)
