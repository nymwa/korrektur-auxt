from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FMTestGenerationJobScriptInterface,
        CoNLLTestGenerationJobScriptInterface,
        FMGenerationRunScriptGeneratorInterface,
        CoNLLGenerationRunScriptGeneratorInterface,
        ValidatedFMGenerationRunScriptGeneratorInterface,
        ValidatedCoNLLGenerationRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECSingleGenerationJobScript
from auxt.generator.run import TestSingleRunScriptGenerator

class FMTestSingleGenerationJobScript(
        FMTestGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class CoNLLTestSingleGenerationJobScript(
        CoNLLTestGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class FMTestSingleGenerationExptRunScript(ExptRunScript):

    def make_path(self):
        return '{}/generate_fm_test.sh'.format(self.index)


class FMTestSingleGenerationAllRunScript(RunScript):

    def make_path(self):
        return 'generate_fm_test.sh'


class CoNLLTestSingleGenerationExptRunScript(ExptRunScript):

    def make_path(self):
        return '{}/generate_conll_test.sh'.format(self.index)


class CoNLLTestSingleGenerationAllRunScript(RunScript):

    def make_path(self):
        return 'generate_conll_test.sh'


class FMTestSingleGenerationRunScriptGenerator(
        ValidatedFMGenerationRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FMTestSingleGenerationJobScript
        self.expt_run_class = FMTestSingleGenerationExptRunScript
        self.all_run_class = FMTestSingleGenerationAllRunScript
        super().__init__()


class CoNLLTestSingleGenerationRunScriptGenerator(
        ValidatedCoNLLGenerationRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = CoNLLTestSingleGenerationJobScript
        self.expt_run_class = CoNLLTestSingleGenerationExptRunScript
        self.all_run_class = CoNLLTestSingleGenerationAllRunScript
        super().__init__()



def bfit_test_generate(fm):
    FMTestSingleGenerationRunScriptGenerator().make()

    if not fm:
        CoNLLTestSingleGenerationRunScriptGenerator().make()

