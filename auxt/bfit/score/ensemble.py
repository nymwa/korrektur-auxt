from auxt.script.run import RunScript
from .util import (
        FMValidScoreJobScriptInterface,
        FMTestScoreJobScriptInterface,
        CoNLLValidScoreJobScriptInterface,
        CoNLLTestScoreJobScriptInterface,
        ValidatedFMScoreRunScriptGeneratorInterface,
        ValidatedCoNLLScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleRunScriptGenerator

class FMValidEnsembleScoreJobScript(
        FMValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FMTestEnsembleScoreJobScript(
        FMTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FMEnsembleScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_ensemble.sh'


class CoNLLValidEnsembleScoreJobScript(
        CoNLLValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class CoNLLTestEnsembleScoreJobScript(
        CoNLLTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class CoNLLEnsembleScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_conll_ensemble.sh'


class FMEnsembleScoreRunScriptGenerator(
        ValidatedFMScoreRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                FMValidEnsembleScoreJobScript,
                FMTestEnsembleScoreJobScript,
                FMEnsembleScoreRunScript)
        super().__init__()


class CoNLLEnsembleScoreRunScriptGenerator(
        ValidatedCoNLLScoreRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                CoNLLValidEnsembleScoreJobScript,
                CoNLLTestEnsembleScoreJobScript,
                CoNLLEnsembleScoreRunScript)
        super().__init__()


def bfit_ensemble_score(fm):
    FMEnsembleScoreRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleScoreRunScriptGenerator().make()

