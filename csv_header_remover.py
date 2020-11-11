import os

os.makedirs("header_removed", exist_ok=True)

for file in os.listdir("."):
    if file.endswith(".csv"):
        print("Removing header from: " + file + "...")
