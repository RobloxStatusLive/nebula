# Copyright 2022 iiPython

# Modules
from itertools import islice
from nebula import app, rpath
from flask import render_template, send_from_directory, request

# Initialization
def chunks(data: dict):
    it = iter(data)
    for i in range(0, len(data), 4):
        yield {k: data[k] for k in islice(it, 4)}

# Routes
@app.route("/", methods = ["GET"])
def route_index() -> None:
    if request.user_agent.platform in ["android", "iphone", "fennec", "iemobile", "mobile"]:
        return route_layout_list()

    return route_layout_grid()

@app.route("/grid", methods = ["GET"])
def route_layout_grid() -> None:
    data = app.reader.get_current()
    if data is None:
        return render_template("errors/nodata.html"), 200

    return render_template("layouts/grid.html", data = chunks(data)), 200

@app.route("/list", methods = ["GET"])
def route_layout_list() -> None:
    data = app.reader.get_current()
    if data is None:
        return render_template("errors/nodata.html"), 200

    return render_template("layouts/list.html", data = data), 200

@app.route("/api/docs", methods = ["GET"])
def route_api_docs() -> None:
    return render_template("api.html"), 200

@app.route("/s/<path:path>", methods = ["GET"])
def route_static_file(path: str) -> None:
    return send_from_directory(rpath("src/static"), path)
