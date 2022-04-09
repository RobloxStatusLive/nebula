# Copyright 2022 iiPython

# Modules
import os
import sys

# Initialization
if "--sync-thread" in sys.argv:
    from nebula.sync import SyncManager
    exit(SyncManager().loop())

# Launch nebula
from nebula import app
if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        port = int(os.getenv("PORT", 8080)),
        debug = True
    )
