# BSON to JSON Converter

A simple Python script to convert **BSON** files to **JSON** using `json_util` from `bson`.  

## Features
- Reads a BSON file (`messages.bson`).
- Converts it to a properly formatted JSON file (`messages.json`).
- Uses `json_util` to ensure BSON-specific types are handled correctly.
- Outputs a structured, indented JSON format.

## Requirements
Ensure you have **Python 3.x** installed and the required dependencies.

### Install Dependencies:
```sh
pip install pymongo
