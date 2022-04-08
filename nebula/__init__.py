# Copyright 2022 iiPython

# Modules
import os
from flask import Flask

from .sync import SyncReader

# Initialization
def rpath(path: str) -> str:
    return os.path.join(os.path.dirname(__file__), path)

app = Flask(
    "Nebula",
    template_folder = rpath("src/templates")
)
app.version = "1.1.1"
app.reader = SyncReader()

# Jinja env
@app.context_processor
def insert_globals() -> dict:
    return {"app": app, "status": app.reader.get_overall_status() or "slow", "read": lambda f: open(rpath(f"src/templates/{f}"), "r").read()}

# Routes
from .routes import (api, public)
