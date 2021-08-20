from auxt.script.run import RunScript
from .util import (
        FMValidGenerationJobScriptInterface,
        FMTestGenerationJobScriptInterface,
        CoNLLValidGenerationJobScriptInterface,
        CoNLLTestGenerationJobScriptInterface,
        ValidatedFMGenerationRunScriptGeneratorInterface,
        ValidatedCoNLLGenerationRunScriptGeneratorInterface)
from auxt.expt.generate.job import GECEnsembleGenerationJobScript
from auxt.generator.run import EnsembleRunScriptGenerator

class FMValidEnsembleGenerationJobScript(
        FMValidGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class FMTestEnsembleGenerationJobScript(
        FMTestGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class FMEnsembleGenerationRunScript(
        RunScript):

    def make_path(self):
        return 'generate_fm_ensemble.sh'


class CoNLLValidEnsembleGenerationJobScript(
        CoNLLValidGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class CoNLLTestEnsembleGenerationJobScript(
        CoNLLTestGenerationJobScriptInterface,
        GECEnsembleGenerationJobScript):
    pass


class CoNLLEnsembleGenerationRunScript(
        RunScript):

    def make_path(self):
        return 'generate_conll_ensemble.sh'


class FMEnsembleGenerationRunScriptGenerator(
        ValidatedFMGenerationRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                FMValidEnsembleGenerationJobScript,
                FMTestEnsembleGenerationJobScript,
                FMEnsembleGenerationRunScript)
        super().__init__()


class CoNLLEnsembleGenerationRunScriptGenerator(
        ValidatedCoNLLGenerationRunScriptGeneratorInterface,
        EnsembleRunScriptGenerator):

    def __init__(self):
        self.valid_job_class, self.test_job_class, self.run_class = (
                CoNLLValidEnsembleGenerationJobScript,
                CoNLLTestEnsembleGenerationJobScript,
                CoNLLEnsembleGenerationRunScript)
        super().__init__()


def bfit_ensemble_generate(fm):
    FMEnsembleGenerationRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleGenerationRunScriptGenerator().make()

