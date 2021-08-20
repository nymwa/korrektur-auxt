from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FMValidGenerationJobScriptInterface,
        CoNLLValidGenerationJobScriptInterface,
        FMGenerationRunScriptGeneratorInterface,
        CoNLLGenerationRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECSingleGenerationJobScript
from auxt.generator.run import ValidSingleRunScriptGenerator

class FMValidSingleGenerationJobScript(
        FMValidGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class CoNLLValidSingleGenerationJobScript(
        CoNLLValidGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class FMValidSingleGenerationExptRunScript(ExptRunScript):

    def make_path(self):
        return '{}/generate_fm_valid.sh'.format(self.index)


class FMValidSingleGenerationAllRunScript(RunScript):

    def make_path(self):
        return 'generate_fm_valid.sh'


class CoNLLValidSingleGenerationExptRunScript(ExptRunScript):

    def make_path(self):
        return '{}/generate_conll_valid.sh'.format(self.index)


class CoNLLValidSingleGenerationAllRunScript(RunScript):

    def make_path(self):
        return 'generate_conll_valid.sh'


class FMValidSingleGenerationRunScriptGenerator(
        FMGenerationRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FMValidSingleGenerationJobScript
        self.expt_run_class = FMValidSingleGenerationExptRunScript
        self.all_run_class = FMValidSingleGenerationAllRunScript
        super().__init__()


class CoNLLValidSingleGenerationRunScriptGenerator(
        CoNLLGenerationRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = CoNLLValidSingleGenerationJobScript
        self.expt_run_class = CoNLLValidSingleGenerationExptRunScript
        self.all_run_class = CoNLLValidSingleGenerationAllRunScript
        super().__init__()


def bfit_valid_generate(fm):
    FMValidSingleGenerationRunScriptGenerator().make()

    if not fm:
        CoNLLValidSingleGenerationRunScriptGenerator().make()

