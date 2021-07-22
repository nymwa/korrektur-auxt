from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FalkoMerlinTestGenerationJobScriptInterface,
        ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECSingleGenerationJobScript
from auxt.generator.run import TestSingleRunScriptGenerator

class FalkoMerlinTestSingleGenerationJobScript(
        FalkoMerlinTestGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class FalkoMerlinTestSingleGenerationExptRunScript(ExptRunScript):
    def make_path(self):
        return '{}/generate_fm_test.sh'.format(self.index)


class FalkoMerlinTestSingleGenerationAllRunScript(RunScript):
    def make_path(self):
        return 'generate_fm_test.sh'


class FalkoMerlinTestSingleGenerationRunScriptGenerator(
        ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface,
        TestSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FalkoMerlinTestSingleGenerationJobScript
        self.expt_run_class = FalkoMerlinTestSingleGenerationExptRunScript
        self.all_run_class = FalkoMerlinTestSingleGenerationAllRunScript
        super().__init__()


def fm_test_generate():
    FalkoMerlinTestSingleGenerationRunScriptGenerator().make()

