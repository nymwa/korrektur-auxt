from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FalkoMerlinValidScoreJobScriptInterface,
        FalkoMerlinScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import ValidSingleRunScriptGenerator

class FalkoMerlinValidSingleScoreJobScript(
        FalkoMerlinValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinValidSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_fm_valid.sh'.format(self.index)


class FalkoMerlinValidSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_valid.sh'


class FalkoMerlinValidSingleScoreRunScriptGenerator(
        FalkoMerlinScoreRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FalkoMerlinValidSingleScoreJobScript
        self.expt_run_class = FalkoMerlinValidSingleScoreExptRunScript
        self.all_run_class = FalkoMerlinValidSingleScoreAllRunScript
        super().__init__()


def fm_valid_score():
    FalkoMerlinValidSingleScoreRunScriptGenerator().make()

