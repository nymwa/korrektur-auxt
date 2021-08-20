from auxt.script.run import RunScript
from auxt.expt.mlm_rerank.job import EnsembleMLMRerankJobScript
from auxt.generator.run import EnsembleMLMRerankRunScriptGenerator

class FMEnsembleMLMRerankJobScript(EnsembleMLMRerankJobScript):

    def make_is_detokenized(self):
        return self.config['rerank']['fm'].get('detokenize', False)


class CoNLLEnsembleMLMRerankJobScript(EnsembleMLMRerankJobScript):

    def make_is_detokenized(self):
        return self.config['rerank']['wf'].get('detokenize', True)


class FMEnsembleMLMRerankRunScript(RunScript):

    def make_path(self):
        return 'mlm_rerank_fm_ensemble.sh'


class CoNLLEnsembleMLMRerankRunScript(RunScript):

    def make_path(self):
        return 'mlm_rerank_conll_ensemble.sh'


class FMEnsembleMLMRerankRunScriptGenerator(
        EnsembleMLMRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = self.test_job_class = FMEnsembleMLMRerankJobScript
        self.run_class = FMEnsembleMLMRerankRunScript
        super().__init__()


class CoNLLEnsembleMLMRerankRunScriptGenerator(
        EnsembleMLMRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'wf'
        self.valid_job_class = self.test_job_class = CoNLLEnsembleMLMRerankJobScript
        self.run_class = CoNLLEnsembleMLMRerankRunScript
        super().__init__()


def bfit_ensemble_mlm_rerank(fm):
    FMEnsembleMLMRerankRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleMLMRerankRunScriptGenerator().make()

