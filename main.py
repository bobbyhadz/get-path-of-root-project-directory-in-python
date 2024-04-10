# Get the path of the Root Project directory using Python

import os

# 👇️ /home/borislav/Desktop/bobbyhadz_python/main.py
print(__file__)

ROOT_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# 👇️ /home/borislav/Desktop/bobbyhadz_python
print(ROOT_DIR)