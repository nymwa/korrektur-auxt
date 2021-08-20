from pathlib import Path
from auxt.expt.result.m2 import M2ResultTableFactory

class FMValidGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'fm-valid' / 'data-bin'
        return str(path.resolve())


class FMTestGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'fm-test' / 'data-bin'
        return str(path.resolve())


class CoNLLValidGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'wf-valid' / 'data-bin'
        return str(path.resolve())


class CoNLLTestGenerationJobScriptInterface:

    def get_data_bin(self):
        path = Path(self.config['data']) / 'wf-test' / 'data-bin'
        return str(path.resolve())


class FMGenerationRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'fm'
        super().__init__()


class CoNLLGenerationRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'wf'
        super().__init__()


class ValidatedFMGenerationRunScriptGeneratorInterface(
        FMGenerationRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid')
        super().__init__()


class ValidatedCoNLLGenerationRunScriptGeneratorInterface(
        CoNLLGenerationRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('wf', 'valid')
        super().__init__()

