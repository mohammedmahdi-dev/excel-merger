import pandas as pd
from pathlib import Path

input_folder = Path("input")
output_file = Path("merged.xlsx")

all_tables = []

for file in sorted(input_folder.glob("*.xlsx")):
    df = pd.read_excel(file)
    df["Source File"] = file.name
    all_tables.append(df)
    print("Read", file.name, "-", len(df), "rows")

if not all_tables:
    print("No Excel files found in", input_folder)
else:
    merged = pd.concat(all_tables, ignore_index=True)
    merged.to_excel(output_file, index=False)
    print("Done! Saved", len(merged), "rows to", output_file)
