from pathlib import Path
from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidEnsembleR2LRescoreJobScriptInterface,
        FalkoMerlinTestEnsembleR2LRescoreJobScriptInterface,
        FalkoMerlinEnsembleR2LRescoreRunScriptGeneratorInterface)
from auxt.expt.job import ExptJobScript
from auxt.generator.run import EnsembleR2LRescoreRunScriptGenerator
from auxt.expt.generate.job import GenerationJobScript, EnsembleGenerationJobScriptInterface

class FalkoMerlinEnsembleR2LRescoreJobScript(
        EnsembleGenerationJobScriptInterface,
        GenerationJobScript):

    def get_score_reference(self):
        return True

    def make_path(self):
        return self.outdir.make_path('rescore.sh')

    def make(self):
        command = self.make_generate_command()

        self.append('{} \\'.format(command))
        ## TODO


class FalkoMerlinValidEnsembleR2LRescoreJobScript(
        FalkoMerlinValidEnsembleR2LRescoreJobScriptInterface,
        FalkoMerlinEnsembleR2LRescoreJobScript):
    pass


class FalkoMerlinTestEnsembleR2LRescoreJobScript(
        FalkoMerlinTestEnsembleR2LRescoreJobScriptInterface,
        FalkoMerlinEnsembleR2LRescoreJobScript):
    pass


class FalkoMerlinEnsembleR2LRescoreRunScript(RunScript):

    def make_path(self):
        return 'r2l_rescore_fm_ensemble.sh'


class FalkoMerlinEnsembleR2LRescoreRunScriptGenerator(
        FalkoMerlinEnsembleR2LRescoreRunScriptGeneratorInterface,
        EnsembleR2LRescoreRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = FalkoMerlinValidEnsembleR2LRescoreJobScript
        self.test_job_class = FalkoMerlinTestEnsembleR2LRescoreJobScript
        self.run_class = FalkoMerlinEnsembleR2LRescoreRunScript
        super().__init__()


def fm_ensemble_r2l_rescore():
    FalkoMerlinEnsembleR2LRescoreRunScriptGenerator().make()

