# Copyright 2022 iiPython

# Modules
import os
import json
from typing import Any

# Initialization
global_defaults = {
    "nebula.enable_memcache": True,
    "nebula.protocol": "https"
}

# Configuration class
class Configuration(object):
    def __init__(self) -> None:
        try:
            with open(os.path.join(os.path.dirname(__file__), "../config.json"), "r") as f:
                self.config = json.loads(f.read())

        except Exception:
            self.config = {}

    def get(self, key: str, default: Any = None) -> Any:
        if key not in self.config:
            return global_defaults.get(key, default)

        return self.config[key]

config = Configuration()
