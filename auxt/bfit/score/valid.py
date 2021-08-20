from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FMValidScoreJobScriptInterface,
        CoNLLValidScoreJobScriptInterface,
        FMScoreRunScriptGeneratorInterface,
        CoNLLScoreRunScriptGeneratorInterface)
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import GECScoreJobScript
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import ValidSingleRunScriptGenerator

class FMValidSingleScoreJobScript(
        FMValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class CoNLLValidSingleScoreJobScript(
        CoNLLValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        GECScoreJobScript):
    pass


class FMValidSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_fm_valid.sh'.format(self.index)


class FMValidSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_valid.sh'


class CoNLLValidSingleScoreExptRunScript(
        ScoreRunScriptInterface,
        ExptRunScript):

    def make_path(self):
        return '{}/score_conll_valid.sh'.format(self.index)


class CoNLLValidSingleScoreAllRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_conll_valid.sh'


class FMValidSingleScoreRunScriptGenerator(
        FMScoreRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FMValidSingleScoreJobScript
        self.expt_run_class = FMValidSingleScoreExptRunScript
        self.all_run_class = FMValidSingleScoreAllRunScript
        super().__init__()


class CoNLLValidSingleScoreRunScriptGenerator(
        CoNLLScoreRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = CoNLLValidSingleScoreJobScript
        self.expt_run_class = CoNLLValidSingleScoreExptRunScript
        self.all_run_class = CoNLLValidSingleScoreAllRunScript
        super().__init__()


def bfit_valid_score(fm):
    FMValidSingleScoreRunScriptGenerator().make()

    if not fm:
        CoNLLValidSingleScoreRunScriptGenerator().make()

