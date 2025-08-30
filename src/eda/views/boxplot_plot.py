import seaborn as sns # Librería basada en matplotlib para crear gráficos estadísticos -> Altamente compatible con pandas
from .base_plot import (prepare_plot, render_or_save_plot)
from ..utils import is_numeric_column

data = {
    "title": []
}


def plot_boxplot(df, column, config): 
    """
    Crea un boxplot para la columna especificada de un DataFrame
    Args:
        df (_dict_): DataFrame con los datos.
        column (_string_): nombre de la columna a graficar. -> Recibo el nombre como string -> La columna debe ser numérica
        config (_dict_): Diccionario con la configuración del gráfico
    
    Returns: 
        None: Muestra el gráfico o lo guarda en un archivo.
    """
    
    is_numeric_column(df, column)
    
    #configuración del gráfico
    title = config.get('title', f"Histograma de {column}")
    orientation = config.get('orientation', 'h')
    xlabel = config.get('xlabel', column)
    ylabel = config.get('ylabel', 'frecuencia')
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"{column}_boxplot.{format}")
    
    sns.boxplot(df, x=column, orient=orientation)
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha)
    render_or_save_plot(output_dir, filename, format, dpi)