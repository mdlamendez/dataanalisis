import seaborn as sns # Librería basada en matplotlib para crear gráficos estadísticos -> Altamente compatible con pandas
from ..views import (prepare_plot, render_or_save_plot)
from ..utils import is_numeric_column

def plot_regresion(df, x_column, y_column, config):
    """
    """
    
    is_numeric_column(df, x_column)
    is_numeric_column(df, y_column)

    title = config.get('title', f"Regresión de {x_column} vs {y_column}")
    xlabel = config.get('xlabel', x_column)
    ylabel = config.get('ylabel', y_column)
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    legend = config.get('legend', True)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"{x_column}_{y_column}_regresion.{format}")
    
    sns.lmplot(df, x=x_column, y=y_column) # Este método crea un gráfico de regresión lineal simple entre dos variables numéricas
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha, legend)
    render_or_save_plot(output_dir, filename, format, dpi)
    
    
    
    
    """
    m = pendiente de la recta
    
    m = np.sum((x[i] - x.mean()) * (y[i] - y.mean())) / np.sum((x[i] - x.mean())**2)
    
    """