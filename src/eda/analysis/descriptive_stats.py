from ..utils import is_numeric_column


def describe_data(df, include='all', exclude=None): # df -> DataFrame -> Estructura propia de Pandas
    """_summary_

    Args:
        df (_type_): _description_
        include (str, optional): _description_. Defaults to 'all'.
        exclude (_type_, optional): _description_. Defaults to None.
    """
    
    return df.describe(include=include, exclude=exclude) # Devuelve un DataFrame con las estadísticas descriptivas de las columnas numéricas y categóricas del DataFrame original


def mean_column(df, column_name):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    return df[column_name].mean()

def median_column(df, column_name):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    return df[column_name].median()


def mode_column(df, column_name):
    """_summary_
        Determina la moda de una columna especifica de un DataFrame. No válida si la columna es númerica
    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    return df[column_name].mode()[0]  # mode() devuelve una Serie, tomamos el primer valor


def central_tendency(df, column_name): 
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    
    is_numeric_column(df, column_name)
    return {
        "promedio": mean_column(df, column_name),
        "mediana": median_column(df, column_name),
        "moda": mode_column(df, column_name)
    }

def standard_variation(df, column_name):
    """
    
    """
    
    return df[column_name].std()

def range_column(df, column_name):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    return df[column_name].max() - df[column_name].min()

def coeficient_variation(df, column_name, mean=0, std=0): # El coeficiente de variación -> Depende del promedio y de la desviación estandar
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    
    mean_calculated = mean
    std_calculated = std
    
    if mean_calculated == 0 or std_calculated == 0:
        mean_calculated = mean_column(df, column_name)
        std_calculated = standard_variation(df, column_name)
    
    coeficient_variation = (std_calculated / mean_calculated * 100) if mean_calculated != 0 else float('inf') #Operador Ternario
    return coeficient_variation
    
# operador ternario -> Solo lo debo ocupar si la condición tiene dos salidas, verdadero o falso. No aplicar para condiciones
# complejas o anidadas -> No es que no se pueda, es que no es legible


def dispersion_measures(df, column_name):
    """_summary_

    Args:
        df (_type_): _description_
        column_name (_type_): _description_
    """
    
    is_numeric_column(df, column_name)
    return {
        "rango": range_column(df, column_name),
        "des_std": standard_variation(df, column_name),
        "coef_var": coeficient_variation(df, column_name)
    }