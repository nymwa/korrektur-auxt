from pathlib import Path

class BaseDir:

    def __init__(self, base = None):
        if base is None:
            self.base = Path('.')
        else:
            self.base = Path(base)

    def make_dir_path(self):
        return ''

    def make_path(self, file_name = None):
        if file_name is None:
            path = self.base / self.make_dir_path()
        else:
            path = self.base / self.make_dir_path() / file_name
        return str(path.resolve())

