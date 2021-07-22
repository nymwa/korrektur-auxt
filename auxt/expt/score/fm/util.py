from auxt.expt.result.m2 import M2ResultTableFactory

class FalkoMerlinValidScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FalkoMerlinTestScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['fm']['test_m2']


class FalkoMerlinScoreRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'fm'
        super().__init__()


class ValidatedFalkoMerlinScoreRunScriptGeneratorInterface(
        FalkoMerlinScoreRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid')
        super().__init__()

