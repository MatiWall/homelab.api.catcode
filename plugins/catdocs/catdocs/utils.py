

def create_name(component):
    return f'{component["metadata"].get("system")}.{component["metadata"].get("application")}.{component["metadata"].get("deployableUnit")}'