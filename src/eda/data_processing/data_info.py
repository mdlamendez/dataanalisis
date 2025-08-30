

def show_info(df): #Voy a mandar un data frame, por ende, viene con los métodos de pandas
    """_summary_
    
    
    """
    
    df.info() # Esto tenemos que asegurar que no explote -> Try Except
    

def show_head(df, number=5):
    """_summary_

    Args:
        df (_type_): _description_
        number (int, optional): _description_. Defaults to 10.
    """
    
    return df.head(number)


def count_duplicates(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    
    return df.duplicated().sum() # Duplicated siempre devuelve siempre un número

def count_missing_values(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    
    return df.isnull().sum() # isNull siempre devuelve un número

def show_tails(df, number=10):
    """_summary_

    Args:
        df (_type_): _description_
        number (int, optional): _description_. Defaults to 10.
    """
    
    df.tail(number)

def get_columns_list(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    
    return df.columns.tolist()