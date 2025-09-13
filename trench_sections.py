#!/usr/bin/env python3
import argparse
import numpy as np
import pandas as pd

from sections.io import load_las_points
from sections.processing import auto_axis, compute_sections
from sections.visualization import create_3d_html, create_2d_html


def main():
    parser = argparse.ArgumentParser(description="Trench sections & previews")
    parser.add_argument("--input", required=True, help="Input LAS/LAZ file")
    parser.add_argument("--spacing", type=float, default=0.10, help="Section spacing (m)")
    parser.add_argument("--thickness", type=float, default=0.10, help="(unused) slice thickness (m)")
    parser.add_argument("--out", default="sections.csv", help="Output CSV (full points) if no --preview")
    parser.add_argument("--preview", action="store_true", help="Generate previews (and skip huge CSV)")
    parser.add_argument("--decimate", type=int, default=1, help="Decimation factor for 3D preview")
    parser.add_argument("--auto-axis", action="store_true", help="Detect axis with PCA")
    parser.add_argument("--auto-orient", action="store_true",help="Αυτόματη ευθυγράμμιση των αξόνων με PCA.")

    args = parser.parse_args()

    print("[loading LAS file]")
    x, y, z = load_las_points(args.input)

    # axis
    if args.auto_axis:
        start, end = auto_axis(x, y)
    else:
        start = np.array([x.min(), y.min()], dtype=float)
        end   = np.array([x.max(), y.max()], dtype=float)

    # sections dataframe
    df = compute_sections(x, y, z, start, end, args.spacing)

    # summary
    summary = (
        df.groupby("section_id", as_index=False)
          .agg(count=("z", "size"),
               z_min=("z", "min"),
               z_max=("z", "max"),
               x_min=("dist_off", "min"),
               x_max=("dist_off", "max"))
    )
    summary.to_csv("sections_summary.csv", index=False)
    print(f"[saved summary CSV: sections_summary.csv]  (sections={len(summary)})")

    # save full CSV
    if not args.preview:
        print(f"[saving CSV full data] {args.out}")
        df.to_csv(args.out, index=False)

    # previews
    if args.preview:
        print("[generating 3D preview with Plotly]")
        create_3d_html(df, args.decimate)

        print("[generating 2D preview with light updates]")
        create_2d_html(df)

if __name__ == "__main__":
    main()
