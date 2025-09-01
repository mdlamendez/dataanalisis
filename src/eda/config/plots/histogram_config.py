from ..path.paths import (
    HISTOGRAM_DIR
)

default_histogram_config = {
    "bins": 10,
    "kde": True,
    "title": None,
    "xlabel": None,
    "ylabel": None,
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "format": "png",
    "dpi": 300,
    "output_dir": HISTOGRAM_DIR,
}


ingresos_histogram_config = {
    **default_histogram_config,
    "title": "Histograma de Ingresos Mensuales",
    "bins": 20,
    "xlabel": "Ingresos Mensuales",
    "ylabel": "Compras",
    "linestyle": "dashdot",
    "output_dir": HISTOGRAM_DIR,
    "filename": "ingresos_histogram.png"
}

