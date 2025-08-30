from .plots.histogram_config import (
    default_histogram_config,
    ingresos_histogram_config,
)

from .plots.boxplot_config import (
    default_boxplot_config,
    ingresos_boxplot_config
)

from .plots.scatter_config import (
    default_scatter_config
)

from .plots.heatmap_config import (
    default_heatmap_config
)

from .plots.regression_config import (
    default_regression_config
)

from .path.paths import (
    ROOT_DIR,
    RESULT_DIR,
    PLOTS_DIR,
    HISTOGRAM_DIR,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR
    
)


__all__ = [
    "default_histogram_config",
    "ingresos_histogram_config",
    "default_boxplot_config",
    "ingresos_boxplot_config",
    "default_scatter_config",
    "default_heatmap_config",
    "default_regression_config",
    "ROOT_DIR",
    "RESULT_DIR",
    "PLOTS_DIR",
    "HISTOGRAM_DIR",
    "DATA_DIR",
    "RAW_DATA_DIR",
    "PROCESSED_DATA_DIR"
]