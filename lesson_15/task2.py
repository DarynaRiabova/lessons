import json
import logging
from pathlib import Path

logging.basicConfig(
    filename="json_ryabova.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

folder = Path("ideas_for_test/work_with_json")

for file in folder.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON file: {file.name}. Error: {e}")