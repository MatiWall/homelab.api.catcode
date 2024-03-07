


class _Cache:

    def __init__(self):
        self.components = {}

    def add(self, comp):
        self.components[comp.name] = comp
        return True

    def remove(self, comp: str):
        del self.components[comp]
        return True

cache = _Cache()