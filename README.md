# ListMaster – List Comparator Tool

ListMaster is a simple desktop application built with Python and Tkinter that allows you to compare two text files and quickly identify common and unique items.

This tool is designed for fast data processing, cleaning, and automation tasks.

---

## 🚀 Features

- Compare two text files line by line
- Detect:
  - Common items (present in both files)
  - Different items (unique values)
- Automatic saving of results to output files
- Real-time progress indicator (percentage)
- Simple GUI – one-click execution

---

## 📁 File Structure

Place the following files in the same folder as the script:

- `List1.txt` – first dataset  
- `List2.txt` – second dataset  
- `Same.txt` – common items output  
- `Different.txt` – unique items output  

---

## ▶️ How to Use

1. Open `List1.txt` and `List2.txt`
2. Add your data (one item per line)
3. Run the program:
   ```bash
   python main.py
