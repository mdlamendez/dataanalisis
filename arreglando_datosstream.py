import pandas as pd
from datetime import datetime
from datetime import datetime 
from src.eda.utils import ( load_csv )
from src.eda.utils import ( 
    load_csv, 
    select_columns_df 
)

col_select = [0,1, 2,3,4,5,6,7,8,10,11,16,29,30,32,36]
df_temp = load_csv("/home/mmendez/dataanalisis/data/raw/streamstats/twitch_stats.csv")
df_tofilter = select_columns_df(df_temp, col_select)
df = df_tofilter[df_tofilter['Minutos de emisión'] > 0] 

dfb = df.copy()
dates = []
dias = []
meses = []
anno = []
diasemana = []
fechas_temp = dfb["Fecha"]

for i in fechas_temp:
    dia=datetime.strptime(i, "%a %b %d %Y")
    dias.append(dia.day)
    diasemana.append(dia.weekday())
    meses.append(dia.month)
    anno.append(dia.year)
    dates.append(dia)
dfb["dates"] = pd.to_datetime(dates)
dfb["dias"] = dias
dfb["daysofweek"] = diasemana
dfb["meses"] = meses
dfb["años"] = anno
dfb["Retencion"]  = (dfb["Minutos visualizados"] / dfb["Minutos de emisión"])
dfb["poremicion"] = ( dfb["Minutos de emisión"]/dfb["Minutos visualizados"] )
dfb["horas_emitidas"] = dfb["Minutos de emisión"]/60
dfb["horas_visualizadas"] = dfb["Minutos visualizados"]/60
    

dfb.to_csv("/home/mmendez/dataanalisis/data/processed/twitchstats/data_procesada.csv")