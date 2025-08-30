from ..path.paths import (
    BOXPLOT_DIR
)

default_boxplot_config = {
    "title": None,
    "orientation": 'h',
    "xlabel": None,
    "ylabel": None,
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "format": "png",
    "dpi": 300,
    "output_dir": BOXPLOT_DIR,
}

ingresos_boxplot_config = {
    **default_boxplot_config,
    "title": "Boxplot de Ingresos Mensuales",
    "orientation": 'v',
    "xlabel": "Ingresos Mensuales",
    "ylabel": "Frecuencia",
    "filename": "ingresos_boxplot.png"
}