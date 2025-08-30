import pandas as pd
from src.eda.utils import ( load_csv )
from datetime import datetime 
from src.eda.data_processing import (
    show_info,
    show_head,
    count_duplicates,
    count_missing_values
)

df = load_csv("/home/mmendez/intropython/proyecto/data/processed/data_procesada.csv")
    
    #IDA
#show_info(df)
#print(show_head(df, 20))
col_select = [0,1, 2,3,4,5,6,7,8,10,11,16,29,30,32,36]
df = df.iloc[:,col_select]
print(df.info())

dates = []
dias = []
meses = []
anno = []
fechas_temp = df["Fecha"]
for i in fechas_temp:
    dia=  datetime.strptime(i, "%a %b %d %Y")
    dates.append(dia)
    dias.append(dia.day)
    meses.append(dia.month)
    anno.append(dia.year)
    
df["dates"] = pd.to_datetime(dates)
