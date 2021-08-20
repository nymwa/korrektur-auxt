from auxt.script.run import RunScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleMLMRerankScoreRunScriptGenerator
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import NamedGECScoreJobScript
from .util import (
        FMValidScoreJobScriptInterface,
        FMTestScoreJobScriptInterface,
        CoNLLValidScoreJobScriptInterface,
        CoNLLTestScoreJobScriptInterface,
        FMScoreRunScriptGeneratorInterface,
        CoNLLScoreRunScriptGeneratorInterface)

class FMValidEnsembleMLMRerankScoreJobScript(
        FMValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class FMTestEnsembleMLMRerankScoreJobScript(
        FMTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class CoNLLValidEnsembleMLMRerankScoreJobScript(
        CoNLLValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class CoNLLTestEnsembleMLMRerankScoreJobScript(
        CoNLLTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class FMEnsembleMLMRerankScoreRunScript(
        ScoreRunScriptInterface, RunScript):

    def make_path(self):
        return 'score_fm_mlm_reranked_ensemble.sh'


class CoNLLEnsembleMLMRerankScoreRunScript(
        ScoreRunScriptInterface, RunScript):

    def make_path(self):
        return 'score_conll_mlm_reranked_ensemble.sh'


class FMEnsembleMLMRerankScoreRunScriptGenerator(
        FMScoreRunScriptGeneratorInterface,
        EnsembleMLMRerankScoreRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                FMValidEnsembleMLMRerankScoreJobScript,
                FMTestEnsembleMLMRerankScoreJobScript,
                FMEnsembleMLMRerankScoreRunScript)
        super().__init__()


class CoNLLEnsembleMLMRerankScoreRunScriptGenerator(
        CoNLLScoreRunScriptGeneratorInterface,
        EnsembleMLMRerankScoreRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                CoNLLValidEnsembleMLMRerankScoreJobScript,
                CoNLLTestEnsembleMLMRerankScoreJobScript,
                CoNLLEnsembleMLMRerankScoreRunScript)
        super().__init__()


def bfit_ensemble_mlm_reranked_score(fm):
    FMEnsembleMLMRerankScoreRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleMLMRerankScoreRunScriptGenerator().make()

