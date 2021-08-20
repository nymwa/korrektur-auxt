class EnsembleReprocJobScriptInterface:

    def make_output_yaml_path(self):
        return self.outdir.make_path('../output.yaml')

    def make_false_source_output_path(self):
        return self.outdir.make_path('false.src')

    def make_false_target_output_path(self):
        return self.outdir.make_path('false.trg')

    def make_false_pref_path(self):
        return self.outdir.make_path('false')


class ValidEnsembleReprocJobScriptInterface:

    def make_tsv_path(self):
        return self.outdir.make_path('valid.tsv')

    def make_source_path(self):
        return self.outdir.make_path('valid.src')

    def make_target_path(self):
        return self.outdir.make_path('valid.trg')

    def make_test_pref(self):
        return self.outdir.make_path('valid')


class TestEnsembleReprocJobScriptInterface:

    def make_tsv_path(self):
        return self.outdir.make_path('test.tsv')

    def make_source_path(self):
        return self.outdir.make_path('test.src')

    def make_target_path(self):
        return self.outdir.make_path('test.trg')

    def make_test_pref(self):
        return self.outdir.make_path('test')


class FMEnsembleReprocJobScriptInterface(EnsembleReprocJobScriptInterface):

    def get_false_source_input_path(self):
        return self.eval_config['fm']['false_bpe_src']

    def get_false_target_input_path(self):
        return self.eval_config['fm']['false_bpe_trg']


class CoNLLEnsembleReprocJobScriptInterface(EnsembleReprocJobScriptInterface):

    def get_false_source_input_path(self):
        return self.eval_config['wf']['false_bpe_src']

    def get_false_target_input_path(self):
        return self.eval_config['wf']['false_bpe_trg']


class FMValidEnsembleReprocJobScriptInterface(
        ValidEnsembleReprocJobScriptInterface,
        FMEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['fm']['valid_bpe_src']


class FMTestEnsembleReprocJobScriptInterface(
        TestEnsembleReprocJobScriptInterface,
        FMEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['fm']['test_bpe_src']


class CoNLLValidEnsembleReprocJobScriptInterface(
        ValidEnsembleReprocJobScriptInterface,
        CoNLLEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['wf']['valid_bpe_src']


class CoNLLTestEnsembleReprocJobScriptInterface(
        TestEnsembleReprocJobScriptInterface,
        CoNLLEnsembleReprocJobScriptInterface):

    def get_source_input_path(self):
        return self.eval_config['wf']['test_bpe_src']

