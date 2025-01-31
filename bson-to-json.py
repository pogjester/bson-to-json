from bson import json_util
import json

# Read BSON file
with open("messages.bson", "rb") as f:
    bson_data = f.read()

# Convert to JSON using json_util
json_data = json_util.dumps(bson_data, indent=4)

# Save JSON output
with open("messages.json", "w") as f:
    f.write(json_data)

print("BSON converted to JSON successfully!")

