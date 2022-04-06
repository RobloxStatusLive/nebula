# Copyright 2022 iiPython

# Modules
import os
from flask import Flask

# Initialization
def rpath(path: str) -> str:
    return os.path.join(os.path.dirname(__file__), path)

app = Flask(
    "Nebula",
    template_folder = rpath("src/templates")
)

# Routes
