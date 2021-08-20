from auxt.script.run import RunScript
from .util import (
        FMScoreRunScriptGeneratorInterface,
        CoNLLScoreRunScriptGeneratorInterface)
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleR2LRerankRunScriptGenerator
from .ensemble import (
        FMValidEnsembleScoreJobScript,
        FMTestEnsembleScoreJobScript,
        CoNLLValidEnsembleScoreJobScript,
        CoNLLTestEnsembleScoreJobScript)

class FMEnsembleR2LRerankScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_r2l_reranked_ensemble.sh'


class CoNLLEnsembleR2LRerankScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_conll_r2l_reranked_ensemble.sh'


class FMEnsembleR2LRerankScoreRunScriptGenerator(
        FMScoreRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                FMValidEnsembleScoreJobScript,
                FMTestEnsembleScoreJobScript,
                FMEnsembleR2LRerankScoreRunScript)
        super().__init__()


class CoNLLEnsembleR2LRerankScoreRunScriptGenerator(
        CoNLLScoreRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                CoNLLValidEnsembleScoreJobScript,
                CoNLLTestEnsembleScoreJobScript,
                CoNLLEnsembleR2LRerankScoreRunScript)
        super().__init__()


def bfit_ensemble_r2l_reranked_score(fm):
    FMEnsembleR2LRerankScoreRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleR2LRerankScoreRunScriptGenerator().make()

