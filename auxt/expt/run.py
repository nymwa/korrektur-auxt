from auxt.script.run import RunScript

class ExptRunScript(RunScript):
    def __init__(self, index, script_list):
        self.index = index
        super().__init__(script_list)

