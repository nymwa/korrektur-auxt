from auxt.expt.result.m2 import M2ResultTableFactory

class FalkoMerlinEnsembleR2LRescoreJobScriptInterface:

    def get_data_bin(self):
        return self.outdir.make_path('data-bin')


class FalkoMerlinValidEnsembleR2LRescoreJobScriptInterface(
        FalkoMerlinEnsembleR2LRescoreJobScriptInterface):

    pass


class FalkoMerlinTestEnsembleR2LRescoreJobScriptInterface(
        FalkoMerlinEnsembleR2LRescoreJobScriptInterface):
    pass


class FalkoMerlinEnsembleR2LRescoreRunScriptGeneratorInterface:

    def __init__(self):
        super().__init__()
        self.dataset = 'fm'
        self.valid_result_table = M2ResultTableFactory().make('fm', 'valid',
                base = self.config['rescore']['r2l_path'])

