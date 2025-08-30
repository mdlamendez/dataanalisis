from ..path.paths import (
    REGRESSION_DIR
)

default_regression_config = {
    "title": None,
    "xlabel": None,
    "ylabel": None,
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "legend": True,
    "format": "png",
    "dpi": 300,
    "output_dir": REGRESSION_DIR,
}

default_regression_config["filename"] = f"regresion_lineal.{default_regression_config['format']}"
