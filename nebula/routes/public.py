# Copyright 2022 iiPython

# Modules
import json
from itertools import islice
from nebula import app, rpath
from flask import render_template, request

# Initialization
def chunks(data: dict):
    it = iter(data)
    for i in range(0, len(data), 4):
        yield {k: data[k] for k in islice(it, 4)}

with open(rpath("icons.json"), "r") as icon_file:
    icons = json.loads(icon_file.read())

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

    return render_template("layouts/grid.html", data = chunks(data), icons = icons), 200

@app.route("/list", methods = ["GET"])
def route_layout_list() -> None:
    data = app.reader.get_current()
    if data is None:
        return render_template("errors/nodata.html"), 200

    return render_template("layouts/list.html", data = data), 200

@app.route("/api/docs", methods = ["GET"])
def route_api_docs() -> None:
    return render_template("api.html"), 200
