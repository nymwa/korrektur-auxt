from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidGenerationJobScriptInterface,
        FalkoMerlinTestGenerationJobScriptInterface,
        ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECEnsembleGenerationJobScript
from auxt.generator.run import EnsembleRunScriptGenerator

class FalkoMerlinValidEnsembleGenerationJobScript(
        FalkoMerlinValidGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class FalkoMerlinTestEnsembleGenerationJobScript(
        FalkoMerlinTestGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class FalkoMerlinEnsembleGenerationRunScript(
        RunScript):
    def make_path(self):
        return 'generate_fm_ensemble.sh'


class FalkoMerlinEnsembleGenerationRunScriptGenerator(
        ValidatedFalkoMerlinGeneraitonRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class = FalkoMerlinValidEnsembleGenerationJobScript
        self.test_job_class = FalkoMerlinTestEnsembleGenerationJobScript
        self.run_class = FalkoMerlinEnsembleGenerationRunScript
        super().__init__()


def fm_ensemble_generate():
    FalkoMerlinEnsembleGenerationRunScriptGenerator().make()

