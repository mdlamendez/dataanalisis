import matplotlib.pyplot as plt
from ..utils import generete_output_path


"""
    -> Patron Abierto/Cerrado -> Las estructuras deben estar abiertas a extensión pero cerradas a modificación
"""

def prepare_plot(
    title=None, 
    xlabel=None, 
    ylabel=None, 
    show_grid=True, 
    linestyle='--', 
    alpha=0.5,
    legend=False
    ):
    
    
    """
    Prepara el gráfico con los parámetros básicos.

    Args:
        title (str, optional): Título del gráfico. Defaults to None.
        xlabel (str, optional): Etiqueta del eje x. Defaults to None.
        ylabel (str, optional): Etiqueta del eje y. Defaults to None.
        show_grid (bool, optional): Mostrar cuadrícula. Defaults to True.
        linestyle (str, optional): Estilo de línea de la cuadrícula. Defaults to '--'.
        alpha (float, optional): Transparencia de la cuadrícula. Defaults to 0.5.
    """
    if title:
        plt.title(title)
    if xlabel: 
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if show_grid:
        plt.grid(True, linestyle=linestyle, alpha=alpha)
    
    plt.tight_layout()

def render_or_save_plot(
    output_dir, 
    filename, 
    format='png', 
    dpi=300):
    
    """_summary_
    """
    if output_dir and filename:
        save_dir = generete_output_path(output_dir, filename)
        plt.savefig(save_dir, format=format, dpi=dpi)
        plt.clf() # Limpia la figura actual para evitar superposiciones en futuros gráficos
    else:
        plt.show()