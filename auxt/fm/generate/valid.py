from auxt.script.run import RunScript
from auxt.expt.run import ExptRunScript
from .util import (
        FalkoMerlinValidGenerationJobScriptInterface,
        FalkoMerlinGenerationRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECSingleGenerationJobScript
from auxt.generator.run import ValidSingleRunScriptGenerator

class FalkoMerlinValidSingleGenerationJobScript(
        FalkoMerlinValidGenerationJobScriptInterface,
        GECSingleGenerationJobScript):
    pass


class FalkoMerlinValidSingleGenerationExptRunScript(ExptRunScript):
    def make_path(self):
        return '{}/generate_fm_valid.sh'.format(self.index)


class FalkoMerlinValidSingleGenerationAllRunScript(RunScript):
    def make_path(self):
        return 'generate_fm_valid.sh'


class FalkoMerlinValidSingleGenerationRunScriptGenerator(
        FalkoMerlinGenerationRunScriptGeneratorInterface,
        ValidSingleRunScriptGenerator):

    def __init__(self):
        self.job_class = FalkoMerlinValidSingleGenerationJobScript
        self.expt_run_class = FalkoMerlinValidSingleGenerationExptRunScript
        self.all_run_class = FalkoMerlinValidSingleGenerationAllRunScript
        super().__init__()


def fm_valid_generate():
    FalkoMerlinValidSingleGenerationRunScriptGenerator().make()

