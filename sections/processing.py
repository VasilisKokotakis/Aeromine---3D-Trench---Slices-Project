import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def auto_axis(x, y):
    xy = np.vstack((x, y)).T
    pca = PCA(n_components=2)
    pca.fit(xy)
    v = pca.components_[0] / np.linalg.norm(pca.components_[0])
    ctr = xy.mean(axis=0)
    start = ctr - v * 10.0
    end   = ctr + v * 10.0
    print(f"[auto-axis] start=({start[0]}, {start[1]}), end=({end[0]}, {end[1]})")
    return start, end

def compute_sections(x, y, z, start, end, spacing):
    axis_vec = end - start
    axis_vec = axis_vec / np.linalg.norm(axis_vec)
    rel = np.vstack((x - start[0], y - start[1])).T
    along = rel @ axis_vec
    off   = rel @ np.array([-axis_vec[1], axis_vec[0]])
    section_id = np.floor(along / spacing).astype(int)
    df = pd.DataFrame(
        {"x": x, "y": y, "z": z,
         "dist_along": along, "dist_off": off, "section_id": section_id}
    )
    return df
