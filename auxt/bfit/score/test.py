from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FMTestScoreJobScriptInterface,
        CoNLLTestScoreJobScriptInterface,
        ValidatedFMScoreRunScriptGeneratorInterface,
        ValidatedCoNLLScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import TestSingleRunScriptGenerator

class FMTestSingleScoreJobScript(
        FMTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FMTestSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_fm_test.sh'.format(self.index)


class FMTestSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_test.sh'


class FMTestSingleScoreRunScriptGenerator(
        ValidatedFMScoreRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FMTestSingleScoreJobScript
        self.expt_run_class = FMTestSingleScoreExptRunScript
        self.all_run_class = FMTestSingleScoreAllRunScript
        super().__init__()


class CoNLLTestSingleScoreJobScript(
        CoNLLTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class CoNLLTestSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_conll_test.sh'.format(self.index)


class CoNLLTestSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_conll_test.sh'


class CoNLLTestSingleScoreRunScriptGenerator(
        ValidatedCoNLLScoreRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = CoNLLTestSingleScoreJobScript
        self.expt_run_class = CoNLLTestSingleScoreExptRunScript
        self.all_run_class = CoNLLTestSingleScoreAllRunScript
        super().__init__()


def bfit_test_score(fm):
    FMTestSingleScoreRunScriptGenerator().make()

    if not fm:
        CoNLLTestSingleScoreRunScriptGenerator().make()

