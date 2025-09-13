# Limitations

Below are key limitations and peculiarities of the tool:

***

## 1. Use of `--decimate`
- The `--decimate` flag controls how many points are kept from the LAS file.  
  - Example: `--decimate 100` → keeps 1 out of every 100 points (sparse cloud).  
  - Example: `--decimate 15` → keeps 1 out of every 15 points (denser cloud).  
- **Warning:** small values (e.g., 1–20) produce a very large number of points, which can cause the **3D visualization to freeze or fail to load**.  
- The section extraction (CSV) is not affected; the data exports correctly even if the preview does not appear.

***

## 2. Preview vs. Output
- The **3D preview** (using matplotlib) is a visualization tool, not a professional point cloud viewer. It cannot handle hundreds of thousands of points efficiently.  
- For preview, use a larger `--decimate` value (e.g., 50–150).  
- For **maximum accuracy** in the section data (CSV), use a small decimate value (e.g., 1–15) or none at all.  
- Alternatively, the CSV output can be loaded into Excel or GIS software for more detailed analysis.

***

## 3. Performance & Hardware
- On systems with **integrated graphics** (e.g., Intel Graphics), visualization freezes occur more quickly.  
- On **more powerful GPUs** (e.g., NVIDIA), preview may work with many more points.  
- Still, matplotlib is not designed for LAS-level point cloud visualization—professional software like *CloudCompare* is recommended for full visualization.

***

## 4. General Notes
- The program primarily targets **section extraction (sections.csv)**, with preview being secondary.  
- If the 3D preview does not appear, do not worry: the output data is still correct.  
- Future improvements may add a separate `--preview-decimate` parameter to independently control preview resolution and calculation accuracy.

***

This text is ready for direct inclusion in a GitHub README.Here is the English translation and GitHub README-appropriate version of the "Limitations" section for easy copy-pasting:

***

# Limitations

Below are key limitations and peculiarities of the tool:

***

## 1. Use of `--decimate`
- The `--decimate` flag controls how many points are kept from the LAS file.  
  - Example: `--decimate 100` → keeps 1 out of every 100 points (sparse cloud).  
  - Example: `--decimate 15` → keeps 1 out of every 15 points (denser cloud).  
- **Warning:** small values (e.g., 1–20) produce a very large number of points, which can cause the **3D visualization to freeze or fail to load**.  
- The section extraction (CSV) is not affected; the data exports correctly even if the preview does not appear.

***

## 2. Preview vs. Output
- The **3D preview** (using matplotlib) is a visualization tool, not a professional point cloud viewer. It cannot handle hundreds of thousands of points efficiently.  
- For preview, use a larger `--decimate` value (e.g., 50–150).  
- For **maximum accuracy** in the section data (CSV), use a small decimate value (e.g., 1–15) or none at all.  
- Alternatively, the CSV output can be loaded into Excel or GIS software for more detailed analysis.

***

## 3. Performance & Hardware
- On systems with **integrated graphics** (e.g., Intel Graphics), visualization freezes occur more quickly.  
- On **more powerful GPUs** (e.g., NVIDIA), preview may work with many more points.  
- Still, matplotlib is not designed for LAS-level point cloud visualization—professional software like *CloudCompare* is recommended for full visualization.

***

## 4. General Notes
- The program primarily targets **section extraction (sections.csv)**, with preview being secondary.  
- If the 3D preview does not appear, do not worry: the output data is still correct.  
- Future improvements may add a separate `--preview-decimate` parameter to independently control preview resolution and calculation accuracy.
