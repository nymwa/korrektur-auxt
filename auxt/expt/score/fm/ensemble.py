from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidScoreJobScriptInterface,
        FalkoMerlinTestScoreJobScriptInterface,
        ValidatedFalkoMerlinScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleRunScriptGenerator

class FalkoMerlinValidEnsembleScoreJobScript(
        FalkoMerlinValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinTestEnsembleScoreJobScript(
        FalkoMerlinTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinEnsembleScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_ensemble.sh'


class FalkoMerlinEnsembleScoreRunScriptGenerator(
        ValidatedFalkoMerlinScoreRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class = FalkoMerlinValidEnsembleScoreJobScript
        self.test_job_class = FalkoMerlinTestEnsembleScoreJobScript
        self.run_class = FalkoMerlinEnsembleScoreRunScript
        super().__init__()


def fm_ensemble_score():
    FalkoMerlinEnsembleScoreRunScriptGenerator().make()

