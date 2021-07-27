from auxt.expt.result.m2 import M2ResultTableFactory

class FalkoMerlinEnsembleR2LRerankJobScriptInterface:

    def get_data_bin(self):
        return self.outdir.make_path('data-bin')


class FalkoMerlinValidEnsembleR2LRerankJobScriptInterface(
        FalkoMerlinEnsembleR2LRerankJobScriptInterface):
    pass


class FalkoMerlinTestEnsembleR2LRerankJobScriptInterface(
        FalkoMerlinEnsembleR2LRerankJobScriptInterface):
    pass


class FalkoMerlinEnsembleR2LRerankRunScriptGeneratorInterface:

    def __init__(self):
        super().__init__()
        self.dataset = 'fm'
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid',
                base = self.config['rerank']['r2l_path'])

