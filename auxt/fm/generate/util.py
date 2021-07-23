from pathlib import Path
from auxt.expt.result.m2 import M2ResultTableFactory

class FalkoMerlinValidGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'fm-valid' / 'data-bin'
        return str(path.resolve())


class FalkoMerlinTestGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'fm-test' / 'data-bin'
        return str(path.resolve())


class FalkoMerlinGenerationRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'fm'
        super().__init__()


class ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface(
        FalkoMerlinGenerationRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid')
        super().__init__()

