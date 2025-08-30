import seaborn as sns
from ..views import (prepare_plot, render_or_save_plot)



def plot_heatmap(df, config):
    """
    
    """
    
    title = config.get('title', 'Heatmap')
    annot= config.get('annot', True)
    numeric_only = config.get('numeric_only', True)
    xlabel = config.get('xlabel', 'Columnas')
    ylabel = config.get('ylabel', 'Columnas')
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', 'heatmap.' + format)
    
    if numeric_only:
        sns.heatmap(df.corr(numeric_only=True), annot=annot)
    else:
        sns.heatmap(df.corr(), annot=annot)
    
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha)
    render_or_save_plot(output_dir, filename, format, dpi)
    


"""
Los valores del gráfico de calor se obtiene a partir del coeficiente de Pearson

+1 -> Correlación positiva perfecta

~0.8 -> Correlación positiva fuerte

~0.5 -> Correlación positiva moderada

~0.2 -> Correlación positiva débil

~0 -> No correlación lineal

~ -0.2 -> Correlación negativa débil

~ -0.5 -> Correlación negativa moderada

~ -0.8 -> Correlación negativa fuerte

-1 -> Correlación negativa perfecta

"""