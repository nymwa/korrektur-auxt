from auxt.expt.result.m2 import M2ResultTableFactory

class EnsembleR2LRerankJobScriptInterface:

    def get_data_bin(self):
        return self.outdir.make_path('data-bin')


class FMEnsembleR2LRerankRunScriptGeneratorInterface:

    def __init__(self):
        super().__init__()
        self.dataset = 'fm'
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid',
                base = self.config['rerank']['r2l_path'])


class CoNLLEnsembleR2LRerankRunScriptGeneratorInterface:

    def __init__(self):
        super().__init__()
        self.dataset = 'wf'
        self.valid_result_table = M2ResultTableFactory().make('wf', 'valid',
                base = self.config['rerank']['r2l_path'])

