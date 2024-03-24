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

def rm_folder(root: Path):

    for p in root.iterdir():
        if p.is_dir():
            rm_folder(p)
        else:
            p.unlink()

    root.rmdir()
