class FalkoMerlinValidEnsembleReprocJobScriptInterface:

    def input_path(self):
        return self.eval_config['fm']['valid_bpe_src']


class FalkoMerlinTestEnsembleReprocJobScriptInterface:

    def input_path(self):
        return self.eval_config['fm']['test_bpe_src']

