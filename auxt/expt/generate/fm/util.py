from auxt.expt.result.m2 import M2ResultTableFactory

class FalkoMerlinValidGenerationJobScriptInterface:

    def get_input_path(self):
        return self.eval_config['fm']['valid_bpe_src']


class FalkoMerlinTestGenerationJobScriptInterface:

    def get_input_path(self):
        return self.eval_config['fm']['test_bpe_src']


class FalkoMerlinGenerationRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'fm'
        super().__init__()


class ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface(
        FalkoMerlinGenerationRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid')
        super().__init__()

