import seaborn as sns # Librería basada en matplotlib para crear gráficos estadísticos -> Altamente compatible con pandas
from ..views import (prepare_plot, render_or_save_plot)
from ..utils import is_numeric_column

# Principio Abierto/Cerrado
data = {
    "title": []
}

"""
SOLID

S: Single Responsibility -> Responsabilidad única
O: Open/Closed -> Abierto/Cerrado
L: Liskov Substitution
I: Interface Segregation -> Segregación de interfaces
D: Dependency Inversion
"""
# Este config es un diccionario con la configuración
def plot_histogram(df, column, config): # Los histogramas solo funciona con valores numéricos
    """_summary_

    Args:
        df (_type_): _description_
        column (_type_): _description_
        bins (int, optional): _description_. Defaults to 10.
    """
    
    # Nos aseguramos que la columna sea numérica
    is_numeric_column(df, column)
    
    #configuración del gráfico
    
    bins = config.get('bins', 10)
    kde = config.get('kde', True)
    title = config.get('title', f"Histograma de {column}")
    xlabel = config.get('xlabel', column)
    ylabel = config.get('ylabel', 'frecuencia')
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"histo_{column}.{format}")
    
    
    sns.histplot(df, x=column, bins=bins, kde=kde) # Kernel Density Estimation -> Define la curva de densidad de probabilidad
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha)
    render_or_save_plot(output_dir, filename, format, dpi)






"""
3 tipos de lenguajes de programación:

Compilados: Son los que la maquina entiende de forma directa. El código fuente se traduce a binario (lenguaje de máquina)
    antes de ser ejecutado. C, C++, Rust, Go

Interpretados: Son los que requieren de otro programa (interprete) que traduce el código a un lenguaje de maquina que pueda
    ser entendido en binario. Python, Javascript, PHP, Ruby
                                |
                                |
                            Programa que 
                            instalamos para
                            ejecutar Python
                                |
                                |
                            El programa de Python que instalamos
                            Toma todo nuestro código y lo traduce
                            En ese proceso el llama y ejecuta paquetes
                            y librerías que se esten llamando    
                                |
                                |
                            Reescribe el código en C++ y lo ejecuta
                                
                                
                                
Hibridos: Son lenguajes que al momento de ejecutar el código ellos mismo lo traducen internanmente a binario o a un lenguaje
    intermedio que luego es interpretado. Java, C#, Swift



Lenguajes imperativos y declarativos

imperativos: Son los que ejecutan instrucciones paso a paso -> Python, C, C++, Java, C#, Javascript, PHP

declarativos: Describen un resultado y la maquina (compilador, interprete, motor o gestor de ejecución) se encarga de 
            generar las instrucciones necesarias a bajo nivel -> SQL, CSS, HTML, XML, React, Vue, Angular

"""

