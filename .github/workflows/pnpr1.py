import os

print("Hello from Earth.")
token = os.environ.get("THIS_SECRET_QUOTE")
if not token:
  raise RuntimeError("Access Denied. Gg.")
print("The env var was found. Good.")
