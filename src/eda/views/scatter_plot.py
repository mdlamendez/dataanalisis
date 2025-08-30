import seaborn as sns
from ..views import (prepare_plot, render_or_save_plot)
from ..utils import is_numeric_column

def plot_scatter(df, x_column, y_column, config):
    """_summary_

    Args:
        df (_type_): _description_
        x_column (_type_): _description_
        y_column (_type_): _description_
        config (_type_): _description_
    """
    
    is_numeric_column(df, x_column)
    is_numeric_column(df, y_column)
    
    title = config.get('title', f"dispersión de {x_column} vs {y_column}")
    xlabel = config.get('xlabel', x_column)
    ylabel = config.get('ylabel', y_column)
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"{x_column}_{y_column}_scatter.{format}")
    
    sns.scatterplot(df, x=x_column, y=y_column)
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha)
    render_or_save_plot(output_dir, filename, format, dpi)
    