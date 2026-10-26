
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"

print("Project directory:", PROJECT_DIR)
print("Raw data directory:", RAW_DIR)

if not RAW_DIR.exists():
    print("ERROR: The raw data directory does not exist.")
else:
    files = list(RAW_DIR.rglob("*"))

    print("\nFiles found:")

    for file_path in files:
        if file_path.is_file():
            print(
                f"Name: {file_path.name} | "
                f"Size: {file_path.stat().st_size:,} bytes"
            )

    if not any(path.is_file() for path in files):
        print("No files found. Please download the dataset first.")
