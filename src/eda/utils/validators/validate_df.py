
def is_numeric_column(df, column_name):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    
    if column_name not in df.columns:
        raise ValueError(f'La columna "{column_name}" no existe en el DataFrame.')
    
    if not df[column_name].dtype in ['int64', 'float64']:
        raise TypeError(f'La columna "{column_name}" debe ser numérica para calcular la media.')

    return True