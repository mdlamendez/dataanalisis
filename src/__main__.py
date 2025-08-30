from eda.utils import ( load_csv )
from eda.data_processing import (
    show_info,
    show_head,
    count_duplicates,
    count_missing_values
)

from eda.analysis import (
    central_tendency,
    dispersion_measures
)

from eda.views import (
    plot_factory
)

from eda.config import (
    ingresos_histogram_config,
    default_boxplot_config,
    ingresos_boxplot_config,
    default_scatter_config,
    default_heatmap_config,
    default_regression_config
)

def main():

    df = load_csv("data/raw/clientes_tienda.csv")
    
    
    #IDA
    show_info(df)
    
    print(" ")
    print("Primeros 20 registros del dataFrame: ")
    print(show_head(df, 20))

    
    print("=" * 50)
    print("Conteo de duplicados: ", count_duplicates(df))
    
    print("=" * 50)
    print("Conteo de valores nulos por Coulumnas: ")
    print(count_missing_values(df))
    
    #EDA
    print('#' * 50)
    print("tendencias de ingresos mensauales")
    print('#' * 50)
    tendency_ingresos = central_tendency(df, "IngresosMensuales")
    print("Promedio de ingresos: " , tendency_ingresos["promedio"])
    print("Mediana de ingresos: " , tendency_ingresos["mediana"])
    print("Moda de ingresos: " , tendency_ingresos["moda"])
    
    
    print('#' * 50)
    print("Dispersión de ingresos Mensuales")
    print('#' * 50)
    dispersion_ingresos = dispersion_measures(df, "IngresosMensuales")
    print("Desvición estandar: ", dispersion_ingresos["des_std"])
    print("Rango: ", dispersion_ingresos["rango"])
    print("Coeficiente de variación: ", f"{dispersion_ingresos['coef_var']}%")
    
    print('#' * 50)
    print("Histograma de Ingresos Mensuales")
    
    plot_factory(df, "histogram", "IngresosMensuales", ingresos_histogram_config)
    plot_factory(df, "boxplot", "IngresosMensuales", ingresos_boxplot_config)
    plot_factory(df, "boxplot", "Edad", default_boxplot_config)
    plot_factory(df, "scatter", ("Edad", "FrecuenciaCompraMensual"), default_scatter_config)
    plot_factory(df, "heatmap", None, default_heatmap_config)
    plot_factory(df, "regression", ("IngresosMensuales", "FrecuenciaCompraMensual"), default_regression_config)
    
    
    #Quiero certificado de Buen compañero de Priscila Maureira
    
    # Nombre -> El tipo de certificados -> config: border: gold
    # Factory -> Recibe el nombre, el tipo y el config
    #       -> El tipo llama a una función que recibe el nombre y el config  (con el certificado especifico)
    #       -> La función crea el certificado y lo guarda en una carpeta específica o renderice

    
    # Funciones para emitir certificados
    # 1. Crear una función general que arma certificados no especificos
    # 2. Crear funciones especificas a partir de la general para cada tipo de certificado
    # 3. El factory
    
    
    
if __name__ == "__main__":
    main()