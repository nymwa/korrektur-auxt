class FalkoMerlinEnsembleReprocJobScriptInterface:

    def make_output_yaml_path(self):
        return self.outdir.make_path('../output.yaml')

    def get_false_source_input_path(self):
        return self.eval_config['fm']['false_bpe_src']

    def get_false_target_input_path(self):
        return self.eval_config['fm']['false_bpe_trg']

    def make_false_source_output_path(self):
        return self.outdir.make_path('false.src')

    def make_false_target_output_path(self):
        return self.outdir.make_path('false.trg')

    def make_false_pref_path(self):
        return self.outdir.make_path('false')


class FalkoMerlinValidEnsembleReprocJobScriptInterface(
        FalkoMerlinEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['fm']['valid_bpe_src']

    def make_tsv_path(self):
        return self.outdir.make_path('valid.tsv')

    def make_source_path(self):
        return self.outdir.make_path('valid.src')

    def make_target_path(self):
        return self.outdir.make_path('valid.trg')

    def make_test_pref(self):
        return self.outdir.make_path('valid')


class FalkoMerlinTestEnsembleReprocJobScriptInterface(
        FalkoMerlinEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['fm']['test_bpe_src']

    def make_tsv_path(self):
        return self.outdir.make_path('test.tsv')

    def make_source_path(self):
        return self.outdir.make_path('test.src')

    def make_target_path(self):
        return self.outdir.make_path('test.trg')

    def make_test_pref(self):
        return self.outdir.make_path('test')

