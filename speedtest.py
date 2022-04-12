# Copyright 2022 iiPython

# Modules
import sys
import time
from requests import get

# Run test
rsl_url = f"{sys.argv[1]}/api/status"
start = time.time()
times = [get(rsl_url).elapsed.total_seconds() * 1000 for i in range(100)]
print(f"Completed in {round((time.time() - start) * 1000, 2)}ms, avg. resp time: {round(sum(times) / len(times), 2)}ms")
