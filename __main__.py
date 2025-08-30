import pandas as pd
import datetime
from src.eda.utils import ( 
    load_csv, 
    select_columns_df 
)
from src.eda.data_processing import (
    show_info,
    show_head,
    count_duplicates,
    count_missing_values
)

from src.eda.analysis import (
    central_tendency,
    dispersion_measures
)

from src.eda.views import (
    plot_factory
)

from src.eda.config import (
    default_histogram_config,
    default_boxplot_config,
    default_scatter_config,
    default_heatmap_config,
    default_regression_config
)

def main():
    
    
    df = load_csv("/home/mmendez/dataanalisis/data/processed/twitchstats/data_procesada.csv")
    
   
    show_info(df)
    
    print(" ")
    print("Primeros 5 registros del dataFrame: ")
    print(show_head(df, 5))

    
    print("=" * 50)
    print("Conteo de duplicados: ", count_duplicates(df))
    
    print("=" * 50)
    print("Conteo de valores nulos por Columnas: ")
    print(count_missing_values(df))
    
    #EDA
    print('#' * 50)
    print("Tendencias de visualizaciones")
    print('#' * 50)
    #define la variable observada
    tendency_visualizaciones = central_tendency(df, "Minutos visualizados")
    print("Promedio de visualizaciones: " , tendency_visualizaciones["promedio"])
    print("Mediana de visualizaciones: " , tendency_visualizaciones["mediana"])
    print("Moda de visualizaciones: " , tendency_visualizaciones["moda"])
    print("Maximo de espectadores: ", df["Espectadores máximos"].max())
    print(type(df["Fecha"]))

    print('#' * 50)
    print("Dispersión de visualizaciones")
    print('#' * 50)
    dispersion_minvis = dispersion_measures(df, "Minutos visualizados")
    print("Desvición estandar: ", dispersion_minvis["des_std"])
    print("Rango: ", dispersion_minvis["rango"])
    print("Coeficiente de variación: ", f"{dispersion_minvis['coef_var']}%")

    
    plot_factory(df, "regression", ("Minutos de emisión", "Minutos visualizados"), default_regression_config)
    plot_factory(df, "scatter", ("Minutos de emisión", "Minutos visualizados"), default_scatter_config)
    plot_factory(df, "histogram", "poremicion" , default_histogram_config)
    plot_factory(df, "boxplot",  "Retencion" , default_boxplot_config)
    col_select = [2,3,4,5,6,7,11,22,23]
    df_temp = select_columns_df(df, col_select)
    plot_factory(df_temp, "heatmap", None, default_heatmap_config)
    #plot_factory(df, "regression", ( "daysofweek","Minutos visualizados"), default_regression_config)
    

    
    
if __name__ == "__main__":
    main()