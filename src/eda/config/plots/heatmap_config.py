from ..path.paths import (
    HEATMAP_DIR
)

default_heatmap_config = {
    "title": None,
    "numeric_only": True,
    "annot": True,
    "xlabel": None,
    "ylabel": None,
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "format": "png",
    "dpi": 300,
    "output_dir": HEATMAP_DIR,
}
