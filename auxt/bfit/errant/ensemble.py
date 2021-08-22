from auxt.expt.result.m2 import M2ResultTableFactory
from auxt.directory.expt.outdir import EnsembleOutDir
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.util.prod import make_train_indices
from auxt.script.run import RunScript
from .util import ErrantJobScript

class FMValidErrantJobScript(ErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['valid_src']

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FMTestErrantJobScript(ErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['test_src']

    def reference_path(self):
        return self.eval_config['fm']['test_m2']


class FMEnsembleErrantRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'errant_fm_ensemble.sh'


def fm_ensemble_errant():
    script_list = []

    valid_outdir = EnsembleOutDir('fm', 'valid')
    test_outdir = EnsembleOutDir('fm', 'test')

    FMEnsembleErrantRunScript([
        FMValidErrantJobScript(valid_outdir),
        FMTestErrantJobScript(test_outdir)])

