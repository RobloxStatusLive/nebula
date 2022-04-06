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
app.version = "1.1.0"
app.reader = SyncReader()

# Routes
from .routes import (api, public)
