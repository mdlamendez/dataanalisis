def ensure_dir_exists(path):
    """_summary_

    Args:
        path (_type_): _description_
    """
    
    path.mkdir(parents=True, exist_ok=True) # mkdir => make directory, parents => Se asegura y crear todos los directorios padres
                                            # exist_ok -> Si el directorio ya existe lo ignora 

def generete_output_path(path, filename):
    """
    
    Args:
        path (Path): _description_
        filename (str): _description_
    """
    ensure_dir_exists(path)
    return path / filename