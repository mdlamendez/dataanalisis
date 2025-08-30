import pandas as pd

def load_csv(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_
    """
    
    return pd.read_csv(file_path) # Siempre devuelve un DataFrame


def load_excel(file_path):
    """_summary_

    Args:
        file_path (_type_): _description_
    """
    
    return pd.read_excel(file_path)


def select_columns_df(df, columns_index):
    """_summary_

    Args:
        file_path (_type_): _description_
    """
    df_cut  = df.iloc[:,columns_index]
    return df_cut