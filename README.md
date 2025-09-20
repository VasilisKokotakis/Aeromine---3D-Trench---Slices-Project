

# Trench Sections & Previews

**Project for Aeromine** – All rights reserved by Aeromine

This project is the **first phase** of a program designed to process 3D trench survey data (LAS/LAZ point clouds), compute cross-sections, and generate both CSV outputs and interactive previews. Future development will expand its features and enhance usability.

---

## Features

* Load 3D point cloud data from LAS/LAZ files.
* Compute cross-sections along a user-defined or automatically detected axis (via PCA).
* Export full point data as CSV (`sections.csv`) or section summaries (`sections_summary.csv`).
* Generate interactive previews:

  * **3D preview** using Plotly
  * **2D per-section preview** with adjustable Z and X ranges, including live metrics
* Decimation options to improve rendering performance for large datasets.

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/VasilisKokotakis/Aeromine---3D-Trench---Slices-Project.git
cd Aeromine---3D-Trench---Slices-Project
```

2. Install dependencies (Python 3.10+ recommended):

```bash
pip install -r requirements.txt
```

**Dependencies include:**

* `numpy`
* `pandas`
* `laspy`
* `plotly`
* `scikit-learn`

---

## Usage

Basic command-line usage:

```bash
python main.py --input path/to/file.las --spacing 0.1 --preview
```

### Arguments

* `--input`: Path to the input LAS/LAZ file (**required**)
* `--spacing`: Distance between cross-sections in meters (default `0.10`)
* `--thickness`: Slice thickness in meters (currently unused, default `0.10`)
* `--out`: CSV output path for full point data (default `sections.csv`)
* `--preview`: Generate interactive 2D/3D previews instead of full CSV
* `--decimate`: Decimation factor for 3D preview (default `1`)
* `--auto-axis`: Automatically detect trench axis using PCA
* `--auto-orient`: Automatically orient axes (experimental)

---

## Output

* **`sections_summary.csv`** – Summary per section including point counts, min/max elevations, and offsets
* **`sections.csv`** – Full points with computed distances and section IDs (if `--preview` is not used)
* **`sections_3d.html`** – Interactive 3D visualization
* **`sections_2d.html`** – Interactive 2D visualization with per-section adjustments

---

## Development & Future Work

This is the **first phase** of the Aeromine trench processing program. Future enhancements will include:

* Advanced filtering and decimation methods for very large point clouds
* Enhanced 2D/3D visualization features
* User-friendly GUI for offline and online workflows
* Automated reporting and integration with Aeromine systems

---

## License

All rights reserved by **Aeromine**. This repository and its contents are the property of Aeromine.

---

## Contact

For questions or collaboration, please contact the Aeromine team (https://www.aeromine.info/) . 

