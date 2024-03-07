from pathlib import Path
def create_folders_if_not_exist(path):
    """
    Create folders from a given path if they do not exist.

    Args:
        path (str): The path for which folders need to be created.
    """
    try:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        print(f"Folders created at path: {path}")
    except Exception as e:
        print(f"Failed to create folders at path: {path}. Error: {e}")
