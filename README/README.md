
# Trench Sections - User Guide

## Purpose of the Program
This program is used to analyze point clouds (LAS files) and create trench sections along an axis.  
This allows easy study of the point distribution and their heights.  
The output consists of:  
- An Excel file (CSV) with the section data.  
- (Optional) A graphical preview (HTML) for quick visual verification.

## Installation

### On Debian / Ubuntu Linux
1. Make sure you have python3 and pip installed:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```
2. Create and activate a virtual environment:
```bash
python3 -m venv trench_env
source trench_env/bin/activate
```
3. Install the required packages:
```bash
pip install laspy pandas matplotlib
```

### On Windows
1. Download and install the latest Python version from [python.org](https://www.python.org/downloads/).  
   - Make sure to check “Add Python to PATH” during installation.
2. Open Command Prompt (cmd).
3. Create a virtual environment:
```cmd
python -m venv trench_env
trench_env\Scripts\activate
```
4. Install the necessary packages:
```cmd
pip install laspy pandas matplotlib
```

## Usage
Run the program with:
```bash
python trench_sections.py --input <file.las> --auto-axis --spacing 0.10 --thickness 0.10 --decimate 100 --out sections.csv --preview
```

### Explanation of Flags
- `--input <file.las>`  
  The point cloud LAS file to analyze.
- `--auto-axis`  
  Automatically selects the section axis (e.g., along the largest axis of the cloud).
- `--spacing <distance>`  
  Distance between sections (e.g., 0.10 = every 10 cm).  
  👉 Smaller spacing = more sections = higher accuracy but heavier processing.
- `--thickness <thickness>`  
  Thickness of each section in meters (e.g., 0.10 = 10 cm).
- `--decimate <percentage>`  
  Reduces the number of points for faster processing.  
  👉 Higher number = fewer points kept (e.g., 100 keeps 1 out of every 100 points).
- `--out <file.csv>`  
  Name of the output CSV file (can be opened in Excel).
- `--preview`  
  Shows a graphical preview of the sections (in a window).

## Output Files
1. `sections.csv` → contains section data (openable with Excel).  
2. `sections_summary.csv` → summary table with information about each section.  
3. (Optional) Preview window with charts.

## Tips
- For higher accuracy → reduce the `--spacing` (e.g., 0.05 instead of 0.10).  
- For faster execution → increase the `--decimate` value.  
- If you want only the Excel output without preview → omit the `--preview` flag.  
- If you want only a quick visual check → keep `--preview` but use a high `--decimate` (e.g., 200).

## Example
```bash
python trench_sections.py --input Skama_fusikou_aeriou_Point_Cloud.las --auto-axis --spacing 0.05 --thickness 0.10 --decimate 50 --out sections.csv --preview
```
👉 This will create the `sections.csv` file with high accuracy (5 cm spacing) and open the preview window.

