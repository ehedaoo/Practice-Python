# Write a Python program to get OS name, platform and release information.

import os
import platform

print(os.name)
print(platform.version())
print(platform._release_filename)
print(platform.__version__)
print(platform.win32_ver())
print(platform.release())
print(platform.python_version())