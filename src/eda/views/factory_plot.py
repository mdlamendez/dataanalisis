from .histogram_plot import plot_histogram
from .boxplot_plot import plot_boxplot
from .scatter_plot import plot_scatter
from .heatmap_plot import plot_heatmap
from .regresion_plot import plot_regresion

PLOT_DISPATCHER = {
    "histogram": plot_histogram,
    "boxplot": plot_boxplot,
    "scatter": plot_scatter,
    "heatmap": plot_heatmap,
    "regression": plot_regresion
}
# Esto lo vamos a crear con programación funcional -> Los ejemplos se suelen hacer con POO pero es aplicable a muchos paradigmas
def plot_factory(df, plot_type, column_or_columns, config):
    """_summary_

    Args:
        df (_type_): _description_
        plot_type (_type_): _description_
        column (_type_): _description_
        config (_type_): _description_
    """
    
    if plot_type not in PLOT_DISPATCHER:
        raise ValueError(f"Tipo de gráfico no soportado: {plot_type}")
    
    plot_function = PLOT_DISPATCHER[plot_type]
    
    if plot_type in ["histogram", "boxplot"]:
        plot_function(df, column=column_or_columns, config=config)
    elif (column_or_columns is None) and plot_type == "heatmap": 
        plot_function(df, config=config) 
    else: 
        x_column, y_column = column_or_columns # Asumiendo que esto es una lista o tupla con dos elementos
        plot_function(df, x_column=x_column, y_column=y_column, config=config)