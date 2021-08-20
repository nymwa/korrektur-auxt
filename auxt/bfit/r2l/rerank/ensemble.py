from auxt.script.run import RunScript
from .util import (
        EnsembleR2LRerankJobScriptInterface,
        FMEnsembleR2LRerankRunScriptGeneratorInterface,
        CoNLLEnsembleR2LRerankRunScriptGeneratorInterface)
from auxt.expt.job import ExptJobScript
from auxt.generator.run import EnsembleR2LRerankRunScriptGenerator
from auxt.expt.r2l_rerank.job import EnsembleR2LRerankJobScript

class FMEnsembleR2LRerankJobScript(
        EnsembleR2LRerankJobScriptInterface,
        EnsembleR2LRerankJobScript):
    pass


class CoNLLEnsembleR2LRerankJobScript(
        EnsembleR2LRerankJobScriptInterface,
        EnsembleR2LRerankJobScript):
    pass


class FMEnsembleR2LRerankRunScript(RunScript):

    def make_path(self):
        return 'r2l_rerank_fm_ensemble.sh'


class CoNLLEnsembleR2LRerankRunScript(RunScript):

    def make_path(self):
        return 'r2l_rerank_conll_ensemble.sh'


class FMEnsembleR2LRerankRunScriptGenerator(
        FMEnsembleR2LRerankRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = self.test_job_class = FMEnsembleR2LRerankJobScript
        self.run_class = FMEnsembleR2LRerankRunScript
        super().__init__()


class CoNLLEnsembleR2LRerankRunScriptGenerator(
        CoNLLEnsembleR2LRerankRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'wf'
        self.valid_job_class = self.test_job_class = CoNLLEnsembleR2LRerankJobScript
        self.run_class = CoNLLEnsembleR2LRerankRunScript
        super().__init__()


def bfit_ensemble_r2l_rerank(fm):
    FMEnsembleR2LRerankRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleR2LRerankRunScriptGenerator().make()

