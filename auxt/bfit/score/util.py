from auxt.expt.result.m2 import M2ResultTableFactory

class FMValidScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FMTestScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['fm']['test_m2']


class CoNLLValidScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['wf']['valid_m2']


class CoNLLTestScoreJobScriptInterface:

    def reference_path(self):
        return self.eval_config['wf']['test_m2']


class FMScoreRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'fm'
        super().__init__()


class CoNLLScoreRunScriptGeneratorInterface:

    def __init__(self):
        self.dataset = 'wf'
        super().__init__()


class ValidatedFMScoreRunScriptGeneratorInterface(
        FMScoreRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid')
        super().__init__()


class ValidatedCoNLLScoreRunScriptGeneratorInterface(
        CoNLLScoreRunScriptGeneratorInterface):

    def __init__(self):
        self.valid_result_table = M2ResultTableFactory().make('wf', 'valid')
        super().__init__()

