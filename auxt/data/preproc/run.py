from auxt.script.run import RunScript

class PreprocRunScript(RunScript):
    def __init__(self, script_list, first=False):
        self.first = first
        super().__init__(script_list)

    def make_path(self):
        if self.first:
            path = 'first_preprocess.sh'
        else:
            path = 'preprocess.sh'
        return path

