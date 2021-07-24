from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidScoreJobScriptInterface,
        FalkoMerlinTestScoreJobScriptInterface,
        FalkoMerlinScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleR2LRescoreRunScriptGenerator

class FalkoMerlinValidEnsembleR2LRescoreScoreJobScript(
        FalkoMerlinValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinTestEnsembleR2LRescoreScoreJobScript(
        FalkoMerlinTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinEnsembleR2LRescoreScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_r2l_reranked_ensemble.sh'


class FalkoMerlinEnsembleR2LRescoreScoreRunScriptGenerator(
        FalkoMerlinScoreRunScriptGeneratorInterface,
        EnsembleR2LRescoreRunScriptGenerator):

    def __init__(self):
        self.valid_job_class = FalkoMerlinValidEnsembleR2LRescoreScoreJobScript
        self.test_job_class = FalkoMerlinTestEnsembleR2LRescoreScoreJobScript
        self.run_class = FalkoMerlinEnsembleR2LRescoreScoreRunScript
        super().__init__()


def fm_ensemble_r2l_reranked_score():
    FalkoMerlinEnsembleR2LRescoreScoreRunScriptGenerator().make()

