# 📊 Excel Merger

Merge every Excel file in a folder into **one clean file**, with a column that shows where each row came from.
Built with **Python** and **pandas**.

## Example
Three monthly files in `input/`:

```
input/
├── sales_January.xlsx
├── sales_February.xlsx
└── sales_March.xlsx
```

Run the script and get `merged.xlsx`:

| Product  | Quantity | Price | Source File          |
|----------|---------:|------:|----------------------|
| Pen      | 11       | 0.5   | sales_February.xlsx  |
| Notebook | 6        | 2     | sales_February.xlsx  |
| Bag      | 3        | 15    | sales_February.xlsx  |
| Pen      | 10       | 0.5   | sales_January.xlsx   |
| ...      | ...      | ...   | ...                  |

## How to run
1. Install Python 3, then the libraries:
   ```
   pip install -r requirements.txt
   ```
2. (Optional) Create sample files to try it:
   ```
   python make_samples.py
   ```
3. Put your own `.xlsx` files in the `input` folder, then run:
   ```
   python merge.py
   ```
4. Open `merged.xlsx`.

## Files
- `merge.py`: reads every `.xlsx` in `input/`, adds a **Source File** column, and saves one merged file
- `make_samples.py`: creates three sample sales files for testing
- `requirements.txt`: the libraries needed

---

<div dir="rtl">

## بالعربي
برنامج بلغة Python يدمج كل ملفات Excel الموجودة بمجلد واحد بملف واحد مرتب، ويضيف عمود يبيّن كل سطر من أي ملف جا.

**طريقة التشغيل:** نصّب المكتبات بـ `pip install -r requirements.txt`، حط ملفاتك بمجلد `input`، وشغّل `python merge.py`.

</div>
