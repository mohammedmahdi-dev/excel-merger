import pandas as pd
from pathlib import Path

folder = Path("input")
folder.mkdir(exist_ok=True)

months = ["January", "February", "March"]

for i, month in enumerate(months):
    data = {
        "Product": ["Pen", "Notebook", "Bag"],
        "Quantity": [10 + i, 5 + i, 2 + i],
        "Price": [0.5, 2.0, 15.0],
    }
    df = pd.DataFrame(data)
    df.to_excel(folder / f"sales_{month}.xlsx", index=False)
    print("Created", month)
