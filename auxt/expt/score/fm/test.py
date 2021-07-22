from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FalkoMerlinTestScoreJobScriptInterface,
        ValidatedFalkoMerlinScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import TestSingleRunScriptGenerator

class FalkoMerlinTestSingleScoreJobScript(
        FalkoMerlinTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FalkoMerlinTestSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_fm_test.sh'.format(self.index)


class FalkoMerlinTestSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_test.sh'


class FalkoMerlinTestSingleScoreRunScriptGenerator(
        ValidatedFalkoMerlinScoreRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FalkoMerlinTestSingleScoreJobScript
        self.expt_run_class = FalkoMerlinTestSingleScoreExptRunScript
        self.all_run_class = FalkoMerlinTestSingleScoreAllRunScript
        super().__init__()


def fm_test_score():
    FalkoMerlinTestSingleScoreRunScriptGenerator().make()

