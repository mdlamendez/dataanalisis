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

df = load_csv("/home/mmendez/dataanalisis/data/processed/twitchstats/data_procesada.csv")
show_info(df)
tendency_espectadores = central_tendency(df, "Espectadores máximos")
print("Promedio de visualizaciones: " , tendency_espectadores["promedio"])
print("Mediana de visualizaciones: " , tendency_espectadores["mediana"])
print("Moda de visualizaciones: " , tendency_espectadores["moda"])
print("Maximo de espectadores: ", df["Espectadores máximos"].max())
print("Minutos de emisión:", df["Minutos de emisión"].mean())
print("Minutos de visualización:", df["Minutos visualizados"].mean())